import aiogram
from .dispatcher_bot import dispatcher
from aiogram.types import Message
@ dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(massage: Message):
    await massage.answer(text= "Привіт, користувач")