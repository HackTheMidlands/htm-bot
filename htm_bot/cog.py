#!/usr/bin/env python
# -*- coding: utf-8 -*-

from discord import Embed
import discord
import typer
import requests
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

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
        url = self.typerCtx.obj['api_url']
        token = self.typerCtx.obj['api_token']
        requests.post(f'{url}?token={token}', data={'user': str(member)})


    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.send('Hello {0.name}... This feels familiar.'.format(member))

def setup(bot: Bot):
    bot.add_cog(Slash(bot))
    bot.add_cog(Greetings(bot))
