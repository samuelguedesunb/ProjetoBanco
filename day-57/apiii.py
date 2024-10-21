import requests

def get_params(name):

    response = requests.get(f'https://api.agify.io/?name={name}')
    response2 = requests.get(f'https://api.genderize.io/?name={name}')
    data_age = response.json()
    data_gender = response2.json()
    return data_age, data_gender

## [0] age e [1] gender

x = get_params("Samuel")
print(x)
name = x[0]['name']
age = x[0]['age']
gender = x[1]['gender']

print(name)
print(age)
print(gender)