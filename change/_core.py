import argparse
import shlex

from . import log


class ConfigArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        return shlex.split(arg_line, comments=True)


CLI = ConfigArgumentParser(
    description="change and manage package information", fromfile_prefix_chars="@"
)
CMD_CLI = CLI.add_subparsers(required=True, dest="CMD")

log.mount_cli(CMD_CLI)


def main():
    options = CLI.parse_args()
    options.__command__(options)
