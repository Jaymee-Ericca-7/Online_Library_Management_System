# Online_Library_Management_System

Features added:
- Views and working functions for Creating, Updating, and Deleting of Books, Book Instance, Authors, and Genres.
- search book function

Currently working on:
1. logic for book instance - jaymee

Features to be added:
1. admin assigns a user as manager - Denise
2. borrowing-returning system - Denise (but wait till I (jaymee) finish the book instance part for this part :>)
3. security features indicated in specs - Enoch & Jan


Take Note:
(temporary fix for #1 on "Features to be added" ^ )
So you guys can access the manager features for now, please do the following:
- create a superuser at command prompt. CMD to where manage.py is located, then type "python manage.py createsuperuser". then enter the details being asked.
- After creating the superuser, please change this file library_system/views.py at line "u_name = jaymee_ericca" to the username you entered for your superuser (sample: u_name = enoch_puno")
- This is so that you can see the features of the manager when you log in.

Reference:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog
https://www.youtube.com/watch?v=-s7e_Fy6NRU
