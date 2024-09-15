import discord
from discord.ext import commands
import random
from random import choice
import asyncio
import os
from os import listdir

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.reply(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.reply("he" * count_heh)

@bot.command()
async def Bye(ctx):
    await ctx.reply("\U0001f642")

@bot.command()
async def rand_value(ctx, min, max):
    value = random.randint(min, max)
    await ctx.reply(f"Рандомное число от {min} {max}: **{value}**")

@bot.command()
async def monetka(ctx):
    actions = ("Орел", "Решка")
    await ctx.reply("Ииииии! Выпадает....")
    await asyncio.sleep(3)
    await ctx.reply(f"Выпадает {choice(actions)}")

@bot.command()
async def gen_pass(ctx, len_password=6):
    chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for _ in range(int(len_password)):
        password += random.choice(chars)
    await ctx.reply(f"Ваш пароль длиной {len_password} символов: ||**{password}**||")

@bot.command()
async def courses(ctx):
    courses_moneys = {
        "Доллар": "90,64",
        "Евро": "100,45",
        "Фунт стерлингов": "118,95",
        "Юань": "12,78",
        "Тайский бат": "2,73"
    }
    await ctx.reply(f"Курсы валют на момент **15.09.2024**")
    for value in courses_moneys:
        await ctx.send(f"**{value}**: *{courses_moneys[value]}*")

# Калькулятор нарушает работу остальных команд, используйте или только калькулятор или для остальных комманд комментируйте эту часть кода

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     for char in message.content:
#         if char in ("+", "-", "*", "/", "**"):
#             await message.channel.send(f"Результат: **{eval(message.content)}**")
#             return
    
@bot.command()
async def mem(ctx):
    # mems_directory = ("images/mem1.jpg", "images/mem2.jpg", "images/mem3.jpg")
    directory = random.choice(listdir('images'))
    with open (f"images/{directory}", "rb") as photo:
        mem_photo = discord.File(photo)
    strings_for_mem = ("Лови свой мем!", "С удовольствием предоставляю тебе мем!", "Держи мем!", "Желаю тебе посмеяться! :)",
                       "Вот твой мем: ", "Надеюсь тебе понятно, над чем тут надо смеяться", "ВХАХВХАХВАХВХАХВАХВХАВХАХВАХ",
                       "Приятного хохотания!", "Надеюсь тебе этот мем понравится", "Кто у нас тут мем заказывал? Держи!")
    await ctx.send(choice(strings_for_mem), file=mem_photo)

bot.run("YOUR TOKEN")
