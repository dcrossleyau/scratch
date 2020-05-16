#!/usr/bin/env python3

import argparse
import logging
import os
import sys

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
    """Say hello."""
    get_options()
    logger.info("Hello info.")
    logger.debug("Hello debug.")
    print("Python version: {}".format(sys.version_info))

if __name__ == "__main__":
    sys.exit(main())
