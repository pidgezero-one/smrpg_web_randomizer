# Uncap Max FP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `UncapMaxFP` boolean flag that, when enabled, lets ally max FP exceed 99 (cap at 255 — the storage byte's hardware limit) by replacing two hardcoded ASM caps with overflow-safe drop-in patches, plus per-site UI display widening for FP renderers.

**Architecture:** Two 6-byte inline ASM patches gated on the flag, applied through the existing `world.patch.add_data(...)` mechanism in `gameworld.py:get_patch()`. Flag plumbing follows the existing `UncapSuperJumps` pattern (class definition in `flags.py`, registered in a category, added to `Settings.__init__()`). UI display fixes are scoped per-site: trace each renderer with the asm-trace skill, land a small tweak if possible, otherwise cut and track as follow-up.

**Tech Stack:** Python 3.12 (Django app), 65816 SNES assembly, `~/.claude/skills/asm-trace/rom_reader.py` for static ROM analysis, bsnes-plus v05 for runtime verification.

**Spec:** `docs/superpowers/specs/2026-05-03-uncap-max-fp-design.md`

**Verification model:** This codebase has no real test suite (`randomizer/tests.py` is empty). Verification happens by (a) building a seed and asserting patched bytes appear at the right ROM offset, and (b) manual playtesting in bsnes-plus. Each task that touches ASM ends with a byte-level static check; a separate end-of-plan task wraps the playtest checklist.

---

## Pre-flight

### Task 0: Verify environment

**Files:** none

- [ ] **Step 1:** Confirm a vanilla SMRPG ROM is reachable for the asm-trace skill.

```bash
ls -la /home/pidge/code/smrpg_web_randomizer/smrpg.sfc
python3 ~/.claude/skills/asm-trace/rom_reader.py read C0C4C5 --length 16
```

Expected: file exists; output line `C0/C4C5 | AF B2 F8 7F 18 65 70 C9 63 90 02 A9 63 8F B2 F8`. If the bytes differ, **stop and re-trace** — the spec assumes vanilla layout.

- [ ] **Step 2:** Confirm the second cap site matches the spec.

```bash
python3 ~/.claude/skills/asm-trace/rom_reader.py read C2C148 --length 24
```

Expected: contains `... C9 63 30 02 A9 63 8F 0D FA 7E 8F 0C FA 7E 60` (the 99-cap pattern at offset $C2:C14F, followed by the dual-store + RTS).

- [ ] **Step 3:** Confirm a vanilla seed builds via the canonical `randomizer.main.create()` factory and produces a working `Patch` object.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
s = Settings()
world = create(1, s)
patch = world.get_patch()
print(f'OK: built seed; patch addresses count = {len(patch.addresses)}')
"
```

Expected: `OK: built seed; patch addresses count = <some integer>`. (The Django setup is required because `Settings` is consumed indirectly through Django app code.) **Note:** the `manage.py make_seed` command exists but its top-level import `from randomizer.logic.main import GameWorld, Settings` does not resolve in this codebase; do **not** use `make_seed` for verification. Use the inline harness shown above.

- [ ] **Step 4:** No commit (this task is environment verification only).

---

## Part 1 — Flag plumbing

### Task 1: Add the `UncapMaxFP` flag class

**Files:**
- Modify: `randomizer/types/flags.py:657-660` (insert immediately after `UncapSuperJumps`)

- [ ] **Step 1:** Open `randomizer/types/flags.py` and find the `UncapSuperJumps` class (line 657). Insert the new class directly after it, before the `# ✅` line that introduces `LearnableSpellEnum`.

Insertion (place between line 660 and line 663):

```python
class UncapMaxFP(BooleanFlag):
    _name = "Uncap maximum FP"
    _description = "If enabled, allies' max FP threshold can exceed 99 (capped at 255)."
    _id = "uncapfp"
```

