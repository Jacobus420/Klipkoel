from models.klientelys_model import create_klientelys_table, add_client, print_klientelys, delete_client

def main():
    # Create klientelys table if it doesn't exist
    create_klientelys_table()

    while True:
        print("\nClient Management System")
        print("1. Add a new client")
        print("2. View client list")
        print("3. Delete")
        print("4. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            kode = input("Enter client code: ")
            client_name = input("Enter client name: ")
            address_line1 = input("Enter address line 1: ")
            address_line2 = input("Enter address line 2 (or leave empty): ")

            add_client(kode, client_name, address_line1, address_line2)
            print("Client added successfully!")

        elif choice == "2":
            print("\nClient List:")
            print_klientelys()

        elif choice == "3":
            kode=input("Enter client kode to delete: ")
            delete_client(kode)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()