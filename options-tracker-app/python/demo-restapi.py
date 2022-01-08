import requests
print("**********************************")
print("Demo API Calls Script v1.1")
print("")
print("")
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print("Step 1: GET function - pulls data from URL ")
print(response.json())
print("")
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print("Step 2: POST function - inserts new data into URL ")
print("POST:")
print(response.status_code)
print(response.headers["Content-Type"])
print(response.json())
print("")
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print("Step 3: PUT function - updates existing data from URL ")
print("Initial GET:")
print(response.json())
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print("Updated request via PUT:")
print(response.json())
print("")
print("**********************************")
