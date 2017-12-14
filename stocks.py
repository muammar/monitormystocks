import json
import requests

def get_stock_price(stock):
    """docstring for get_stock_price"""

    url = 'https://finance.google.com/finance?q={}&output=json' .format(stock)
    rsp = requests.get(url)
    if rsp.status_code in (200,):

        # This magic here is to cut out various leading characters from the JSON
        # response, as well as trailing stuff (a terminating ']\n' sequence), and then
        # we decode the escape sequences in the response
        # This then allows you to load the resulting string
        # with the JSON module.
        fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
        print(fin_data)

        # print out some quote data
        print('Opening Price: {}'.format(fin_data['op']))
        print('Price/Earnings Ratio: {}'.format(fin_data['pe']))
        print('52-week high: {}'.format(fin_data['hi52']))
        print('52-week low: {}'.format(fin_data['lo52']))

get_stock_price('AAPL')
