"""DisableGardenIntro: skip the opening "garden intro" sequence on both the
new-game and load-game paths (always-on).

These are the two LazyShell "Intro" editor checkboxes - *Disable garden intro
(load game)* and *Disable garden intro (new game)* - both enabled in the
open-mode base ROM (Editor.Intro/Opening.cs in LAZYSHELL-UPDATED). Vanilla
plays the opening garden intro sequence; open mode skips straight to gameplay.
Both checkboxes are confirmed set in the legacy open_mode.json, so this is a
pure relocation - diff-verify with
manage.py diff_open_mode --module randomizer.patches.asm.disable_garden_intro.

Sites (raw file offsets; HiROM $Cx:xxxx -> file 0x0xxxxx):

1. $C0:087D (file 0x0087D) - LOAD-GAME path. Vanilla 22 00 00 C3
   (JSL $C30000, which runs the garden intro) -> EA EA EA EA (4 NOPs),
   so loading a save no longer plays the intro.

2. $C3:4872 (file 0x34872) - NEW-GAME path. Vanilla 82 A8 6D
   (BRL into the intro) -> 4C 44 00 (JMP $0044), branching past the
   intro on a new game.

(The LazyShell "Intro" editor also writes the title-screen graphics - main
title GFX at 0x3F216E, title-card GFX at 0x3F1913, bootup-logo GFX at
0x3EFD18, opening palette at 0x3F0080, coords at 0x09E66B-0x09EF51,
title-mode selector at 0x09E640 - but the open-mode base leaves all of
those at vanilla, so they need no module. The only title-region open_mode
writes are DATA blobs handled elsewhere: bootup-logo bytes at 0x3EFD02 and
the partial main-title CGFX edits at 0x3FDBB2 / 0x3FE4B0.)
"""


def get_patch() -> dict[int, bytes]:
    return {
        # $C0:087D - load-game garden intro: JSL $C30000 -> 4 NOPs
        0x0087D: bytes([0xEA, 0xEA, 0xEA, 0xEA]),
        # $C3:4872 - new-game garden intro: BRL -> JMP $0044 (skip)
        0x34872: bytes([0x4C, 0x44, 0x00]),
    }
