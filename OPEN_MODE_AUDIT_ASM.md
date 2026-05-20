# `open_mode.json` — ASM-only filter (deconstruction targets)

**Filter assumption:** entries in non-ASM ROM regions are fully overwritten by smrpgpatchbuilder's collection `render()` methods (event scripts, rooms, allies, monsters, items, spells, animations, dialogs, sprite data, etc. all rebuild from Python sources in `randomizer/data/` + `smrpgpatchbuilder/datatypes/`). Verify any DATA-region entries before dropping — partial overwrites or vanilla GFX could survive.

**Re-categorization sweep (2026-05-19):** The original audit left 344 entries
in an UNKNOWN bucket because they didn't fall into the audit script's
ROM_REGIONS map. Cross-checking against `doc_offsets.txt` resolves all 344
into either DROP_COVERED (covered by collection render) or REVIEW (small
gap regions worth eyeballing). 5 new ASM/PTR entries surfaced that the
original audit missed — they're folded into the ASM section below.

## Shrink summary

| bucket | entries | bytes | % of bytes |
|---|---:|---:|---:|
| **ASM/engine PTR (keep — needs `asm/*.py` deconstruction)** | 25 | 198 | 0.01% |
| DATA (drop — overwritten by collection render or runtime recalc) | 6281 | 1568688 | 98.7% |
| REVIEW (small gaps, mostly DATA tail injections) | 35 | 20669 | 1.3% |
| **total** | **6341** | **1589555** | 100% |

## ASM/engine PTR entries (25 entries, 198 bytes)

These touch live engine code or pointer tables that `render()` methods do
not regenerate. Each needs a corresponding entry in `randomizer/patches/asm/*.py`
once `open_mode.json` is removed.

### SA-1 init + engine ASM ($C0 SA-1 bus) — 11 entries, 89 bytes

| SNES | file ofs | len | bytes | purpose |
|---|---|---:|---|---|
| `$C0:8130` | +0x08130 | 7 | `22 B0 20 FA 4C 93 3E` | JSL hook in SA-1 init |
| `$C0:9009` | +0x09009 | 3 | `A9 00 EA` | **Ally-loader char-index gutting — KEEP NOP'd.** Stamps `LDA $0000,Y` (`B9 00 00`) with `LDA #$00 / NOP`, forcing char 0 into every party-slot iteration so the lead slot always loads sprite `$1F` (alt protagonist via the `$9B86` patch) regardless of who is currently in slot 0. A naive restore to vanilla **breaks the "protagonist always renders" invariant** (verified 2026-05-19): party-swap-mid-room leaves stale animation-index data at `$58,X`, and any script that puts a non-protagonist into slot 0 then renders that character instead of the protagonist. The `$9B4E` loader also writes a per-char *animation index* to `$58,X` (Geno → `$05`, lead default → `$07`, follower default → `$06`), which the alt-protagonist sprite is tuned for `$07`; restoring `$9009` cuts that. Per-slot character dispatch for follower slots (the `CHARACTER_IN_SLOT_2` use case in `script_1710.py`) needs a **hybrid**: keep `$9009` forcing char 0 for slot 0, but use the real roster char id for slot 1+. Implementation requires a JSR hook (3 bytes of patched space is enough for `JSR $XXXX`; the helper goes in C0 free space). |
| `$C0:C302` | +0x0C302 | 4 | `F0 F8 A9 15` | event-handler patch |
| `$C0:C37C` | +0x0C37C | 4 | `F0 F8 A9 15` | event-handler patch (same pattern) |
| `$C0:C3B2` | +0x0C3B2 | 4 | `F0 F8 A9 15` | event-handler patch (same pattern) |
| `$C0:C443` | +0x0C443 | 7 | `0F 27 90 03 A9 0F 27` | level/HP cap raise (paired with `$C2:9319`, `$C3:3F03`) |
| `$C0:C841` | +0x0C841 | 2 | `30 81` | engine PTR (within Event function pointers 256) |
| `$C0:E42C` | +0x0E42C | 15 | `EA × 15` | ALL-NOP — engine ASM in `00E397-00EEB0` range |
| `$C2:9319` | +0x29319 | 7 | `0F 27 90 03 A9 0F 27` | level/HP cap raise (battle) |
| `$C2:BDE9` | +0x2BDE9 | 1 | `FF` | single-byte engine patch |
| `$C2:F96F`+ | +0x2F96F | 5+26 | `8F F9 94 F9 9B` + data | (REVIEW: at `02F96F`/`02F988` in `02E6C6-02F9A5` "data/functions?" range — likely engine PTRs feeding `02F9A6+` gap) |

