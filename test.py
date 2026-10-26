import discord
from discord.ext import commands

# 1. Setup Intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message contents

# 2. Initialize the Bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# 3. Event: Triggered when the bot is online and ready
@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user} (ID: {bot.user.id})")
    print("-----------------------------------------")

# 4. Simple Command: Type '!ping' in chat
@bot.command(name="ping")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! 🏓 Latency is {latency}ms")

# 5. Run the bot
bot.run("YOUR_BOT_TOKEN_HERE")
