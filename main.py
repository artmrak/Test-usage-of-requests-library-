import requests

try:
    html = requests.get('https://www.google.com/search?q=coffee')
    print(html.status_code)
except Exception as error:
    print('This website is not available at the moment :(')
    print(error)

try:
    val = 56/0
    print(val)
except Exception as error:
    print(error)