### CPU event functions ($C0 S-CPU bus) — 1 entry, 11 bytes

| SNES | file ofs | len | bytes | purpose |
|---|---|---:|---|---|
| `$C0:3EB2` | +0x03EB2 | 11 | `EA × 11` | **MARIO/PEACH/BOWSER/GENO/MALLOW resolver gutting** — keeps the engine returning slot 0 for name-targeted scripts. **KEEPS this NOP** under randomizer's "protagonist-static" semantics. |

### CPU init + core engine ASM ($C0 S-CPU bus) — 2 entries, 6 bytes

| SNES | file ofs | len | bytes | purpose |
|---|---|---:|---|---|
| `$C0:00CC` | +0x000CC | 2 | `0E 3E` | CPU reset-vector patch (jumps into open-mode init code) |
| `$C0:087D` | +0x0087D | 4 | `EA × 4` | ALL-NOP — neuters something in CPU init |

### Windowing / menu ASM ($C3) — 11 entries, 123 bytes

The original audit caught 7 here; re-categorization picks up 4 more (`$C3:5308`, `$C3:623F`, `$C3:626F`, `$C3:62AE`) that were in the UNKNOWN bucket.

| SNES | file ofs | len | bytes | purpose |
|---|---|---:|---|---|
| `$C3:15B7` | +0x315B7 | 1 | `80` | branch flip |
| `$C3:3AFC` | +0x33AFC | 9 | `16 43 86 62 20 02 79 A2 16` | menu plumbing |
| `$C3:3B0E` | +0x33B0E | 2 | `02 79` | menu plumbing |
| `$C3:3F03` | +0x33F03 | 7 | `0F 27 90 03 A9 0F 27` | level/HP cap raise (X-menu) |
| `$C3:3F6E` | +0x33F6E | 7 | `16 43 86 62 20 02 79` | menu plumbing |
| `$C3:3FA1` | +0x33FA1 | 1 | `16` | menu byte |
| `$C3:3FB0` | +0x33FB0 | 2 | `02 79` | menu plumbing |
| `$C3:5308` | +0x35308 | 1 | `F0` | single-byte branch flip |
| `$C3:623F` | +0x3623F | 24 | `EA EA A5 15 89 08 D0 28 …` | bit-test / branch table |
| `$C3:626F` | +0x3626F | 59 | `38 AD 2A 09 ED 29 09 C9 FF F0 4D …` | sub/cmp logic block |
| `$C3:62AE` | +0x362AE | 10 | `EA × 10` | ALL-NOP tail of the same block |

### Embedded cartridge header ($C0 S-CPU) — 1 entry, 4 bytes

| SNES | file ofs | len | bytes | purpose |
|---|---|---:|---|---|
| `$C0:7FDC` | +0x07FDC | 4 | `E2 F2 1D 0D` | SNES checksum bytes — **make_seed.py recomputes after all patches apply**, so this entry is harmless / DROP. |

## DROP_COVERED (6281 entries, 1568688 bytes)

All collection-rendered or runtime-recalculated. Verified `render()` exists
in smrpgpatchbuilder for every region listed below. Drop wholesale once
`open_mode.json` is deconstructed.

### Already-rendered collections

