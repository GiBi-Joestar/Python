import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# =========================
# LOAD ENVIRONMENT VARIABLES
# =========================
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Safety check (prevents crash if token missing)
if token is None:
    raise ValueError("DISCORD_TOKEN not found in .env file")

# =========================
# LOGGING SETUP
# =========================
# This will save bot logs into a file called discord.log
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w'
)

# =========================
# BOT INTENTS (PERMISSIONS)
# =========================
intents = discord.Intents.default()
intents.message_content = True  # Required to read messages
intents.members = True          # Required for member join events

# =========================
# CREATE BOT INSTANCE
# =========================
bot = commands.Bot(command_prefix='!', intents=intents)

# Role name used in role commands
secret_role = "Gamer"

# =========================
# EVENTS
# =========================

@bot.event
async def on_ready():
    """Runs when the bot is online"""
    print(f'✅ Bot is ready! Logged in as {bot.user.name}')


@bot.event
async def on_member_join(member):
    """Sends a DM when someone joins the server"""
    try:
        await member.send(f"Welcome to the server, {member.name}! 🎉")
    except:
        print(f"Could not DM {member.name}")


@bot.event
async def on_message(message):
    """Moderation: deletes bad words"""
    
    # Prevent bot from replying to itself
    if message.author == bot.user:
        return

    # Simple bad word filter
    bad_words = ["shit"]

    if any(word in message.content.lower() for word in bad_words):
        await message.delete()
        await message.channel.send(
            f"{message.author.mention} - please don't use that word! ⚠️"
        )

    # VERY IMPORTANT: allows commands to still work
    await bot.process_commands(message)


# =========================
# BASIC COMMANDS
# =========================

@bot.command()
async def hello(ctx):
    """Greets the user"""
    await ctx.send(f"Hello {ctx.author.mention}! 👋")


@bot.command()
async def reply(ctx):
    """Replies directly to a message"""
    await ctx.reply("This is a reply to your message!")


@bot.command()
async def dm(ctx, *, msg):
    """Sends a private message to the user"""
    await ctx.author.send(f"You said: {msg}")


# =========================
# ROLE COMMANDS
# =========================

@bot.command()
async def assign(ctx):
    """Gives the user a role"""
    role = discord.utils.get(ctx.guild.roles, name=secret_role)

    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} now has the role **{secret_role}** 🎮")
    else:
        await ctx.send("❌ Role doesn't exist")


@bot.command()
async def remove(ctx):
    """Removes the role from the user"""
    role = discord.utils.get(ctx.guild.roles, name=secret_role)

    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} had the role removed ❌")
    else:
        await ctx.send("❌ Role doesn't exist")


@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    """Only users with the role can use this"""
    await ctx.send("🎉 Welcome to the secret club!")


@secret.error
async def secret_error(ctx, error):
    """Error handler if user lacks role"""
    if isinstance(error, commands.MissingRole):
        await ctx.send("🚫 You do not have permission to use this command!")


# =========================
# POLL COMMAND
# =========================

@bot.command()
async def poll(ctx, *, question):
    """Creates a simple poll with reactions"""

    # Delete user's command (optional, cleaner chat)
    await ctx.message.delete()

    # Create an embed (fancy message)
    embed = discord.Embed(
        title='📊 New Poll',
        description=question,
        color=discord.Color.blue()
    )

    # Send the poll
    poll_message = await ctx.send(embed=embed)

    # Add reaction options
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")


# =========================
# RUN BOT
# =========================
bot.run(token, log_handler=handler, log_level=logging.DEBUG)