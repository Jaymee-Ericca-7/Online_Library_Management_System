# Online_Library_Management_System

Features added:
- Views and working functions for Creating, Updating, and Deleting of Books, Authors, and Genres. 

Currently working on: 
- Create, update, delete of Book Instance
- specific user assigned as manager, student/teacher, and admin (working on it now - jaymee) 

Features to be added: 
- borrowing-returning system 
- security features indicated in specs
- search book function (will work on this - jaymee)


Take Note: 
(temporary fix)
since I am still working on the specific user assignment part (if student/teacher or if manager or if admin), for now, please do the following:
- create a superuser at command prompt. CMD to where manage.py is located, then type "python manage.py createsuperuser". then enter the details being asked. 
- After creating the superuser, please change this file library_system/views.py at line "u_name = jaymee_ericca" to the username you entered for your superuser (sample: u_name = enoch_puno")
- This is so that you can see the features of the manager when you log in.

Reference: 
https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog
https://www.youtube.com/watch?v=-s7e_Fy6NRU
