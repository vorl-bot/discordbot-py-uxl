from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import gacha
import fishingresult

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!', reference=message)

     #가챠
    if message.content.startswith(f'{PREFIX}가챠'):
        gacha_result = gacha.getGacha()
        gacha_message = '달그락, 달그락... <'+gacha_result+'>이(가) 나왔다!'
        await message.channel.send(gacha_message, reference=message)

    #다이스(1d100)
    if message.content.startswith(f'{PREFIX}다이스'):
        d = random.randrange(1,101)
        embed = discord.Embed(description=":game_die:도르르륵...",
                            color=0x000000)
        embed.add_field(name=d, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #동전
    if message.content.startswith(f'{PREFIX}동전'):
        c = random.choice(['앞면','뒷면'])
        embed=discord.Embed(description=":coin:팅그르르...",
                            color=0x61b866)
        embed.add_field(name=c, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #낚시
    if message.content.startswith(f'{PREFIX}낚시'):
        
        fish = fishingresult.fishresult()

        text1 = fish[0]
        text2 = fish[1]        

        embed = discord.Embed(title = '즐거운 낚시 시간!',
                              description = '낚싯대를 잡아당기면...',
                              color = discord.Color.blue())
        embed.add_field(name = text1, value = text2, inline=False)

        await message.channel.send(embed=embed, reference=message)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")