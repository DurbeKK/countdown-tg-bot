from aiogram import types


async def set_default_commands(dp):
    """Set commands for the bot.

    This could have also been done directly through BotFather.
    """

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "about info"),
            types.BotCommand("help", "how to use the bot"),
        ]
    )