###
###
###

# class User:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def greeting(self):
#         return f'My name is {self.name} and i am {self.age}'

#     def has_birthday(self):
#         self.age += 1

# brad = User('brad traversy', 'brad@gmail.com', 37)

# brad.has_birthday()

# print(brad.greeting())
import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "Age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'ford', 'model': 'Ford', 'yesr': 1970}

carJSON = json.dumps(car)

print(carJSON)
