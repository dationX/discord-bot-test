import discord
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$random'):
        number = random.randint(0, 10)
        await message.channel.send(f"Рандомное число от 0 до 10: **{number}**")
    elif message.context.startswith("$monetka"):
        actions = ("Орел", "Орешка")
        await message.channel.send(f"**{random.choice(actions)}**")
    else:
        await message.channel.send(message.content)

client.run("YOUR TOKEN DISCORD BOT")
