# NPC Palette-Swap Sprite Unification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce the number of distinct sprite ids per room by collapsing sprites that are byte-identical apart from `palette_offset`, so fewer NPCs need dedicated VRAM and the packed cursor stops overrunning clone buffer A.

**Architecture:** A generated table of palette-swap equivalence classes drives a merge pass inside `_recalculate_room_partition`, run before buffer assignment. Pure duplicates (identical `palette_offset`) merge by sprite-id override alone. Offset-shifted members additionally declare palette residency on the first object carrying that `palette_id` and receive an `A_IncPaletteRowBy` bump injected into the room's pre-existing `*_SHUFFLED_NPC_ANIMATION_LOADER` stub.

**Tech Stack:** Python 3.12, Django management commands, pytest 8.3.5, smrpgpatchbuilder (PyPI pin — never edit inside `patchvenv/`).

## Global Constraints

- Design spec: `docs/superpowers/specs/2026-07-30-npc-palette-swap-unification-design.md`
- Run tests with `patchvenv/bin/python -m pytest <path> -q`. Tests live in `.claude/tests/`.
- Run management commands with `patchvenv/bin/python manage.py <name>`.
- Never edit `smrpgpatchbuilder` inside `patchvenv/`. Changes to it go in `~/code/smrpgpatchbuilder`, followed by asking the user to run `publish-smrpg`.
- Project rules from `CLAUDE.md`: use `isinstance`, never `hasattr`/`getattr`, never `Any` typing, never `# type: ignore`. Do not silence a `NoneType` error with a skip — ask first.
- The `world` fixture is expensive (~25s). Use `@pytest.fixture(scope="module")`.
- Every bound in this plan is a **skip with a log line**, never a silent truncation.
- Dedicated VRAM ceiling is packed `$40` (32 linear slots). Clone buffer bases are literals: A=`$40`, B=`$80`, C=`$C0`.

---

### Task 1: Unblock room 315 — drop the stale `cannot_clone` override on object 8

Independent of the merge system. Fixes the reported bug on its own.

Object 8 carries a room-level `cannot_clone=True` dating from when this slot held Jonathan Jones alongside Yaridovich. Under boss shuffle its sprite is often 263 (Piranha Plant), already resident in buffer C via objects 4 and 5. The override forces a dedicated allocation anyway, walking the cursor to packed `$40` — clone buffer A's base, where object 0 lives.

Removing the override moves object 8 from "forced dedicated" to "auto-decide". `_recalculate_room_partition` Step 7 then either shares the buffer (when the sprite is buffered) or sets `cannot_clone=True` **and** sizes `min_vram_size` properly via `_size_dedicated_min_vram`. Both outcomes are correct; today's forced path also fixes the second defect, that sprite 263 needs `min_vram_size=1` (molds 6-11 carry 18 subtiles) but the record ships 0, and `$C0:8ED0` skips the bounds check entirely when `min_vram_size == 0`.

**Files:**
- Modify: `randomizer/data/rooms/room_315.py:309`
- Test: `.claude/tests/test_room315_dedicated_vram_cap.py`

**Interfaces:**
- Consumes: `randomizer.logic.partition_calculator._recalculate_room_partition(world, room_id)`; `randomizer.main.create(seed, Settings())`
- Produces: `dedicated_high_water(world, room_id) -> int` and `PACKED_BUFFER_A = 0x40` in the new test module. Task 8 imports both.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_room315_dedicated_vram_cap.py`:

```python
"""Dedicated NPC VRAM must never reach clone buffer A.

Clone buffer bases are literals in the engine -- $C0:8E98-$C0:8EB7 loads #$40,
#$80, #$C0 for buffers A, B and C -- and $C0:8F83 writes that base into the same
object field ($18,X) the dedicated path fills from the packed cursor $6D. So
dedicated NPCs own packed $00-$3F and nothing more. The only guard
($C0:8ED4-$C0:8EFD) stops a block straddling packed $20 or $30; both sit below
$40. A cursor that walks past $40 silently allocates on top of buffer A.
"""
import pytest

from randomizer import main
from randomizer.data.rooms import npcs
from randomizer.logic.partition_calculator import _recalculate_room_partition
from randomizer.types.gameworld import Settings
from smrpgpatchbuilder.datatypes.levels.classes import BufferType

ROOM_ID = 315

# $C0:8E9B loads #$40 as clone buffer A's base, in the same packed units as $6D.
PACKED_BUFFER_A = 0x40


def linear(packed: int) -> int:
    """Packed cursor is (row << 4) | col with 8 columns per row ($C0:B830)."""
    return (packed >> 4) * 8 + (packed & 0x0F)


def packed_add(packed: int, slots: int) -> int:
    """$C0:B830: add slots to a packed cursor, carrying columns into rows."""
    col = (packed & 0x0F) + slots
    return (packed & 0xF0) + ((col & 0xF8) << 1) + (col & 0x07)


def dedicated_high_water(world, room_id: int) -> int:
    """Replay $C0:8FF9 cursor init + $C0:8EBC allocation, return the end cursor.

    Mirrors the engine exactly: ally buffer, then the extra sprite buffer only if
    allowed, then each buffer's main_buffer_space, then one block of
    4 * (min_vram_size + 1) slots per cannot_clone NPC in room-object order, with
    the straddle realign at $C0:8ED4.
    """
    room = world.rooms._rooms[room_id]
    partition = room.partition
    assert partition is not None

    cursor = partition.ally_sprite_buffer_size * 4
    if partition.allow_extra_sprite_buffer:
        cursor += (partition.extra_sprite_buffer_size + 1) * 4
    for buf in partition.buffers:
        cursor += buf.main_buffer_space * 4

    # $C0:908E-$C0:90AA: $01D5 is $41 when buffer A is not EMPTY_3, else $61,
    # selecting the $20 or $30 straddle boundary.
    boundary = 0x20 if partition.buffers[0].buffer_type != BufferType.EMPTY_3 else 0x30

    for obj in room.objects:
        cc = obj.cannot_clone
        if cc is None:
            cc = obj._npc.cannot_clone
        if not cc:
            continue
        mv = obj.min_vram_size
        if mv is None:
            mv = obj._npc.min_vram_size
        slots = 4 * (mv + 1)
        base = cursor
        end = packed_add(base, slots)
        # $C0:8ED0: min_vram_size == 0 skips the straddle check completely.
        if mv != 0 and end > boundary and base < boundary:
            base = boundary
            end = packed_add(base, slots)
        cursor = end
    return cursor


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def test_object_8_is_not_force_dedicated(world):
    """The room-level cannot_clone override on object 8 is a Yaridovich-era
    hardcode. It must be absent so Step 7 can auto-decide -- sharing buffer C
    when the slot's sprite is already buffered, and sizing min_vram_size
    correctly when it is not."""
    room = world.rooms._rooms[ROOM_ID]
    assert room.objects[8].cannot_clone is None


def test_dedicated_allocations_stay_below_buffer_a(world):
    """With object 8 sharing sprite 263's buffer, the cursor must end below
    packed $40. It reached exactly $40 before, putting object 8's block on top
    of object 0."""
    room = world.rooms._rooms[ROOM_ID]
    room.objects[8]._npc = npcs.PIRANHA_PLANT_NPC
    room.objects[8].set_cannot_clone(None)
    room.objects[8].set_min_vram_size(None)

    _recalculate_room_partition(world, ROOM_ID)

    high_water = dedicated_high_water(world, ROOM_ID)
    assert linear(high_water) <= linear(PACKED_BUFFER_A), (
        f"dedicated cursor reached packed ${high_water:02X} "
        f"(linear {linear(high_water)}); buffer A starts at linear "
        f"{linear(PACKED_BUFFER_A)}"
    )
```

Before running, confirm the NPC constant name for sprite 263:

```bash
grep -n "SPR0263_PIRANHA_PLANT" randomizer/data/rooms/npcs.py | head -3
```

If the constant is not `PIRANHA_PLANT_NPC`, substitute the real name in the test.

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_room315_dedicated_vram_cap.py -q`
Expected: FAIL — `test_object_8_is_not_force_dedicated` asserts `cannot_clone is None` but it is currently `True`.

