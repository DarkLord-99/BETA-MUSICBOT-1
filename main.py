import asyncio
from pytgcalls import idle
from Beta.jeol import SUPPORT
from Beta.main import call_py, bot, user as Herox

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()
    await bot.join_chat("beta_bot_updates")
    await Herox.send_message(
               SUPPORT,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )    
                          
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
