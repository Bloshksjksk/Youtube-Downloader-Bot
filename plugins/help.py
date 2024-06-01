from pyrogram import Client, filters, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("𝐓𝐑𝐔𝐌𝐁𝐎𝐓𝐒", url="https://t.me/movie_time_botonly")]]
    )
@Client.on_message(filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_photo(photo="https://th.bing.com/th/id/OIG4.kIKwAP6q4rN21rOhb71Z?pid=ImgGn",caption=helptxt,reply_markup=keyboard)
