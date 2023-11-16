from typing import Callable, Awaitable, Dict, Any
from MyKeyboard import sub_channel
from aiogram import BaseMiddleware
from aiogram.types import Message


class CheckSubscription(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        char_member = await event.bot.get_chat_member("-1001543097478", event.from_user.id)
        if char_member.status == "left":
            await event.answer(
                "Подпишись на канал, чтобы пользоваться ботом!",
                reply_markup=sub_channel
            )
        else:
            return await handler(event, data)
