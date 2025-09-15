if True:
    import requests

    url = "https://my_account.discourse.group/chat/hooks/123453abcde"
    payload = {"text": "Hello from webhook!"}
    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.text)
