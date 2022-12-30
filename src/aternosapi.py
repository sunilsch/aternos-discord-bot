from python_aternos import Client
import bot
import asyncio

async def logIn(channel):
    global aternos, serverID
    aternos = Client.restore_session('../config/aternosLogin.txt')
    if(len(aternos.list_servers())) == 0:
        await bot.send_message("Login to aternos failed, please insert new cookie", channel)
        return False
    serverID = open('../config/aternosServer.txt').read()
    return True
async def getServer(channel):
    try:
        server = aternos.get_server(serverID)
    except:
        await bot.send_message("Can't reach server", channel)
        return None
    if(server == None):
        await bot.send_message("Can't reach server", channel)
    return server
async def startServer(channel):
    asyncio.sleep(1)
    if not await logIn(channel):
        return
    server = await getServer(channel)
    if(server == None):
        return
    if(server.status == "offline"):
        await bot.send_message("Server is starting....", channel)
    else:
        await bot.send_message("Server is currently not offline", channel)
        return
    server.start()
    task = asyncio.create_task(waitForServer(channel))
async def waitForServer(channel):
    server = await getServer(channel)
    while(server.status != "online"):
        await asyncio.sleep(2)
        server = await getServer(channel)
    await bot.send_message("Server is now online!", channel)
if __name__ == '__main__':
    startServer()