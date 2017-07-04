#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import optparse
import sys
import os
from jinja2 import Template
from configparser import ConfigParser

def main():
    __version__ = "v0.1 (04.07.2017)"
    __description__ = "Generates output file based on Jinja2 template and configs file"

    max_width = 80
    max_help_position = 80

    help_format = optparse.IndentedHelpFormatter(width=max_width, max_help_position=max_help_position)
    kw = {
        'formatter': help_format,
        'usage': '%prog [OPTIONS]',
        'add_help_option': False,
        'description': __description__,
    }

    parser = optparse.OptionParser(**kw)
    parser.add_option(
        '-h', '--help',
        action='help',
        help='Print this help text and exit')
    parser.add_option(
        '-v', '--version',
        action='version',
        help='Print program version and exit')
    parser.version = __version__

    general = optparse.OptionGroup(parser, 'General Options')
    general.add_option(
        '-t', '--template',
        dest='template_location', metavar='FILE',
        help='Location of the Jinja2 template file')
    general.add_option(
        '-c', '--config',
        dest='config_location', metavar='FILE',
        help='Location of the INI config file')
    general.add_option(
        '-o', '--output',
        dest='output_location', metavar='FILE',
        help='Location of the output file')
    general.add_option(
        '-s', '--section',
        dest='config_section', metavar='STRING',
        help='Section from config file')
    parser.add_option_group(general)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        sys.exit(1)

    command_line_conf = sys.argv[1:]
    (opts, args) = parser.parse_args(command_line_conf)

    def _validate_path_arg(path, arg_name):
        if not (path and os.path.isfile(path)):
            msg = "Please specify exist path to {}.\n".format(arg_name)
            msg += "Type generate.py --help to see a list of all options."
            parser.error(msg)

    _validate_path_arg(opts.template_location, "Jinja2 template with -t arg")
    _validate_path_arg(opts.config_location, "INI config file with -c arg")

    if not opts.output_location:
        msg = "Please specify path to output file with -o arg.\n"
        msg += "Type generate.py --help to see a list of all options."
        parser.error(msg)

    if not opts.config_section:
        msg = "Please specify section from config file.\n"
        msg += "Type generate.py --help to see a list of all options."
        parser.error(msg)

    config = ConfigParser()
    config.optionxform = str
    config.read(opts.config_location)

    if opts.config_section not in config.sections():
        msg = "Section '{}' not found in config file".format(opts.config_section)
        parser.error(msg)

    with open(opts.template_location, 'r') as t:
        template = Template(t.read())

    with open(opts.output_location, 'w') as w:
        w.write(template.render(config[opts.config_section]))
        w.close(    )

if __name__ == '__main__':
    main()