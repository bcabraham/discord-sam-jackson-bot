import os
import random
import datetime

from discord import Client, Message
from dotenv import load_dotenv

from utils import load_data

load_dotenv()
START_TIME = datetime.datetime.now()

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


def get_uptime():
    current_time = datetime.datetime.now()

    diff = current_time - START_TIME

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return (hours, minutes, seconds)


def get_status():
    hours, minutes, seconds = get_uptime()

    msg = (
        "I'm a mushroom cloud laying motherfucker, motherfucker! "
        + "I'm superfly TNT. I'm the Guns of the motherfuckin Navarone.\n"
        + f"I've been up for {hours} goddamn hours, "
        + f"{minutes} motherfuckin minutes and "
        + f"{seconds} fuckin seconds.\n"
        + 'My status is: "Bad Motherfucker"'
    )

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
    elif message_lower == "!mf status":
        await message.reply(get_status())
    elif "what" in message_lower and random.random() < 0.333:
        await message.reply("Say what again, motherfucker!")
    elif "!mf" in message_lower:
        reply_message = replace_all(message.content, repl_dict)
        await message.reply(reply_message)


def main(client):
    client.run(os.getenv("DISCORD_API_TOKEN"))


if __name__ == "__main__":
    main(client)
