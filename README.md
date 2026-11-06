##Back-End-Development-Pictures
##Environment Setup
Repository created from the provided coding-project-template.
Environment initialized locally.
Python version: 3.9.x
Virtual environment: backend-pics-venv
Flask application configured.
REST API implemented.
##Project Setup

Check Python version:

bash
python --version


##Create virtual environment:

bash
python -m venv backend-pics-venv


##Activate virtual environment:

Windows PowerShell:

powershell
.\backend-pics-venv\Scripts\Activate.ps1


Install dependencies:

bash
python -m pip install -r requirements.txt


Run setup script (in a Bash environment):

bash
bash ./bin/setup.sh


##Expected result: setup script completed successfully.

##API Endpoints
Method	Endpoint	Description
GET	/health	Health check
GET	/count	Count pictures
GET	/picture	Get all pictures
GET	/picture/{id}	Get picture by ID
POST	/picture	Create picture
PUT	/picture/{id}	Update picture
DELETE	/picture/{id}	Delete picture
Running the Application
bash
py app.py


##Application URL: http://127.0.0.1:5001

##Testing

Run all tests:

bash
py -m pytest -v

##Technologies
Python 3.9.x
Flask
REST API
Pytest
JSON
