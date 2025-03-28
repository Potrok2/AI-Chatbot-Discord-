import discord
import openai
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  
    
    if message.content.startswith("/ask"):
        prompt = message.content[5:].strip()
        if not prompt:
            await message.channel.send("Please provide a question.")
            return
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response["choices"][0]["message"]["content"]
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send("Error fetching response. Try again later.")
            print(e)


client.run(TOKEN)
## CHANGE THE TOKEN 
## CREDITS : POTROK
## CREDITS : https://github.com/Potrok2