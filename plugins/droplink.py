import aiohttp
from pyrogram import Client, filters

@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(_, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        await message.reply(f'**Long URL:** {links[num]}\n**Shortened URL:** {short_link}\n\nMade by <a href="https://github.com/dakshy">ToonsHub</a>', quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://shorturllink.in/api'
    params = '87855078f16e4cb79931428f7efd9454a4767ef7'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
