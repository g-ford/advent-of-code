#!/usr/bin/env python3

from os import mkdir
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def next(day: int):
    if not 1 < day < 26:
        raise typer.BadParameter("Day must be between 1 and 25")

    day_path = Path(f"day{day:02d}")
    day_path.mkdir(exist_ok=True)
    input_path = Path(day_path, "input.txt")
    input_path.touch()
    main = Path(day_path, "main.py")

    if main.exists():
        print("main.py already exists, skipping templating")
    else:
        main.write_text(
            f"""\
from utils import log_time


@log_time
def part1(parts):
    pass


@log_time
def part2(parts):
    pass


@log_time
def parse_input(lines):
    pass


lines = open("{input_path}", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
"""
        )


if __name__ == "__main__":
    app()
