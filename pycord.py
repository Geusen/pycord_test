import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)

@bot.slash_command(guild_ids=[id])
async def ping(ctx):
    await ctx.send('pong', file=discord.File('white.png'))

bot.run(token)
