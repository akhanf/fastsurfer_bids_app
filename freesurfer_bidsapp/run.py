#!/usr/bin/env python3
from pathlib import Path

from snakebids.app import SnakeBidsApp


def get_parser():
    """Exposes parser for sphinx doc generation, cwd is the docs dir."""
    app = SnakeBidsApp(Path(__file__).resolve().parent)  # to get repository root
    return app.parser


def main():
    """Run the app."""
    app = SnakeBidsApp(
        Path(__file__).resolve().parent,  # to get repository root
    )
    app.run_snakemake()


if __name__ == "__main__":
    main()
