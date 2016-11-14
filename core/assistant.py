# Open Assistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# core.py - Open Assistant System Core

import logging
import os
import sys
import subprocess

logger = logging.getLogger(__name__)

class Assistant:

    def __init__(self, config=None):
        logger.info("Initializing Assistant")
        self.config = config if config is not None else {}