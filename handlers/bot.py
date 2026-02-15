import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database.db import init_db  # make sure you have a working db.py

# Routers
from handlers.start import router as start_router
from handlers.name_handler import router as name_router

async def main():
    # Initialize database
    init_db()

    # Create bot & dispatcher
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Register routers
    dp.include_router(start_router)
    dp.include_router(name_router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
