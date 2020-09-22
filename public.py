import asyncio
from telethon import TelegramClient

async def auth():
    # register session session(str), api_id(int), api_hash(str) on client connect by https://my.telegram.org/auth
    session = "CLIENT"
    api_id = 11111111
    api_hash = "giohehreorgi32i5hjr3489tyh34y98thy3948tr5"
    client = TelegramClient(session, api_id, api_hash)
    await client.start()
    await public(client)

async def public(client):
    # parsing and sorting group members by parameters ;)
    _list = []
    chat = "@binanceexchange"
    # target group
    try:
        async for users in client.iter_participants(chat):
            _list.append(users)
            if users.bot == False and users.deleted == False and users.is_self == False not in _list:
                # print example users.id and user.username ........
                print(users)
    except:
        pass

async def main():
    await auth()

if __name__ == '__main__':
    asyncio.run(auth())

