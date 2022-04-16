import os
import random

from discord import Client, Message
from dotenv import load_dotenv

from utils import load_data

load_dotenv()

client = Client()

repl_dict = load_data("data.json")


def replace_all(text, dic) -> str:
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def get_help_message() -> str:
    commands = [f"{key}:\t\t\t{value}\n" for key, value in repl_dict.items()]

    msg = "> Look, motherfucker, here's some motherfuckin help:\n> \n"
    msg += "> Use this\tTo motherfucking get this\n> "
    msg += ":\t".join(commands)

    return msg


@client.event
async def on_ready():
    print("I have motherfuckin arrived!")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    message_lower = message.content.lower()

    if message_lower == "!mf help":
        await message.reply(get_help_message())
    elif "what" in message_lower and random.random() < 0.333:
        await message.reply("Say what again, motherfucker!")
    elif "!mf" in message_lower:
        reply_message = replace_all(message.content, repl_dict)
        await message.reply(reply_message)


def main(client):
    client.run(os.getenv("DISCORD_API_TOKEN"))


if __name__ == "__main__":
    main(client)
