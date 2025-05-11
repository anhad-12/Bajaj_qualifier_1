
# Bajaj Finserv Health | Qualifier 1 - Python Solution

## Overview

This project involves building a Python application that interacts with an API to generate a webhook, solve a SQL problem based on the response, and submit the solution via a POST request using an authentication token.

## Steps I Followed

1. **Set Up Virtual Environment**
   I created a virtual environment to manage dependencies and keep the project isolated.

   ```bash
   python -m venv venv
   ```

2. **Installed Required Dependencies**
   I installed the `requests` library to handle HTTP requests in Python.

   ```bash
   pip install requests
   ```

3. **Generated Webhook**
   I created a function in `post_request.py` that sends a POST request to the API with user details (name, registration number, and email) to generate a webhook URL and retrieve an access token.

4. **Solved SQL Problem**
   Based on the provided question, I solved the SQL problem (not detailed in this README).

5. **Submitted Solution**
   I created a function in `sql_submission.py` that sends the final SQL query to the provided webhook URL using the authentication token. The solution is sent as a POST request with the token included in the headers.

## Code Files

* `post_request.py`: Handles the request to generate the webhook and retrieve the access token.
* `sql_submission.py`: Submits the final SQL query to the webhook URL.