- [ ] **Step 3: Remove the override**

In `randomizer/data/rooms/room_315.py`, object 8 (line 309) currently ends:

```python
            byte7_upper2=3, cannot_clone=True),
```

Change to:

```python
            byte7_upper2=3),
```

Leave objects 6 and 7 unchanged — their sprites have no buffer and legitimately need dedicated VRAM.

- [ ] **Step 4: Run test to verify it passes**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_room315_dedicated_vram_cap.py -q`
Expected: PASS, 2 passed

- [ ] **Step 5: Run the existing VRAM suite for regressions**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_dedicated_vram_sizing.py -q`
Expected: PASS, 8 passed. That suite pins room 315's boss slot (object 7), which this change does not touch.

- [ ] **Step 6: Commit**

```bash
git add randomizer/data/rooms/room_315.py .claude/tests/test_room315_dedicated_vram_cap.py
git commit -m "fix: drop stale cannot_clone override on room 315 object 8

Object 8's room-level cannot_clone=True dates from the Yaridovich-era layout.
Under boss shuffle its sprite is often 263, already resident in buffer C via
objects 4 and 5, but the override forced a dedicated allocation anyway --
walking the packed cursor to \$40, which is clone buffer A's hardcoded base,
where object 0 lives.

Auto-decide handles both cases correctly and also sizes min_vram_size, fixing
a second defect: sprite 263 needs 1 (molds 6-11 carry 18 subtiles) but the
record ships 0, and \$C0:8ED0 skips the bounds check when min_vram_size is 0."
```

---

### Task 2: Generate the palette-swap class table

**Files:**
- Create: `randomizer/management/commands/palette_swap_classes.py`
- Create (generated): `randomizer/data/sprites/palette_swap_classes.py`
- Test: `.claude/tests/test_palette_swap_classes.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces:
  - `randomizer.data.sprites.palette_swap_classes.PURE: dict[int, int]` — non-canonical sprite id to canonical sprite id, same `palette_offset`.
  - `randomizer.data.sprites.palette_swap_classes.SHIFTED: dict[int, tuple[int, int]]` — non-canonical sprite id to `(canonical_sprite_id, pack_offset)`, where `pack_offset` is the non-canonical sprite's own `palette_offset`.
  - `randomizer.management.commands.palette_swap_classes.build_tables() -> tuple[dict[int, int], dict[int, tuple[int, int]]]` — the pure computation, importable by the drift test.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_palette_swap_classes.py`:

```python
"""The palette-swap class table is generated from sprite data. It must not drift.

A class is a set of sprite ids whose definitions are byte-identical once
`palette_offset` is stripped, restricted to sprites that have real graphics and a
palette other than SPAL000_NOTHING. Without that filter the empty
protagonist-remap slots (sprites 31-37, 847-927, 997-1023) collapse into one
false 119-member class.
"""
from randomizer.data.sprites import palette_swap_classes as table
from randomizer.management.commands.palette_swap_classes import build_tables


def test_table_matches_regeneration():
    """Regenerating from current sprite data must reproduce the checked-in table."""
    pure, shifted = build_tables()
    assert pure == table.PURE
    assert shifted == table.SHIFTED


def test_no_sprite_is_in_both_tables():
    assert set(table.PURE) & set(table.SHIFTED) == set()


def test_canonical_sprites_are_not_themselves_merged():
    """A canonical target must never itself be a merge source, or merging is
    order-dependent."""
    merged = set(table.PURE) | set(table.SHIFTED)
    canonicals = set(table.PURE.values()) | {c for c, _ in table.SHIFTED.values()}
    assert canonicals & merged == set()


def test_known_pure_duplicates_present():
    """Sprite 386 is a byte-identical duplicate of 263 (Piranha Plant) at the
    same palette_offset, so merging it needs no palette work at all."""
    assert table.PURE[386] == 263


def test_known_offset_shift_present():
    """Bandana Blue (331) is Bandana Red (267) at pack offset 1."""
    assert table.SHIFTED[331] == (267, 1)


def test_bandana_class_splits_across_both_tables():
    """[267, 331, 380] at offsets [0, 1, 0]: 380 is a free duplicate of 267,
    331 needs a bump."""
    assert table.PURE[380] == 267
    assert table.SHIFTED[331] == (267, 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_classes.py -q`
Expected: FAIL with `ModuleNotFoundError` for both new modules.

- [ ] **Step 3: Write the generator**

Create `randomizer/management/commands/palette_swap_classes.py`:

```python
"""Generate randomizer/data/sprites/palette_swap_classes.py.

Two sprites belong to the same palette-swap class when their definitions are
byte-identical once `palette_offset` is stripped. Such sprites share tile data
outright, so they can share one VRAM clone buffer -- a buffer holds exactly one
sprite_id, and that is the constraint forcing extra NPCs into dedicated VRAM.

Sprites with no graphics, or with palette SPAL000_NOTHING, are excluded. They are
placeholder records (the protagonist-remap slots, the ally slots) whose files are
identical to each other for reasons that have nothing to do with recolouring.

Run: patchvenv/bin/python manage.py palette_swap_classes
"""
import collections
import hashlib
import pathlib
import re

from django.core.management.base import BaseCommand

SPRITE_DIR = pathlib.Path("randomizer/data/sprites/objects")
OUTPUT = pathlib.Path("randomizer/data/sprites/palette_swap_classes.py")

_OFFSET = re.compile(r"palette_offset=(\d+)")
_PALETTE = re.compile(r"palette_id=(\w+)")
_TILE = re.compile(r"\bTile\(")
_MOLD = re.compile(r"\bMold\(")


def _scan() -> dict[int, tuple[str, int]]:
    """sprite_id -> (hash of definition without palette_offset, palette_offset)."""
    found: dict[int, tuple[str, int]] = {}
    for path in SPRITE_DIR.glob("sprite_*.py"):
        match = re.search(r"sprite_(\d+)", path.name)
        if match is None:
            continue
        text = path.read_text()
        offset = _OFFSET.search(text)
        palette = _PALETTE.search(text)
        if offset is None or palette is None:
            continue
        if palette.group(1) == "SPAL000_NOTHING":
            continue
        if not _TILE.search(text) or not _MOLD.search(text):
            continue
        body = "\n".join(
            line
            for line in text.splitlines()
            if "palette_offset=" not in line and not line.startswith("#")
        )
        found[int(match.group(1))] = (
            hashlib.sha1(body.encode()).hexdigest(),
            int(offset.group(1)),
        )
    return found


def build_tables() -> tuple[dict[int, int], dict[int, tuple[int, int]]]:
    """Return (PURE, SHIFTED). Canonical member of a class is its lowest id."""
    scanned = _scan()
    groups: dict[str, list[int]] = collections.defaultdict(list)
    for sprite_id, (digest, _) in scanned.items():
        groups[digest].append(sprite_id)

    pure: dict[int, int] = {}
    shifted: dict[int, tuple[int, int]] = {}
    for members in groups.values():
        if len(members) < 2:
            continue
        members.sort()
        canonical = members[0]
        canonical_offset = scanned[canonical][1]
        for sprite_id in members[1:]:
            offset = scanned[sprite_id][1]
            if offset == canonical_offset:
                pure[sprite_id] = canonical
            else:
                shifted[sprite_id] = (canonical, offset)
    return dict(sorted(pure.items())), dict(sorted(shifted.items()))


HEADER = '''"""Palette-swap equivalence classes. GENERATED -- do not edit by hand.

Regenerate with: patchvenv/bin/python manage.py palette_swap_classes
Drift is caught by .claude/tests/test_palette_swap_classes.py

PURE:    sprite_id -> canonical_sprite_id
         Same palette_offset. Merging is a sprite-id override and nothing else.
SHIFTED: sprite_id -> (canonical_sprite_id, pack_offset)
         Merging additionally needs palette residency plus an A_IncPaletteRowBy
         bump; see docs/superpowers/specs/2026-07-30-npc-palette-swap-unification-design.md
"""
'''


class Command(BaseCommand):
    help = "Generate the palette-swap equivalence class table."

    def handle(self, *args, **options):
        pure, shifted = build_tables()
        lines = [HEADER, "", "PURE: dict[int, int] = {"]
        for sprite_id, canonical in pure.items():
            lines.append(f"    {sprite_id}: {canonical},")
        lines.append("}")
        lines.append("")
        lines.append("SHIFTED: dict[int, tuple[int, int]] = {")
        for sprite_id, (canonical, offset) in shifted.items():
            lines.append(f"    {sprite_id}: ({canonical}, {offset}),")
        lines.append("}")
        lines.append("")
        OUTPUT.write_text("\n".join(lines))
        self.stdout.write(
            f"wrote {OUTPUT}: {len(pure)} pure, {len(shifted)} shifted"
        )
```