- [ ] **Step 2:** Verify the class is syntactically discoverable.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "from randomizer.types.flags import UncapMaxFP; f=UncapMaxFP(); print(f._id, f._name, f.enabled, f.default)"
```

Expected output: `uncapfp Uncap maximum FP False False`

- [ ] **Step 3:** Commit.

```bash
git add randomizer/types/flags.py
git commit -m "feat: add UncapMaxFP flag class"
```

---

### Task 2: Register `UncapMaxFP` in `CharacterStatsSpellsSubcategory`

**Files:**
- Modify: `randomizer/types/flags.py:2535-2549` (the `CharacterStatsSpellsSubcategory._flags` list)

- [ ] **Step 1:** Find `class CharacterStatsSpellsSubcategory(FlagCategory):` (around line 2535). Add `UncapMaxFP` to `_flags` immediately after `UncapSuperJumps`.

Before:

```python
    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        InfuseSpellElements,
        CharacterSpellElements,
        UncapSuperJumps,
        AvailableSpells,
    ]
```

After:

```python
    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        InfuseSpellElements,
        CharacterSpellElements,
        UncapSuperJumps,
        UncapMaxFP,
        AvailableSpells,
    ]
```

- [ ] **Step 2:** Verify the flag is reachable through the category.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
from randomizer.types.flags import CharacterStatsSpellsSubcategory, UncapMaxFP
assert UncapMaxFP in CharacterStatsSpellsSubcategory._flags
print('OK: UncapMaxFP in subcategory')
"
```

Expected: `OK: UncapMaxFP in subcategory`

- [ ] **Step 3:** Commit.

```bash
git add randomizer/types/flags.py
git commit -m "feat: register UncapMaxFP in CharacterStatsSpells subcategory"
```

---

### Task 3: Register `UncapMaxFP` in `Settings.__init__()`

**Files:**
- Modify: `randomizer/types/settings.py:78` (the `_flags` dict in `Settings.__init__`)

- [ ] **Step 1:** Open `randomizer/types/settings.py`, find `UncapSuperJumps: UncapSuperJumps(),` at line 78, and insert the new entry directly after it.

Before:

```python
            UncapSuperJumps: UncapSuperJumps(),
            AvailableSpells: AvailableSpells(),
```

After:

```python
            UncapSuperJumps: UncapSuperJumps(),
            UncapMaxFP: UncapMaxFP(),
            AvailableSpells: AvailableSpells(),
```

- [ ] **Step 2:** Verify the flag is wired into a fresh `Settings()` instance.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
from randomizer.types.settings import Settings
from randomizer.types.flags import UncapMaxFP
s = Settings()
assert UncapMaxFP in s._flags
assert s.isflag_enabled(UncapMaxFP) is False
print('OK: default-disabled, registered')
"
```

Expected: `OK: default-disabled, registered`

- [ ] **Step 3:** Commit.

```bash
git add randomizer/types/settings.py
git commit -m "feat: register UncapMaxFP in Settings._flags"
```

---

## Part 2 — ASM cap patches

### Task 4: Patch the event-script `Add7000ToMaxFP` cap (`$C0:C4CC`)

**Files:**
- Modify: `randomizer/types/gameworld.py:1918` (insert a new `if` block immediately after the `ShowEquips` block, before the `# Battle music IDs` comment)

- [ ] **Step 1:** Open `randomizer/types/gameworld.py`. Find the `ShowEquips` block (line 1917-1918). Insert the new flag-gated patch block immediately after.

Before:

```python
        if self.settings.isflag_enabled(ShowEquips):
            patch.add_data(0x033B6D, bytes([0x29, 0x1F, 0xEA]))

        # Battle music IDs - write 8 selected music IDs to the music pointer table
```

After:

```python
        if self.settings.isflag_enabled(ShowEquips):
            patch.add_data(0x033B6D, bytes([0x29, 0x1F, 0xEA]))

        if self.settings.isflag_enabled(UncapMaxFP):
            # Add7000ToMaxFP handler ($C0:C4CC): replace 99-cap with 255-cap.
            # BCS catches 8-bit ADC overflow so a wrap cannot regress max FP.
            patch.add_data(0xC4CC, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])

        # Battle music IDs - write 8 selected music IDs to the music pointer table
```

- [ ] **Step 2:** Verify the import for `UncapMaxFP` resolves. `gameworld.py` imports `from .settings import *` (or similar) — check the existing pattern.

