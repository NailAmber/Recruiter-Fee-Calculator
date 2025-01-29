# Telegram Admin Checker Bot

A Go-based Telegram bot that verifies user admin status by checking against a REST API endpoint.

## 📝 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Requirements](#-api-requirements)
- [Troubleshooting](#-troubleshooting)

## ✨ Features
- Real-time admin status verification
- Error handling for API communication failures
- Environment variable configuration
- Support for nested API responses
- Immediate user feedback with status messages

## ⚙️ Prerequisites
- [Go 1.21+](https://go.dev/dl/)
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Running REST API endpoint

## 📥 Installation
1. Clone the repository (or create new directory)
2. Initialize Go module:
```bash
go mod init telegram-bot-admin-checker
```
Install dependencies:


```bash
go get github.com/go-telegram-bot-api/telegram-bot-api/v5
```
## 🔧 Configuration


```Go
const (
	BotToken   = "BOT_TOKEN"
	BaseAPIURL = "http://localhost:5000"
)
```
## 🚀 Usage

Run the bot:
```bash

go run telegram_bot_admin_checker.go
```

## 📡 API Requirements

Your API must implement this endpoint:
```py

@app.route('/get_all_admins', methods=['GET'])
def api_get_all_admins():
    # Should return format:
    # {"status": "success", "admins": [[admin_id_1], [admin_id_2], ...]}
```
Example valid response:
```json

{
  "status": "success",
  "admins": [[123456789], [987654321]]
}
```
## 🛠️ Troubleshooting

| Error Message                  | Solution                          |
| :---------------------------- | :-------------------------------- |
| Invalid token                  | Verify BOT_TOKEN in .env          |
| API connection failed          | Check API server availability     |
| Unexpected response format     | Validate API JSON structure       |