- [ ] **Step 4: Generate the table**

Run: `patchvenv/bin/python manage.py palette_swap_classes`
Expected: `wrote randomizer/data/sprites/palette_swap_classes.py: 42 pure, 155 shifted`

These are **per-member** counts: each non-canonical sprite is classified against its own canonical's offset, so a class holding both matching and differing offsets contributes members to both tables. The design document's "26 classes / 32 ids" and "99 classes / 165 ids" are a **class-level** tally of the same 197 ids — 9 mixed classes contribute 10 members to `PURE` and 17 to `SHIFTED`, which is exactly the difference (`42 - 10 = 32`, `155 + 10 = 165`). The Bandana class `[267, 331, 380]` is one of them: 380 lands in `PURE`, 331 in `SHIFTED`. Class count is 125 under either tally.

If the counts differ from 42 and 155, sprite data really has changed. Do not adjust the generator to force the old numbers — update the expected counts here and note the change in the commit message.

- [ ] **Step 5: Run tests to verify they pass**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_classes.py -q`
Expected: PASS, 6 passed

- [ ] **Step 6: Commit**

```bash
git add randomizer/management/commands/palette_swap_classes.py \
        randomizer/data/sprites/palette_swap_classes.py \
        .claude/tests/test_palette_swap_classes.py
git commit -m "feat: generate palette-swap equivalence class table

125 classes across the sprite set, 197 removable sprite ids: 32 pure
duplicates that merge with no palette work, 165 needing a row bump. Excludes
sprites with no graphics or palette SPAL000_NOTHING, which otherwise collapse
the empty protagonist-remap slots into one false 119-member class."
```

---

### Task 3: Extract the CGRAM row model into a shared module

`npc_palette_rows` currently lives in `green_switch_glow.py`. It is a general
room-layout primitive, and the merge pass is a second consumer.

**Files:**
- Create: `randomizer/logic/palette_rows.py`
- Modify: `randomizer/logic/green_switch_glow.py`
- Test: `.claude/tests/test_palette_rows.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces:
  - `randomizer.logic.palette_rows.npc_palette_rows(world, room) -> dict[int, int]` — palette id to CGRAM row. Moved verbatim.
  - `randomizer.logic.palette_rows.PROTAGONIST_PALETTE_ROW: int` (= 8)
  - `randomizer.logic.palette_rows.LAST_SPRITE_PALETTE_ROW: int` (= 15)
  - `randomizer.logic.palette_rows.rows_remaining(world, room) -> int` — free CGRAM rows after current allocations. Task 7 consumes this.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_palette_rows.py`:

```python
"""CGRAM sprite palette rows are a scarce shared budget.

green_switch_glow.npc_palette_rows gives the layout: rows are allocated per
distinct palette_id, starting at PROTAGONIST_PALETTE_ROW + ally_sprite_buffer_size,
one row each plus extra_palette_row_count more. Sprite CGRAM ends at row 15, so a
room at ally buffer 1 has seven rows for NPC palettes.

Only the FIRST object in room order carrying a palette sets its row count --
npc_palette_rows skips later objects with `if palette in rows: continue`. Any
residency declared on a later object is silently ignored.
"""
import pytest

from randomizer import main
from randomizer.logic.palette_rows import (
    LAST_SPRITE_PALETTE_ROW,
    PROTAGONIST_PALETTE_ROW,
    npc_palette_rows,
    rows_remaining,
)
from randomizer.types.gameworld import Settings

ROOM_ID = 315


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def test_constants():
    assert PROTAGONIST_PALETTE_ROW == 8
    assert LAST_SPRITE_PALETTE_ROW == 15


def test_rows_start_after_the_ally_buffer(world):
    room = world.rooms._rooms[ROOM_ID]
    rows = npc_palette_rows(world, room)
    assert rows, "room 315 has NPC palettes"
    lowest = min(rows.values())
    assert lowest == PROTAGONIST_PALETTE_ROW + room.partition.ally_sprite_buffer_size


def test_rows_remaining_is_consistent_with_allocation(world):
    room = world.rooms._rooms[ROOM_ID]
    rows = npc_palette_rows(world, room)
    highest = max(rows.values())
    assert rows_remaining(world, room) == LAST_SPRITE_PALETTE_ROW - highest


def test_green_switch_glow_still_imports_it(world):
    """The glow feature must keep working through the moved function."""
    from randomizer.logic import green_switch_glow

    assert green_switch_glow.npc_palette_rows is npc_palette_rows
```

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_rows.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'randomizer.logic.palette_rows'`

- [ ] **Step 3: Create the module and move the function**

First read the current implementation and its imports so the move is verbatim:

```bash
sed -n '1,60p' randomizer/logic/green_switch_glow.py
grep -n "PROTAGONIST_PALETTE_ROW\|def npc_palette_rows\|def protagonist_palette_id\|EMPTY_SPRITE_ID\|PROTAGONIST_BASE_SPRITE_ID" randomizer/logic/green_switch_glow.py
```

Create `randomizer/logic/palette_rows.py` containing `PROTAGONIST_PALETTE_ROW`,
`protagonist_palette_id`, `npc_palette_rows` moved unchanged from
`green_switch_glow.py`, plus:

```python
# Sprite palettes occupy CGRAM rows 8-15. Row 8 is the protagonist's; each
# ally_sprite_buffer_size unit pushes the first NPC palette up by one.
LAST_SPRITE_PALETTE_ROW = 15


def rows_remaining(world: "GameWorld", room: "Room") -> int:
    """Free CGRAM sprite palette rows in `room` after current allocations.

    Each extra row a palette claims shifts every later palette up by one, and
    per reference_effects_npc_palette_row some effects records target hardcoded
    rows -- so growing residency is never free.
    """
    rows = npc_palette_rows(world, room)
    if not rows:
        return LAST_SPRITE_PALETTE_ROW - (
            PROTAGONIST_PALETTE_ROW + room.partition.ally_sprite_buffer_size
        ) + 1
    return LAST_SPRITE_PALETTE_ROW - max(rows.values())
```

In `green_switch_glow.py`, delete the moved definitions and import them instead:

```python
from .palette_rows import (
    PROTAGONIST_PALETTE_ROW,
    npc_palette_rows,
    protagonist_palette_id,
)
```

Keep every other name in `green_switch_glow.py` as it is. Do not change
`GLOW_RECORDS` or `get_patch`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_rows.py -q`
Expected: PASS, 4 passed

- [ ] **Step 5: Verify the glow feature still builds a patch**

Run:
```bash
patchvenv/bin/python -c "
from randomizer import main
from randomizer.types.gameworld import Settings
from randomizer.logic import green_switch_glow
w = main.create(1, Settings())
print('glow patch entries:', len(green_switch_glow.get_patch(w)))
"
```
Expected: a non-zero count, no traceback.

- [ ] **Step 6: Commit**

```bash
git add randomizer/logic/palette_rows.py randomizer/logic/green_switch_glow.py \
        .claude/tests/test_palette_rows.py
