#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typer
from .bot import bot
from .cog import setup

app = typer.Typer()


@app.command()
def run(token: str = typer.Argument(default="", envvar="DISCORD_TOKEN")):
    setup(bot)
    bot.run(token)
