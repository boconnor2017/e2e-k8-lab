import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print("Initial GET:")
print(response.json())
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print("Updated request via PUT:")
print(response.json())