git commit -m "refactor: lift npc_palette_rows into logic/palette_rows

It is a general room-layout primitive that happened to live in a feature
module, and the palette-swap merge pass is about to be a second consumer.
Adds rows_remaining() for the merge pass's CGRAM budget check."
```

---

### Task 4: Tier 1 merge — pure duplicates

Pure duplicates share `palette_offset`, so merging is a sprite-id override and
nothing else: no residency, no bump, no stub, no CGRAM row cost.

**Files:**
- Modify: `randomizer/logic/partition_calculator.py` (add `_merge_palette_swaps`, call it from `_recalculate_room_partition` before Step 3)
- Test: `.claude/tests/test_palette_swap_merge.py`

**Interfaces:**
- Consumes: `randomizer.data.sprites.palette_swap_classes.PURE` (Task 2)
- Produces: `randomizer.logic.partition_calculator._merge_palette_swaps(world, room_id) -> list[tuple[int, int]]` — list of `(obj_index, row_bump)` for objects needing `A_IncPaletteRowBy`. Returns `[]` in this task; Task 7 fills it.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_palette_swap_merge.py`:

```python
"""Merging palette-swap-equivalent sprites frees clone buffers.

A buffer holds exactly one sprite_id, and a room has three. Sprites that are
byte-identical apart from palette_offset can share one buffer once they share a
sprite_id, which is what this pass arranges. It runs before Step 3 of
_recalculate_room_partition, because Step 3 is where "one buffer per unique
sprite ID" is decided.
"""
import copy

import pytest

from randomizer import main
from randomizer.data.sprites.palette_swap_classes import PURE
from randomizer.logic.partition_calculator import (
    _merge_palette_swaps,
    _recalculate_room_partition,
)
from randomizer.types.gameworld import Settings

ROOM_ID = 315


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _sprite_of(obj):
    """A room object's effective sprite is its NPC record's sprite_id.

    Room objects have no per-object sprite override: `RegularNPC` exposes no
    `sprite_id` attribute at all, `BaseRoomObject._sprite_id` is written by
    `set_sprite_id` and read by nothing, and both `_get_npc_signature` and
    `_render_npc` key on the record. Merging therefore swaps the record.
    """
    return int(obj._npc.sprite_id)


@pytest.fixture
def restore_npcs(world):
    """Restore every object's NPC record. Records are shared across rooms, so a
    leaked mutation corrupts unrelated rooms -- see the room 41 landmine."""
    room = world.rooms._rooms[ROOM_ID]
    saved = [obj._npc for obj in room.objects]
    yield room
    for obj, npc in zip(room.objects, saved):
        obj._npc = npc


def _record_with_sprite(npc, sprite_id):
    """A copy of `npc` pointing at `sprite_id`, leaving the shared original alone."""
    record = copy.copy(npc)
    record.set_sprite_id(sprite_id)
    return record


def test_pure_duplicate_is_rewritten_to_canonical(world, restore_npcs):
    """An object whose record carries a PURE source sprite ends up on the canonical."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(obj) == canonical


def test_pure_merge_emits_no_row_bumps(world, restore_npcs):
    """Pure duplicates share palette_offset, so nothing needs A_IncPaletteRowBy."""
    room = restore_npcs
    source, _ = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    assert _merge_palette_swaps(world, ROOM_ID) == []


def test_merge_does_not_mutate_the_shared_record(world, restore_npcs):
    """The pass must copy, never mutate in place -- NPC records are global."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    shared = _record_with_sprite(obj._npc, source)
    obj._npc = shared

    _merge_palette_swaps(world, ROOM_ID)

    assert int(shared.sprite_id) == source, "the pass mutated the record in place"
    assert obj._npc is not shared


def test_merge_reduces_distinct_sprite_count(world, restore_npcs):
    """Two objects on the two halves of a PURE class collapse to one sprite."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj_a, obj_b = room.objects[0], room.objects[1]
    obj_a._npc = _record_with_sprite(obj_a._npc, canonical)
    obj_b._npc = _record_with_sprite(obj_b._npc, source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(obj_a) == _sprite_of(obj_b) == canonical


def test_merge_is_idempotent(world, restore_npcs):
    """Running twice must not change anything the second time."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    _merge_palette_swaps(world, ROOM_ID)
    first = _sprite_of(obj)
    assert _merge_palette_swaps(world, ROOM_ID) == []
    assert _sprite_of(obj) == first == canonical


def test_recalculate_still_succeeds_with_merge_in_place(world):
    """The pass runs inside _recalculate_room_partition without breaking it."""
    _recalculate_room_partition(world, ROOM_ID)
    room = world.rooms._rooms[ROOM_ID]
    assert room.partition is not None
    assert len(room.partition.buffers) == 3
```

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_merge.py -q`
Expected: FAIL with `ImportError: cannot import name '_merge_palette_swaps'`

- [ ] **Step 3: Implement the tier 1 pass**

In `randomizer/logic/partition_calculator.py`, add near the other module-level
helpers:

```python
import copy

from ..data.sprites.palette_swap_classes import PURE


def _canonical_record(npc: NPC, canonical_sprite_id: int) -> NPC:
    """A copy of `npc` pointing at `canonical_sprite_id`.

    Room objects have no usable per-object sprite override -- `RegularNPC`
    exposes no `sprite_id` attribute, `BaseRoomObject._sprite_id` is written by
    `set_sprite_id` and read by nothing, and both `_get_npc_signature` and
    `_render_npc` key on the record. So merging swaps the record instead.

    This MUST copy rather than mutate: NPC records are shared across rooms, and
    mutating one in place corrupts every other room using it. Two objects merged
    onto the same canonical produce records with identical signatures, so
    `_get_npc_signature` dedups them into a single NPC-table entry and they share
    one clone buffer -- which is the whole point.
    """
    record = copy.copy(npc)
    record.set_sprite_id(canonical_sprite_id)
    return record


