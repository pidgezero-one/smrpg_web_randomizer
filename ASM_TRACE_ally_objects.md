# ASM Trace — why `CHARACTER_IN_SLOT_2` won't show in room 206

> Static ROM trace run autonomously while pidge slept.
> ROM: `SMRPG_US_9.0.0_open_9e4d01abaced03ba5c709ec7322fa555_1516381142_DEBUG.sfc`
> Tool: `~/.claude/skills/asm-trace/rom_reader.py` (`ROM_PATH` repointed to the ROM above).

---

## BOTTOM LINE

`CHARACTER_IN_SLOT_2` is **not** mis-resolving. It correctly and deterministically targets
physical overworld object **1** (the 2nd party slot). The script logic and the `apply.py`
numbering fix are both correct.

The bug is in the **overworld ally-sprite loader**. When a room loads, a loop sets up the
party-member objects and loads their graphics — but in this ROM that loop loads
**character 0's sprite into every ally object slot** (it calls the ally-sprite loader with
character index `0` on every iteration). The lead's sprite slot is the one the randomizer
repoints to the protagonist (Geno).

Net effect: physical object 1 *exists and is set up*, but it carries **the protagonist's
graphics**. So `SummonObjectToCurrentLevelAtMariosCoords(CHARACTER_IN_SLOT_2)` makes a
Geno-looking object appear **on top of** the protagonist (it's summoned *at Mario's coords*)
and the action queue walks it — which reads exactly as your symptom: *"it animates my
protagonist and doesn't summon a distinct second character."*

This is also why **randomizer room 28 doesn't run the `script_3282` party animations** even
though vanilla does — same root cause. The randomizer's "play as X" overworld sprite system
does not load distinct sprites for the non-lead party members; every overworld party object
gets the protagonist sprite.

**CAUTION (2026-05-19).** The collapse-to-char-0 is **load-bearing** — it protects the
"protagonist always renders" invariant. A naive restore breaks more than it fixes; see
"Status update" at the bottom of this doc before designing a fix.

---

## WHAT THIS MEANS FOR YOUR CUTSCENE

- Nothing more to fix in `script_1710.py` or in the `apply.py` numbering conversion — those are correct.
- Bumping room 206's `ally_sprite_buffer_size` will **not** fix it. The buffer is VRAM *space*;
  the problem is *what sprite gets loaded into it*. Both object 0 and object 1 are loaded with
  the protagonist's sprite base.
- Showing a *real* recruited ally in the overworld needs the engine to load that ally's own
  sprite into object 1 — that is an **overworld-sprite-system change** (engine patch territory,
  alongside `non_mario_character.py` / the protagonist sprite swap), not a room or script tweak.

---

## THE TRACE (evidence)

**1. Event command dispatch.** Interpreter entry `$C0:3E93`: reads the opcode byte, then
`JMP ($C6A5,X)` — a 256-entry handler table at `$C0:C6A5`. For object commands it then reads
the *action* byte; actions `≥ $F0` go through a 16-entry table at `$C0:C685`.

**2. `CHARACTER_IN_SLOT_*` → physical object (deterministic).** Table `$C0:C6A5` sends opcodes
`$07–$0B` to handler `$C0:3EC1`, which does `A = opcode − 8`:

| area object | opcode | physical object |
|---|---|---|
| `CHARACTER_IN_SLOT_1` | `$08` | object 0 (lead = the character you control) |
| `CHARACTER_IN_SLOT_2` | `$09` | **object 1** |
| `CHARACTER_IN_SLOT_3` | `$0A` | object 2 |

Fixed subtraction — no runtime table, no ambiguity. (Opcodes `$10+` *do* use a runtime table
at RAM `$7098`; `CHARACTER_IN_SLOT_*` does not.) Object structs live at `$6000 + N·$60`
(obj0 `$6000`, obj1 `$6060`, obj2 `$60C0`).

**3. "Summon" = a flag, not a spawn.** `0xF8` (`$C0:40F7`) sets **bit 7 of object byte `$07`**
("present in level"). `0xF7` (`$C0:4085`) copies Mario's coords into the object, then sets that
bit. `0xF9` clears it. So summon just flips a present/visible flag on an *already-existing*
object struct — it cannot give the object graphics it doesn't have.

**4. Room-load ally setup loop (`$C0:8FEE`–`$C0:9042`).** On room load:
- `ally_sprite_buffer_size` = bits 5–6 of partition byte 0.
- For the first `ally_sprite_buffer_size` objects: `JSR $9B4E` (ally-sprite loader).
- For the remaining objects: their present bit (`$07.7`) is force-cleared.
- The loop body at `$C0:9009` does `LDA #$00 / STA $60` **every iteration**, then
  `JSR $9B4E`. `$60` is the **character index** the ally-sprite loader uses.

**5. Ally-sprite loader `$C0:9B4E`.** Maps character index `$60` → overworld sprite base:
`0→$1F, 1→$07, 2→$0D, 3→$19, 4→$13`. The `$1F` (character 0) constant lives at `$C0:9B86` —
and `randomizer/patches/asm/non_mario_character.py` **patches exactly that byte** to the
protagonist's sprite base for a non-Mario protagonist.

⇒ Because the loop always passes `$60 = 0`, **every** ally object (0, 1, …) is loaded with
character 0's sprite = `$1F` = (randomizer-patched) the protagonist's sprite. Object 1 ends
up holding Geno's graphics.

---

## PROVEN vs INFERRED

**Proven by static disassembly:**
- `CHARACTER_IN_SLOT_2` → physical object 1; object struct math; summon = `$07.7`.
- `$C0:9B4E` maps character index → sprite base; `$1F` byte at `$C0:9B86` is the
  randomizer-patched protagonist slot.
