# MikeLegal Campaign Email Sender and Subscriber Manager
## Introduction

This repository contains two key components for managing email campaigns and subscribers: the Campaign Email Sender and the Email Campaign Manager. These components are designed to help you efficiently send emails and manage your subscriber list.

## 1. Campaign Email Sender
### Email Sender - Mailgun & Celery
The email sender function is developed using the Mailgun API and Celery with Redis as a message broker.
To run this component, execute the relevant Python file. For the Celery version, make sure to start the Redis server and Celery worker.

### Mail Sender - Mailgun with Threads
An alternative email sender function that utilizes Mailgun and threads for improved performance.
Run the file using a standard Python command.

## 2. Email Campaign Manager
### Key Features
Created a subscribers table in the models.py file to store subscriber information.

Implemented a set of RESTful APIs for managing subscribers, including:

* List all subscribers: GET http://127.0.0.1:8000/subscribers/ 
* Retrieve a subscriber by ID: GET http://127.0.0.1:8000/subscribers/{subscriber_id}/ 
* Create a new subscriber: POST http://127.0.0.1:8000/subscribers/ 
* Update a subscriber by ID: PUT http://127.0.0.1:8000/subscribers/{subscriber_id}/
* Delete a subscriber by ID: DELETE http://127.0.0.1:8000/subscribers/{subscriber_id}/
* Get all subscribers (active) : GET http://127.0.0.1:8000/subscribers/active_subscribers/
* Get all subscribers (inactive) : GET http://127.0.0.1:8000/subscribers/inactive_subscribers/ 
* Inactive the subscriber : PUT http://127.0.0.1:8000/subscribers/{subscriber_id}/deactivate_subscriber/
* Developed an Admin UI for easy management and interaction with subscriber data. : http://127.0.0.1:8000/admin/


## Getting Started
Install the project dependencies by running: **pip install -r requirements.txt**

Start the server using the following command: **python manage.py runserver**

## Contact
 If you have any questions or need assistance, please feel free to contact us at **hemasaitej@gmail.com**.