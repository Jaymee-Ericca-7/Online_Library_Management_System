# Online_Library_Management_System

* Programmers: 
   * Villacruz, Jaymee
   * Puno, Enoch
   * Silverio, Jan
   * Fernandez, Lourdes

Last Modified: 09/30/2020


* Main Features
  * User registration
  * Profile Page for Regular (Student/Faculty) user
  * Search/Browsing function - can search for any book based on what is typed in the search bar
  * Anonymous user can search books and view books and book details only. 
  * Only Admin can change user role
  * Only Manager can perform CRUD functions for Book, Author, Genre, Book Instance
  * Only Regular (student/faculty) user can Borrow a book, Return a book, Leave a book review

* Authentication
  * Username and password combination is required to authenticate students, teachers, managers, and administrators.
  * User is temporarily locked out for too many failed login attempts.
  * Cryptography is enabled for secure password storage
  * Allows users to change their password

* Authorization
  * Users is not allowed to access pages that are not included in their role privileges

* Session Management
  * Manual Logout link/button
  * Session logout is the user is idle for a predefined length of time (1 minute)

* Data Validation
  * Password policy during registration (i.e., minimum length, required characters, restrictions)
  * Field validation for other attributes required during registration (i.e. email format)

* Logging
* Some system activities must be logged



Notes: 
To run the application, make sure to do the following:
* python manage.py makemigrations
* python manage.py migrate
* pip install django-brutebuster2
* python manage.py migrate --run-syncdb
* python manage.py createsuperuser <- for admin access
* python manage.py runserver

  
