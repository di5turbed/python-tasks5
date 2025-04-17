import json
import random
import string

def generator(length=12):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for n in range(length))
    return password

def generator_name():
    names = ["Muhammed", "Nikita", "Maxim", "Alexander", "Artem", "Roman", "Georgiy", "Pavel"]
    return f"{random.choice(names)}"

def generator_email(name):
    return f"{name.lower()}@example.com"

name = generator_name()
age = random.randint(1, 120)
email = generator_email(name)
password = generator()

user_info = {
    "name": name,
    "age": age,
    "email": email,
    "password": password
}

json_string = json.dumps(user_info)
print("Сгенерированные данные (JSON) -> \n", json_string)

print("\nДесериализованный объект (Python) -> \n", json.loads(json_string))

with open("userinformation.json", "w", encoding="utf-8") as f:
    f.write(json_string)
