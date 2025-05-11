import requests

def submit_sql_query(webhook_url, access_token, sql_query):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    payload = {
        "finalQuery": sql_query
    }

    try:
        response = requests.post(webhook_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.status_code, response.text

    except requests.RequestException as err:
        print("\nSubmission failed due to a request error.")
        print(f"Details: {err}")
        return None, str(err)

def main():
    # Replace these with your actual values
    webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDUzIyMTAzNyIsIm5hbWUiOiJBbmhhZCBSYW5hIiwiZW1haWwiOiJhbmhhZHJhbmEyMjEwOTVAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYzMDg0LCJleHAiOjE3NDY5NjM5ODR9.VY6TupvNpXNGbiJws8HoZomVjknv8I5N0cfm7_Q0yf8"

    final_sql_query = """
        SELECT 
            P.AMOUNT AS SALARY,
            CONCAT(E.FIRST_NAME, ' ', E.LAST_NAME) AS NAME,
            FLOOR(DATEDIFF(CURDATE(), E.DOB)/365.25) AS AGE,
            D.DEPARTMENT_NAME
        FROM PAYMENTS P
        JOIN EMPLOYEE E ON P.EMP_ID = E.EMP_ID
        JOIN DEPARTMENT D ON E.DEPARTMENT = D.DEPARTMENT_ID
        WHERE DAY(P.PAYMENT_TIME) != 1
        ORDER BY P.AMOUNT DESC
        LIMIT 1;
    """

    print("\nSubmitting SQL query to the webhook...\n")

    status_code, server_response = submit_sql_query(webhook_url, access_token, final_sql_query)

    if status_code == 200:
        print(f"[SUCCESS] Query submitted successfully.")
        print(f"Server Response: {server_response}")
    else:
        print(f" [ERROR] Submission failed.")
        print(f"Status: {status_code}")
        print(f" Response: {server_response}")

if __name__ == "__main__":
    main()
