import discord
import os
import random
from discord.ext.commands import Context

BARON_ROLE_ID = int(os.getenv("BARON_ROLE_ID"))
ALLOWED_ROLES_ID = os.getenv("ALLOWED_ROLES_ID", "").split(",")
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)


@bot.slash_command()
async def bang(ctx: Context):
    is_allowed_to_run = [str(role.id) for role in ctx.author.roles if str(role.id) in ALLOWED_ROLES_ID]
    if not is_allowed_to_run:
        await ctx.respond("You're not allowed to run this, fuck off")
        return

    role = ctx.guild.get_role(BARON_ROLE_ID)

    target = random.choice(role.members)
    await target.remove_roles(role)

    await ctx.respond("%s has lost their Baron privileges" % target.name)


bot.run(BOT_TOKEN)