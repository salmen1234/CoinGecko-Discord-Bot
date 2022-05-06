import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import soupsieve

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
    
    def trend(self):
        response = requests.get(url + 'search/trending').json()['coins']

        coins = []

        for coin in response:
            coins.append(coin['item'][0])

        return coins

cg = CoinGecko()

@bot.command()
async def price(ctx, value1):
    price = cg.price(value1, 'usd', 'false')

    await ctx.send(str(value1) + ' price is ' + str(price[value1]['usd']) + '$' + '.') 

@bot.command()
async def search(ctx, value1):
    try:
        search = cg.search(value1)
        search_url = 'https://www.coingecko.com/en/coins/' + search.lower()

        res = requests.get(search_url).text
        soup = BeautifulSoup(res, 'lxml')
        images = []

        for img in soup.findAll('img'):
            images.append(img.get('src'))
                
        thumb = images[12]
        author_img = images[0]

        embed = discord.Embed(title=search, url=search_url, color=0x2491CF)
        embed.set_author(name='Coin Gecko', icon_url=author_img)
        embed.set_thumbnail(url=thumb)
        
        await ctx.send(embed=embed)
    except:
        await ctx.send('"' + value1 + '" ' + 'does not exist.')

@bot.command()
async def trend(ctx):
    trendings = cg.trend()

    embed = discord.Embed(title='Trending coins in last 24hours', color=0x2491CF)

    for trend_coin in trendings:
        embed.add_field(name=trend_coin, value=trendings)

    await ctx.send(embed=embed)

bot.run(token)
