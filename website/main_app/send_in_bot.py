import asyncio
from aiogram import Bot

token = '6128297834:AAEs7Hd1YdNu6LXrgNv_LNeHACuGhB6p0m0'
bot = Bot(token)

async def gg(text):
        await bot.send_message(5975226637, text)
        await bot.session.close()


def send_message(text):
    asyncio.run(gg(text))


