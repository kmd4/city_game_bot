import asyncio
from src.constants import *
from handlers.handlers import router
from aiogram import Bot, Dispatcher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
