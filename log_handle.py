#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.handlers.TimedRotatingFileHandler('log/chrome.log', when='D', interval=1, backupCount=10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d] messages: %(message)s"))

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(file_handler)
logger.addHandler(console_handler)