- The room-load loop calls `$C0:9B4E` once per ally-buffer slot.

**Inferred (one step):** that the loop passes `$60 = 0` for *every* slot. The bytes at
`$C0:9009` decode as `LDA #$00 / NOP / STA $60` (the `NOP` is a patch artifact). This is the
single link I could not 100% confirm statically.

### Confirm it in bsnes-plus (5 min)
1. Open the ROM in bsnes-plus v05.
2. Execution breakpoint at **`$C0:900E`** on the **SA-1 bus** (overworld sprite/VRAM code runs
   on SA-1).
3. Enter room 206 (Bandits Way 5).
4. It should break **`ally_sprite_buffer_size` times** (twice for room 206). On each break read
   direct-page **`$00:0060`** and register **X**.
   - Expected if the diagnosis holds: `$60 = 00` every time; `X` = `6000` then `6060`.
   - If `$60` instead steps `00, 01, …` then the loader *is* getting per-slot characters and
     the real fault is elsewhere — re-trace from there.

---

## FIX DIRECTION

To make object 1 show the actual 2nd party member, the room-load ally loop must pass that
slot's **real character index** to `$C0:9B4E`, instead of a hard `0`. That slot's character is
available at runtime in party RAM (vanilla's loader read it per slot; the randomizer's
overworld-sprite path collapsed it to "always the protagonist").

That is a change in the same engine layer as `non_mario_character.py` — it needs the loop at
`~$C0:9009` to load `$60` from the party roster per object, and the ally buffer sized to fit
the extra character's sprite (your `ally_sprite_buffer_size` reasoning then applies normally).
It is **not** fixable from `script_1710.py` or `room_206.py` alone.

(Open question — resolved below.)

---

## UPDATE — both gutting patches live in `open_mode.json`

`randomizer/static/randomizer/patches/open_mode.json` (the base open-mode patch) contains two
entries that collapse the overworld multi-character system to "everyone is character 0":

| Offset (dec / SNES) | Bytes | Effect |
|---|---|---|
| `16050` / `$C0:3EB2` | `EA × 11` | NOPs the body of the MARIO/PEACH/BOWSER/GENO/MALLOW resolver. The handler falls through to `$3EBD: LDA $81 / BRA $3EEC` where `$81` was `STZ`'d → returns slot 0. The prelude at `$3EA5–$3EB1` is intact (`LDX #$3033 / LDA $00303F / STA $80 / STZ $81 / LDA $70`) — that's the search setup; the search itself was stamped out. |
| `36873` / `$C0:9009` | `A9 00 EA` | Stamps out a 3-byte instruction (almost certainly `BD xx xx` = `LDA <roster_table>,X`) with `LDA #$00 / NOP`. Forces character index `0` into `$60` for every ally-buffer iteration in the room-load loop, so `JSR $9B4E` loads char-0's sprite into every party-object slot. |

Neither is in any `randomizer/patches/asm/*.py`. `non_mario_character.py`'s patches (`$9B86`
default sprite base, `$94AF` clone-protagonist handler) are *downstream* of these — they
reroute "character 0's sprite" to the protagonist, which only does useful work because
everything upstream was collapsed to character 0.

### To restore follower display

**Status update 2026-05-19.** The naive restore (`$9009` → `B9 00 00`, `non_mario_character.py`
patches the protagonist's actual loader slot) was tried and **reverted** — see commit history.
It broke the "protagonist always renders" invariant that the open-mode collapse was protecting:

- The `$9B4E` loader doesn't only return a sprite base; it also writes a *per-character
  animation index* to `$58,X` (Geno → `$05`, lead default → `$07`, follower default → `$06`).
  The alt-protagonist sprite was tuned for `$07`. Restoring `$9009` made non-Mario leads get
  their char-specific index instead, breaking walking-animation sequences.
- Mid-room party swaps don't re-run the room-load loop, so the `$58,X` animation-index value
  becomes stale when the slot-0 character changes (one of the user-observed symptoms).
- Any script that puts a non-protagonist character into slot 0 then renders that character as
  themselves (since the loader now correctly reads their roster char id), instead of as the
  protagonist sprite. The buggy collapse was preventing this.

### Correct direction: hybrid hook

For the `CHARACTER_IN_SLOT_2` use case (cutscene follower-slot rendering) without losing the
protagonist invariant, we need:

- **Slot 0 (lead)**: keep forcing char id = 0 so the loader always returns alt-protagonist
  sprite `$1F` and animation index `$07`.
- **Slot 1+ (followers)**: use the real roster char id so each follower loads their own
  sprite.

Implementation sketch — patch `$9009` from `A9 00 EA` (load `0`) to a 3-byte `JSR $XXXX` to
a helper in C0 free space:

```
helper:
  CPY #$33     ; first roster offset = slot 0?
  BNE not_lead
  LDA #$00     ; lead → force char 0
  RTS
not_lead:
  LDA $0000,Y  ; vanilla per-slot lookup
  RTS
```

Then the existing `STA $60` at `$900C` stores the right value. The `non_mario_character.py`
`$9B86` patch stays as-is (lead always loads char 0 → alt protagonist sprite).

Open question: free C0 space for the helper. Candidates from `doc_offsets.txt` gaps —
`$00CA45-$00CA81` (61 bytes), `$00F2B1-$00F7F0` (~1.3 KB), `$00FBEC-$00FFFF` (~1 KB) — but
the open-mode patch may have already used some of these (audit each via `OPEN_MODE_AUDIT_ASM.md`'s
DROP_COVERED list before claiming a region).

`ally_sprite_buffer_size` becomes load-bearing again once the hybrid lands, as originally
described.
