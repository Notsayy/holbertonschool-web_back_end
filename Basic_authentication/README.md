# Basic Authentication API

## Description

This project demonstrates the implementation of a Basic Authentication system for a simple RESTful API using Python and Flask. The goal is to understand the authentication process by building it step by step, including Base64 encoding and handling HTTP Authorization headers. **Note:** In real-world applications, you should use established libraries or frameworks for authentication.

## Learning Objectives

By completing this project, you will be able to:

- Explain what authentication means
- Understand Base64 encoding and how to encode a string in Base64
- Describe Basic Authentication and its mechanism
- Send and process the HTTP Authorization header
- Implement a simple authentication system in Python

## Requirements

- Python 3.9
- pip 25.3
- All scripts must be executable and follow [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) (version 2.5)
- Each Python file, class, and function must have a meaningful docstring
- All files must end with a new line
- A `README.md` file is required at the root of the project

## Resources

- [REST API Authentication Mechanisms](https://www.digitalocean.com/community/tutorials/api-authentication-mechanisms)
- [Base64 in Python](https://docs.python.org/3/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Project Structure

```
Basic_authentication/
├── README.md
├── SimpleAPI/
│   ├── README.md
│   ├── requirements.txt
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── app.py
│   │       └── views/
│   │           ├── __init__.py
│   │           ├── index.py
│   │           └── users.py
│   └── models/
│       ├── __init__.py
│       ├── base.py
│       └── user.py
```

## Usage

1. Install dependencies:
   ```bash
   pip install -r SimpleAPI/requirements.txt
   ```
2. Run the API:
   ```bash
   python3 SimpleAPI/api/v1/app.py
   ```
3. Use a tool like [Postman](https://www.postman.com/) or `curl` to interact with the API, sending the `Authorization` header as needed.

## Author

[Notsayy](https://github.com/Notsayy)
