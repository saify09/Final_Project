import requests
try:
    response = requests.get("http://localhost:8501")
    if response.status_code == 200:
        print("Status Code: 200")
        print("App is reachable!")
    else:
        print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
