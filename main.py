from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?',description='Bot')

token = 'OTcxMzk2NTM3MzM2ODgxMTky.YnJ5hg.-ilV17ct5oOKWEiHX7a-fcx-Xsk'

cg = CoinGeckoAPI()

@bot.command()
async def price(ctx, value1):
    prices = cg.get_price(ids=value1, vs_currencies='eur')
    
    await ctx.send("Le prix du(de l') " + value1 + ' est de : ' + str(prices[value1]['eur']) + '€')


bot.run(token)