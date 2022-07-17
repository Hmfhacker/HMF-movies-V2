import aiohttp
from pyrogram import Client, filters

@Client.on_message(filters.command('Ustart') & filters.private)
async def start(_, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm a specialised bot for shortening links which can help you earn money by just sharing links. Made by <a href=\">ToonsHub</a>.")


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
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
