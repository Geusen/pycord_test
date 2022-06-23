import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)
channel = int(settings.CHANNEL)

@bot.slash_command(guild_ids=[id])
async def upload():
    ctx = client.get_channel(channel)
    await ctx.respond('test')
    await ctx.send(file=discord.File('white.png'))
    await bot.close()
    exit()

bot.run(token)
