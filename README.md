# Coffee Shop Full Stack

## Introduction

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

 The application is capable of:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## Table of contents
  - [Introduction](#Introduction)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview))
  - [Project Structure](#project-structure)
  - [How to use the application](#how-to-use-the-application)
  - [Authors](#authors)

## Overview
### Backend Dependencies
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-CORS** the extension to handle cross origin requests from our frontend server. <br>

More detailed information can be found in the  [readme file](./backend/README.md) in the backend folder. 
### Frontend Dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. <br>
`ionic` must be installed. Detailed method of installing can be found at [here](https://ionicframework.com/docs/intro/cli). There is a issue of executing `ionic serve` with windows environment, please refer to this [stack overflow page](https://stackoverflow.com/questions/29331276/ionic-framework-ionic-is-not-recognized-as-an-internal-or-external-command). <br>
More detailed information can be found in the  [readme file](./frontend/README.md) in the frontend folder. 

## Project Structure
```sh
  ├── README.md
  ├── backend
      ├── src -- the main application
          ├──auth: foler for authentication and permission control
          ├──database: folder for database
          ├──api.py: main application
          ├──__init__.py
      ├── README.md -- readme file for backend.
      ├── requirements.txt -- The dependencies to run the backend
      ├── udacity-fsnd-udaspicelatte.postman_collection.json -- Use [postmen](https://web.postman.co/home) to test the API
  ├── frontend
      ├── e2e
      ├── src
          ├── environments -- folder contain setups that define the interactions between API and backend
          ├── ...
      ├── packages.json -- dependencies to run the frontend
      ├── ...
```
Overall:
* The backend application and databases are in the `backend` folder, where we mainly define the APIs. APIs are further called in the front end. 
* The `frontend` directory contains a complete React frontend to consume the data from the Flask server. The frontend uses the APIs provided by the backend to have interactions with the application user.  

## How to use the application
1. Understand the Project Structure (explained above) and where important files are located.
2. git clone this repo to your local folder using `https://github.com/hellogaga/udacity_coffee.git`
3. Install all the dependencies (both frontend and backend) according to the instructions. 
4. Navigate to **backend/src**, start the backend using the following commands (linux environment):
```bash
export FLASK_APP=api.py
export FLASK_ENV=development
flask run
```
5. Open a **new** bash console. Navigate to folder `frontend` and run the following commands. They will start the front end. 
```bash
npm install \*only need to execute once*\
npm npm install -g @ionic/cli \*only need to execute once*\
ionic serve
```
6. Navigate to project homepage [http://127.0.0.1:8100/](http://127.0.0.1:8100/) or [http://localhost:8100](http://localhost:8100) 
7. Enjoy the application.

### Test the backend
To test the backend:
1. start the backend
2. open [postmen](https://web.postman.co/home)
3. import the `backend\udacity-fsnd-udaspicelatte.postman_collection.json`
4. replace the tokens in `barista` and `manager` with valid ones
5. run the test

## Authors
* Hellogaga used the starting code from [udacity](www.udacity.com) to finish the API and test code.