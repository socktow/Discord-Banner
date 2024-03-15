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

    # Tải ảnh từ URL
    url = 'https://---Link Ảnh tại đây'
    response = requests.get(url)
    image_data = response.content

    # Chuyển đổi ảnh thành base64
    image_base64 = discord.utils._bytes_to_base64_data(image_data)

    # Tạo payload
    payload = {'banner': image_base64}

    # Gửi yêu cầu PATCH để cập nhật biểu ngữ của bot
    async with aiohttp.ClientSession() as session:
        async with session.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {TOKEN}'}, json=payload) as response:
            if response.status == 200:
                print('Anh bìa đã được cập nhật thành công!')
            else:
                print(f'Lỗi khi cập nhật ảnh bìa : {response.status}')

# Chạy bot
client.run(TOKEN)