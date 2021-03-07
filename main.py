import os

import discord
from dotenv import load_dotenv

repl_dict = {"!MF": "motherfucker", "!mf": "motherfucking"}


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def get_help_message() -> str:
    msg = "> Motherfucker, here's some motherfuckin help:\n> \n"
    msg += "> Use this\tTo motherfucking get this\n> "
    msg += "> ".join([f"{key}:\t\t{value}\n" for key, value in repl_dict.items()])

    return msg


load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print("I have motherfuckin arrived!")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    message_lower = message.content.lower()

    if message_lower == "!mf help":
        await message.reply(get_help_message())
    elif "what" == "".join(e for e in str(message_lower).strip(" ") if e.isalnum()):
        await message.reply("Say what again, motherfucker!")
    elif "!mf" in message_lower:
        reply_message = replace_all(message.content, repl_dict)
        await message.reply(reply_message)


client.run(os.getenv("DISCORD_API_TOKEN"))
