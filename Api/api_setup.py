import requests
import json

parameters = {

}

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-06-07&end_date=2023-06-08&api_key=DEMO_KEY")
print(response.status_code)

original_data = list(response)

print(f"The original data:\n{original_data}")

sorted_data = json.dumps(original_data, sort_keys=True)

print(f"The sorted data based on the keys:\n{sorted_data}")

# with open('data.json','w') as file:
#     response = .dumps()
#     file.write(response.text)

# with open('data.json','r') as file:
#     pass
