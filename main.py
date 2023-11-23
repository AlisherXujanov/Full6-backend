# HOMEWORK
# 1. Create a new repository on Github
# 2. Create a new project called my_project
# 3. Get 1-beginner file and do all tasks




# JavaScript Object Notation (JSON)
import requests
from faker import Faker
import json
URL = 'https://jsonplaceholder.typicode.com/todos/1'

# In python we do:
response = requests.get(URL)

# To get the status code:
print("status_code: ", response.status_code)

# To get the content:
print("content: ", response.content)

# To get the json:
print("json(): ", response.json())
# ===================================================================

# JSON.stringify(data)
# JSON.parse(data)

# stringify   [{...}, {...}, {...}]  =>  "..."
# parse       "..."   =>  [{...}, {...}, {...}]

# json.dumps(...)  =>  "..."
# json.loads(...)  =>  {...}