def _merge_palette_swaps(world: GameWorld, room_id: int) -> list[tuple[int, int]]:
    """Collapse palette-swap-equivalent sprites in `room_id` onto one sprite_id.

    A VRAM clone buffer holds exactly one sprite_id and a room has three, so two
    sprites with byte-identical tile data still cost two buffers until they share
    an id. This rewrites the duplicates to the class's canonical sprite.

    Returns [(obj_index, row_bump)] for objects that additionally need an
    A_IncPaletteRowBy queued into the room's sprite-loader stub. Pure duplicates
    share palette_offset and never need one, so this returns [] until offset-
    shifted merging lands.

    Must run before Step 3 of _recalculate_room_partition, which is where one
    buffer per unique sprite id is decided.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None

    for obj in room.objects:
        canonical = PURE.get(int(obj._npc.sprite_id))
        if canonical is not None:
            obj._npc = _canonical_record(obj._npc, canonical)

    return []
```

Then call it at the very top of `_recalculate_room_partition`, immediately after
the existing `assert room.partition is not None` and before the Step 1 banner:

```python
    # Collapse palette-swap-equivalent sprites before anything counts distinct
    # sprite ids. Step 3 assigns one buffer per unique sprite id, so merging
    # after that point buys nothing.
    _merge_palette_swaps(world, room_id)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_merge.py -q`
Expected: PASS, 5 passed

- [ ] **Step 5: Run the full VRAM suite**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_dedicated_vram_sizing.py .claude/tests/test_room315_dedicated_vram_cap.py .claude/tests/test_empty_placeholder_vram.py -q`
Expected: all PASS

- [ ] **Step 6: Headless smoke run**

Run:
```bash
patchvenv/bin/python -c "
from randomizer import main
from randomizer.types.gameworld import Settings
for seed in (1, 2, 3):
    main.create(seed, Settings())
    print('seed', seed, 'ok')
"
```
Expected: three `ok` lines, no traceback.

- [ ] **Step 7: Commit**

```bash
git add randomizer/logic/partition_calculator.py .claude/tests/test_palette_swap_merge.py
git commit -m "feat: merge pure palette-swap duplicate sprites before buffer assignment

32 sprite ids are byte-identical duplicates of another sprite at the same
palette_offset. Collapsing them to a canonical id lets them share one clone
buffer, which is the constraint that forces extra NPCs into dedicated VRAM.
No palette work needed for this tier."
```

---

### Task 5: VERIFICATION GATE — settle two runtime unknowns

**This task produces a written answer, not code. Tasks 6, 7 and 8 are blocked on it.**
Tasks 1-4 are already shipped and do not depend on it.

Two things must be observed rather than inferred. Both need the user at a
bsnes-plus v05 session or an in-game check; an agentic worker cannot complete this
task alone and must hand it back.

**Question 1 — does a merged offset-shifted sprite need an extra CGRAM row?**

`npc_palette_rows` keys rows on `palette_id` alone. Every member of a palette-swap
class shares its `palette_id` by construction, so the helper says they already
share one row. But before merging, sprite 267 and sprite 331 visibly render in
different colours, which a single shared row cannot explain unless
`sprite.palette_offset` re-aims the upload per sprite.

Determine: with two objects in one room on sprites 267 and 331, how many CGRAM
rows are occupied, and does each sprite's `palette_offset` select its source row
within the palette pack?

Method: build a seed, load a room containing both, and inspect CGRAM rows 8-15 in
bsnes-plus. **Breakpoints and memory watches on the S-CPU bus** (not the SA-1
bus).

Impact: if merging costs an extra row, Task 7's budget check is load-bearing and
`rows_remaining` gates most merges. If it does not, merging is row-neutral and the
check is a cheap guard.

**Question 2 — does `A_IncPaletteRowBy` count against the 10-object sprite-state limit?**

Per `project_room422_ten_object_sprite_state_limit`, only 10 objects in a room can
take a mold or sequence override. It is not known whether a palette row bump is
subject to the same cap.

Method: in room 422 (Belome's treasury, 15 objects), queue `A_IncPaletteRowBy` at
objects beyond the tenth and observe whether the bump applies.

Impact: if capped, Task 7 needs a per-room bump budget alongside the row budget,
and rooms with many merged objects must skip the excess.

- [ ] **Step 1: Answer question 1 and record the result**

Append the finding to
`docs/superpowers/specs/2026-07-30-npc-palette-swap-unification-design.md` under
the "Verification gate" section, replacing the open question with the observed
behaviour.

- [ ] **Step 2: Answer question 2 and record the result**

Same file, same section.

- [ ] **Step 3: Commit the findings**

```bash
git add docs/superpowers/specs/2026-07-30-npc-palette-swap-unification-design.md
git commit -m "docs: record palette row and IncPaletteRowBy verification results"
```

- [ ] **Step 4: Adjust Tasks 6-8 if either answer differs from the assumption**

The plan below assumes: merging an offset-shifted sprite costs **one extra CGRAM
row** per class per room, and `A_IncPaletteRowBy` is **not** subject to the
10-object cap. If either is wrong, update Task 7's budget logic and tests before
implementing it.

---

### Task 6: Generate the room-to-stub map

**Blocked by Task 5.**

96 event scripts named `*_SHUFFLED_NPC_ANIMATION_LOADER` exist. All 96 are empty
(`Return()` only) and all 96 are already invoked from their room's loader chain,
so they are ready-made injection points that avoid the
`reference_room_loader_e0015_ordering` landmine.

**Files:**
- Create: `randomizer/management/commands/sprite_loader_events.py`
- Create (generated): `randomizer/data/rooms/sprite_loader_events.py`
- Test: `.claude/tests/test_sprite_loader_events.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces:
  - `randomizer.data.rooms.sprite_loader_events.ROOM_SPRITE_LOADER: dict[int, int]` — room id to stub event script id.
  - `randomizer.management.commands.sprite_loader_events.build_map() -> dict[int, int]` — importable by the drift test. Raises `ValueError` on any stub resolving to zero or more than one room.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_sprite_loader_events.py`:

```python
"""Each room's reserved sprite-loader stub is the injection point for palette
row bumps.

All 96 *_SHUFFLED_NPC_ANIMATION_LOADER scripts are empty and already invoked
from their room's loader -- room 315's is RunEventAsSubroutine(E0802_...) at
script_1146.py:67, inside the boss-available branch. Because they are subroutine
calls rather than tail jumps, they sidestep the E0015 fade-ordering landmine.

Naive reachability is ambiguous: traversing shared hub events returns five
candidate stubs for room 315. The generator resolves by nearest caller and raises
at build time on anything still ambiguous, so ambiguity is settled by hand once,
never at seed time.
"""
from randomizer.data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER
from randomizer.management.commands.sprite_loader_events import build_map


def test_map_matches_regeneration():
    assert build_map() == ROOM_SPRITE_LOADER


def test_room_315_maps_to_its_own_stub():
    """E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER."""
    assert ROOM_SPRITE_LOADER[315] == 802


def test_no_stub_serves_two_rooms():
    stubs = list(ROOM_SPRITE_LOADER.values())
    assert len(stubs) == len(set(stubs))


def test_every_mapped_stub_is_empty():
    """A stub with content is not a free injection point -- appending to it
    would run alongside whatever else is there."""
    import re
    import pathlib

    for room_id, event_id in ROOM_SPRITE_LOADER.items():
        path = pathlib.Path(
            f"randomizer/data/overworld_scripts/event/scripts/script_{event_id}.py"
        )
        body = path.read_text().split("script = EventScript(", 1)[-1]
        commands = re.findall(r"\b([A-Z]\w+)\(", body)
        assert commands == ["Return"], (
            f"room {room_id} stub E{event_id:04d} is not empty: {commands}"
        )
```

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_sprite_loader_events.py -q`
Expected: FAIL with `ModuleNotFoundError` for both new modules.

- [ ] **Step 3: Write the generator**

Create `randomizer/management/commands/sprite_loader_events.py`:

```python
"""Generate randomizer/data/rooms/sprite_loader_events.py.

Maps each room to its reserved *_SHUFFLED_NPC_ANIMATION_LOADER stub -- an empty
event script already invoked from that room's loader chain, reserved for
per-object sprite setup.

Resolution is by nearest caller: find each stub's call site, then walk outward
from each room's entrance_event and take the stub reachable in the fewest hops.
Anything still ambiguous raises, so it is settled by hand at generation time
rather than silently at seed time.

