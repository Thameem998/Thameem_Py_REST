# Thameem_Py_REST
An application showcasing the integration of Flask framework, SQLAlchemy, and REST API.

## Project Description

The code includes two primary models: 'Invoice' and 'InvoiceItem'. Upon starting the framework, the webpage initializes and creates the first 'Invoice'.Subsequently, the application gives the power to user for adding invoice to the item and also enables viewing the invoice. The implementation also includes showcasing the usage of a Restful API through specific endpoints utilizing the GET method.

### Technology Stack

- HTML
- Flask Framework
- ORM- SQLAlchemy
- Database: MySQL
- Language: Python & Object-Oriented Programming (OOP) concepts
- API Client Used (for testing): Postman

## Dependencies

- Python: Install Python.
  
- Flask and SQLAlchemy: Install Flask and SQLAlchemy using the following commands:
  pip install flask
  pip install sqlalchemy
  pip install flask-sqlalchemy

- Also, refer to requirements.txt file


## Instruction to run docker file ##

Go to main working directory where the 'docker-compose.yml' and 'Dockerfile' is located.

Now, rune the below mentioned command:

* docker-compose up

**NOTE**: 
Now, check whther all the containers in docker are running or not (i.e. 'tham_py_rest-db-1' and 'tham_py_rest-app-1' containers). 

  **If 'tham_py_rest-app-1' container is failing**
      
      * Open 'Docker Desktop'
        
      * Re-start the 'tham_py_rest-app-1' container again from the 'Docker Desktop'

## Now, you are good to go ahead !!!
