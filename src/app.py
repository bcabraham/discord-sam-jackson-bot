import os
import json

from discord import Client, Message
from dotenv import load_dotenv

client = Client()

# TODO: Move to json file or db
repl_dict = {}

ROOT_DIR = os.path.abspath(os.curdir)
data_path = os.path.join(ROOT_DIR, "data.json")

with open(data_path) as data:
    repl_dict = json.load(data)


def replace_all(text, dic) -> str:
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def get_help_message() -> str:
    commands = [f"{key}:\t\t\t{value}\n" for key, value in repl_dict.items()]

    msg = "> Look, motherfucker, here's some motherfuckin help:\n> \n"
    msg += "> Use this\tTo motherfucking get this\n> "
    msg += "> ".join(commands)

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
    elif "what" in message_lower:
        await message.reply("Say what again, motherfucker!")
    elif "!mf" in message_lower:
        reply_message = replace_all(message.content, repl_dict)
        await message.reply(reply_message)


def main(client):
    load_dotenv()

    client.run(os.getenv("DISCORD_API_TOKEN"))


if __name__ == "__main__":
    main(client)
