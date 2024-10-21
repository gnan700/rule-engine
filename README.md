# Rule Engine Application with AST

This project is a 3-tier rule engine application that determines user eligibility based on various attributes (age, department, salary, etc.) using dynamically created rules. 
The application consists of a UI, an API, and a backend with a rule engine represented by an Abstract Syntax Tree (AST). The system allows for dynamic creation, combination, and modification of rules.


## Table of Content
1) **Features**
2) **Project Structure**
3) **Tech Stack**
4) **Build Instructions**
5) **Running the Application**
6) **Design Choices**
7) **API Endpoints**
8) **Tests**

## Features :
1) **Dynamic Rule Creation** : Create complex eligibility rules based on user data.
2) **AST Representation** : Uses Abstract Syntax Trees (ASTs) to represent rules for efficient processing.
3) **Combining Rules** : Combine multiple rules for advanced eligibility checks.
4) **REST API** : Provides a REST API to create, evaluate, and modify rules.
5) **Web UI** : A simple frontend for users to input rules and check eligibility.
6) **Frontend** : A simple HTML form where users can input rules.
7) **Backend** : A Flask-based backend that processes the rules and evaluates eligibility.

 ## Project Structure
 **rule-engine**->
1) app.py #Main Flask app handling routes and logic
2) rule_engine.py #Rule engine logic with AST creation and evaluation
3) requirements.txt #Python dependencies
4) docker-compose.yml   #Container orchestration (Flask + SQLite)
5) data.db #SQLite Database file
6) templates -> index.html #Frontend HTML form for rule input
7) tests-> test_app.py #Unit tests for the application

## Tech Stack
1) **Backend:** Flask(Python).
2) **Frontend:** HTML5
3) **DataBase:** SQLite (used locally, but replaceable with any other DB via Docker).
4) **Containerization:** Docker / Podman
5) **Unit Testing:** unittest (Python)

## Build Instructions:
1) **Clone the repository**:
     (open in command prompt or other terminal)


    "git clone https://github.com/yourusername/rule-engine.git"

    "cd rule-engine"

2) **Install Dependencies:**

   "pip install -r requirements.txt"

3) **Set-up Database:**  Run the database migration or initialize the database if necessary.

4)  **Run the Flask app:**

     "flask run"

    The application should be accessible at http://localhost:5000

**Using Docker:**
1) **Build the Docker Image:**

"docker build -t rule-engine .".

2) **Run the app with Docker Compose:** 

"docker-compose up"
 
 The application should be accessible at http://localhost:5000.

3) **Run the Application**

    After creating the codes, execute with:

   "python app.py"

The application should be accessible at http://localhost:5000.   

## Running the Application:
1) Open your browser and go to http://127.0.0.1:5000/.
2) Input a rule in the form (e.g., age > 30 AND department = 'Sales') and submit.
3) The backend will process the rule and respond with the AST and eligibility status.

**API Endpoints:**

1) **Create Rule Endpionts:**

1) URL: /create_rule

2) Method: POST

3) Description: This endpoint takes a rule string and converts it into an AST.

4) Payload Example: 

{
  "rule_string": "age > 30 AND department = 'Sales'"
}

2) **Evaluate Rule Endpoint:**

 1) URL: /evaluate_rule
 
 2) Method: POST

 3) Description:  Evaluates a rule's AST against the user attributes.

 4) Payload Example:

 {
 
  
  "ast": { "type": "operator", "operator": "AND", "left": {...}, "right": {...} },
  
  
  "data": { "age": 35, "department": "Sales", "salary": 60000 }


}

## Design Choices
1) **Three tier Architechture:** A simple HTML form for user input.
2) **Logic Layer(API):** A Flask-based API that manages rule creation and evaluation using an Abstract Syntax Tree (AST).
3) **Data Layer(Backend):** The system uses SQLite for data storage, containerized for consistency.
4) **Abstract Syntax Tree:** Rules are represented as an AST, which provides a structured way to define and evaluate conditions.
5) **Containerization for Deployment:**  Docker/Podman ensures consistent environments across different machines and simplifies the deployment process.

## API EndPoints
1) **/create_rule**

   1) Method: POST
   2) Description: Create a rule by converting the rule string to an AST.
   3) Request Body Example:

   {

   
  "rule_string": "age > 30 AND department = 'Sales'"

   }

   4) Response:

   {

   
  "status": "Rule created",
  
  "AST": {...}
   
   }

2) **/evaluate_rule**

   1) Method: POST
   2) Description: Evaluate a rule (AST) with given user attributes.
   3) Request Body Example:
  
      {

      
  "ast": { ... },
  
  "data": {
  
    "age": 35,
   
    "department": "Sales",
   
    "salary": 60000
  
  }

  }

  4) Response:

     {

     
  "eligible": true

}

## Tests

1) Unit tests are provided in the tests/ folder using the unittest framework.
2) To run the tests:

   python -m unittest discover tests

## Future Improvements
1) **UI Enhancements:**  Improve the frontend by adding validation, better styling, and more user feedback.
2) **Rule Storage:**  Implement persistent storage for rules in the database.
3) **More Rule Types:**  Extend the system to handle more complex conditions (e.g., nested rules, NOT conditions).


## License
**This project is licensed under the MIT License**

  

