import discord

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_message(m):
    if m.content == "!hi":
        await m.channel.send("Hi! How are you")


bot.run("")
