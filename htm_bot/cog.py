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
    typerCtx: typer.Context
    bot: Bot
    url: str
    token: str

    def __init__(self, bot: Bot, typer_ctx: typer.Context):
        self.bot = bot
        self.typerCtx = typer_ctx
        self.url = typer_ctx.obj["api_url"]
        self.token = typer_ctx.obj["api_token"]

    @cog_ext.cog_slash(name="ping", guild_ids=[724630949521784852])
    async def _ping(self, ctx: SlashContext):
        await ctx.send(content="Pong!")

    @cog_ext.cog_slash(name="shark", guild_ids=[724630949521784852])
    async def _shark_tank(self, ctx: SlashContext):
        member_id = ctx.author_id
        member = ctx.author
        typer.echo(f"POST {member}: {self.url}/{member_id}")
        try:
            resp = requests.post(f"{self.url}/{member_id}?token={self.token}")
            typer.echo(resp)
        except Exception as e:
            typer.echo(e, err=True)
            await ctx.send("Oops! something went wrong.")
            return
        await ctx.send("Well done!")


def setup(bot: Bot, ctx: typer.Context):
    bot.add_cog(Slash(bot, ctx))
