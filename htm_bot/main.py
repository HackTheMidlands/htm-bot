#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typer
from .bot import bot
from .cog import setup

app = typer.Typer()


@app.command()
def run(
    ctx: typer.Context,
    token: str = typer.Argument(default="", envvar="DISCORD_TOKEN"),
    api_url: str = typer.Argument(default = "https://achivements.hackthemidlands.com/api", envvar="API_BASE"),
    api_token: str = typer.Argument(default="", envvar="API_TOKEN")
):
    ctx.obj = {
        "api_url": api_url,
        "api_token": api_token
    }
    setup(bot, ctx)
    bot.run(token)
