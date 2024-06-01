from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/movie_time_botonly")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/fligher")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name} i am YouTube Video Downloader Bot\nSimply Send a Youtube Link to me</b>\n/help for More info"
    await message.reply_photo(photo="https://th.bing.com/th/id/OIG4.kIKwAP6q4rN21rOhb71Z?pid=ImgGn",caption=welcomed, reply_markup=joinButton)
    raise StopPropagation
    
@Client.on_message(filters.command(["about"]), group=-2)
async def about(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/movie_time_botonly")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/fligher")]
    ])
    abouttxt = f"""<b>✯ Mʏ Nᴀᴍᴇ : YouTubeDownloader</b>
<b>✯ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/fligher>☢ Owner of TrumBots ☢</a></b>

<b>✯ Uᴘᴅᴀᴛᴇs : <a href=https://t.me/movie_time_botonly>TrumBots Updates 👾</a></b>

<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ2.0.62 [Sᴛᴀʙʟᴇ]</b>"""
    x=await message.reply_text(photo="https://th.bing.com/th/id/OIG4.kIKwAP6q4rN21rOhb71Z?pid=ImgGn",caption=abouttxt, reply_markup=joinButton)
    await asyncio.sleep(8)  # Wait for 5 seconds before deleting the message
    await x.delete()
    raise StopPropagation
