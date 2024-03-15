import discord
import aiohttp
import requests

# Khai báo token của bot
TOKEN = 'token here'

# Khởi tạo client với các intents cần thiết
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.guild_messages = True
intents.members = True

client = discord.Client(intents=intents)

# Event khi bot được kết nối
@client.event
async def on_ready():
    print('Bot đã sẵn sàng!')

    # Thay đổi biểu ngữ
    await change_banner()

    # Thay đổi avatar
    await change_avatar()

async def change_banner():
    url = 'URL_BANNER_CUA_BAN'
    response = requests.get(url)
    image_data = response.content

    image_base64 = discord.utils._bytes_to_base64_data(image_data)

    payload = {'banner': image_base64}

    async with aiohttp.ClientSession() as session:
        async with session.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {TOKEN}'}, json=payload) as response:
            if response.status == 200:
                print('Ảnh bìa đã được cập nhật thành công!')
            else:
                print(f'Lỗi khi cập nhật ảnh bìa : {response.status}')

async def change_avatar():
    url_avatar = 'URL_AVATAR_CUA_BAN'
    response_avatar = requests.get(url_avatar)
    avatar_data = response_avatar.content

    avatar_base64 = discord.utils._bytes_to_base64_data(avatar_data)

    payload_avatar = {'avatar': avatar_base64}

    async with aiohttp.ClientSession() as session:
        async with session.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {TOKEN}'}, json=payload_avatar) as response:
            if response.status == 200:
                print('Avatar đã được cập nhật thành công!')
            else:
                print(f'Lỗi khi cập nhật avatar: {response.status}')

# Chạy bot
client.run(TOKEN)
