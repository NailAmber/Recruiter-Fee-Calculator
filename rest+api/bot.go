package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
)

func addClient(name, formula string) {
    data := map[string]string{"name": name, "formula": formula}
    jsonData, err := json.Marshal(data)
    if err != nil {
        fmt.Println(err)
        return
    }

    response, err := http.Post("http://localhost:5000/add_client", "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        fmt.Println(err)
        return
    }
    defer response.Body.Close()
    body, err := io.ReadAll(response.Body)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(string(body))
}

func deleteClient(name string) {
    client := &http.Client{}
    req, err := http.NewRequest("DELETE", "http://localhost:5000/delete_client/"+name, nil)
    if err != nil {
        fmt.Println(err)
        return
    }
    response, err := client.Do(req)
    if err != nil {
        fmt.Println(err)
        return
    }
    defer response.Body.Close()
    body, err := io.ReadAll(response.Body)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(string(body))
}

func getAllClients() {
    response, err := http.Get("http://localhost:5000/get_all_clients")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer response.Body.Close()
    body, err := io.ReadAll(response.Body)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(string(body))
}

func main() {
    addClient("Client1", "amount * 1.2")
    // deleteClient("Client1")
    getAllClients()
}
