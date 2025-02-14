Car Rental Service
This project allows users to authenticate and search for car availability in a car rental service through a simple command-line interface. It interacts with an API to fetch car data, handling authentication and error responses.

Features
User authentication with email and password.
Search for cars by make and model.
Fetch paginated car data and check availability.
Requirements
Python 3.x
requests library
Environment variables (API_BASE_URL)
Installation
1. Clone the repository
bash
Copy
Edit
git clone <repository-url>
cd <repository-directory>
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set up environment variables
Create a .env file in the root of the project directory and define the following environment variable:

env
Copy
Edit
API_BASE_URL=http://localhost:5000  # Replace with the actual API base URL
Usage
1. Login
The user is prompted to provide an email and password. If authentication is successful, a token is received, which is used for subsequent requests.

2. Search for Car Availability
Once authenticated, the user can choose to search for cars by specifying the make and model. The system will check availability across paginated results and inform the user if the car is available.

Running the Application
To run the application, execute the main.py script:

bash
Copy
Edit
python main.py
API Client Functions
login(email, password): Authenticates the user and returns an authentication token.
get_auth_headers(token): Returns headers with the authentication token.
get_cars(token, page=1, limit=10): Fetches paginated car data.
Error Handling
The handle_api_error function catches any errors when interacting with the API and provides an error message.

File Structure
bash
Copy
Edit
.
├── api_client.py        # Handles API requests
├── error_handler.py     # Error handling functions
├── main.py              # Main entry point for user interaction
├── service.py           # Contains the car search logic
└── .env                 # Environment variables
Example Usage
Upon running main.py, the user is prompted to authenticate:

markdown
Copy
Edit
Enter your email: user@example.com
Enter your password: ********
Once authenticated, the user can search for car availability:

pgsql
Copy
Edit
🚗 Car Rental Service Menu
1. Search for a car by make/model
2. Exit
Select an option: 1
Enter car make (e.g., Toyota, Honda): Toyota
Enter car model (e.g., Corolla, Civic): Corolla
✅ The Toyota Corolla is **available** for rent!
If no cars match the criteria, the message will reflect that the car is not available.

Error Handling
If any error occurs during API requests or data fetching, an appropriate error message is displayed:

cpp
Copy
Edit
❌ Authentication failed. Please check your credentials and try again.
Contributing
Feel free to submit issues or pull requests to improve the functionality or add new features!

License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

This README will guide users in setting up the project, using it, and understanding how the application works.
