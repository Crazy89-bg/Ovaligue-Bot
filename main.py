import discord
import time as cwazy
from function import *
from annoucemment import *


client = discord.Client()

print("WAIT")

@client.event
async def on_ready():
    print("Vous êtes sur {0.user}".format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.channel.send(entry)

client.run("ODQ5Mzg3NTA1NzIyNTg5MjI2.YLabwg.KDCulqa5BOLJW-RRk_68JgDKKW0")
