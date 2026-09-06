"""
Filename: cli.py

Description:
    Simple command line tool to generate the 
    '.picounits' automatically to working
    directories.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from picounits.configuration.picounits import GENERATE_HELP, GENERATE_DESCRIPTION
from picounits.configuration.picounits import PICOUNITS_DESCRIPTION, DEFAULT_CONFIG

# pylint: disable=line-too-long

def generate(args: argparse.Namespace | None = None) -> None:
    """ Generates the '.picounits' file in working directories """
    _ = args

    target = Path.cwd() / ".picounits"
    if target.exists():
        print(f"Warning: .picounits already exists at {target}")
        reply = input("Overwrite? (y/N): ").strip().lower()

        # Asks the user if they want to overwrite past file
        if reply == "n":
            print("Aborted. No changes made.")
            return

    try:
        target.write_text(DEFAULT_CONFIG.strip() + "\n", encoding="utf-8")
        print(f"Successfully created .picounits at: {target}")
        print("\n\nYou can now edit it to switch to custom symbols (t/l/m) or change the dimension order.")
        print("picounits will automatically use your settings in this project!")

    except OSError as e:
        print(f"Failed to write .picounits to {target}: {e}")
        return

    # Asks the user if they want to see the configuration structure
    reply = input("Show the generated config now? (Y/n): ").strip().lower()

    if reply == "y":
        print("\n\n--- Generated .picounits content ---")
        print(DEFAULT_CONFIG)
        print("------------------------------------")


def main(args: argparse.Namespace | None = None) -> None:
    """ Adds the argparse argument `generate` to `picounits` main argument """
    parser = argparse.ArgumentParser(prog="picounits", description=PICOUNITS_DESCRIPTION)

    # Adds the `generate` argument for `picounits`
    subparsers = parser.add_subparsers()
    gen_parser = subparsers.add_parser("generate", help=GENERATE_HELP, description=GENERATE_DESCRIPTION)

    # Sets the python function `generate` as the route for `picounit generate`
    gen_parser.set_defaults(func=generate)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        # If there is no functions to execute, prints help and exits
        parser.print_help()
        return

    args.func(args)
