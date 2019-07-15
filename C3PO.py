import discord
import json
import time
import aiohttp
import asyncio
from discord import Game
from discord.ext.commands import Bot

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')

@client.event
async def wait_until_login():
    await client.change_presence(game=discord.Game(name="Looking for   Master"))
    print("C-3PO is booting up." + cient.user.name)


@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hello, I am C-3PO, human cyborg relations.")

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "575157257126281238":
                print ("Welcome {member.mention} to the Galactic Republic.")

@client.event
async def on_member_join(member):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Youngling")
    await client.add_roles(user, role)

@client.event
async def on_member_remove(member):
    print(member.name + ", has left the Republic.  The Force has weakened")

@client.event
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.clientSession() as session:
        raw_response = await session.get(url)
        repsonse = await raw_response.next()
        repsonse = json.loads(response)
        await client.say("Bitcoin price: $" + response['bpi']['USD']['rate'])

#Bot Commands Section ---------------------------------

client.run(token)
