#!/usr/bin/env python3

import argparse
import logging
import os
import pprint
import sys

import requests
import yaml

if sys.version_info[0] < 3:
    raise RuntimeError("Python 3 or above is required.")

LOGLEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}
PROG_NAME = os.path.basename(sys.argv[0])
PROG_DESC = __import__('__main__').__doc__
LOG_FORMAT = "%(levelname)s: %(name)s: %(message)s"
logger = logging.getLogger(PROG_NAME)
logging.basicConfig(format=LOG_FORMAT)

CONFIG_FILE = "https://raw.githubusercontent.com/folio-org/folio-org.github.io/master/_data/api.yml"

def get_options():
    """Gets the command-line options."""
    parser = argparse.ArgumentParser(description=PROG_DESC)
    parser.add_argument(
        "-l", "--loglevel",
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
        help="Logging level. (Default: %(default)s)"
    )
    args = parser.parse_args()
    loglevel = LOGLEVELS.get(args.loglevel.lower(), logging.NOTSET)
    logger.setLevel(loglevel)

def main():
    get_options()
    try:
        http_response = requests.get(CONFIG_FILE)
        http_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.critical("HTTP error retrieving configuration file: %s", err)
        return 2
    except Exception as err:
        logger.critical("Error retrieving configuration file: %s", err)
        return 2
    else:
        try:
            config = yaml.safe_load(http_response.text)
        except yaml.YAMLError as err:
            logger.critical("Trouble parsing YAML configuration file '%s': %s", CONFIG_FILE, err)
            return 2
        else:
            logger.debug("Successfully retrieved configuration.")
            pprint.pprint(config['mod-notes'])

if __name__ == "__main__":
    sys.exit(main())
