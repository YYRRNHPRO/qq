from settings import settings
import discord
from discord.ext import commands
import os, random
import requests



intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh )
@bot.command()
async def commandss(ctx,):
    await ctx.send("commands: $hello - привет я бот ...  $heh - heh x5  $mem - random mem  $duck - random duck meme  $dog - random dog meme  $fox - random fox meme" )

@bot.command()
async def mem(ctx):
    img_name=random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('fox')
async def fox(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)


bot.run(settings["TOKEN"])
    
