"""StaticData: open-mode base ROM content the randomizer does not regenerate.

Carries the *render-disjoint* bytes of the open-mode base ROM — spell/effect
animation graphics + molds + palettes (``$F3``/``$F4``), object/effect palettes
(``$E5``), compressed tilesets (``$FD``), and assorted gap data
(``$D4``/``$DD``/``$E0``/``$E4``/``$F7``/``$F9``/``$FA``/``$FE``/``$FF``) that no
``smrpgpatchbuilder`` ``render()`` method writes. The randomizer only renders a
subset of animation banks (``_02``/``_35``/``_3A``), so these banks fall
through; without this module the data would revert to vanilla when
``open_mode.json`` is retired (verified: dropping it changes a real ROM).

Stored as a checked-in binary asset (``static_data.bin``) rather than inline
literals (~137 KB). The loader streams it into the patch as ``{offset: bytes}``.
Record format (same as ``title_screen.bin``)::

    [u32 file_offset LE][u32 length LE][length bytes] ...

Only the render-disjoint bytes are carried (per-byte, so partially-rendered
entries don't clobber the bytes their collection owns).

ORDERING: this must be applied **before** the palette cosmetic renders
(``sprite_palettes`` / ``event_palettes`` / spell palettes) so those override
the effect-palette base where they overlap.

To regenerate ``static_data.bin``, re-extract the render-disjoint bytes for
file offsets ``>= 0x140000`` (banks ``$D4``+) — see the deconstruction notes.
"""

import os
import struct
from collections.abc import Iterator

_ASSET = os.path.join(os.path.dirname(__file__), "static_data.bin")

# Ranges owned by a ``render()`` pass that regenerates them on EVERY build.
# static_data.bin must not carry base-ROM bytes here: a leftover blob is applied
# in address order (patch keys are sorted at build time) and clobbers freshly
# rendered data whose key sits below it.
#
# credits.py (update_credits): ending-credits command buffer, string-pointer
# table, strings. A stale blob lands between two freshly written strings and
# clobbers the tail of the one before it (garbled lines, e.g. "WITHOUT YOU..."
# -> "WITHOUER DSGN."). Ranges mirror credits.py finalize().
#
# rooms.render() (RoomCollection): the entire room-object region 0x148000-0x14FFFF
# (512-entry pointer table + object data). The extraction captured base-ROM FF
# padding at 0x14EDFC-0x14F017; when a seed's packed room data grows past
# 0x14EDFC (postgame/shuffle content), that pad is applied after the last room
# and clobbers room 509's final objects (clones 11-14) into 0xFF.
#
# The render-disjoint extraction predated the open_mode->render() moves and
# wrongly captured these regions; trim them out here.
_RENDERER_OWNED = (
    (0x148000, 0x150000),
    (0x3F9C40, 0x3F9FF8),
    (0x3FDBB0, 0x3FF104),
    (0x3FFDDA, 0x3FFDDE),
)


def _excluding_owned(offset: int, data: bytes) -> Iterator[tuple[int, bytes]]:
    """Yield the sub-records of ``[offset, offset+len(data))`` that remain after
    removing every renderer-owned range (so static_data never overwrites a
    region that a ``render()`` pass regenerates on every build)."""
    start, end = offset, offset + len(data)
    pos = start
    for lo, hi in sorted(r for r in _RENDERER_OWNED if r[0] < end and r[1] > start):
        if lo > pos:
            yield pos, data[pos - start : lo - start]
        pos = max(pos, hi)
    if pos < end:
        yield pos, data[pos - start : end - start]


def get_patch() -> dict[int, bytes]:
    """Stream the render-disjoint base-ROM records from ``static_data.bin``."""
    out: dict[int, bytes] = {}
    with open(_ASSET, "rb") as handle:
        blob = handle.read()
    pos = 0
    while pos < len(blob):
        offset, length = struct.unpack_from("<II", blob, pos)
        pos += 8
        for sub_off, sub_data in _excluding_owned(offset, blob[pos : pos + length]):
            if sub_data:
                out[sub_off] = sub_data
        pos += length
    return out
