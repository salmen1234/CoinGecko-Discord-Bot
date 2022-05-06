from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?',description='Bot')

token = 'Bot Token'

url = 'https://api.coingecko.com/api/v3/'

class CoinGecko():
    def price(self, ids, vs_currencies, include_market_cap):
        query = {
            'ids': ids,
            'vs_currencies': vs_currencies,
            'include_market_cap': include_market_cap
        }

        response = requests.get(url + 'simple/price', params=query).json()

        return response

    def supported_currencies(self):
        response = requests.get(url + 'simple/supported_vs_currencies').json()      

        return response

    def search(self, keyword=''):
        query = {'query': keyword}

        response = requests.get(url + 'search', params=query).json()['coins'][0]['name']

        return response

cg = CoinGecko()

#price = cg.price(ids='ethereum', vs_currencies='sats', include_market_cap='false')
#supported_c = cg.supported_currencies()
search = cg.search('')

#print(price)
#print(list)
print(search)
