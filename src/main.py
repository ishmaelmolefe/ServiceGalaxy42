from service import search_car_availability
from api_client import login

def main():
    # Ask user for email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Authenticate and retrieve token
    token = login(email, password)
    
    if not token:
        print("❌ Authentication failed. Please check your credentials and try again.")
        return  # Prevent going further if authentication fails

    while True:
        print("\n🚗 Car Rental Service Menu")
        print("1. Search for a car by make/model")
        print("2. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            make = input("Enter car make (e.g., Toyota, Honda): ").strip()
            model = input("Enter car model (e.g., Corolla, Civic): ").strip()
            is_available = search_car_availability(token, make, model)
            
            if is_available:
                print(f"✅ The {make} {model} is **available** for rent!")
            else:
                print(f"❌ The {make} {model} is **not available** at the moment.")
        
        elif choice == "2":
            print("Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    main()
