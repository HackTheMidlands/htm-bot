#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import requests
import typer
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord_slash import SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType


class PingPongCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", guild_ids=[724630949521784852])
    async def _ping(self, ctx: SlashContext):
        await ctx.send(content="Pong!")


class SharkCog(Cog):
    typerCtx: typer.Context
    bot: Bot
    url: str
    token: str

    def __init__(self, bot: Bot, typer_ctx: typer.Context):
        self.bot = bot
        self.typerCtx = typer_ctx
        self.url = typer_ctx.obj["api_url"]
        self.token = typer_ctx.obj["api_token"]
        self.flags = typer_ctx.obj["flags"]

    @cog_ext.cog_slash(
        name="flag",
        guild_ids=[724630949521784852],
        options=[
            create_option(
                name="challenge",
                description="Challenge.",
                option_type=3,
                required=False,
            ),
            create_option(
                name="flag", description="Flag.", option_type=3, required=False
            ),
        ],
    )
    async def _ctf_flag(self, ctx: SlashContext, challenge: str, flag: str):
        if correct := self.flags.get(challenge):
            if correct == flag:
                await self._submit(ctx, challenge, ctx.author_id)
            else:
                await ctx.send(content="Nice try!")
        else:
            await ctx.send(content="I don't recognise that flag...")

    async def _submit(self, ctx, name, user):
        try:
            resp = requests.post(f"{self.url}/{name}/{user}?token={self.token}")
            typer.echo(resp)
        except Exception as e:
            typer.echo(e, err=True)
            await ctx.send("Oops! Something went wrong.")
            return
        await ctx.send("Successfully submitted {name}!")

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
    bot.add_cog(SharkCog(bot, ctx))
    bot.add_cog(PingPongCog(bot))
