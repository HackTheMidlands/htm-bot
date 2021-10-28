#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import typer
from pathlib import Path
import json

from .bot import bot
from .cog import setup

app = typer.Typer()


@app.command()
def run(
    ctx: typer.Context,
    token: str = typer.Argument(default="", envvar="DISCORD_TOKEN"),
    api_url: str = typer.Argument(
        default="https://achivements.hackthemidlands.com/api", envvar="API_BASE"
    ),
    api_token: str = typer.Argument(default="", envvar="API_TOKEN"),
    ctf_flags: Path = typer.Argument(default=None, envvar="CTF_FLAGS_FILE"),
):
    ctx.obj = {"api_url": api_url, "api_token": api_token}
    if ctf_flags:
        with open(ctf_flags, "r") as file:
            ctx.obj["flags"] = json.load(file)
    else:
        ctx.obj["flags"] = {}
    typer.echo(ctx.obj)
    typer.echo(f'Using API endpoint: {api_url}, token: {re.sub(".", "*", api_token)}')
    setup(bot, ctx)
    bot.run(token)
