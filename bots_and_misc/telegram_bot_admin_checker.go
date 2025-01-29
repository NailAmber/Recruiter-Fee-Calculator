package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

const (
	BotToken   = "BOT_TOKEN"
	BaseAPIURL = "http://localhost:5000"
)

type APIResponse struct {
	Status  string     `json:"status"`
	Admins  [][]int64  `json:"admins"` // Handle nested array structure
	Message string     `json:"message"`
}

func main() {
	bot, err := tgbotapi.NewBotAPI(BotToken)
	if err != nil {
		log.Panic("Failed to initialize bot:", err)
	}

	bot.Debug = true
	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message == nil {
			continue
		}

		userID := update.Message.From.ID
		isAdmin, err := checkAdminStatus(userID)
		
		var messageText string
		if err != nil {
			messageText = "❌ Error: " + err.Error()
		} else if isAdmin {
			messageText = "✅ You are an administrator!"
		} else {
			messageText = "⛔ You are not authorized."
		}

		msg := tgbotapi.NewMessage(update.Message.Chat.ID, messageText)
		if _, err := bot.Send(msg); err != nil {
			log.Println("Error sending message:", err)
		}
	}
}

func checkAdminStatus(userID int64) (bool, error) {
	resp, err := http.Get(BaseAPIURL + "/get_all_admins")
	if err != nil {
		return false, fmt.Errorf("API request failed: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return false, fmt.Errorf("API returned status: %d", resp.StatusCode)
	}

	var apiResponse APIResponse
	if err := json.NewDecoder(resp.Body).Decode(&apiResponse); err != nil {
		return false, fmt.Errorf("failed to decode response: %w", err)
	}

	if apiResponse.Status != "success" {
		return false, fmt.Errorf("API error: %s", apiResponse.Message)
	}

	// Handle nested array structure
	for _, adminGroup := range apiResponse.Admins {
		if len(adminGroup) > 0 && adminGroup[0] == userID {
			return true, nil
		}
	}

	return false, nil
}