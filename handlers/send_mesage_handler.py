# (c) @AbirHasan2005 & @HuzunluArtemis

import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards import inline_keyboard_markup

async def sendMessage(bot: Client, text: str, message_id: int, chat_id: int, reply_markup: inline_keyboard_markup):
    """
    Custom Send Message Function with FloodWait Error Handler & Website Preview Disabled. You can Send Message with a Reply to Group Message.

    :param bot: Pass Bot Client.
    :param text: Pass Text for Reply.
    :param message_id: Pass Message ID for Reply.
    :param chat_id: Pass Group Chat ID.
    """
    
    try:
        sentmessage = await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=message_id,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return sentmessage
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait")
        await asyncio.sleep(e.x)
        await sendMessage(bot, text, message_id, chat_id)