| region | entries | bytes | rendered by |
|---|---:|---:|---|
| Object uncompressed GFX (`$E8:0000`-`$F2:FFFF`) | 4196 | 695393 | `SpriteCollection.render()` |
| Spell/Effect animations (`$F3:0000`-`$F4:CFFF`) | 174 | 111252 | `AnimationCollection.render()` |
| Object animation data/molds (`$F6:0000-FFFF`) | 175 | 64911 | `AnimationCollection.render()` |
| Event Data (`$DE:0C00-FFFF`, `$DF:0C00-FFFF`) | 83 | 179473 | `EventScriptCollection.render()` |
| Object Sequences (`$E5:9000`-`$E7:FFFF`) | 29 | 157598 | `SpriteCollection.render()` |
| Dialogue (`$E2:0000`-`$E4:8FFF`) | 1294 | 162131 | `DialogCollection.render()` |
| Object Movement Sequences (`$E1:0800`-`$E1:BADE`) | 24 | 41459 | `ActionScriptCollection.render()` |
| Tilesets, compressed (`$FB:0000`-`$FD:B5D3`) | 7 | 20466 | `RoomCollection.render()` / area mapping |
| Battle Event pointers + data (`$FA:6000-70FF`) | 5 | 4034 | `BattleEventCollection.render()` |
| Monster Battle Script data | 6 | 7077 | `MonsterCollection.render()` |
| Battle Dialogue + Monster names | 30 | 10314 | `MonsterCollection.render()` + `BattleDialogCollection.render()` |
| Object GFX/Palette + animation data tables | 5 | 7700 | `SpriteCollection.render()` |
| Object mapping properties | 54 | 524 | `SpriteCollection.render()` |
| Equipment/Item names + description | 11 | 99 | `ItemCollection.render()` |
| Spell Names + description | 43 | 83 | `SpellCollection.render()` |
| Monster Stats + EXP/coins/items | 24 | 478 | `MonsterCollection.render()` |
| Monster targetting cursor + Flower Bonus | 20 | 47 | `MonsterCollection.render()` |
| Shop Prices + Data | 2 | 5 | `ShopCollection.render()` |
| Magic Stats + Spell description | 3 | 43 | `SpellCollection.render()` |
| Monster Formation/Pack/Stats + battle event + music | 5 | 5 | `MonsterFormationCollection.render()` |
| Monster Battle Script pointers (1.6KB) | 1 | 1622 | `MonsterCollection.render()` |
| Battle Message pointers + messages | 1 | 5 | `BattleDialogCollection.render()` |
| Sprite Map / Sprite Mapping / Sprite Tilesets | 9 | 29687 | `SpriteCollection.render()` / `RoomCollection.render()` |
| Area Layout / Event Modifications / Exit Field / Overlap | 11 | 12888 | `RoomCollection.render()` / `EventModificationCollection.render()` |
| Event Data pointer tables (`$DE/DF/E0:0000-0BFF`) | 4 | 8157 | `EventScriptCollection.render()` |
| Object Movement Sequence pointers | 2 | 4557 | `ActionScriptCollection.render()` |
| Area Event Mapping pointers + data | 2 | 7604 | `RoomCollection.render()` |
| World maps + Menu Text + Location Names + Map Location data | 16 | 732 | `WorldMapCollection.render()` (engine-rendered images) |
| Spell GFX assignments + mold/palette pointers | 3 | 4029 | `SpellCollection.render()` / `SpriteCollection.render()` |
| Object palettes (`$E5:3000-8FFF`) | 12 | 1754 | `SpriteCollection.render()` |
| Dialogue Table + alphanumeric widths | 5 | 47 | `DialogCollection.render()` |
| Alphanumeric symbol GFX (`$F7:C000-DFFF`) | 7 | 860 | `DialogCollection.render()` (font tables) |
| Dialogue pointer tables (`$F7:E000-FFFF`) | 2 | 8114 | `DialogCollection.render()` |
| Monster Formations (`$F9:C000-F3FF`) | 1 | 1 | `MonsterFormationCollection.render()` |
| **(remaining tail buckets, all DROP)** | — | — | — |

## REVIEW (35 entries, 20669 bytes — mostly gap-region DATA injections)

These fall in gaps not annotated by `doc_offsets.txt`. Visual inspection of
the bytes shows structured DATA (pointer/index patterns), not ASM —
likely the open-mode patch is extending DATA tables into adjacent free
space. Worth eyeballing before final removal, but probably DROP.

