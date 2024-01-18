import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher
from config_reader import config
from MessageHandler import ButtonHandler, MessageAns
from middleware.check_sub import CheckSubscription
from postSQL import connection, execute_read_query, execute_query

bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
routers = [ButtonHandler.router, MessageAns.router]


async def send_messages_to_users(loop):
    now = datetime.now()
    connection.autocommit = True
    select_users = "SELECT tg_id FROM users"
    users_id = execute_read_query(connection, select_users)
    if now.hour == 19:
        for user_id in users_id:
            await bot.send_message(chat_id=user_id[0], text="Test database")

    await asyncio.sleep(10)
    loop.call_later(10, lambda: loop.create_task(send_messages_to_users(loop)))


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.call_later(10, lambda: loop.create_task(send_messages_to_users(loop)))
dp = Dispatcher()
dp.message.middleware(CheckSubscription())
dp.include_routers(*routers)
loop.run_until_complete(dp.start_polling(bot, skip_updates=True))

# async def main():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.call_later(10, lambda: loop.create_task(anton(loop)))
#
#     dp = Dispatcher()
#     dp.message.middleware(CheckSubscription())
#
#     dp.include_routers(ButtonHandler.router, MessageAns.router)
#     # await bot.delete_webhook(drop_pending_updates=True)
#     # await dp.start_polling(bot)
#     loop.run_until_complete(dp.start_polling(bot, skip_updates=True))
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
