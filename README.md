Project Overview: Workout Tracker API
This project is a specialized backend service designed to streamline fitness data management through a structured RESTful API. Built using the Flask framework, the application focuses on secure data persistence and user-specific access control. At its core, the system utilizes SQLAlchemy as an Object-Relational Mapper (ORM) to interface with a SQLite database, ensuring that all workout entries—including exercise names, durations, and intensities—undergo strict server-side validation before storage. To prioritize security, the backend implements robust authentication using Flask-Bcrypt for password hashing and manages user states through persistent session cookies. The architecture follows a clean separation of concerns, utilizing Flask-RESTful resources to handle complex logic such as pagination for workout history and role-based data isolation, ensuring users only interact with their own personal records.

Installation and Setup
To get the development environment running locally on your machine, follow these steps:

Clone the Repository: Download the source code and navigate into the root folder.

Environment Configuration: Ensure you have Python 3.12 installed. It is recommended to use Pipenv to manage dependencies and avoid version conflicts. Run pipenv install to create the virtual environment and install the necessary libraries.

Database Initialization: The project uses Flask-Migrate to handle schema changes. You must initialize the database by running flask db init, followed by flask db upgrade to generate the local SQLite instance.

Seed Data: Run the seed.py script to populate the database with a test user and initial workout logs to verify the system is functioning.

Execution: Launch the development server using python app.py. The API will be accessible at http://127.0.0.1:5555.

API Interaction Examples
Below are JSON structures representing the expected inputs and outputs for key operations. These can be used with tools like Postman or Insomnia to test the API endpoints.

User Authentication
Endpoint: POST /signup or POST /login

JSON
{
  "username": "Edwin_Dev",
  "password": "securepassword123"
}
Creating a Workout Entry
Endpoint: POST /workouts

JSON
{
  "exercise": "Bench Press",
  "duration": 45,
  "intensity": "High",
  "date": "2026-04-25"
}
Server Response (Successful Retrieval)
Endpoint: GET /workouts?page=1

JSON
{
  "workouts": [
    {
      "id": 1,
      "exercise": "Squats",
      "duration": 30,
      "intensity": "Medium",
      "user_id": 5
    }
  ],
  "total_pages": 3,
  "current_page": 1
}