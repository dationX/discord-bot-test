import discord
from discord.ext import commands
import random
from random import choice
import asyncio

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

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    for char in message.content:
        if char in ("+", "-", "*", "/", "**"):
            await message.channel.send(f"Результат: **{eval(message.content)}**")
            return

bot.run("YOUR TOKEN")
