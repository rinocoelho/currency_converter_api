import requests


url = 'https://v6.exchangerate-api.com/v6/ad4e6a5e322aa98c0575dc1e/latest/USD'

call = requests.get(url)
api_json = call.json()
currency_list = api_json["conversion_rates"]
base_currency = api_json["conversion_rates"]['USD']


menu_prompt = (
    '- Press A CONVERT CURRENCY\n'
    '- Press B to CHECK EXCHANGE RATES\n'
    '- Press Q to QUIT\n'
    '- Choose: '
)


def menu():
    menu_input = ""

    while menu_input.upper() != "Q":
        if menu_input.upper() == 'A':
            convert_currency()
        elif menu_input.upper() == 'B':
            check_rates()
        menu_input = input(menu_prompt)


def convert_currency():

    for currency, rate in currency_list.items():
        print(f"CURRENCY: {currency} - RATE: {rate}")
    
        user_input = input("CHOOSE AMOUNT $ USD: ")
        choose_currency = input("CHOOSE CURRENCY: ")
        if choose_currency == currency:
            x = user_input * rate
            print(x)

    #x = input("Dollar bebe")



def check_rates():
    for currency, rate in api_json["conversion_rates"].items():
        print(f" ({currency}) RATE: {rate}")


print(api_json["conversion_rates"])
