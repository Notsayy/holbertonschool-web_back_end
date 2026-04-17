# User authentication service

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to declare API routes in a Flask app
How to get and set cookies
How to retrieve request form data
How to return various HTTP status codes

## Requirements

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
You should use SQLAlchemy
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
All your classes should have a documentation (python3 -c 'print(**import**("my_module").MyClass.**doc**)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)')
A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
All your functions should be type annotated
The flask app should only interact with Auth and never with DB directly.
Only public methods of Auth and DB should be used outside these classes

## Setup

You will need to install bcrypt

pip3 install bcrypt

## Tasks

0. User model

1. create user

2. Find user

3. update user

4. Hash password

5. Register user

6. Basic Flask app

7. Register user

8. Credentials validation

9. Generate UUIDs

10. Get session ID

11. Log in

12. Find user by session ID

13. Destroy session

14. Log out

15. User profile

16. Generate reset password token

17. Get reset password token

18. Update password

19. Update password end-point
