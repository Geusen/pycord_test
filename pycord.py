import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)

@bot.slash_command(name='a', guild_ids=[id])
async def ping(ctx):
    await ctx.send('pong', file=discord.File('white.png'))
    await bot.close()
    exit()

bot.run(token)
