# DO NOT REMOVE CREDITS
# Copyright (c) 2021 dakshy/droplink-bot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('8967766')
API_HASH = environ.get('505dc1f394f59c8a55b1aa798a0715f9')
BOT_TOKEN = environ.get('5071513445:AAHu03aJqQ2728J6RbYFF23JlYXG3JtYa0g')
API_KEY = environ.get('87855078f16e4cb79931428f7efd9454a4767ef7')

bot = Client('droplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('Ustart') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm a specialised bot for shortening links which can help you earn money by just sharing links. Made by <a href=\">ToonsHub</a>.")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
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


bot.run()
