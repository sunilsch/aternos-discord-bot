import aternosapi
import asyncio
import os
import pathlib
def helpFile():
    return open('../txt/help.txt').read()
async def handle_response(message) -> str:
    author = message.author
    user_message = message.content
    channel = message.channel
    guildId = str(message.guild.id)
    os.get_exec_path
    if not os.path.exists("../config/"+guildId):
        os.mkdir("../config/"+guildId+"/")
        open('../config/'+guildId+'/aternosServer.txt', 'x').close()
        open('../config/'+guildId+'/aternosLogin.txt', 'w').close()
    p_message = str(user_message).lower()
    if p_message.startswith("!start"):
        asyncio.create_task(aternosapi.startServer(channel,guildId))
        return "Try to start"
    elif p_message.startswith("!set-server-id"):
        if author.guild_permissions.administrator:
            split = user_message.split(" ")
            if len(split) != 2:
                return "Invalid format"
            with open('../config/'+guildId+'/aternosServer.txt', 'w') as f:
                f.write(split[1])
            return "Set server ID to " + split[1]
        else:
            return "You're not allowed to change the server id"
    elif p_message.startswith("!set-login-cookie"):
        if author.guild_permissions.administrator:
            split = user_message.split(" ")
            if len(split) != 2:
                return "Invalid format"
            with open('../config/'+guildId+'/aternosLogin.txt', 'w') as f:
                f.write(split[1])
            return "Set login Cookie to " + split[1]
    elif p_message.startswith("!help"):
        return helpFile()
    else:
        return "nothing"