Run: patchvenv/bin/python manage.py sprite_loader_events
"""
import collections
import pathlib
import re

from django.core.management.base import BaseCommand

SCRIPT_DIR = pathlib.Path("randomizer/data/overworld_scripts/event/scripts")
NAMES = pathlib.Path("randomizer/data/variables/event_script_names.py")
ROOM_DIR = pathlib.Path("randomizer/data/rooms")
OUTPUT = pathlib.Path("randomizer/data/rooms/sprite_loader_events.py")

_CALL = re.compile(r"(?:RunEventAsSubroutine|JmpToEvent|RunEventAtReturn)\((E\d+_\w+)")
_LABEL = re.compile(r'"EVENT_(\d+)_')


def _load():
    names = NAMES.read_text()
    name_to_id = {
        m.group(1): int(m.group(2))
        for m in re.finditer(r"^(E(\d+)_\w+)\s*=\s*\d+", names, re.M)
    }
    stub_ids = {
        int(m.group(1))
        for m in re.finditer(
            r"^E(\d+)_\w*SHUFFLED_NPC_ANIMATION_LOADER\s*=", names, re.M
        )
    }
    scripts = {}
    for path in SCRIPT_DIR.glob("script_*.py"):
        match = re.search(r"script_(\d+)", path.name)
        if match is not None:
            scripts[int(match.group(1))] = path.read_text()
    return name_to_id, stub_ids, scripts


def _edges(script_id: int, name_to_id, scripts) -> set[int]:
    text = scripts.get(script_id, "")
    out = set()
    for m in _CALL.finditer(text):
        target = name_to_id.get(m.group(1))
        if target is not None:
            out.add(target)
    for m in _LABEL.finditer(text):
        out.add(int(m.group(1)))
    return out


def build_map() -> dict[int, int]:
    """room_id -> stub event id, resolved by nearest caller."""
    name_to_id, stub_ids, scripts = _load()

    result: dict[int, int] = {}
    for path in sorted(ROOM_DIR.glob("room_*.py")):
        match = re.search(r"room_(\d+)", path.name)
        if match is None:
            continue
        room_id = int(match.group(1))
        entry = re.search(r"entrance_event=(E\d+_\w+)", path.read_text())
        if entry is None or entry.group(1) not in name_to_id:
            continue

        # Breadth-first so the first stub found is the nearest one.
        start = name_to_id[entry.group(1)]
        seen = {start}
        frontier = collections.deque([start])
        nearest: list[int] = []
        depth_of_hit = None
        depth = {start: 0}
        while frontier:
            node = frontier.popleft()
            if depth_of_hit is not None and depth[node] > depth_of_hit:
                break
            if node in stub_ids:
                depth_of_hit = depth[node]
                nearest.append(node)
            for nxt in _edges(node, name_to_id, scripts):
                if nxt not in seen:
                    seen.add(nxt)
                    depth[nxt] = depth[node] + 1
                    frontier.append(nxt)
        if len(nearest) > 1:
            raise ValueError(
                f"room {room_id}: {len(nearest)} stubs tied at the same distance "
                f"({sorted(nearest)}). Resolve by hand before regenerating."
            )
        if nearest:
            result[room_id] = nearest[0]

    owners = collections.Counter(result.values())
    shared = {stub: n for stub, n in owners.items() if n > 1}
    if shared:
        raise ValueError(f"stubs claimed by more than one room: {shared}")
    return dict(sorted(result.items()))


HEADER = '''"""Room to reserved sprite-loader stub. GENERATED -- do not edit by hand.

Regenerate with: patchvenv/bin/python manage.py sprite_loader_events
Drift is caught by .claude/tests/test_sprite_loader_events.py

Each value is an empty *_SHUFFLED_NPC_ANIMATION_LOADER event already invoked from
that room's loader chain, reserved for per-object sprite setup.
"""
'''


class Command(BaseCommand):
    help = "Generate the room-to-sprite-loader-stub map."

    def handle(self, *args, **options):
        mapping = build_map()
        lines = [HEADER, "", "ROOM_SPRITE_LOADER: dict[int, int] = {"]
        for room_id, event_id in mapping.items():
            lines.append(f"    {room_id}: {event_id},")
        lines.append("}")
        lines.append("")
        OUTPUT.write_text("\n".join(lines))
        self.stdout.write(f"wrote {OUTPUT}: {len(mapping)} rooms mapped")
```

- [ ] **Step 4: Generate the map**

Run: `patchvenv/bin/python manage.py sprite_loader_events`

If it raises `ValueError` about tied stubs, the nearest-caller heuristic did not
separate them. Resolve by inspecting the named stub against the room name — for
example `E0802_SEASIDE_OCCUPIED_BEACH_...` belongs to room 315
`R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH` — and add an explicit override dict
at the top of the generator for those rooms, consulted before the BFS. Do not
loosen the raise.

Expected once clean: `wrote randomizer/data/rooms/sprite_loader_events.py: N rooms mapped`
where N is at most 96.

- [ ] **Step 5: Run tests to verify they pass**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_sprite_loader_events.py -q`
Expected: PASS, 4 passed

- [ ] **Step 6: Commit**

```bash
git add randomizer/management/commands/sprite_loader_events.py \
        randomizer/data/rooms/sprite_loader_events.py \
        .claude/tests/test_sprite_loader_events.py
git commit -m "feat: map rooms to their reserved sprite-loader stubs

All 96 *_SHUFFLED_NPC_ANIMATION_LOADER scripts are empty and already invoked
from their room's loader, so they are ready-made injection points that avoid
the E0015 fade-ordering landmine. Resolution is by nearest caller and raises on
ambiguity, settling it at generation time rather than at seed time."
```

---

### Task 7: Tier 2 merge — offset-shifted sprites

**Blocked by Task 5.**

> **Amended 2026-07-30.** The code below still uses `obj.set_sprite_id(...)` and
> reads `obj.sprite_id`. Neither works: room objects expose no `sprite_id`
> attribute, `BaseRoomObject._sprite_id` is written by `set_sprite_id` and read by
> nothing, and both `_get_npc_signature` and `_render_npc` key on the NPC record.
> Rewrite every such call to the record-swap form Task 4 established —
> `obj._npc = _canonical_record(obj._npc, canonical)` for writes and
> `int(obj._npc.sprite_id)` for reads — and reuse Task 4's `_canonical_record`
> helper rather than defining a second one. The residency setters
> (`set_extra_palette_source_offset`, `set_extra_palette_row_count`) are genuine
> per-object overrides and are unaffected.

**Files:**
- Modify: `randomizer/logic/partition_calculator.py` (extend `_merge_palette_swaps`, add `_emit_palette_bumps`)
- Test: `.claude/tests/test_palette_swap_merge_shifted.py`

**Interfaces:**
- Consumes: `SHIFTED` (Task 2), `rows_remaining` (Task 3), `_merge_palette_swaps` (Task 4), `ROOM_SPRITE_LOADER` (Task 6)
- Produces: `randomizer.logic.partition_calculator._emit_palette_bumps(world, room_id, bumps: list[tuple[int, int]]) -> int` — appends one `ActionQueueSync` per bump to the room's stub before its trailing `Return()`, returns the number emitted.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_palette_swap_merge_shifted.py`:

```python
"""Offset-shifted merges need residency AND application.

extra_palette_source_offset / extra_palette_row_count make the palette rows
available in the level; A_IncPaletteRowBy moves the object onto one and requires
residency to already be set. Same pairing as room 422, where SHARED_ITEM_BASE
loads the rows and A_IncPaletteRowBy(2) recolours the frog coins.

