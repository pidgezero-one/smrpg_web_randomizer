"""BlankDummyEffect: erase the tile data behind the shared "DUMMY" battle
effect so that effect ids flagged as DUMMY render nothing at all.

Applied only when the RemoveFlashes accessibility flag is on. Several battle
animations open with a full-screen colour blast whose only purpose is the
flash; the cleanest way to suppress one without disturbing the surrounding
script is to repoint its ``NewEffectObject`` at an effect that draws nothing.
No such effect exists in vanilla - every id resolves to real tile data - so
this patch makes one.

Why the effect id has to stay valid
-----------------------------------
``NewEffectObject`` (opcode ``0x72``, ``$C2:48AF``) is the only writer of the
animation slot's effect index at ``$40:002C,X``. ``Layer3On`` (``0x77``,
reads it at ``$C2:49DC``) and ``FadeOutObject`` (``0x7E``, ``$C2:5146``) both
read it back to post their graphics-load and fade requests. Deleting or
replacing the ``NewEffectObject`` leaves those reading whatever the slot last
held, so the effect object has to stay - only its contents can go.

Effect / animation-packet layout
--------------------------------
Effect records are 4 bytes at ``0x251000 + id * 4``::

    byte 0  palette index (& 7)
    byte 1  animation packet
    byte 2  X offset, stored as (x - 1 ^ 255)
    byte 3  Y offset, same encoding

All 32 ids named ``DUMMY`` (0, 1, 23, 24, 26, 29-31, 33-35, 44, 73-75, 81,
84, 113-127) carry ``animationPacket = 0``, and no non-DUMMY effect uses
packet 0 - verified by dumping all 128 records out of vanilla.

Animation packets are addressed by a 24-bit pointer table at
``0x252C00 + packet * 3``. Entry 0 is ``$F3:0000`` = file offset
``0x330000``, inside the ``0x330000-0x34CFFF`` "Spell/Effect animations"
region. Each packet is a self-contained blob whose header is::

    +0x00  u16  total length          (262 for packet 0)
    +0x02  u16  graphics offset       (18)
    +0x04  u16  palette offset        (146)
    +0x06  u16  sequence offset       (244)
    +0x08  u16  mold offset           (251)
    +0x0A  u16  (unknown)
    +0x0C  u8   width                 (9)
    +0x0D  u8   height                (8)
    +0x0E  u16  codec                 (0)
    +0x10  u16  tileset offset        (178)

So packet 0's graphics run from ``0x330000 + 18 = 0x330012`` for
``146 - 18 = 128`` bytes. 65 of those are non-zero in vanilla, which is why
a DUMMY effect draws a visible graphic rather than nothing.

What this patch does
--------------------
Zero those 128 bytes. Every tile pixel becomes colour index 0, which is
transparent on a BG layer, so the effect object still loads, still satisfies
the ``$0B78`` waits its script pairs with, and still fades - it just has
nothing to show. The header, palette, tileset, sequences and molds are left
intact so the packet stays well-formed; blanking the mold list instead would
be a smaller write but risks walking the mold parser off the end.

Collateral: vanilla drives packet 0 in exactly two places, both in the
extended-animation queue ``command_0x3551CB``
(``randomizer/data/battle_animation/_35/contents/script_0x353437.py``
lines 2040 and 2087), where the DUMMY object is a parent container for a
child queue that spawns the actual visible sprites. Those two lose their
backdrop when the flag is on; the child sprites are unaffected.
"""


# Packet 0 blob base + its header's graphics offset (18).
_PACKET_0_GRAPHICS = 0x330012
# Palette offset (146) - graphics offset (18).
_PACKET_0_GRAPHICS_LENGTH = 128


def get_patch() -> dict[int, bytes]:
    return {
        # Animation packet 0 tile data -> fully transparent.
        _PACKET_0_GRAPHICS: bytes(_PACKET_0_GRAPHICS_LENGTH),
    }
