#!/usr/bin/env python3
"""Module 0 task"""

from typing import List
import re


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join([f"{field}=[^{separator}]*" for field in fields])
    return re.sub(f'({pattern})', lambda m: m.group(0).split('=')[0]
                  + '=' + redaction, message)
