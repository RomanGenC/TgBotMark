import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config
from MessageHandler import ButtonHandler, MessageAns
from middleware.check_sub import CheckSubscription


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.message.middleware(CheckSubscription())

    dp.include_routers(ButtonHandler.router, MessageAns.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Some changes test
    asyncio.run(main())