| SNES | file ofs | len | likely purpose |
|---|---|---:|---|
| `$FD:D800` | +0x3DD800 | 5206 | Big DATA block in gap between Physical Tile properties (3DC000-3DD7FF) and Dialogue BG GFX (3DF000). Pattern: `25 06 0C 00 68 00 …` → looks like extended tile/exit field data. |
| `$F9:F400` | +0x39F400 | 3072 | Gap between Monster Formations end and `$3A0000`. Pattern: pointer-like. Extended formation table? |
| `$FF:DBB2` | +0x3FDBB2 | 2294 | Within Main Title GFX (CGFX region 3F216F-3FFFFF). Likely tilemap/CGFX. |
| `$FA:5600` | +0x3A5600 | 2118 | Gap between Equipment/Item names (3A55EF end) and Battle Event data start (3A6000). Likely extended item-data table. |
| `$FD:B5E0` | +0x3DB5E0 | 1966 | Tail of Tilesets-compressed region. DATA. |
| `$FF:E4B0` | +0x3FE4B0 | 1545 | Within Main Title CGFX. |
| `$DD:C600` | +0x1DC600 | 1463 | Between Object mapping properties (1DC5FF) and Sprite Mapping parameters (1DDE00). Likely extended sprite-mapping data. |
| `$F7:9A00` | +0x379A00 | 807 | Tail of Flower Garden CGFX. |
| `$DD:B190` | +0x1DB190 | 735 | Between NPC Sprite Packets (1DB18F) and Object mapping properties (1DB800). Likely extended packet data. |
| `$F9:BC60` | +0x39BC60 | 541 | Between Experience Increments (39BC56) and Monster Formations (39C000). |
| `$FA:CA6A` | +0x3ACA6A | 410 | FA tail (after Battle Event data overflow). |
| `$FA:A6A7` | +0x3AA6A7 | 185 | FA tail. |
| `$F9:260A` | +0x39260A | 118 | F9 gap between Formation Packs end and Formation Stats start. |
| `$FA:ADD5` | +0x3AADD5 | 62 | FA tail. |
| `$FA:20B0` | +0x3A20B0 | 61 | FA gap between Stat Bonus modifications end and Magic Stats start. |
| `$FA:E0DF`/`E0EE`/`E0D2` | +0x3AE0DF.. | 6/8/9 | FA tail — runs of `5E` bytes (padding/sentinel). |
| `$C0:6935` | +0x06935 | 3 | Within Dialogue Function Pointers (06905-06952). Engine PTR — **possibly KEEP_ASM** (function-pointer table not normally regenerated). |
| `$C3:4872` | +0x34872 | 3 | Gap after C3 alphanumeric TXT. Likely small DATA. |
| `$FA:CF5B`/`D352`/`DDE5`/`DE04`/`DE90`/`DEC4` | various | 3 each | FA tail — `0A 0A 0A` runs. |
| `$FA:DDEA`/`DE09`/`DEC4` | various | 1 each | FA tail single bytes. |
| `$C2:F988`/`F96F` | +0x2F988/2F96F | 26+5 | "data/functions?" range — possibly engine PTRs (listed above in ASM section pending REVIEW). |

## Deconstruction roadmap

1. ✅ **DONE — audit.** ASM-needs-asm/*.py = 25 entries / 198 bytes (this file).
2. ✅ **DONE — `$C0:9009` analysis.** Naive restore breaks the "protagonist always renders" invariant (party-swap leaves stale `$58,X` animation index; non-protagonist in slot 0 renders as themselves). The follower-slot per-char dispatch (`CHARACTER_IN_SLOT_2` use case) needs a **hybrid hook**, not a vanilla restore — see the `$9009` row above for the design. Tracked separately.
3. Build asm/*.py modules for the remaining 23 trivial ASM entries (mostly menu / CPU-init / SA-1 init / level-cap patches with established functional intent; bytes identical to open_mode.json — the deconstruction is just relocation for traceability).
4. Verify the 35 REVIEW gap entries are DATA (eyeball + cross-check with smrpgpatchbuilder collection renderers).
5. Once all 25 ASM entries are mirrored in asm/*.py and REVIEW entries confirmed DATA, regenerate `open_mode.json` from a clean ROM with only the C-source patches that we *don't* have Python equivalents for, then progressively delete entries from `open_mode.json` as their asm/*.py counterparts land.