```bash
cd /home/pidge/code/smrpg_web_randomizer
grep -n "from .settings\|from .flags\|UncapSuperJumps\|isflag_enabled" randomizer/types/gameworld.py | head -10
```

Expected: existing wildcard or named import already pulls flag classes in. If `UncapSuperJumps` resolves elsewhere in the file, `UncapMaxFP` will resolve identically. If not, add `UncapMaxFP` to the appropriate import line — match the style used for `UncapSuperJumps` if it's named-imported, otherwise no change needed for a wildcard import.

- [ ] **Step 3:** Verify the patch applies in a built seed. Use the canonical factory `randomizer.main.create()` and check the bytes at `0xC4CC`.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
from randomizer.types.flags import UncapMaxFP
s = Settings()
s._flags[UncapMaxFP].enable()
world = create(1, s)
patch = world.get_patch()
data = bytes(patch.get_data(0xC4CC))
print('bytes at 0xC4CC:', data.hex())
assert data == bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]), f'WRONG: {data.hex()}'
print('OK: patch applied')
"
```

Expected: `bytes at 0xC4CC: b0028002a9ff` then `OK: patch applied`.

- [ ] **Step 4:** Verify the patch is **not** applied when the flag is off.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
s = Settings()
world = create(1, s)
patch = world.get_patch()
data = bytes(patch.get_data(0xC4CC))
assert data == b'', f'leaked patch with flag off: {data.hex()}'
print('OK: clean when flag off')
"
```

Expected: `OK: clean when flag off`

- [ ] **Step 5:** Commit.

```bash
git add randomizer/types/gameworld.py
git commit -m "feat: patch event-script max FP cap when UncapMaxFP enabled"
```

---

### Task 5: Patch the battle bump-max-FP cap (`$C2:C14F`)

**Files:**
- Modify: `randomizer/types/gameworld.py` (the `if UncapMaxFP` block from Task 4)

- [ ] **Step 1:** Extend the `UncapMaxFP` block to also patch the battle handler.

Before:

```python
        if self.settings.isflag_enabled(UncapMaxFP):
            # Add7000ToMaxFP handler ($C0:C4CC): replace 99-cap with 255-cap.
            # BCS catches 8-bit ADC overflow so a wrap cannot regress max FP.
            patch.add_data(0xC4CC, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
```

After:

```python
        if self.settings.isflag_enabled(UncapMaxFP):
            # Add7000ToMaxFP handler ($C0:C4CC): replace 99-cap with 255-cap.
            # BCS catches 8-bit ADC overflow so a wrap cannot regress max FP.
            patch.add_data(0xC4CC, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
            # Battle bump-max-FP handler ($C2:C14F): same fix, identical bytes.
            patch.add_data(0x2C14F, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
```

- [ ] **Step 2:** Verify both patches apply.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
from randomizer.types.flags import UncapMaxFP
s = Settings()
s._flags[UncapMaxFP].enable()
world = create(1, s)
patch = world.get_patch()
expected = bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
for addr in (0xC4CC, 0x2C14F):
    data = bytes(patch.get_data(addr))
    assert data == expected, f'addr {addr:#x}: {data.hex()}'
print('OK: both cap sites patched')
"
```

Expected: `OK: both cap sites patched`

- [ ] **Step 3:** Verify the patched bytes disassemble correctly. Build a ROM with the patch applied and disassemble the cap regions.

```bash
cd /home/pidge/code/smrpg_web_randomizer
# Build a ROM by combining vanilla smrpg.sfc + base open_mode.json + flag-on patch.
python3 - <<'PYEOF'
import django, os, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
from randomizer.types.flags import UncapMaxFP

rom = bytearray(open('smrpg.sfc', 'rb').read())
base_patch = json.load(open('randomizer/static/randomizer/patches/open_mode.json'))
for ele in base_patch:
    key = list(ele)[0]
    addr = int(key)
    for byte in ele[key]:
        rom[addr] = byte
        addr += 1

s = Settings()
s._flags[UncapMaxFP].enable()
world = create(1, s)
patch = world.get_patch()
for addr in patch.addresses:
    cur = addr
    for byte in patch.get_data(addr):
        rom[cur] = byte
        cur += 1

