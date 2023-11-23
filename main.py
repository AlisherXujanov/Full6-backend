# JavaScript Object Notation (JSON)
import requests
from faker import Faker
import json


# In js we would do:
# axios.get('https://...')

# In python we do:
response = requests.get('https://...')

# To get the status code:
print(response.status_code)

# To get the content:
print(response.content)

# To get the json:
print(response.json())


# JSON.stringify(data)
# JSON.parse(data)

# stringify   [{...}, {...}, {...}]  =>  "..."
# parse       "..."   =>  [{...}, {...}, {...}]

# json.dumps(...)  =>  "..."
# json.loads(...)  =>  {...}