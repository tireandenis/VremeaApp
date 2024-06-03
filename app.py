import requests

celsius = 0

cheie_api = "90382af5d55d423a926fd04fa89c2c3a"

input_oras = input("Alege orasul: ")

date_vreme =  requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={input_oras}&units=imperial&APPID={cheie_api}")


if date_vreme.json()['cod'] == '404':
    print("Orasul nu exista!")
else:
    starea = date_vreme.json()['weather'][0]['description']
    temperatura = date_vreme.json()['main']['temp']

celsius = round((temperatura - 32) * 5/9)

print(f"Temperatura in {input_oras} este de: {celsius} (\u00B0C)")
print(f"Starea vremii a orasului {input_oras} este {starea}.")


