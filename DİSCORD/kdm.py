import discord
from discord.ext import commands
import asyncio
# Tüm varsayılan niyetleri etkinleştirin
intents = discord.Intents.default()
intents.members = True  # Üye olaylarını dinlemek için
intents.message_content = True  # Mesaj içeriğini okumak için

def dchesap_start(token, hedef_kullanici_id, mesaj):
    global bot
    # Botu oluştur
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Bot olarak oturum açıldı {bot.user}')

        # Hedef kullanıcıya spam gönderme
        hedef_kullanici = await bot.fetch_user(hedef_kullanici_id)
        mesajlar = [mesaj] * 100  # 100 kere aynı mesajı oluştur

        # Mesajları paralel olarak gönder
        async def send_messages():
            for m in mesajlar:
                try:
                    await hedef_kullanici.send(m)
                    await asyncio.sleep(0.1)  # 0.1 saniye bekle 
                except discord.HTTPException as e:
                    if e.code == 50007:  # DM'leri kapalı ise hata kodu 50007
                        print(f"{hedef_kullanici.name}'in DM'leri kapalı.")
                        await bot.close()  # Botu kapat
                        return  # Döngüden çık
                    else:
                        print(f"Bir hata oluştu: {e}")

        asyncio.create_task(send_messages())

    bot.run(token)