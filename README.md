Event Planner Web Application

This is a Django based web application where users can sign up, log in, view events and submit their RSVP (Going, Maybe, Decline). Admin users can create, edit, delete events and also view RSVP summaries for each event. Users can update their RSVP before the event date.

Setup and Installation

Clone the repository:

git clone https://github.com/Vishal-9648169281/event-planner-vishal
cd event-planner-vishal


Create a virtual environment:

python -m venv venv


Activate the environment:

venv\Scripts\activate    (Windows)


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create an admin user:

python manage.py createsuperuser


Start the server:

python manage.py runserver

Technologies Used

Django

SQLite

Python

HTML, CSS, Bootstrap

Render for deployment

Django was chosen because it offers a built-in authentication system, ORM, and fast backend development. SQLite is suitable for small applications and assignments. Render was used for deployment as it is simple and free.

ER Diagram (Text Description)

User

id

username

email

password

role (admin or user)

Event

id

title

description

date

start_time

end_time

location

created_by (User foreign key)

RSVP

id

user (foreign key)

event (foreign key)

status (Going, Maybe, Decline)

updated_at

unique constraint: (user, event)

API Endpoints
Authentication

GET/POST: /auth/signup/ – register

GET/POST: /auth/login/ – login

GET: /auth/logout/ – logout

Events

GET: /events/ – list events

GET: /events/<id>/ – event detail

GET/POST: /events/create/ – create event (admin)

GET/POST: /events/<id>/edit/ – edit event (admin)

POST: /events/<id>/delete/ – delete event (admin)

GET: /events/<id>/summary/ – RSVP summary (admin)

RSVP

POST: /rsvp/<id>/submit/ – submit/update RSVP

GET: /rsvp/my/ – list my RSVPs

Deployment Link

Live application:
https://event-planner-vishal.onrender.com

## Demo Video Link
https://drive.google.com/file/d/1XuJs08QDD_YOTFQx1CwkQTWcnc9K9a8S/view?usp=sharing