open('/tmp/uncap.sfc', 'wb').write(rom)
print('wrote /tmp/uncap.sfc')
PYEOF
cp ~/.claude/skills/asm-trace/rom_reader.py /tmp/rom_reader_uncap.py
sed -i 's|ROM_PATH = .*|ROM_PATH = "/tmp/uncap.sfc"|' /tmp/rom_reader_uncap.py
echo "=== event handler ==="
python3 /tmp/rom_reader_uncap.py disasm C0C4C5 --count 8
echo "=== battle handler ==="
python3 /tmp/rom_reader_uncap.py disasm C2C148 --count 8
```

Expected output for event handler:

```
C0/C4C5: AF B2 F8 7F  LDA $7FF8B2
C0/C4C9: 18           CLC
C0/C4CA: 65 70        ADC $70
C0/C4CC: B0 02        BCS $C0C4D0
C0/C4CE: 80 02        BRA $C0C4D2
C0/C4D0: A9 FF        LDA #$FF
C0/C4D2: 8F B2 F8 7F  STA $7FF8B2
C0/C4D6: 60           RTS
```

Expected output for battle handler (same structure, different store):

```
C2/C148: AF 0D FA 7E  LDA $7EFA0D
C2/C14C: 18           CLC
C2/C14D: 65 FB        ADC $FB
C2/C14F: B0 02        BCS $C2C153
C2/C151: 80 02        BRA $C2C155
C2/C153: A9 FF        LDA #$FF
C2/C155: 8F 0D FA 7E  STA $7EFA0D
```

- [ ] **Step 4:** Confirm vanilla seed (flag off) is byte-identical to baseline at the cap sites. Build a flag-off ROM with the same harness pattern as Step 3 (just omit the `s._flags[UncapMaxFP].enable()` line) and check the bytes.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 - <<'PYEOF'
import django, os, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings

rom = bytearray(open('smrpg.sfc', 'rb').read())
base_patch = json.load(open('randomizer/static/randomizer/patches/open_mode.json'))
for ele in base_patch:
    key = list(ele)[0]
    addr = int(key)
    for byte in ele[key]:
        rom[addr] = byte
        addr += 1

s = Settings()  # flag off
world = create(1, s)
patch = world.get_patch()
for addr in patch.addresses:
    cur = addr
    for byte in patch.get_data(addr):
        rom[cur] = byte
        cur += 1

assert rom[0xC4CC:0xC4D2] == bytes([0xC9,0x63,0x90,0x02,0xA9,0x63]), \
    f'event site changed: {rom[0xC4CC:0xC4D2].hex()}'
assert rom[0x2C14F:0x2C155] == bytes([0xC9,0x63,0x30,0x02,0xA9,0x63]), \
    f'battle site changed: {rom[0x2C14F:0x2C155].hex()}'
print('OK: flag-off seed preserves vanilla cap')
PYEOF
```

Expected: `OK: flag-off seed preserves vanilla cap`

- [ ] **Step 5:** Commit.

```bash
git add randomizer/types/gameworld.py
git commit -m "feat: patch battle bump-max-FP cap when UncapMaxFP enabled"
```

---

## Part 3 — UI display fixes (per-site fallback)

The remaining tasks update FP renderers to display 3 digits when `UncapMaxFP` is enabled. **Each task starts by tracing the renderer with the asm-trace skill.** If the renderer turns out to require shifting tilemap geometry or restructuring text-window dimensions, the task is **cut from this PR** and tracked as a follow-up: comment out the `patch.add_data` call, leave a `# TODO(uncapfp follow-up): widen <site>` comment, and update the flag's `_description` to acknowledge "battle/menu UI may overflow visually".

For each UI task, "small tweak" means: a single-instruction or 2-3-byte digit-count change at a clearly identified renderer entry point. Anything broader is "structural" and gets cut.

### Task 6: Status-menu FP display (X menu)

**Files:**
- Trace target: bank `$C3` (menus). Specific routine to be identified during the task.
- Modify (if small tweak): `randomizer/types/gameworld.py` (extend the `UncapMaxFP` block).

