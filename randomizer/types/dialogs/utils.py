"""Functions that help with dialog development."""

import re

COMPRESSION_TABLE = [
    ("[0x7000]", b"\x1C\x00"),
    ("[0x7024]", b"\x1C\x01"),
    ("[0x7000timer]", b"\x1C\x02"),
    ("[0x70A7]", b"\x1A"),
    ("[filename]", b"\x1C\x03"),
    ("[await][pause]", b"\x05"),
    ("\x20\x20\x20\x20", b"\x0A"),
    ("\x20\x20\x20", b"\x09"),
    ("\x20\x20", b"\x08"),
    ("[await][page]\n", b"\x03"),
    ("[page]\n", b"\x04"),
    ("[await]\n", b"\x02"),
    ("[await]", b"\x00"),
    ("\n", b"\x01"),
    ("[end]", b"\x06"),
    ("[select]", b"\x07"),
    ("[delay]", b"\x0C"),
    ("Booster", b"\x18"),
    ("Booster", b"\x19"),
    ("Mario", b"\x13"),
    (" and ", b"\x15"),
    (" to ", b"\x11"),
    (" I ", b"\x14"),
    (" the", b"\x0E"),
    (" you", b"\x0F"),
    ("in", b"\x10"),
    ("’s ", b"\x12"),
    ("'s ", b"\x12"),
    ("is ", b"\x16"),
    (" so", b"\x17"),
    ("“", b"\x22"),
    ("”", b"\x23"),
    ("♥", b"\x24"),
    ("♪", b"\x25"),
    ("‘", b"\x26"),
    ("’", b"\x27"),
    ("••", b"\x2B"),
    ("•", b"\x2A"),
    ("~", b"\x3A"),
    ("「", b"\x3B"),
    ("」", b"\x3C"),
    ("『", b"\x3D"),
    ("』", b"\x3E"),
    ("©", b"\x40"),
    (":", b"\x8E"),
    (";", b"\x8F"),
    ("<", b"\x90"),
    (">", b"\x91"),
    ("···", b"\x92"),
    ("#", b"\x93"),
    ("×", b"\x94"),
    ("+", b"\x95"),
    ("%", b"\x96"),
    ("↑", b"\x97"),
    ("→", b"\x98"),
    ("←", b"\x99"),
    ("*", b"\x9A"),
    ("'", b"\x9B"),
    ("&", b"\x9C"),
]


def compress(string: str) -> bytearray:
    """Turns a dialog string into bytes."""
    output = bytearray()
    tbl = dict(COMPRESSION_TABLE)
    cursor = 0
    while cursor < len(string):
        regex_result = re.search(r"^(\x20\x20\x20\x20\x20+)", string[cursor:])
        if regex_result:
            token = regex_result.group()
            output += bytearray([0x0B, len(token)])
            cursor += len(token)
            continue
        regex_result = re.search(r"^(\[delay_\d+\])", string[cursor:])
        if regex_result:
            token = regex_result.group()
            delay_int = re.search(r"\d+", token).group()
            delay = int(delay_int)
            output += bytearray([0x0D, delay])
            cursor += len(token)
            continue
        cursor_key = None
        for key in tbl:
            if string[cursor:].startswith(key):
                cursor_key = key
                break
        if cursor_key:
            tmp = tbl[cursor_key]
            output += tmp
            cursor += len(cursor_key)
            continue
        output.append(ord(string[cursor]))
        cursor += 1
    last_byte = output[len(output) - 1]
    if last_byte not in [0x00, 0x06]:
        output.append(0x00)  # Null terminate strings.
    return output
