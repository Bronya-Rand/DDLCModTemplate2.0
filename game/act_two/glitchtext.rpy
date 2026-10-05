## glitchtext.rpy

# This file defines the glitched/corrupted text seen in DDLC.

init python:
    import unicodedata

    # Precomputed string/list of non-unicode / glitched characters.
    # Preserved for backward-compatibility with DDLC and mod scripts referencing `nonunicode`.
    nonunicode = u"¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def _build_glitchtext_pool():
        """
        Builds a pool of valid, printable unicode characters across multiple scripts
        suitable for glitched text generation.
        """
        text_ranges = [
            (0x00C0, 0x00FF),  # Latin-1 Supplement (accented characters)
            (0x0100, 0x017F),  # Latin Extended-A
            (0x0180, 0x024F),  # Latin Extended-B
            (0x1E00, 0x1EFF),  # Latin Extended Additional
            (0x0370, 0x03FF),  # Greek and Coptic
            (0x0400, 0x04FF),  # Cyrillic
        ]
        exclude_chars = set([
            0x00AD,  # Soft hyphen
        ])
        pool = []
        for start, end in text_ranges:
            for code_point in range(start, end + 1):
                if code_point not in exclude_chars:
                    ch = unichr(code_point)
                    # In Python 2, check that the character is not a control character or separator
                    cat = unicodedata.category(ch)
                    if cat[0] not in ('C', 'Z'):
                        pool.append(ch)
        return pool

    _glitchtext_pool = _build_glitchtext_pool()

    def glitchtext(length):
        """
        Generates a string of random unicode characters of a specified length.

        :param length: The length of the string to generate.
        :type length: int
        :return: A string of random unicode characters.
        :rtype: unicode
        """
        if length <= 0:
            return u""

        result = [renpy.random.choice(_glitchtext_pool) for _ in range(length)]
        return u"".join(result)
