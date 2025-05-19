import json

with open('data.json', 'r+') as file:
  try:
    data = json.load(file)
    print(data)
    user_input = input("Enter data to add to database")
    json.dump(user_input, file)
    print("Success")
  except json.JSONDecodeError:
    print("Error")