- [ ] **Step 1:** Trace the FP renderer on the X-menu character status screen. Use the asm-trace skill or run rom_reader directly.

```bash
# Find code reading current FP ($7F:F8B1) or max FP ($7F:F8B2) in bank C3.
python3 ~/.claude/skills/asm-trace/rom_reader.py find "AF B1 F8 7F" --start C30000 --end C40000
python3 ~/.claude/skills/asm-trace/rom_reader.py find "AF B2 F8 7F" --start C30000 --end C40000
```

Disassemble each hit (`disasm <addr> --count 30`). Look for the digit-print loop: typically a routine that does either (a) BCD division by 10 to extract digits, or (b) a 2-digit print loop. Identify whether widening to 3 digits is a small instruction tweak or a tilemap layout change.

- [ ] **Step 2:** Decide cut-or-implement.

If the renderer uses a generic 2-digit print routine and there is a 3-digit variant nearby, or if a single byte changes the loop count, **implement** in step 3.

If it requires shifting tilemap positions or rewriting the text-window dimensions, **cut**:
- Add a comment to the `UncapMaxFP` block: `# TODO(uncapfp follow-up): widen X-menu FP display (bank $C3 ~$XXXX)`
- Update the flag description in `flags.py:UncapMaxFP._description` to add: `<br><br>Note: HUD displays may visually overflow when FP exceeds 99.`
- Skip to Step 5.

- [ ] **Step 3:** Apply the small tweak. Add to the existing `UncapMaxFP` block in `gameworld.py`:

```python
            # X-menu FP display: <document the change in 1 line — e.g. "extend digit-print loop from 2 to 3">
            patch.add_data(<addr>, [<bytes>])
```

Replace `<addr>` and `<bytes>` with the values determined in step 1.

