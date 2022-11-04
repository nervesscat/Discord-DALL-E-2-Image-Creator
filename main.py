from dalleIMG import dalleIMG
from censuredWords import censuredWords
import os
import discord

DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

client = discord.Client(intents = discord.Intents.all())
dalleClient = dalleIMG()
censuredWords = censuredWords()
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!create'):
        promp = message.content[8:]
        correctedPromp = censuredWords.deleteWords(promp)
        image_url = dalleClient.get_dalle(correctedPromp)
        await message.channel.send(image_url)
        

client.run(DISCORD_TOKEN)