Residency goes on the FIRST object in room order carrying that palette_id --
npc_palette_rows skips later objects with `if palette in rows: continue`, so
residency declared on a later merged object is silently ignored.
"""
import pytest

from randomizer import main
from randomizer.data.sprites.palette_swap_classes import SHIFTED
from randomizer.logic.partition_calculator import _merge_palette_swaps
from randomizer.types.gameworld import Settings

ROOM_ID = 315
BANDANA_BLUE = 331
BANDANA_RED = 267


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _effective_sprite(obj):
    sprite_id = obj.sprite_id
    return obj._npc.sprite_id if sprite_id is None else sprite_id


@pytest.fixture
def room(world):
    """Restore every object override this module touches."""
    r = world.rooms._rooms[ROOM_ID]
    saved = [
        (o.sprite_id, o.extra_palette_source_offset, o.extra_palette_row_count)
        for o in r.objects
    ]
    yield r
    for obj, (sprite, source, count) in zip(r.objects, saved):
        obj.set_sprite_id(sprite)
        obj.set_extra_palette_source_offset(source)
        obj.set_extra_palette_row_count(count)


def test_shifted_source_is_rewritten_to_canonical(world, room):
    room.objects[0].set_sprite_id(BANDANA_RED)
    room.objects[1].set_sprite_id(BANDANA_BLUE)

    _merge_palette_swaps(world, ROOM_ID)

    assert _effective_sprite(room.objects[1]) == BANDANA_RED


def test_shifted_merge_returns_a_bump_for_the_shifted_object(world, room):
    room.objects[0].set_sprite_id(BANDANA_RED)
    room.objects[1].set_sprite_id(BANDANA_BLUE)

    bumps = _merge_palette_swaps(world, ROOM_ID)

    assert (1, 1) in bumps, f"expected object 1 to need a +1 row bump, got {bumps}"
    assert not any(index == 0 for index, _ in bumps), "object 0 is already canonical"


def test_residency_lands_on_the_first_object_with_that_palette(world, room):
    """Object 0 carries the palette first, so the row count belongs to it --
    declaring it on object 1 would be silently ignored by npc_palette_rows."""
    room.objects[0].set_sprite_id(BANDANA_RED)
    room.objects[1].set_sprite_id(BANDANA_BLUE)

    _merge_palette_swaps(world, ROOM_ID)

    assert room.objects[0].extra_palette_row_count == 1
    assert room.objects[0].extra_palette_source_offset == 0


def test_merge_skipped_when_span_exceeds_residency_field(world, room):
    """extra_palette_row_count is 2 bits, so a class may only merge members
    spanning at most 3 pack rows."""
    wide = [s for s, (_, off) in SHIFTED.items() if off > 3]
    if not wide:
        pytest.skip("no class in the table spans more than 3 pack rows")
    source = wide[0]
    canonical, _ = SHIFTED[source]

    room.objects[0].set_sprite_id(canonical)
    room.objects[1].set_sprite_id(source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _effective_sprite(room.objects[1]) == source, "should have been skipped"


def test_no_bump_when_room_has_no_stub(world, room):
    """Tier 2 needs an injection point. Without one the merge is skipped, but
    tier 1 still applies."""
    from randomizer.data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER

    unstubbed = [
        rid
        for rid, r in enumerate(world.rooms._rooms)
        if r is not None and rid not in ROOM_SPRITE_LOADER and len(r.objects) >= 2
    ]
    if not unstubbed:
        pytest.skip("every room with objects has a stub")
    target = unstubbed[0]
    other = world.rooms._rooms[target]
    saved = [o.sprite_id for o in other.objects]
    try:
        other.objects[0].set_sprite_id(BANDANA_RED)
        other.objects[1].set_sprite_id(BANDANA_BLUE)
        bumps = _merge_palette_swaps(world, target)
        assert bumps == []
    finally:
        for obj, sprite in zip(other.objects, saved):
            obj.set_sprite_id(sprite)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_merge_shifted.py -q`
Expected: FAIL — `_merge_palette_swaps` returns `[]` and does not rewrite `SHIFTED` sources.

- [ ] **Step 3: Extend the merge pass**

In `randomizer/logic/partition_calculator.py`, replace the tier 1 body of
`_merge_palette_swaps` with the full version:

```python
from ..data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER
from ..data.sprites.palette_swap_classes import PURE, SHIFTED
from .palette_rows import rows_remaining

# extra_palette_row_count is 2 bits, so a merged class may span at most 3 extra
# CGRAM rows beyond its lowest pack offset.
_MAX_PACK_SPAN = 3


def _merge_palette_swaps(world: GameWorld, room_id: int) -> list[tuple[int, int]]:
    """Collapse palette-swap-equivalent sprites in `room_id` onto one sprite_id.

    A VRAM clone buffer holds exactly one sprite_id and a room has three, so two
    sprites with byte-identical tile data still cost two buffers until they share
    an id.

    Returns [(obj_index, row_bump)] for objects needing A_IncPaletteRowBy queued
    into the room's sprite-loader stub.

    Must run before Step 3 of _recalculate_room_partition, which is where one
    buffer per unique sprite id is decided.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None

    def effective(obj) -> int:
        override = obj.sprite_id
        return int(obj._npc.sprite_id if override is None else override)

    # Tier 1: pure duplicates. No palette work, no stub needed.
    for obj in room.objects:
        canonical = PURE.get(effective(obj))
        if canonical is not None:
            obj.set_sprite_id(canonical)

    # Tier 2 needs somewhere to put the row bumps.
    if room_id not in ROOM_SPRITE_LOADER:
        return []

    # Group the offset-shifted candidates by canonical sprite.
    by_canonical: dict[int, list[tuple[int, int]]] = {}
    for index, obj in enumerate(room.objects):
        sprite = effective(obj)
        entry = SHIFTED.get(sprite)
        if entry is None:
            continue
        canonical, offset = entry
        by_canonical.setdefault(canonical, []).append((index, offset))

    bumps: list[tuple[int, int]] = []
    for canonical, members in by_canonical.items():
        offsets = [offset for _, offset in members]
        # The canonical sprite itself sits at its own pack offset; include it so
        # residency covers every row the merged group renders from.
        canonical_offset = world.get_sprite(canonical).palette_offset
        present = any(effective(o) == canonical for o in room.objects)
        if present:
            offsets.append(canonical_offset)
        low, high = min(offsets), max(offsets)
        span = high - low
        if span > _MAX_PACK_SPAN:
            logging.info(
                "room %d: skipping palette merge onto sprite %d, pack span %d "
                "exceeds the %d-row residency field",
                room_id, canonical, span, _MAX_PACK_SPAN,
            )
            continue
        if span > rows_remaining(world, room):
            logging.info(
                "room %d: skipping palette merge onto sprite %d, needs %d extra "
                "CGRAM rows but only %d remain",
                room_id, canonical, span, rows_remaining(world, room),
            )
            continue

        palette = world.get_sprite(canonical).palette_id
        for index, offset in members:
            room.objects[index].set_sprite_id(canonical)
            if offset > low:
                bumps.append((index, offset - low))

        # Residency belongs to the FIRST object carrying this palette, because
        # npc_palette_rows skips later objects with `if palette in rows: continue`.
        for obj in room.objects:
            if world.get_sprite(effective(obj)).palette_id != palette:
                continue
            obj.set_extra_palette_source_offset(low)
            obj.set_extra_palette_row_count(span)
            break

    return bumps
```

Add `import logging` at the top of the module if it is not already imported.

- [ ] **Step 4: Emit the bumps into the stub**

Add to the same module:

```python
def _emit_palette_bumps(
    world: GameWorld, room_id: int, bumps: list[tuple[int, int]]
) -> int:
    """Queue A_IncPaletteRowBy for each merged object in the room's stub.

    The stub is an empty *_SHUFFLED_NPC_ANIMATION_LOADER already invoked from the
    room's loader as a subroutine, so the queue runs before the fade without any
    of the E0015 tail-jump ordering hazards. Queues are Sync, matching the room
    422 precedent -- Async loses the race against FadeInFromBlack.
    """
    if not bumps:
        return 0
    event_id = ROOM_SPRITE_LOADER[room_id]
    script = world.get_event_script(event_id)
    for index, delta in bumps:
        script.insert_before_nth_command(
            0,
            ActionQueueSync(
                target=AREA_OBJECTS[index],
                subscript=[A_IncPaletteRowBy(delta)],
            ),
        )
    return len(bumps)
```

Resolve the object-constant list and the import paths before writing this:

```bash
grep -n "NPC_0\|NPC_1" patchvenv/lib/python3.12/site-packages/smrpgpatchbuilder/datatypes/overworld_scripts/arguments/area_objects.py | head -12
grep -n "A_IncPaletteRowBy\|ActionQueueSync" randomizer/logic/apply.py | head -4
```

Define `AREA_OBJECTS` as an index-ordered tuple of the `NPC_0`..`NPC_N` constants
in this module, matching how `apply.py` targets objects for the room 422 queues.

Then call it from `_recalculate_room_partition`, replacing the Task 4 call site:

```python
    _emit_palette_bumps(world, room_id, _merge_palette_swaps(world, room_id))
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_palette_swap_merge_shifted.py .claude/tests/test_palette_swap_merge.py -q`
Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add randomizer/logic/partition_calculator.py \
        .claude/tests/test_palette_swap_merge_shifted.py
git commit -m "feat: merge offset-shifted palette-swap sprites with row bumps

Residency (extra_palette_source_offset / extra_palette_row_count) goes on the
first object carrying the palette, since npc_palette_rows ignores it anywhere
else. Application (A_IncPaletteRowBy) goes into the room's reserved
sprite-loader stub. Skips with a log line when the class spans more pack rows
than the 2-bit residency field holds, when CGRAM rows would overflow, or when
the room has no stub."
```

---

### Task 8: Integration — room 315 Culex regression and full smoke

**Blocked by Task 5.**

**Files:**
- Test: `.claude/tests/test_room315_culex_merge.py`

