import responses
import discord

async def send_message(message,channel):
    try:
        await channel.send(message)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = open('../config/discordToken.txt').read()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        response = await responses.handle_response(message)
        await send_message(response,message.channel)
    
    client.run(TOKEN)