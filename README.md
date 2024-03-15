# Discord Banner

Dễ dàng đơn giản khi sử dụng

![Dino Cover](https://media.discordapp.net/attachments/1189441843054788689/1218045534141550762/image.png?ex=66063c4d&is=65f3c74d&hm=95bbd7a558b13bfb05ea8ad079525aa23d0d75e7dca8eb0ccc94ed57eab286c9&=&format=webp&quality=lossless)

## Installation



```bash
pip install discord.py
pip install aiohttp
pip install requests
```

## Run

```python
Python banner.py
```

## Config

```config
# Khai báo token của bot
TOKEN = 'token here'
```

```config
# Tải ảnh từ URL
url = 'https://---Link Ảnh tại đây'- có hỗ trợ gif
```

## Change Avatar
```avatar
async def change_avatar():
    url_avatar = 'Link URL'
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
```
