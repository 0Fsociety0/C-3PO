import discord
import random
import requests
from discord.ext import commands


client = commands.Bot(command_prefix='./')


#Handlers
#get_bitcoin() is used in bitcoin bot command to gather data
def get_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    return data


#log() can be used in multiple commands and events when you need to log some shit.
def log(log_message):
    f = open('logfile.txt', 'a')
    f.write(log_message)


#read_token, obviously
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
    return lines[0].strip()


###Client Events###
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="TestRole")
    await member.add_roles(role)


###Client Commands###
@client.command(pass_context=True, aliases = ['Bitcoin', 'BITCOIN'])
async def bitcoin(ctx):
    data = get_bitcoin()
    channel = ctx.message.channel
    await channel.send('Bitcoin price is currently: ' + data['bpi']['USD']['rate'])



@client.command(pass_context=True, aliases = ['Hello', 'HELLO'])
async def hello(ctx):
    channel = ctx.message.channel
    display_name = ctx.author.display_name
    greetings = [
        " I am C3PO, Human Cyborg Relations",
        " I dont know what all this trouble is about, but I'm sure it must be your fault",
        " His  High Exhaltedness, the great Jabba the Hutt, has decreed that you are to be terminated immediately",
        " I am fluent in over six million forms of communication",
        " Its against my protocol to impersonate a deity",
        " I suggest a new strategy, let the Wookie win."
    ]
    i = random.randrange(0, len(greetings))
    await channel.send("Greetings, " + display_name + "." + greetings[i])


token = read_token()
client.run(token, reconnect=True)
