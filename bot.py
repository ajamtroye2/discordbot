import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❗ Il manque un argument.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Cette commande n'existe pas.")
    else:
        await ctx.send(f"Erreur inconnue : {str(error)}")

initial_extensions = [
    "cogs.hello",
    "cogs.maths",
    "cogs.api"
]

for ext in initial_extensions:
    bot.load_extension(ext)

bot.run(TOKEN)
