from db_functions import create_table, calculate_payment, get_all_clients

def choose_client():
    clients = get_all_clients()
    if not clients:
        print("No clients available.")
        return None
    print("\n--- Clients List ---")
    for i, client in enumerate(clients):
        print(f"{i + 1}. {client[1]}")
    while True:
        try:
            choice = int(input("Choose a client by number: ")) - 1
            if 0 <= choice < len(clients):
                return clients[choice][1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    create_table()
    
    while True:
        print("\n--- Options Menu ---")
        print("1. Calculate Payment")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            client_name = choose_client()
            if client_name:
                try:
                    amount = float(input(f"Enter amount for {client_name}: "))
                    calculate_payment(client_name, amount)
                except ValueError:
                    print("\nInvalid amount. Please enter a numeric value.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
