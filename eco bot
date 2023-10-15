from settings import settings
import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


non_eco_products = [
    'Пластиковые изделия',
    'Мясо и молочные продукты',
    'Продукты с высоким содержанием сахара и соли',
    'Фаст-фуд и обработанные продукты',
    'Продукты с высоким уровнем ингредиентов GMO',
    'Продукты, выращиваемые с использованием пестицидов и гербицидов',
    'Продукты, произведенные на дальние расстояния'
]

@bot.command()
async def e1mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


eco_memes = [
    'Осень в Нью-Йорке очаровательна — можно любоваться тем, как мусор меняет цвета',
    'Самый чистый путь во Вселенную лежит через лесную глушь',
    'Леса — величайшие источники здоровья и вдохновения.',
    'Мы готовы срубить дерево, если нам нужна зубочистка.',
    'Природу легче всего подчинить, повинуясь ей.'
]

@bot.command()
async def emem(ctx):
    await ctx.send(random.choice(eco_memes))

@bot.command()
async def neeco(ctx):
    await ctx.send(random.choice(non_eco_products))

@bot.command()
async def helpp(ctx):
    await ctx.send('$e1mem - случайный эко мем (картинки)   $emem - эко текст мем   $neeco - неэкологичные продукты')

bot.run(settings["TOKEN"])
