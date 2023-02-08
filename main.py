from telethon.sync import TelegramClient, events
from telethon import utils
from telethon.tl.functions.account import UpdateProfileRequest
from asyncio import sleep

import configparser



config = configparser.ConfigParser()
config.read("config.ini")



client = TelegramClient(
    "bot",
    int(config["MAIN"]["API_ID"]),
    config["MAIN"]["API_HASH"]
)
client.start()



@client.on(events.NewMessage(pattern=r"(?i).spam"))
async def spam(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        try:
            await event.delete()
            for i in range(int(str(event.text.split('||')[0]).split("spam ")[1])):
                await event.respond(event.text.split('||')[1])
        except:
            pass



@client.on(events.NewMessage(pattern=r"(?i).work"))
async def work(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        await event.delete()
        config.read("config.ini")
        await client(UpdateProfileRequest(first_name=config["MAIN"]["work"]))



@client.on(events.NewMessage(pattern=r"(?i).afk"))
async def afk(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        await event.delete()
        config.read("config.ini")
        await client(UpdateProfileRequest(first_name=config["MAIN"]["afk"]))



@client.on(events.NewMessage(pattern=r"(?i).sleep"))
async def sleep(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        await event.delete()
        config.read("config.ini")
        await client(UpdateProfileRequest(first_name=config["MAIN"]["sleep"]))



@client.on(events.NewMessage(pattern=r"(?i).eth"))
async def eth(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["eth"])



@client.on(events.NewMessage(pattern=r"(?i).btc"))
async def btc(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["btc"])



@client.on(events.NewMessage(pattern=r"(?i).tron"))
async def tron(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["tron"])



@client.on(events.NewMessage(pattern=r"(?i).usdt"))
async def usdt(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["usdt"])



@client.on(events.NewMessage(pattern=r"(?i).qiwi"))
async def qiwi(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["qiwi"])



@client.on(events.NewMessage(pattern=r"(?i).ymoney"))
async def ymoney(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["ymoney"])



@client.on(events.NewMessage(pattern=r"(?i).lolz"))
async def lolz(event):
    if int(event.message.from_id.user_id) == int((await client.get_entity("me")).id):
        config.read("config.ini")
        await event.edit(config["MAIN"]["lolz"])



while True:
    try:
        client.run_until_disconnected()
    except:
        client.run_until_disconnected()
