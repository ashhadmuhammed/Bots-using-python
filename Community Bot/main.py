from telethon import TelegramClient, events, Button, functions
import os

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 20315645
api_hash = '4b643a7d1ab5a3171aa4c3046b21973a'
enqno = 0
#5894568672:AAGwrjUr1Zkdvn9ei-OoPk-WcEMYydAbj64
LOCK = 1
# Create the client and connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start()
keyboard = [
    [

        Button.inline("Materials", data=b"Materials"),
        Button.url("Enquiry","https://mail.google.com/mail/u/0/?fs=1&to=ktumcacommunity20@gmail.com&su=&body=&bcc=&tf=cm")
    ],

    [
        Button.url("Go", "https://techworldthink.github.io/MCA/")
    ]
]

keyboard1 = [
    [
        Button.inline("S1", data=b"s1"),
        Button.inline("S2", data=b"s2"),
        Button.inline("S3", data=b"s3"),
        Button.inline("S4", data=b"s4"),
        Button.inline("Back", data=b'back')
    ]

]

keyboard12 = [
    [
        Button.inline("Syllabus", data=b"syllabus12"),
    ],
    [

        Button.inline("AN", data=b"an"),
        Button.inline("ADBMS", data=b"adbms"),
        Button.inline("ADS", data=b"ads"),

    ],
    [
        Button.inline("Statistics", data=b"stati"),
        Button.inline("OB", data=b"ob"),
    ],
    [
        Button.inline("AI", data=b"ai"),
        Button.inline("IPR", data=b"ipr"),
    ]
]

keyboard11 = [
    [
        Button.inline("Syllabus", data=b"syllabus12"),
    ],
    [
        Button.inline("MATH", data=b"maths"),
        Button.inline("DFCA", data=b"dfca"),
        Button.inline("SE", data=b"se"),
        Button.inline("ADS", data=b"ads"),

    ],
    [Button.inline("Back", data=b'back')]

]

k = [keyboard, ]


@client.on(events.ChatAction())
async def handler(event):
    # Check if the message is a new member join event
    if event.user_joined or event.user_added:
        await event.reply("Welcome to KTU MCA COMMUNITY")


@client.on(events.NewMessage())
async def grpmessage(event):
    if LOCK:

        if "result" in event.message.message:
            print(LOCK)
            await client.send_message(event.chat_id, "Expecting in 2 weeks")
            print(event.chat_id)

        elif event.message.message == '/start':
            await client.send_message(event.chat_id, "Choose an option:", buttons=keyboard)


        # remove user with abusive content

        elif event.message.message.lower() in ['', 'poda', 'podi']:
            # Kick some user from some chat, and deleting the service message
            sender = await event.get_sender()
            print(sender.id)
            try:
                msg = await client.kick_participant(event.chat_id, sender.id)
                await msg.delete()
            except:
                print("admin error")


@client.on(events.CallbackQuery)
async def callback_query_handler(event):
    if event.data == b"Materials":

        await client.send_message(event.chat_id, "Choose year:", buttons=keyboard1)
    elif event.data == b'enquiry':
        global LOCK
        LOCK = 0




        # await client.send_message(event.chat_id, "Enter your NAME,KTU REGISTER NO,QUERY in line by line")
        #
        # @client.on(events.NewMessage())
        # async def enquiry_handler(event):
        #
        #     enquiry_data = event.message.message.split()
        #     global enqno
        #     enqno += 1
        #     path = (r"C:\Users\MCA\Desktop\Enquiries")
        #     path += "\\" + "enq" + str(enqno) + ".txt"
        #
        #     f = open(path, 'w')
        #     for i in enquiry_data:
        #
        #         f.write(str(i)+'\n')
        #     f.close()
        #     await event.reply("Query sent..")






    elif event.data == b"s1":

        await client.send_message(event.chat_id, "Here are the subjcts:", buttons=keyboard11)
        k.append(keyboard1)
    elif event.data == b"s2":

        await client.send_message(event.chat_id, "Choose year:", buttons=keyboard12)
        k.append(keyboard1)

    elif event.data == b"syllabus12":
        await client.send_file(event.chat_id, r'C:\Users\MCA\Desktop\pythonProject\MCA\s3.pdf', caption='Syll')

    elif event.data == b'an':
        os.chdir('C:\\Users\\MCA\\Desktop\\pythonProject\\MCA\\crypto')
        files = os.listdir()
        for i in files:
            await event.answer("Downloading...")
            await client.send_file(event.chat_id, i, caption='')

    elif event.data == b"back":
        if len(k) > 1:
            await client.send_message(event.chat_id, "Choose year:", buttons=k[-1])
            k.pop()


client.run_until_disconnected()
