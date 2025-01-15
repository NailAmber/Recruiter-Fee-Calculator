from db_functions import add_client, update_client_formula, create_table, delete_client, connect_db, get_all_clients

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

def menu():
    while True:
        print("\n--- Recruiter Database Management Menu ---")
        print("1. Add Client")
        print("2. Update Client Formula")
        print("3. Delete Client")
        print("4. View All Clients")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter client name: ")
            formula = input("Enter payment formula: ")
            add_client(name, formula)
        elif choice == "2":
            client_name = choose_client()
            if client_name:
                new_formula = input(f"Enter new payment formula for {client_name}: ")
                update_client_formula(client_name, new_formula)
        elif choice == "3":
            client_name = choose_client()
            if client_name:
                delete_client(client_name)
        elif choice == "4":
            view_all_clients()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def view_all_clients():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    print("\n--- Clients List ---")
    for client in clients:
        print(f"ID: {client[0]}, \tName: {client[1]}, \tFormula: {client[2]}")
    cur.close()
    conn.close()

def get_all_clients():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    cur.close()
    conn.close()
    return clients

if __name__ == "__main__":
    create_table()  # Ensure the table is created
    menu()
