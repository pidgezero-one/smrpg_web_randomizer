"""ROM title + version text writes.

* SNES header title at ROM ``$7FC0`` (20 bytes, space-padded).
* Major version byte at ROM ``$7FDB``.
* Name-entry-screen version string at ROM ``$3E:F140`` (10 bytes,
  space-padded).
"""


def _title_bytes(seed: int) -> bytes:
    title = "SMRPG-R {}".format(seed).ljust(20)
    if len(title) > 20:
        title = title[:19] + "?"
    return title.encode("latin1")


def _version_text_bytes(version: str) -> bytes:
    text = ("v" + version).ljust(10)
    if len(text) > 10:
        raise ValueError("Version text is too long: {!r}".format(text))
    return text.encode("latin1")


def get_patch(seed: int, version: str) -> dict[int, bytes]:
    """Return ROM-header / on-screen version writes."""
    major_version = int(version.split(".")[0])
    return {
        0x3EF140: _version_text_bytes(version),
        0x7FC0: _title_bytes(seed),
        0x7FDB: bytes([major_version]),
    }
