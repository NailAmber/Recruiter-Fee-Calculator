package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

// Функция для добавления клиента
func addClient(name, formula string) {
    data := map[string]string{"name": name, "formula": formula}
    jsonData, err := json.Marshal(data)
    if err != nil {
        fmt.Println("Error marshalling data:", err)
        return
    }

    response, err := http.Post("http://localhost:5000/add_client", "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer response.Body.Close()
    body, err := ioutil.ReadAll(response.Body)
    if err != nil {
        fmt.Println("Error reading response:", err)
        return
    }
    fmt.Println("Add Client Response:", string(body))
}

// Функция для расчета выплаты
func calculatePayment(clientName string, amount float64) {
    data := map[string]interface{}{"client_name": clientName, "amount": amount}
    jsonData, err := json.Marshal(data)
    if err != nil {
        fmt.Println("Error marshalling data:", err)
        return
    }

    response, err := http.Post("http://localhost:5000/calculate_payment", "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer response.Body.Close()
    body, err := ioutil.ReadAll(response.Body)
    if err != nil {
        fmt.Println("Error reading response:", err)
        return
    }
    fmt.Println("Calculate Payment Response:", string(body))
}

func main() {
    // Добавляем клиента с формулой (salary * 12) * 0.18 - 6%
    addClient("ExampleClient1", "(amount*12)*0.18-6")

    // Рассчитываем выплату для клиента "ExampleClient" с зарплатой 100
    calculatePayment("ExampleClient1", 100)
}
