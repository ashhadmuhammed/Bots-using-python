from telethon import TelegramClient, events,Button
from cryptography.fernet import Fernet

api_id = ''
api_hash = ''
key = ''
# Create the client and connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start()
print(key)
@client.on(events.NewMessage(pattern="^/start"))
async def start_handler(event):

    print(event.raw_text)
    await event.respond('Hello World!')

@client.on(events.NewMessage(pattern='^/encrypt'))
async def encrypt_handler(event):

    _,message=event.raw_text.split("/encrypt")
    print(_)
    print(message)

    # value of key is assigned to a variable
    m=bytes(message,'utf-8')
    print(m)
    f = Fernet(key)
    # the plaintext is converted to ciphertext
    token = f.encrypt(m)
    print(type(token))
    await event.respond(token.decode())


@client.on(events.NewMessage(pattern='^/decrypt'))
async def encrypt_handler(event):

    _,message=event.raw_text.split("/decrypt")
    print(_)
    print(message)

    # value of key is assigned to a variable
    m=bytes(message,'utf-8')
    print(m)
    f = Fernet(key)
    # the plaintext is converted to ciphertext
    token = f.decrypt(m)
    print(type(token))
    await event.respond(token.decode())


client.run_until_disconnected()



