package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

const BASE_URL = "http://localhost:5000"

func addClient() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter client name: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	fmt.Print("Enter formula: ")
	formula, _ := reader.ReadString('\n')
	formula = strings.TrimSpace(formula)

	data := map[string]string{"name": name, "formula": formula}
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	resp, err := http.Post(BASE_URL+"/add_client", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func deleteClient() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter client name to delete: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	url := BASE_URL + "/delete_client/" + name
	req, err := http.NewRequest("DELETE", url, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func addAdmin() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter admin id: ")
	id, _ := reader.ReadString('\n')
	id = strings.TrimSpace(id)

	data := map[string]string{"id": id}
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	resp, err := http.Post(BASE_URL+"/add_admin", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func removeAdmin() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter admin id to remove: ")
	id, _ := reader.ReadString('\n')
	id = strings.TrimSpace(id)

	url := BASE_URL + "/remove_admin/" + id
	req, err := http.NewRequest("DELETE", url, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func getAllAdmins() {
	resp, err := http.Get(BASE_URL + "/get_all_admins")
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func updateClientFormula() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter client name: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	fmt.Print("Enter new formula: ")
	newFormula, _ := reader.ReadString('\n')
	newFormula = strings.TrimSpace(newFormula)

	data := map[string]string{"name": name, "new_formula": newFormula}
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	url := BASE_URL + "/update_client_formula"
	req, err := http.NewRequest("PUT", url, bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func calculatePayment() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter client name: ")
	clientName, _ := reader.ReadString('\n')
	clientName = strings.TrimSpace(clientName)

	fmt.Print("Enter payment: ")
	payment, _ := reader.ReadString('\n')
	payment = strings.TrimSpace(payment)

	data := map[string]string{"client_name": clientName, "payment": payment}
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	resp, err := http.Post(BASE_URL+"/calculate_payment", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func getAllClients() {
	resp, err := http.Get(BASE_URL + "/get_all_clients")
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	printResponse(resp)
}

func printResponse(resp *http.Response) {
	fmt.Printf("Status Code: %d\n", resp.StatusCode)
	body, _ := io.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(body, &result)
	fmt.Println(result)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Println("\nMenu:")
		fmt.Println("1. Add Client")
		fmt.Println("2. Delete Client")
		fmt.Println("3. Update Client Formula")
		fmt.Println("4. Calculate Payment")
		fmt.Println("5. Get All Clients")
		fmt.Println("6. Add admin")
		fmt.Println("7. Delete admin")
		fmt.Println("8. Get All Admins")
		fmt.Println("9. Exit")

		fmt.Print("Enter your choice: ")
		choice, _ := reader.ReadString('\n')
		choice = strings.TrimSpace(choice)

		switch choice {
		case "1":
			addClient()
		case "2":
			deleteClient()
		case "3":
			updateClientFormula()
		case "4":
			calculatePayment()
		case "5":
			getAllClients()
		case "6":
			addAdmin()
		case "7":
			removeAdmin()
		case "8":
			getAllAdmins()
		case "9":
			fmt.Println("Exiting...")
			return
		default:
			fmt.Println("Invalid choice, please try again.")
		}
	}
}