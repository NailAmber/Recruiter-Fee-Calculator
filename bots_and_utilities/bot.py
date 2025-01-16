import requests

BASE_URL = "http://localhost:5000"

def add_client():
    name = input("Enter client name: ")
    formula = input("Enter formula: ")
    data = {"name": name, "formula": formula}
    response = requests.post(f"{BASE_URL}/add_client", json=data)
    print(f"Status Code: {response.status_code}")
    print(response.json())

def delete_client():
    name = input("Enter client name to delete: ")
    response = requests.delete(f"{BASE_URL}/delete_client/{name}")
    print(f"Status Code: {response.status_code}")
    print(response.json())

def add_admin():
    id = input("Enter admin id: ")
    data = {"id": id}
    response = requests.post(f"{BASE_URL}/add_admin", json=data)
    print(f"Status Code: {response.status_code}")
    print(response.json())

def remove_admin():
    id = input("Enter admin id to remove: ")
    response = requests.delete(f"{BASE_URL}/remove_admin/{id}")
    print(f"Status Code: {response.status_code}")
    print(response.json())

def get_all_admins():
    response = requests.get(f"{BASE_URL}/get_all_admins")
    print(f"Status Code: {response.status_code}")
    print(response.json())

def update_client_formula():
    name = input("Enter client name: ")
    new_formula = input("Enter new formula: ")
    data = {"name": name, "new_formula": new_formula}
    response = requests.put(f"{BASE_URL}/update_client_formula", json=data)
    print(f"Status Code: {response.status_code}")
    print(response.json())

def calculate_payment():
    client_name = input("Enter client name: ")
    payment = input("Enter payment: ")
    data = {"client_name": client_name, "payment": payment}
    response = requests.post(f"{BASE_URL}/calculate_payment", json=data)
    print(f"Status Code: {response.status_code}")
    print(response.json())

def get_all_clients():
    response = requests.get(f"{BASE_URL}/get_all_clients")
    print(f"Status Code: {response.status_code}")
    print(response.json())

def main():
    while True:
        print("\nMenu:")
        print("1. Add Client")
        print("2. Delete Client")
        print("3. Update Client Formula")
        print("4. Calculate Payment")
        print("5. Get All Clients")
        print("6. Add admin")
        print("7. Delete admin")
        print("8. Get All Clients")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_client()
        elif choice == '2':
            delete_client()
        elif choice == '3':
            update_client_formula()
        elif choice == '4':
            calculate_payment()
        elif choice == '5':
            get_all_clients()
        elif choice == '6':
            add_admin()
        elif choice == '7':
            remove_admin()
        elif choice == '8':
            get_all_admins()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
