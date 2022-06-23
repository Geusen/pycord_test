import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)

@bot.slash_command
async def ping(ctx):
    await ctx.respond('pong')

bot.run(token)
