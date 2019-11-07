import argparse

from . import log

CLI = argparse.ArgumentParser(description="change and manage package information")
# TODO: add pyproject.toml defaults support
CMD_CLI = CLI.add_subparsers(required=True, dest="CMD")

log.mount_cli(CMD_CLI)


def main():
    options = CLI.parse_args()
    options.__command__(options)
