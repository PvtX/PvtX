import asyncio
import logging
from datetime import datetime

from pyrogram.enums import ChatType

import config
from AnieXEricaMusic import app
from AnieXEricaMusic.core.call import AMBOT, autoend
from AnieXEricaMusic.utils.database import get_client, is_active_chat, is_autoend

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        logger.info("Starting auto_leave task")
        while not await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME):
            from AnieXEricaMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in ["supergroup", "group", "channel"]:
                            chat_id = i.chat.id
                            if chat_id not in [
                                config.LOGGER_ID,
                                -1001603822916,
                                -1001775986475,
                                -1001829172962
                            ]:
                                if left == 20:
                                    break
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(chat_id)
                                        left += 1
                                        logger.info(f"Left chat {chat_id}")
                                    except Exception as e:
                                        logger.error(f"Failed to leave chat {chat_id}: {e}")
                except Exception as e:
                    logger.error(f"Error while iterating dialogs: {e}")

asyncio.create_task(auto_leave())

async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await AMBOT.stop_stream(chat_id)
                    logger.info(f"Stopped stream for chat {chat_id}")
                except Exception as e:
                    logger.error(f"Failed to stop stream for chat {chat_id}: {e}")
                try:
                    await app.send_message(
                        chat_id,
                        "» Bot automatically left video chat because no one was listening on video chat.",
                    )
                except Exception as e:
                    logger.error(f"Failed to send message to chat {chat_id}: {e}")

asyncio.create_task(auto_end())
