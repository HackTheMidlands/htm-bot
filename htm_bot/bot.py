#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import typer
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix="<", bot=True, reconnect=False, intents=discord.Intents.all())
slash = SlashCommand(
    bot, sync_commands=True, delete_from_unused_guilds=True
)  # Declares slash commands through the client.

@bot.event
async def on_ready():
    typer.echo('Ready!')


@bot.event
async def on_disconnect():
    typer.echo('disconnecting')
    await session.close()
