from pyrogram import Client, filters
from pyrogram.types import Message
from utils import ButtonManager

button_manager = ButtonManager()

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = (
        "**📚 Bot Commands & Usage**\n\n"
        "Here are the available commands:\n\n"
        "👥 **User Commands:**\n"
        "• /start - Start the bot\n"
        "• /help - Show this help message\n"
        "• /about - About the bot\n\n"
    )
    await message.reply_text(help_text, reply_markup=button_manager.help_button())
