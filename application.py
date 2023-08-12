import discord
from discord.ext import commands
from decouple import config
from wise_yoda import Quotes

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print("Whoops! I'm aware, hmm!")

@bot.command()
async def hello(ctx):
    quote = Quotes().random_quote()
    await ctx.send("*\``"+quote.description+"\``*")    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")

TOKEN = config('TOKEN')
bot.run(TOKEN)
