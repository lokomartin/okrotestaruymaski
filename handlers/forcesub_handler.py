# (c) @AbirHasan2005 & @HuzunluArtemis

import asyncio
from configs import Config
from pyrogram import Client
from handlers.database.access_db import db
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.FORCE_SUB_CHANNEL) if Config.FORCE_SUB_CHANNEL.startswith("-100") else Config.FORCE_SUB_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.chat.id,
                text=f"Sorry, You are Banned! You will be Kicked from This Group within {Config.AUTO_KICK_TIME} Seconds.\n" \
                    f"Sorry, Banned ka Kabayan! Maglalaho ka parang bula sa loob ng {Config.AUTO_KICK_TIME} Segundo.\n\n" \
                    f"Contact / Bildir: {Config.CONTACT_ADRESS}.",
                disable_web_page_preview=True,
                reply_to_message_id=cmd.message_id
            )
            await asyncio.sleep(int(Config.AUTO_KICK_TIME))
            return 404
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.FORCE_SUB_CHANNEL) if Config.FORCE_SUB_CHANNEL.startswith("-100") else Config.FORCE_SUB_CHANNEL))
        except FloodWait as e:
            print(f"Sleep of {e.x}s caused by FloodWait")
            await asyncio.sleep(e.x)
            return 200
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.FORCE_SUB_CHANNEL}\n\nError: {err}")
            return 200
        send_ = await bot.send_message(
            chat_id=cmd.chat.id,
            text = f"""
Hey {cmd.from_user.mention}, seems like you haven't joined our channel. Please [Join Channel]({invite_link.invite_link}) and turn back here!
Hoy {cmd.from_user.mention}, hindi ka pa ata ng join sa channel ko. Paki [Join Channel]({invite_link.invite_link}) at bumalik ka dito!""",
            reply_to_message_id=cmd.message_id,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🤖 Join / Katıl", url=invite_link.invite_link)]
                ]
            )
        )
        await db.set_group_message_id(cmd.from_user.id, group_message_id=send_.message_id)
        return 400
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait")
        await asyncio.sleep(e.x)
        return 200
    except Exception as err:
        print(f"Unable to do Force Subscribe to {Config.FORCE_SUB_CHANNEL}\n\nError: {err}")
        return 200