**Interfaces:**
- Consumes: `dedicated_high_water` and `PACKED_BUFFER_A` from `.claude/tests/test_room315_dedicated_vram_cap.py` (Task 1); `_recalculate_room_partition` (existing)
- Produces: nothing.

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_room315_culex_merge.py`:

```python
"""Room 315 with Culex is the case that motivated palette-swap merging.

Boss shuffle gives six distinct sprite ids across nine objects: four crystals
(838/840/842/844), Culex small (633) twice, and Piranha Plant (263) three times.
Three clone buffers cannot hold six sprites, so five NPCs went dedicated and the
packed cursor walked to $40 -- clone buffer A's base, where object 0 lives.
"""
import pytest

from randomizer import main
from randomizer.data.rooms import npcs
from randomizer.logic.partition_calculator import _recalculate_room_partition
from randomizer.types.gameworld import Settings

from test_room315_dedicated_vram_cap import (
    PACKED_BUFFER_A,
    dedicated_high_water,
    linear,
)

ROOM_ID = 315

CULEX_LAYOUT = [
    (0, npcs.FIRE_CRYSTAL_GRIDPLANE_NPC),
    (1, npcs.WATER_CRYSTAL_GRIDPLANE_NPC),
    (2, npcs.EARTH_CRYSTAL_GRIDPLANE_NPC),
    (3, npcs.WIND_CRYSTAL_GRIDPLANE_NPC),
    (6, npcs.CULEX_SMALL_NPC),
    (7, npcs.CULEX_SMALL_NPC),
]


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def test_culex_layout_stays_below_buffer_a(world):
    """The reported bug: objects 6, 7 and 8 partially overwrote object 0."""
    room = world.rooms._rooms[ROOM_ID]
    saved = [(o._npc, o.cannot_clone, o.min_vram_size) for o in room.objects]
    try:
        for index, npc in CULEX_LAYOUT:
            room.objects[index]._npc = npc
            room.objects[index].set_cannot_clone(None)
            room.objects[index].set_min_vram_size(None)

        _recalculate_room_partition(world, ROOM_ID)

        high_water = dedicated_high_water(world, ROOM_ID)
        assert linear(high_water) <= linear(PACKED_BUFFER_A), (
            f"dedicated cursor reached packed ${high_water:02X}; buffer A is at "
            f"${PACKED_BUFFER_A:02X} and holds object 0"
        )
    finally:
        for obj, (npc, cc, mv) in zip(room.objects, saved):
            obj._npc = npc
            obj.set_cannot_clone(cc)
            obj.set_min_vram_size(mv)
```

Resolve the Culex-small NPC constant before running:

```bash
grep -n "SPR0633_CULEX_SMALL" randomizer/data/rooms/npcs.py | head -3
```

Substitute the real constant name for `npcs.CULEX_SMALL_NPC` if it differs.

`.claude/tests/` has no `conftest.py`, so the cross-module import works via
pytest's rootdir insertion. If the import fails, add
`sys.path.insert(0, str(pathlib.Path(__file__).parent))` above it rather than
duplicating the helper.

- [ ] **Step 2: Run test to verify it fails**

Run: `patchvenv/bin/python -m pytest .claude/tests/test_room315_culex_merge.py -q`
Expected: FAIL if the merge does not reduce the distinct sprite count enough. If
it already PASSES because Task 1 alone was sufficient for this layout, keep the
test — it is the regression guard — and note that in the commit message.

- [ ] **Step 3: Run the whole suite**

Run: `patchvenv/bin/python -m pytest .claude/tests/ -q`
Expected: all PASS. Investigate any failure rather than skipping it — per
`CLAUDE.md`, never resolve a failure with an exception skip.

- [ ] **Step 4: Multi-seed headless smoke**

Run:
```bash
patchvenv/bin/python -c "
from randomizer import main
from randomizer.types.gameworld import Settings
for seed in range(1, 11):
    main.create(seed, Settings())
    print('seed', seed, 'ok')
"
```
Expected: ten `ok` lines, no traceback.

- [ ] **Step 5: Confirm the NPC table has not overflowed**

Per-object `sprite_id` overrides produce distinct NPC-table signatures, so
merging can change how many 7-byte records are emitted. The table runs
`0x1DB800`-`0x1DE000`, about 1462 slots.

Run:
```bash
patchvenv/bin/python -c "
from randomizer import main
from randomizer.types.gameworld import Settings
w = main.create(1, Settings())
patches = w.rooms.render()
npc_slots = [a for a in patches if 0x1DB800 <= a < 0x1DE000]
print('npc records written:', len(npc_slots), 'of', (0x1DE000-0x1DB800)//7)
"
```
Expected: a count below the capacity, no `ValueError` from the renderer.

- [ ] **Step 6: Commit**

```bash
git add .claude/tests/test_room315_culex_merge.py
git commit -m "test: regression for room 315 Culex clone buffer A overrun

Six distinct sprite ids across nine objects forced five dedicated NPCs and
walked the packed cursor to \$40, clone buffer A's hardcoded base, where object
0 lives. Asserts the cursor now ends below it."
```

---

## Self-Review

**Spec coverage**

| Spec section | Task |
|---|---|
| Problem / room 315 overrun | 1, 8 |
| Generated class table + drift test | 2 |
| Two-tier PURE / SHIFTED split | 2, 4, 7 |
| Row model extraction + budget | 3 |
| Merge pass before Step 3 | 4, 7 |
| Generated stub map + build-time ambiguity raise | 6 |
| Residency on first object with the palette | 7 |
| Bumps into the reserved stub | 7 |
| Bound: 2-bit residency field | 7 |
| Bound: CGRAM row budget | 7 |
| Bound: no reachable stub | 7 |
| Bound: table drift | 2, 6 |
| Verification gate | 5 |
| Immediate unblock | 1 |
| Testing section | every task |

The spec's ordering constraint — `sprite_palette_copies` rewriting `palette_id`
before the merge reads it — is **not** covered by a task above. It is asserted
implicitly by Task 8's multi-seed smoke only if a seed exercises
`DifferentiateRepeatedBosses`. Add this step to Task 7 before committing:

- [ ] **Task 7, Step 5b: Assert the palette-copy ordering**

Add to `.claude/tests/test_palette_swap_merge_shifted.py`:

```python
def test_merge_reads_post_copy_palette_ids(world):
    """apply.py's sprite_palette_copies rewrites palette_id when
    DifferentiateRepeatedBosses is off, which can change class membership. The
    merge must read the rewritten ids, not the static ones."""
    from randomizer.logic.apply import apply_shuffler_results_to_game_data
    import inspect

    source = inspect.getsource(apply_shuffler_results_to_game_data)
    copies_at = source.find("sprite_palette_copies")
    recalc_at = source.find("_recalculate_room_partition")
    if recalc_at == -1:
        pytest.skip("recalc is not called directly from apply")
    assert copies_at < recalc_at, (
        "sprite_palette_copies must run before partition recalculation"
    )
```

**Placeholder scan:** no TBD/TODO/"handle edge cases" steps. Every code step
carries real code. Three steps ask the implementer to resolve a constant name by
grep before use (Tasks 1, 7, 8) — these are lookups with an exact command and a
stated fallback, not deferred decisions.

**Type consistency:** `_merge_palette_swaps(world, room_id) -> list[tuple[int, int]]`
is introduced in Task 4 and extended in Task 7 with the same signature.
`_emit_palette_bumps(world, room_id, bumps) -> int` consumes exactly that return
type. `PURE: dict[int, int]` and `SHIFTED: dict[int, tuple[int, int]]` are used
consistently in Tasks 2, 4 and 7. `rows_remaining(world, room) -> int` is defined
in Task 3 and consumed in Task 7 with matching arguments.

**Known gap:** Task 7's budget logic assumes one extra CGRAM row per merged class
and no cap on `A_IncPaletteRowBy` count. Task 5 exists to confirm both, and its
Step 4 instructs revision if either is wrong.