- [ ] **Step 4:** Verify by booting `/tmp/uncap.sfc` in bsnes-plus, opening a save with max FP raised above 99 (if you don't have one, use bsnes-plus memory editor to write `7F:F8B2 = $C8` (200) directly), and opening the X menu. Confirm the FP shows `XXX/200` (or whatever the current/max is). Take a screenshot if helpful.

- [ ] **Step 5:** Commit (whichever path you took).

```bash
git add randomizer/types/gameworld.py randomizer/types/flags.py
git commit -m "feat: widen X-menu FP display for UncapMaxFP"
# or, if cut:
git commit -m "docs: note X-menu FP display overflow under UncapMaxFP follow-up"
```

---

### Task 7: Battle spell-selection FP display

**Files:**
- Trace target: bank `$C2` (battle).
- Modify (if small tweak): `randomizer/types/gameworld.py`.

- [ ] **Step 1:** Trace the FP renderer used when picking a spell.

```bash
# Look for FP display routines in bank C2 around the spell-menu code.
python3 ~/.claude/skills/asm-trace/rom_reader.py find "AF 0C FA 7E" --start C20000 --end C30000
python3 ~/.claude/skills/asm-trace/rom_reader.py find "AF 0D FA 7E" --start C20000 --end C30000
```

Disassemble each hit. Look for digit-extraction or print-2-digit calls. Identify the FP display vs comparison sites (writing to a tilemap buffer = display; just CMP/store = math).

- [ ] **Step 2:** Decide cut-or-implement (same rules as Task 6).

If a layout shift is needed, **cut**: add `# TODO(uncapfp follow-up): widen battle spell-menu FP display` and update the flag description if Task 6 didn't already.

- [ ] **Step 3:** Apply the small tweak. Add to the existing `UncapMaxFP` block:

```python
            # Battle spell-menu FP display: <one-line description>
            patch.add_data(<addr>, [<bytes>])
```

- [ ] **Step 4:** Verify in bsnes-plus by entering a battle, raising max FP via memory editor (`7E:FA0D = $C8`), and opening the spell menu. Confirm `current/max` displays correctly past 99.

- [ ] **Step 5:** Commit.

```bash
git add randomizer/types/gameworld.py
git commit -m "feat: widen battle spell-menu FP display for UncapMaxFP"
# or, if cut:
git commit -m "docs: note battle spell-menu FP display overflow under UncapMaxFP follow-up"
```

---

### Task 8: Royal Syrup / Kerokero Cola heal popup digit width

**Files:**
- Trace target: bank `$C2`.
- Modify (if small tweak): `randomizer/types/gameworld.py`.

- [ ] **Step 1:** Trace the Kerokero Cola item handler to determine whether it routes through the additive-heal path (`$C2:C040`) or the absolute-set path (`$C2:C13F`).

The additive path stores the raw heal delta in `$7E:0045,X` (`STA $7E:0045,X` at `$C2:C069`). If KKC uses this path with full-heal semantics, the delta can exceed 99 when max FP > 99. The absolute path doesn't drive a delta popup.

```bash
# Find places that JSR/JSL into either path.
python3 ~/.claude/skills/asm-trace/rom_reader.py find "20 40 C0" --start C20000 --end C30000  # JSR to ?
python3 ~/.claude/skills/asm-trace/rom_reader.py find "22 40 C0 C2" 2>&1 | head        # JSL into $C2:C040
python3 ~/.claude/skills/asm-trace/rom_reader.py find "22 3F C1 C2" 2>&1 | head        # JSL into $C2:C13F
```

Cross-reference with the item table for Kerokero Cola (look in `randomizer/data/items/` or via `grep -r "Kerokero" randomizer/data/`).

- [ ] **Step 2:** If KKC routes through the absolute-set path, **no popup widening is needed** — skip to Step 5 with no changes (commit nothing for this task; close it out with a note in the description).

If KKC routes through the additive path, locate the popup digit-print routine (find the renderer that reads `$7E:0045,X` and writes to a tilemap). This is typically the same generic digit-print routine that handles damage popups; SMRPG damage popups already display 4 digits, so the renderer probably already supports >99.

- [ ] **Step 3:** Decide cut-or-implement. If the popup renderer already handles 3+ digits (likely true since damage popups can show 4 digits), **no patch is needed**. If a per-site cap exists in the FP-popup-specific code, apply the small tweak.

- [ ] **Step 4:** Verify in bsnes-plus: enter a battle with at least one ally at high max FP, use Kerokero Cola, observe the popup. The displayed delta should match the actual heal (no truncation, no wrap).

- [ ] **Step 5:** Commit (or no-op if no patch was needed).

```bash
# If a patch was needed:
git add randomizer/types/gameworld.py
git commit -m "feat: widen FP heal popup digits for UncapMaxFP"
# Otherwise: no commit; just record findings in step 5 description for the playtest task.
```

---

## Part 4 — Verification

### Task 9: End-to-end byte-level verification

**Files:** none (verification only).

- [ ] **Step 1:** Build a seed with `UncapMaxFP` enabled and confirm both ASM patches landed.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
from randomizer.types.flags import UncapMaxFP
s = Settings()
s._flags[UncapMaxFP].enable()
world = create(42, s)
patch = world.get_patch()

expected_cap = bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
for label, addr in (('event', 0xC4CC), ('battle', 0x2C14F)):
    got = bytes(patch.get_data(addr))
    assert got == expected_cap, f'{label} site {addr:#x}: {got.hex()}'
    print(f'OK {label} cap @ {addr:#x}: {got.hex()}')
"
```

Expected: two `OK` lines.

- [ ] **Step 2:** Build a seed with the flag **disabled** and confirm neither patch is present.

```bash
cd /home/pidge/code/smrpg_web_randomizer
python3 -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()
from randomizer.main import create
from randomizer.types.settings import Settings
s = Settings()
world = create(42, s)
patch = world.get_patch()
for addr in (0xC4CC, 0x2C14F):
    got = bytes(patch.get_data(addr))
    assert got == b'', f'unexpected patch at {addr:#x}: {got.hex()}'
print('OK: no UncapMaxFP patches when flag is off')
"
```

Expected: `OK: no UncapMaxFP patches when flag is off`

- [ ] **Step 3:** Build a full ROM and confirm the disassembly at the cap sites.

```bash
cd /home/pidge/code/smrpg_web_randomizer
# (Use the harness from Task 5 step 3 to write a ROM with the flag enabled.)
sed -i 's|ROM_PATH = .*|ROM_PATH = "/tmp/uncap.sfc"|' /tmp/rom_reader_uncap.py 2>/dev/null || true
python3 /tmp/rom_reader_uncap.py disasm C0C4CC --count 4
python3 /tmp/rom_reader_uncap.py disasm C2C14F --count 4
```

Expected: each site shows `BCS / BRA / LDA #$FF` in that order.

- [ ] **Step 4:** No commit.

---

### Task 10: Manual playtest checklist

**Files:** none (manual verification).

This is a checklist for a human running `/tmp/uncap.sfc` in bsnes-plus. Each item is a separate observation; check them all before declaring the feature done. Capture the result of each in the PR description.

- [ ] **Step 1: Cap-removal sanity.** Start a new game, reach Mushroom Way, level up to ~level 6 by farming. Confirm max FP rises above the vanilla `Add7000ToMaxFP` ceiling at the level-up events.

- [ ] **Step 2: Specific event scripts.** The following scripts call `Add7000ToMaxFP` per the spec. Hit each in a playthrough (or with save states); confirm max FP goes up and is not silently clamped at 99: `script_2305`, `script_2491`, `script_2492`, `script_2817`, `script_214`, `script_3072`, `script_1801`, `script_216`, `script_3363`, `script_1685..1688`. Use a save-state library if available.

- [ ] **Step 3: Royal Syrup correctness.** With max FP at 99, 100, 200, 250, and 255 (set via bsnes-plus memory editor at `$7E:FA0D` and `$7F:F8B2`), use Royal Syrup in battle. Confirm:
  - Heal amount popup shows `50` (no wrap).
  - Current FP rises by exactly 50 unless capped by max.
  - When max=255 and current=255, Royal Syrup is a no-op (or whatever vanilla does — record observed behavior).
  - When max=200 and current=180, current ends at 200 (50 was capped).
  - When max=200 and current=130, current ends at 180.

- [ ] **Step 4: Kerokero Cola correctness.** With max FP at 200 on all party members and current at varying values, use Kerokero Cola in battle. Confirm all members are restored to their respective max values, and any popup display matches the actual heal amount.

- [ ] **Step 5: Spell cost gating.** With current FP > 99, attempt to cast spells of varying costs. Confirm spells are correctly enabled/disabled based on `current_fp >= cost`.

- [ ] **Step 6: Save/load.** Save the game with max FP > 99, reload, confirm the value persists (it's stored at `$7F:F8B2` in save data, which the game's own save logic handles — should "just work" but worth confirming once).

- [ ] **Step 7: Vanilla parity.** Run a flag-off seed; confirm leveling never pushes max FP above 99 (vanilla behavior preserved).

- [ ] **Step 8: HUD overflow inspection.** Open the X menu and observe the FP display at max FP > 99. If Task 6 was cut, expect visual overflow (note in PR description). If implemented, confirm 3-digit display.

- [ ] **Step 9: Battle FP HUD inspection.** In a battle, observe the spell-menu FP display at max FP > 99. Same expectations as Step 8 vs Task 7.

- [ ] **Step 10:** No commit. Write up findings in the PR description: per-step observations, screenshots if useful, list of any UI sites that were cut and what their follow-up will need.

---

## Self-review notes (already applied during plan writing)

- Spec coverage: every section of the spec maps to a task — flag class (Task 1), category (Task 2), settings (Task 3), event-handler patch (Task 4), battle-handler patch (Task 5), three UI sites (Tasks 6/7/8), verification matrix (Tasks 9/10).
- Placeholder scan: UI tasks intentionally include `<addr>` and `<bytes>` placeholders **inside the conditional implementation step** because the addresses must be discovered during tracing — but the surrounding decision logic, cut path, and verification is fully concrete. This is the lesser of two evils versus inventing fake addresses.
- Type/name consistency: flag class is `UncapMaxFP` everywhere, `_id` is `"uncapfp"` everywhere, ROM offsets `0xC4CC` and `0x2C14F` are stable across tasks, patched bytes `[0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]` are stable across both sites.
