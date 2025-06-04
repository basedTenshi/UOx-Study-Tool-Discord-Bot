import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # to read the messages on the server they're in

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
# Bot token so that our bot connects sa discord and go online

bot.run("token is located at the bot-token channel")

