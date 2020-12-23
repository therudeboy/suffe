import discord

import random
from discord.ext import commands, tasks
from itertools import cycle



client = commands.Bot(command_prefix = "/")
status = cycle(["/yardim", "Ehli Suffe", "Suffe.org", "Hilali Ebed", "Hilaliebed.net", "Kurucu: Emir Selim Soydan", "https://discord.gg/bDkQVBU2s4", "Created by Яudeboy" ])

@client.event
async def on_ready():
    change_status.start()
    #await client.change_presence(status=discord.Status.online, activity=discord.Game("Ehli Suffe",))
    print("Bot Hazır!")




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Dostum bu dediklerini anlayamadım tekrar yazabilirmisin?")



@tasks.loop(seconds=5)
async def change_status():
   await client.change_presence(activity=discord.Game(next(status)))



@client.event
async def on_member_join(member):
    print(f"{member} sunucumuza hoşgeldin.")

@client.event
async def on_member_remove(member):
    print(f"{member} çıktı. Yine bekleriz.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pinginiz {round(client.latency * 1000)}ms")


@client.command(aliases=["soru","test"])
async def _soru(ctx, *, question):
    responses = ["Bu kesin.",
                 "Kesinlikle öyle.",
                 "Şüphesiz.",
                 "Evet kesinlikle.",
                 "Ona güvenebilirsiniz.",
                 "Gördüğüm kadarıyla evet.",
                 "Büyük ihtimalle.",
                 "İyi görünüm.",
                 "Evet.",
                 "İşaretler eveti gösteriyor.",
                 "Bulanık cevap tekrar deneyin.",
                 "Sonra tekrar sor.",
                 "Sana şimdi söylememek daha iyi.",
                 "Şimdi tahmin edemem.",
                 "Konsantre ol ve tekrar sor.",
                 "Güvenme."
                 "Cevabım hayır",
                 "Kaynaklarım olumsuz diyor.",
                 "Görünüş o kadar iyi değil.",
                 "Niyetimiz halis ise.",
                 "Niyetimiz halis ise.",
                 "Niyetimiz halis ise.",
                 "Nasipte varsa.",
                 "Çok şüpheli."]
    await ctx.send(f"Soru: {question}\nCevap: {random.choice(responses)}")

@client.command()
async def napim(ctx):
    await ctx.send(f"Kullanıcı banlama protokolü başlatılıyor...")


#@client.command()
#async def sil(ctx, amount=5):
#    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
#        await ctx.channel.purge(limit= amount+1)
#@sil.error
#async def clear_error(ctx, error):
#    if isinstance(error, commands.MissingPermissions):
#       await ctx.send('Üzgünüm dostum bunu yapmaya yetkin yok.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx,amount=5):
    await ctx.channel.purge(limit=amount+1)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def ben(ctx):
    await ctx.send(f"Galiba bu sensin {ctx.author} {ctx.author.avatar_url}")

@client.command()
async def sa(ctx):
    await ctx.send(f"Selamın Aleyküm!")

@client.command(aliases=["as",])
async def _as(ctx):
    await ctx.send(f"Aleyküm Selam!")

@client.command()
async def yardim(ctx):
    await ctx.send(f"Merhaba Suffe Bot yardım sayfası                                                                                                                       /sa - /as Komutları Selam verip alır.                                                                                                                   /ben Komutu kim olduğunuzu söyler.                                                                                                                 /sil Komutu belirlenen mesajları siler belirlenmezse 5 tane siler!                                                                 /ban - /kick Komutları atma ve yasaklama yapar.                                                                                           /soru Komutu sorunuza (evet veya hayır olacak şekilde) cevap verir.                                                        /ping Komutu anlık pinginizi ölçer.                                                                                                                        /yardim Komutu komutları gösterir                                                                                                                     Created by Яudeboy")



client.run('Nzg5OTA3NzUzNzU3NTczMTMw.X9447A._F4_uBr052QhiuZFtI_tpxOoOck')






