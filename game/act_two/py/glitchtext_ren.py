# This file contains the Python code for the glitched/corrupted text that appears in DDLC during Act 2-4 of DDLC.

# The code logic is the same as the original game, only rewritten to use the Ren'Py's `_ren.py` approach for Python
# code.

import random

"""renpy
init python:
"""


def glitchtext(length: int) -> str:
    """
    Generates a string of random unicode characters of a specified length.

    :param length: The length of the string to generate.

    :type length: int
    :return: A string of random unicode characters.
    :rtype: str
    """
    if length <= 0:
        return ""

    ## Set of unicode ranges to use for generating the glitched text that are visible
    ## This can be expanded with more ranges depending on font compatibility.
    text_ranges = [
        (0x00C0, 0x00FF),  # Latin-1 Supplement (accented characters)
        (0x0100, 0x017F),  # Latin Extended-A
        (0x0180, 0x024F),  # Latin Extended-B
        (0x1E00, 0x1EFF),  # Latin Extended Additional
        (0x0370, 0x03FF),  # Greek and Coptic
        (0x0400, 0x04FF),  # Cyrillic
    ]

    exclude_chars = {
        0x00AD,  # Soft hyphen
    }

    ## Generate a string of random unicode characters
    result: list[str] = []
    while len(result) < length:
        # Randomly select a range from the text_ranges
        for start, end in text_ranges:
            for code_point in range(start, end + 1):
                if code_point not in exclude_chars and chr(code_point).isprintable():
                    result.append(chr(code_point))

    # Shuffle the result to ensure randomness
    random.shuffle(result)
    return "".join(result[:length])
