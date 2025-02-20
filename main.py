import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

async def main():
    # Включаем логирование
    logging.basicConfig(level=logging.INFO)
    
    # Инициализируем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Подключаем роутер с хендлерами
    dp.include_router(router)
    
    # Удаляем все обновления, которые произошли после последнего выключения бота
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 