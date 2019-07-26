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

#logic to find if a proposed movie already exists in the watch list
def movie_exists(arg):
    videos = []
    movie = arg.lower()
    f = open("watch_list", 'r').readlines()
    for a in f:
        vids = a.strip().split(',')
        videos.append(vids[1])
    for film in videos:
        if movie == film.lower():
            return True
    return False



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
    role = discord.utils.get(member.guild.roles, name="Youngling")
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
        " I am C3PO, Human Cyborg Relations.",
        " I dont know what all this trouble is about, but I'm sure it must be your fault.",
        " His  High Exhaltedness, the great Jabba the Hutt, has decreed that you are to be terminated immediately.",
        " I am fluent in over six million forms of communication.",
        " Its against my protocol to impersonate a deity.",
        " I suggest a new strategy, let the Wookie win."
    ]
    i = random.randrange(0, len(greetings))
    await channel.send("Greetings, " + display_name + "." + greetings[i])


@client.command(pass_context=True, aliases =["Dice_roll","Dice_Roll", "DICE_ROLL"])
async def dice_roll(ctx, arg):
    author = ctx.message.author.display_name
    channel = ctx.message.channel
    if arg.isdigit() is False:
        await channel.send("Thats not a number...")
    elif int(arg) > 10000:
        await channel.send("Please use a number less than 10000")
    else:
        number = random.randrange(0, int(arg))
        await channel.send(author + " has rolled a " + str(number))


@client.command(pass_context=True, aliases = [])
async def suggestions(ctx, arg):
    author = ctx.message.author.display_name
    channel = ctx.message.channel
    if not movie_exists(arg):
        with open("watch_list", 'a') as f:
            f.write(author + "," + arg + "\n")
        await channel.send(author + ", " + str(channel) + ", " + arg + " has been added to the list")
    else:
        await channel.send(author + ", the movie already existed in the list")


@client.command(pass_context=True, aliases=[])
async def movie_list(ctx):
    author = ctx.message.author.display_name
    channel = ctx.message.channel
    await channel.send("Not implemented")

token = read_token()
client.run(token, reconnect=True)
