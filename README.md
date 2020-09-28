# Online_Library_Management_System

INSTALL:
FOR BRUTE FORCE LOG IN ATTEMPT
pip install django-brutebuster2

1. Add BruteBuster to your INSTALLED_APPS list in settings.py
2. Add BruteBuster.middleware.RequestMiddleware to your MIDDLEWARE_CLASSES in settings.py
3. Run python manage.py migrate --run-syncdb to add the BruteBuster table to your database
4. That's it! Don't forget to restart your server, if needed.

If everything is working properly, you should see a Failed attempts table in the Django admin interface. Whenever a failed login is detected, the Failures counter for the respective Username/IP address combo is incremented. If the counter goes over a certain threshold (called BB_MAX_FAILURES), login attempts for this User and IP are blocked until BB_BLOCK_INTERVAL (minutes) passes without a failed login.



FOR CRYPTOGRAPHY(Meantime)
pip install django-cryptography


Reference:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog
https://www.youtube.com/watch?v=-s7e_Fy6NRU
