import asyncio
import sys
import logging

from aiogram import Bot
from handlers import dp

from config import TOKEN


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
