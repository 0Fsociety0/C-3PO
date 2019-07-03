import time
import json
import aiohttp
import asyncio
import discord
from discord import Game
from discord.ext import commands

messages = joined = 0
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()
client = discord.Client()
client = commands.Bot(command_prefix = './')

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("logs.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

                messages = 0 
                joined = 0

                await asyncio.sleep(5)
         except Exception as e:
                print(e)
                await asyncio.sleep(5)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("Eurphuct") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Do not try that!")

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel is member.server.channels:
        if str(channel) == "general":
            await channnel.send (f"""Welcome to the Galactic Republic {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild('fill this with ID')
    channels = ["commands"]
    valid_users = ["Eurphuct#3594"]
    bad_words = ["Nigger", "Nig", "nigger", "nig", "Faggot", "fag"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("Ah ah ahhhhh, that was naughty")
            await message.channel.purge(limit=1)

        if message.content == "./help":
            embed = discord.Embed(title="Help on C-3PO", description="My commands"
            embed.add_field(name="./hello", value="Greets the user")
            embed.add_field(name="./users", value="Prints number of users")
            embed.add_field(name="./bitcoin", value="Currency of bitcoin")
            embed.add_field(name="./ping", value="Will tell you your ping")
            await message.channel.send(content=None, embed=embed)

        if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("./hello") ./= -1:
        await message.channel.send("Hello, I am C-3PO.  I am here to serve you.")
        elif message.content == "./users":
        await message.channel.send(f"""# of Members: {id.member_count}""")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print('C-3PO is booting up.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Youngling')
    await client.add_roles(member, role)

@client.event
async def on_member_join(member):
    print("A new Youngling named " + member.name + " has joined the force.")
    await client.send_message(member, newUserMessage)
    print("sent message to " + member.name)

@client.event
async def on_member_remove(member):
    print(member.name + "has left the Republic.  The Force has weakened")
    
@client.event
async def bitcoin():
    url = 'https:///api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.clientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])



#Bot commands section

@client.command
async def ping(ctx):
    await client.send(f'Pong! {round(Bot.latency * 1000}ms')


client.loop.create_task(update_logs())
client.run(token)
