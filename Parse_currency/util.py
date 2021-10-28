def f1nd(currency):
    import requests
    response = requests.get('https://bitpay.com/api/rates')
    tosearch = response.json()
    for i in tosearch:
        if i['code'] == currency:
            return str(i['rate'])

# print(type(f1nd('UAH')))

