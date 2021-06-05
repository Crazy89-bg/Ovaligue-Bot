import discord
import time as cwazy
from function import *


client = discord.Client()
token()
chargement_turtle()
print("WAIT")
cwazy.sleep(5)


@client.event
async def on_ready():
    print("Vous êtes sur {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!annonce'):
        i = 1
        while i == 1:
            annonce = str(input("Annonce : "))
            await message.channel.send(annonce)


client.run(f"{token}")
