#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import requests
import typer
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord_slash import SlashContext, cog_ext


class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test")
    async def _test(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)


class Greetings(commands.Cog):
    def __init__(self, bot: Bot, typerCtx: typer.Context):
        self.bot = bot
        self.typerCtx = typerCtx

    @commands.command()
    async def post(self, ctx, *, member: discord.Member = None):
        """Post to API"""
        member = member or ctx.author
        url = self.typerCtx.obj["api_url"]
        token = self.typerCtx.obj["api_token"]
        requests.post(f"{url}/{member}?token={token}")
        await ctx.send("You have been posted!")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.send(f"Hello {member.name}...")


def setup(bot: Bot, ctx: typer.Context):
    bot.add_cog(Slash(bot))
    bot.add_cog(Greetings(bot, ctx))
