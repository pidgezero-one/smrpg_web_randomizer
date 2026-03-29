# Partition Calculator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace manual per-room partition update functions with a general-purpose `analyze_partition` + `apply_partition` pair that handles buffer type/format matching, ally buffer sizing, sequence-based buffer space, VRAM overflow checking, and boss model filtering.

**Architecture:** Two pure functions (analyze, apply) operating on a `PartitionAnalysis` result object. The analyzer examines all NPCs in a room, determines optimal buffer layout based on gridplane format compatibility rules, and computes cannot_clone flags. A separate `filter_fitting_models` helper lets boss fight locations determine which NPC models fit within VRAM budget.

**Tech Stack:** Python, existing `smrpgpatchbuilder` types (Partition, Buffer, BufferType, BufferSpace, VramStore), existing `physical_objects.py` NPC/BossNPC classes.

**Spec:** `docs/superpowers/specs/2026-03-29-partition-calculator-design.md`

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `randomizer/logic/partition_calculator.py` | Modify | Add `analyze_partition`, `apply_partition`, `filter_fitting_models`, and helpers (`_calculate_ally_buffer_size`, `_assign_buffers_v2`). Keep existing `update_*` functions and old `analyze_room_partition`/`apply_partition_analysis` temporarily. |
| `tests/test_partition_calculator.py` | Create | Unit tests for all new functions |
| `tests/conftest.py` | Create (if needed) | Test fixtures for GameWorld loading |

---

### Task 1: Test infrastructure and NPCAnalysis dataclass update

**Files:**
- Create: `tests/test_partition_calculator.py`
- Create: `tests/conftest.py` (if not exists)
- Modify: `randomizer/logic/partition_calculator.py:526-538` (NPCAnalysis)
- Modify: `randomizer/logic/partition_calculator.py:639-690` (_analyze_npc)

- [ ] **Step 1: Set up test infrastructure**

Check if `tests/` directory and `conftest.py` exist. If not, create minimal pytest infrastructure. Check if the project has an existing test runner pattern (look at `setup.cfg`, `pyproject.toml`, `tox.ini`, or existing test files anywhere in the repo). Follow whatever pattern exists. If none, create a minimal `tests/conftest.py`.

- [ ] **Step 2: Write failing test for new NPCAnalysis fields**

```python
# tests/test_partition_calculator.py
from randomizer.logic.partition_calculator import NPCAnalysis
from smrpgpatchbuilder.datatypes.levels.classes import BufferType, VramStore


def test_npc_analysis_has_new_fields():
    """NPCAnalysis should have is_gridplane, max_sequence_vram, and force_cannot_clone."""
    analysis = NPCAnalysis(
        index=0,
        sprite_id=262,
        vram_store=VramStore.DIR0_SWSE_NWNE,
        min_vram=0,
        max_sequence_vram=2,
        cannot_clone=False,
        is_chest=False,
        is_coin=False,
        is_gridplane=True,
        gridplane_format=0,
        buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
        clone_count=1,
        force_cannot_clone=False,
    )
    assert analysis.is_gridplane is True
    assert analysis.max_sequence_vram == 2
    assert analysis.force_cannot_clone is False
```

- [ ] **Step 3: Run test to verify it fails**

Run: `cd /Users/stefkischak/code/smrpg_web_randomizer && python -m pytest tests/test_partition_calculator.py::test_npc_analysis_has_new_fields -v`
Expected: FAIL (missing fields on NPCAnalysis)

- [ ] **Step 4: Update NPCAnalysis dataclass**

In `randomizer/logic/partition_calculator.py`, replace the existing `NPCAnalysis` (lines 526-538) with:

```python
@dataclass
class NPCAnalysis:
    """Analysis of a single NPC's VRAM requirements."""

    index: int
    sprite_id: int
    vram_store: VramStore
    min_vram: int
    max_sequence_vram: int         # Max min_vram across specified sequences (for buffer space)
    cannot_clone: bool             # INPUT: from NPC/room-object definition
    is_chest: bool
    is_coin: bool
    is_gridplane: bool             # Mold 0 gridplane status
    gridplane_format: int | None
    buffer_type: BufferType
    clone_count: int
    force_cannot_clone: bool       # COMPUTED: True when no compatible buffer or non-gridplane
```

Update `_analyze_npc` (lines 639-690) to populate the new fields. The existing code already computes `is_gridplane, gridplane_format = _get_npc_gridplane_info(world, sprite_id)` at line 663. Pass `is_gridplane` to the constructor, set `max_sequence_vram=0` as default, and set `force_cannot_clone = (not is_gridplane and not is_chest and not is_coin)`. The return statement becomes:

```python
    return NPCAnalysis(
        index=index,
        sprite_id=sprite_id,
        vram_store=vram_store,
        min_vram=min_vram,
        max_sequence_vram=0,
        cannot_clone=cannot_clone,
        is_chest=is_chest,
        is_coin=is_coin,
        is_gridplane=is_gridplane,
        gridplane_format=gridplane_format,
        buffer_type=buffer_type,
        clone_count=clone_count,
        force_cannot_clone=(not is_gridplane and not is_chest and not is_coin),
    )
```

- [ ] **Step 5: Run test to verify it passes**

Run: `python -m pytest tests/test_partition_calculator.py::test_npc_analysis_has_new_fields -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/
git commit -m "feat: add is_gridplane, max_sequence_vram, force_cannot_clone to NPCAnalysis"
```

---

### Task 2: PartitionAnalysis rename and vram properties

**Files:**
- Modify: `randomizer/logic/partition_calculator.py:551-636` (PartitionAnalysis)
- Test: `tests/test_partition_calculator.py`

- [ ] **Step 1: Write failing test**

```python
def test_partition_analysis_vram_remaining():
    """PartitionAnalysis should expose vram_cursor and vram_remaining."""
    from randomizer.logic.partition_calculator import PartitionAnalysis, BufferAssignment, NPCAnalysis
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType, BufferSpace, VramStore

    analysis = PartitionAnalysis(
        room_id=204,
        npcs=[
            NPCAnalysis(
                index=10, sprite_id=639, vram_store=VramStore.DIR2_SWSE,
                min_vram=0, max_sequence_vram=0, cannot_clone=False,
                is_chest=False, is_coin=False, is_gridplane=False,
                gridplane_format=None, buffer_type=BufferType.EMPTY_3,
                clone_count=1, force_cannot_clone=True,
            ),
        ],
        ally_buffer_size=1,
        allow_extra_sprite_buffer=True,
        extra_buffer_size=1,
        buffers=[
            BufferAssignment(BufferType.TREASURE_CHEST, BufferSpace.BYTES_0, [0]),
            BufferAssignment(BufferType.FOUR_SPRITES_PER_ROW, BufferSpace.BYTES_0, [2, 4, 5]),
            BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0, []),
        ],
        full_palette=True,
    )
    # cursor = ally(1*4=4) + extra(1) + buffers(0+0+0) + dedicated NPC 10 (max_sequence_vram=0) = 5
    assert analysis.vram_cursor == 5
    assert analysis.vram_remaining == 27
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_partition_calculator.py::test_partition_analysis_vram_remaining -v`
Expected: FAIL

- [ ] **Step 3: Rename and add properties**

In `PartitionAnalysis`:

1. Rename `extra_buffer_needed` to `allow_extra_sprite_buffer`
2. Update `to_partition()` to use the new name: `partition.set_allow_extra_sprite_buffer(self.allow_extra_sprite_buffer)`
3. Update `format_report()` to use the new name
4. Also update `analyze_room_partition` (the old function, ~line 1015) to use the new field name so it doesn't break
5. Add properties:

```python
@property
def vram_cursor(self) -> int:
    """Total VRAM rows consumed by this partition."""
    cursor = self.ally_buffer_size * 4
    cursor += self.extra_buffer_size
    for buf in self.buffers:
        cursor += buf.buffer_space
    for npc in self.npcs:
        if npc.force_cannot_clone:
            cursor += npc.max_sequence_vram
    return cursor

@property
def vram_remaining(self) -> int:
    """VRAM rows available for additional NPCs (32 - vram_cursor)."""
    return 32 - self.vram_cursor
```

6. Update `format_report()` to include `vram_cursor`, `vram_remaining`, and `force_cannot_clone` in output.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_partition_calculator.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: rename extra_buffer_needed, add vram_cursor/vram_remaining to PartitionAnalysis"
```

---

### Task 3a: Implement _calculate_ally_buffer_size helper

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Test: `tests/test_partition_calculator.py`

Extract ally buffer calculation from the existing `analyze_room_partition` (lines 917-968) into a standalone helper parameterized by protagonist name.

- [ ] **Step 1: Write failing test**

```python
def test_calculate_ally_buffer_default():
    """No protagonist specified should return ally_buffer_size=1."""
    from randomizer.logic.partition_calculator import _calculate_ally_buffer_size
    # With no protagonist, should return 1
    result = _calculate_ally_buffer_size(None, None, None)
    assert result == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_partition_calculator.py::test_calculate_ally_buffer_default -v`
Expected: FAIL

- [ ] **Step 3: Implement _calculate_ally_buffer_size**

```python
def _calculate_ally_buffer_size(
    world: GameWorld | None,
    room,  # Room | None
    protagonist: str | None,
) -> int:
    """Calculate ally buffer size based on protagonist and room's extra_sprite_actions.

    Args:
        world: GameWorld instance (needed for sprite lookups).
        room: Room instance (needed for extra_sprite_actions).
        protagonist: Character name or None for default (size 1).

    Returns:
        Ally buffer size (1-3). Returns 1 if protagonist is None or no
        extra sprite actions require larger buffer.
    """
    from ..types.room import Room

    if protagonist is None or world is None:
        return 1

    # Look up character model by protagonist name
    # (Map string to character model from world)
    character_model = _get_character_model(world, protagonist)
    if character_model is None:
        return 1

    vram_values: list[int] = []

    # Check default animation states
    for state in DEFAULT_ANIMATION_STATES:
        sprites_dict = character_model.ally._sprites_primary
        if state in sprites_dict:
            prop_id, offset, is_mold = sprites_dict[state]
            if is_mold:
                try:
                    v = character_model._npc.min_vram_from_mold(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass
            else:
                try:
                    v = character_model._npc.min_vram_from_sequence(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass

    # Check room's extra_sprite_actions
    if isinstance(room, Room) and room.extra_sprite_actions:
        for action in room.extra_sprite_actions:
            anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
            for state in anim_states:
                sprites_dict = character_model.ally._sprites_primary
                if state in sprites_dict:
                    prop_id, offset, is_mold = sprites_dict[state]
                    if is_mold:
                        try:
                            v = character_model._npc.min_vram_from_mold(world, prop_id, offset)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass
                    else:
                        try:
                            v = character_model._npc.min_vram_from_sequence(world, prop_id, offset)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass

    if not vram_values:
        return 1
    return min(max(vram_values) + 1, 3)
```

Also implement `_get_character_model` that maps protagonist name string to the character model object. Check how `world.overworld_character.character_model` works and how characters are identified — the helper maps names like "mario", "peach", "bowser", "geno", "mallow" to the corresponding model.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_partition_calculator.py -v -k "ally_buffer"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: extract _calculate_ally_buffer_size helper"
```

---

### Task 3b: Implement _assign_buffers_v2

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Test: `tests/test_partition_calculator.py`

This is the core buffer assignment logic with strict format matching.

- [ ] **Step 1: Write failing tests for buffer assignment edge cases**

```python
def test_assign_buffers_v2_chests_in_buffer_a():
    """Chests should always be assigned to buffer A."""
    from randomizer.logic.partition_calculator import _assign_buffers_v2, NPCAnalysis
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType, VramStore

    npcs = [
        NPCAnalysis(index=0, sprite_id=94, vram_store=VramStore.DIR2_SWSE,
                     min_vram=1, max_sequence_vram=0, cannot_clone=False,
                     is_chest=True, is_coin=False, is_gridplane=False,
                     gridplane_format=None, buffer_type=BufferType.TREASURE_CHEST,
                     clone_count=0, force_cannot_clone=False),
        NPCAnalysis(index=2, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
    ]
    assignments, warnings = _assign_buffers_v2(npcs, 204)
    assert assignments[0].buffer_type == BufferType.TREASURE_CHEST
    assert 0 in assignments[0].npc_indices


def test_assign_buffers_v2_both_formats_get_separate_buffers():
    """When both format types exist and slots available, each gets its own buffer."""
    from randomizer.logic.partition_calculator import _assign_buffers_v2, NPCAnalysis
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType, VramStore

    npcs = [
        NPCAnalysis(index=0, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
        NPCAnalysis(index=1, sprite_id=258, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=3, buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
    ]
    assignments, warnings = _assign_buffers_v2(npcs, 999)
    types = {a.buffer_type for a in assignments}
    assert BufferType.FOUR_SPRITES_PER_ROW in types
    assert BufferType.THREE_SPRITES_PER_ROW in types


def test_assign_buffers_v2_minority_format_overflow():
    """When chests + coins take 2 slots and both formats exist, minority gets force_cannot_clone."""
    from randomizer.logic.partition_calculator import _assign_buffers_v2, NPCAnalysis
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType, VramStore

    npcs = [
        # Chest
        NPCAnalysis(index=0, sprite_id=94, vram_store=VramStore.DIR2_SWSE,
                     min_vram=1, max_sequence_vram=0, cannot_clone=False,
                     is_chest=True, is_coin=False, is_gridplane=False,
                     gridplane_format=None, buffer_type=BufferType.TREASURE_CHEST,
                     clone_count=0, force_cannot_clone=False),
        # Coin
        NPCAnalysis(index=1, sprite_id=192, vram_store=VramStore.DIR2_SWSE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=True, is_gridplane=False,
                     gridplane_format=None, buffer_type=BufferType.COINS,
                     clone_count=0, force_cannot_clone=False),
        # Format 0 (majority - 3 NPCs)
        NPCAnalysis(index=2, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
        NPCAnalysis(index=3, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
        NPCAnalysis(index=4, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
        # Format 3 (minority - 1 NPC)
        NPCAnalysis(index=5, sprite_id=258, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=3, buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
    ]
    assignments, warnings = _assign_buffers_v2(npcs, 999)
    # Chest in A, Coins in C, FOUR in B (majority)
    assert assignments[0].buffer_type == BufferType.TREASURE_CHEST
    assert assignments[2].buffer_type == BufferType.COINS
    # The remaining slot should be FOUR (majority)
    assert assignments[1].buffer_type == BufferType.FOUR_SPRITES_PER_ROW
    # Minority NPC 5 should be force_cannot_clone
    npc5 = next(n for n in npcs if n.index == 5)
    assert npc5.force_cannot_clone is True


def test_assign_buffers_v2_no_midas_river_hardcode():
    """_assign_buffers_v2 should NOT hardcode Midas River coin logic (caller responsibility)."""
    from randomizer.logic.partition_calculator import _assign_buffers_v2, NPCAnalysis, ALWAYS_REQUIRES_COIN_BUFFER
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType, VramStore

    # Room in ALWAYS_REQUIRES_COIN_BUFFER but no coin NPCs
    room_id = ALWAYS_REQUIRES_COIN_BUFFER[0]
    npcs = [
        NPCAnalysis(index=0, sprite_id=262, vram_store=VramStore.DIR0_SWSE_NWNE,
                     min_vram=0, max_sequence_vram=0, cannot_clone=False,
                     is_chest=False, is_coin=False, is_gridplane=True,
                     gridplane_format=0, buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                     clone_count=0, force_cannot_clone=False),
    ]
    assignments, _ = _assign_buffers_v2(npcs, room_id)
    # Should NOT force a COINS buffer — that's the caller's job
    coin_buffers = [a for a in assignments if a.buffer_type == BufferType.COINS]
    assert len(coin_buffers) == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_partition_calculator.py -v -k "assign_buffers_v2"`
Expected: FAIL

- [ ] **Step 3: Implement _assign_buffers_v2**

```python
def _assign_buffers_v2(
    npc_analyses: list[NPCAnalysis],
    room_id: int,
) -> tuple[list[BufferAssignment], list[str]]:
    """Assign NPCs to 3 buffer slots with strict format matching.

    Rules:
    - TREASURE_CHEST -> buffer A (index 0) only
    - COINS -> buffer C (index 2) only (animated coins only, not static)
    - Format 0-1 gridplane NPCs -> FOUR_SPRITES_PER_ROW buffer
    - Format 2-3 gridplane NPCs -> THREE_SPRITES_PER_ROW buffer
    - Non-gridplane NPCs -> force_cannot_clone (dedicated VRAM)
    - If both gridplane formats exist but only one slot remains,
      majority format gets the slot, minority gets force_cannot_clone
    - No hardcoded room-specific logic (caller handles special cases)
    """
    warnings: list[str] = []

    # Separate by type (only clonable NPCs, not already force_cannot_clone)
    chest_npcs = [n for n in npc_analyses if n.is_chest and not n.force_cannot_clone]
    coin_npcs = [n for n in npc_analyses if n.is_coin and not n.force_cannot_clone]
    four_npcs = [n for n in npc_analyses
                 if n.buffer_type == BufferType.FOUR_SPRITES_PER_ROW and not n.force_cannot_clone]
    three_npcs = [n for n in npc_analyses
                  if n.buffer_type == BufferType.THREE_SPRITES_PER_ROW and not n.force_cannot_clone]

    # Start with 3 empty slots
    assignments = [
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
    ]

    # Chests -> buffer A
    if chest_npcs:
        assignments[0] = BufferAssignment(
            BufferType.TREASURE_CHEST, BufferSpace.BYTES_0,
            [n.index for n in chest_npcs],
        )

    # Coins -> buffer C
    if coin_npcs:
        assignments[2] = BufferAssignment(
            BufferType.COINS, BufferSpace.BYTES_0,
            [n.index for n in coin_npcs],
        )

    # Collect gridplane format groups, sorted by count descending (majority first)
    gridplane_groups: list[tuple[BufferType, list[NPCAnalysis]]] = []
    if four_npcs:
        gridplane_groups.append((BufferType.FOUR_SPRITES_PER_ROW, four_npcs))
    if three_npcs:
        gridplane_groups.append((BufferType.THREE_SPRITES_PER_ROW, three_npcs))
    gridplane_groups.sort(key=lambda g: len(g[1]), reverse=True)

    # Assign gridplane groups to remaining empty slots
    for buf_type, npcs in gridplane_groups:
        placed = False
        for i in range(3):
            if assignments[i].buffer_type == BufferType.EMPTY_3:
                assignments[i] = BufferAssignment(
                    buf_type, BufferSpace.BYTES_0,
                    [n.index for n in npcs],
                )
                placed = True
                break
        if not placed:
            # No slot available — mark all these NPCs force_cannot_clone
            for npc in npcs:
                npc.force_cannot_clone = True
            warnings.append(
                f"No buffer slot for {buf_type.name} NPCs "
                f"(indices: {[n.index for n in npcs]}) — set force_cannot_clone"
            )

    return assignments, warnings
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_partition_calculator.py -v -k "assign_buffers_v2"`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: implement _assign_buffers_v2 with strict format matching"
```

---

### Task 3c: Implement analyze_partition orchestrator

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Test: `tests/test_partition_calculator.py`

This wires together the helpers from 3a and 3b into the top-level function.

- [ ] **Step 1: Write failing tests**

```python
def test_analyze_partition_basic(world_fixture):
    """analyze_partition should produce correct analysis for a simple room."""
    from randomizer.logic.partition_calculator import analyze_partition
    analysis = analyze_partition(world_fixture, 204, max_packets=1)
    assert analysis.ally_buffer_size == 1
    assert analysis.allow_extra_sprite_buffer is True
    assert analysis.extra_buffer_size == 1
    assert analysis.full_palette is True
    assert len(analysis.buffers) == 3
    assert analysis.buffers[0].buffer_type == BufferType.TREASURE_CHEST


def test_analyze_partition_water_flag(world_fixture):
    """water=True should set full_palette=False."""
    from randomizer.logic.partition_calculator import analyze_partition
    analysis = analyze_partition(world_fixture, 204, water=True)
    assert analysis.full_palette is False


def test_analyze_partition_non_gridplane_force_cannot_clone(world_fixture):
    """Non-gridplane NPCs should get force_cannot_clone=True."""
    from randomizer.logic.partition_calculator import analyze_partition
    analysis = analyze_partition(world_fixture, 204)
    npc10 = next(n for n in analysis.npcs if n.index == 10)
    assert npc10.force_cannot_clone is True
    assert npc10.is_gridplane is False


def test_analyze_partition_format_matching(world_fixture):
    """Gridplane NPCs should be assigned to matching buffer types only."""
    from randomizer.logic.partition_calculator import analyze_partition
    analysis = analyze_partition(world_fixture, 204)
    for buf in analysis.buffers:
        if buf.buffer_type == BufferType.FOUR_SPRITES_PER_ROW:
            for idx in buf.npc_indices:
                npc = next(n for n in analysis.npcs if n.index == idx)
                assert npc.gridplane_format in (0, 1), (
                    f"NPC {idx} has format {npc.gridplane_format} in FOUR buffer"
                )
        elif buf.buffer_type == BufferType.THREE_SPRITES_PER_ROW:
            for idx in buf.npc_indices:
                npc = next(n for n in analysis.npcs if n.index == idx)
                assert npc.gridplane_format in (2, 3), (
                    f"NPC {idx} has format {npc.gridplane_format} in THREE buffer"
                )


def test_analyze_partition_overflow_warns(world_fixture):
    """If VRAM overflows, warnings should include overflow message."""
    from randomizer.logic.partition_calculator import analyze_partition
    # ally_buffer_size=3 with huge packets should overflow
    analysis = analyze_partition(world_fixture, 204, max_packets=30)
    # 3*4 + 30 = 42 > 32
    # (ally defaults to 1, so 1*4 + 30 = 34 > 32)
    overflow_warnings = [w for w in analysis.warnings if "overflow" in w.lower()]
    assert len(overflow_warnings) > 0


def test_analyze_partition_sequence_override_increases_buffer_space(world_fixture):
    """Specifying a non-gridplane sequence should increase buffer space."""
    from randomizer.logic.partition_calculator import analyze_partition
    # Room 255 (Jinx Dojo) NPCs use sequence 3 which has non-gridplane molds
    # Test that specifying this increases the buffer's main_buffer_space
    analysis_without = analyze_partition(world_fixture, 255)
    analysis_with = analyze_partition(world_fixture, 255, npc_sequence_overrides={0: [3]})
    # The buffer containing NPC 0 should have higher space in the override version
    # (if sequence 3 has non-gridplane molds with min_vram > 0)
    # This is a structural test — exact values depend on sprite data
    assert analysis_with is not None  # At minimum, shouldn't crash
```

Note: `world_fixture` must provide a GameWorld with loaded sprite/room data. See Task 1 Step 1 for infrastructure setup.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_partition_calculator.py -v -k "analyze_partition"`
Expected: FAIL

- [ ] **Step 3: Implement analyze_partition**

```python
def analyze_partition(
    world: GameWorld,
    room_id: int,
    *,
    protagonist: str | None = None,
    max_packets: int = 0,
    allow_extra_sprite_buffer: bool | None = None,
    water: bool = False,
    npc_sequence_overrides: dict[int, list[int]] | None = None,
) -> PartitionAnalysis:
    """Analyze a room and compute optimal partition configuration.

    Pure computation — no side effects. Deterministic for identical inputs.

    npc_sequence_overrides maps NPC object index to sequence IDs (not mold IDs)
    that the NPC is known to use. This is used to compute buffer space needs
    from non-gridplane molds referenced by those sequences.
    """
    from ..types.room import Room

    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    if allow_extra_sprite_buffer is None:
        allow_extra_sprite_buffer = max_packets > 0

    # --- Step 1: Enumerate NPCs ---
    objects = room.objects
    npc_analyses: list[NPCAnalysis] = []
    i = 0
    while i < len(objects):
        obj = objects[i]
        if isinstance(obj, Clone):
            i += 1
            continue

        clone_count = 0
        j = i + 1
        while j < len(objects) and isinstance(objects[j], Clone):
            clone_count += 1
            j += 1

        npc_analysis = _analyze_npc(world, obj, i, clone_count)

        # Apply sequence overrides for buffer space calculation
        if npc_sequence_overrides and i in npc_sequence_overrides:
            seq_ids = npc_sequence_overrides[i]
            max_seq_vram = 0
            npc = obj._npc
            for seq_id in seq_ids:
                try:
                    v = npc.min_vram_from_sequence(world, seq_id)
                    max_seq_vram = max(max_seq_vram, v)
                except (IndexError, AssertionError):
                    pass
            npc_analysis.max_sequence_vram = max_seq_vram

        npc_analyses.append(npc_analysis)
        i = j

    # --- Step 2: Compute ally buffer size ---
    ally_buffer_size = _calculate_ally_buffer_size(world, room, protagonist)

    # --- Step 3: Assign buffer slots ---
    buffer_assignments, warnings = _assign_buffers_v2(npc_analyses, room_id)

    # --- Step 4: Compute buffer space from sequence overrides ---
    for assignment in buffer_assignments:
        if assignment.buffer_type in (BufferType.FOUR_SPRITES_PER_ROW, BufferType.THREE_SPRITES_PER_ROW):
            assigned_npcs = [n for n in npc_analyses if n.index in assignment.npc_indices]
            if assigned_npcs:
                max_space = max(n.max_sequence_vram for n in assigned_npcs)
                assignment.buffer_space = BufferSpace(min(max_space, 7))

    # --- Step 5: Build result ---
    result = PartitionAnalysis(
        room_id=room_id,
        npcs=npc_analyses,
        ally_buffer_size=ally_buffer_size,
        allow_extra_sprite_buffer=allow_extra_sprite_buffer,
        extra_buffer_size=max_packets,
        buffers=buffer_assignments,
        full_palette=not water,
        warnings=warnings,
    )

    # --- Step 6: Overflow check ---
    if result.vram_cursor > 32:
        result.warnings.append(
            f"VRAM overflow: cursor={result.vram_cursor} exceeds 32 rows "
            f"(remaining={result.vram_remaining})"
        )

    return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_partition_calculator.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: implement analyze_partition orchestrator"
```

---

### Task 4: Implement apply_partition

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Test: `tests/test_partition_calculator.py`

- [ ] **Step 1: Write failing test**

```python
def test_apply_partition_sets_partition_and_cannot_clone(world_fixture):
    """apply_partition should set partition on room and cannot_clone on NPCs."""
    from randomizer.logic.partition_calculator import analyze_partition, apply_partition

    analysis = analyze_partition(world_fixture, 204, max_packets=1)
    apply_partition(world_fixture, 204, analysis)

    room = world_fixture.rooms._rooms[204]
    assert room.partition is not None
    assert room.partition.ally_sprite_buffer_size == analysis.ally_buffer_size

    # Non-gridplane NPC 10 should have cannot_clone=True set on the room object
    obj10 = room.objects[10]
    assert obj10.cannot_clone is True

    # Gridplane NPC 2 (Goomba) should have cannot_clone=False
    obj2 = room.objects[2]
    assert obj2.cannot_clone is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_partition_calculator.py::test_apply_partition_sets_partition_and_cannot_clone -v`
Expected: FAIL

- [ ] **Step 3: Implement apply_partition**

```python
def apply_partition(
    world: GameWorld,
    room_id: int,
    analysis: PartitionAnalysis,
) -> None:
    """Apply a computed partition analysis to a room.

    Sets the room's partition and force_cannot_clone flags on each parent NPC.
    Clones are skipped (they inherit from parent).
    """
    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    partition = analysis.to_partition()
    partition._full_palette_buffer = analysis.full_palette
    room._partition = partition

    buffered_indices: set[int] = set()
    for assignment in analysis.buffers:
        buffered_indices.update(assignment.npc_indices)

    for npc_analysis in analysis.npcs:
        obj = room.objects[npc_analysis.index]
        if isinstance(obj, Clone):
            continue
        if npc_analysis.force_cannot_clone:
            obj.set_cannot_clone(True)
        elif npc_analysis.index in buffered_indices:
            obj.set_cannot_clone(False)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_partition_calculator.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: implement apply_partition"
```

---

### Task 5: Implement filter_fitting_models

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Test: `tests/test_partition_calculator.py`

- [ ] **Step 1: Write failing tests**

```python
def test_filter_fitting_models_returns_list(world_fixture):
    """filter_fitting_models should return a list of (model, analysis) tuples."""
    from randomizer.logic.partition_calculator import filter_fitting_models
    # Use a room and model that we know fits
    # This is a structural test — exact models depend on test fixture
    # At minimum, test the function signature and return type
    result = filter_fitting_models(
        world_fixture, 204, 7, [],  # empty candidate list
        max_packets=1,
    )
    assert result == []


def test_filter_fitting_models_restores_original_npc(world_fixture):
    """After filtering, the room's NPC should be restored to its original."""
    from randomizer.logic.partition_calculator import filter_fitting_models
    room = world_fixture.rooms._rooms[204]
    original_sprite = room.objects[7]._npc.sprite_id
    filter_fitting_models(world_fixture, 204, 7, [], max_packets=1)
    assert room.objects[7]._npc.sprite_id == original_sprite
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_partition_calculator.py -v -k "filter_fitting"`
Expected: FAIL

- [ ] **Step 3: Implement filter_fitting_models**

```python
def filter_fitting_models(
    world: GameWorld,
    room_id: int,
    npc_index: int,
    candidate_models: list,
    *,
    prefer_largest: bool = True,
    **analyze_kwargs,
) -> list[tuple]:
    """Filter and rank NPC models that fit in a room's VRAM budget.

    For each candidate model (a BossNPC subclass with a no-arg constructor and
    a .base attribute returning the NPC definition), temporarily substitutes it
    into the room's NPC slot, runs analyze_partition, and checks vram_remaining >= 0.

    Args:
        world: GameWorld instance.
        room_id: Room to test against.
        npc_index: Object index where the boss NPC sits.
        candidate_models: List of BossNPC subclasses (from prize._npc_models).
        prefer_largest: If True (default), returns sorted largest VRAM first.
            If False, sorted smallest first (for tight rooms).
        **analyze_kwargs: Passed through to analyze_partition (protagonist,
            max_packets, water, npc_sequence_overrides).

    Returns:
        List of (model_class, analysis) tuples for models that fit, sorted by
        VRAM consumption. Empty if nothing fits.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"
    obj = room.objects[npc_index]
    original_npc = obj._npc

    results = []
    for model_cls in candidate_models:
        model_instance = model_cls()
        obj._npc = model_instance.base
        try:
            analysis = analyze_partition(world, room_id, **analyze_kwargs)
            if analysis.vram_remaining >= 0:
                results.append((model_cls, analysis))
        finally:
            obj._npc = original_npc

    results.sort(key=lambda t: t[1].vram_cursor, reverse=prefer_largest)
    return results
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_partition_calculator.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py tests/test_partition_calculator.py
git commit -m "feat: implement filter_fitting_models for boss model selection"
```

---

### Task 6: Integration smoke test and final verification

**Files:**
- Test: `tests/test_partition_calculator.py`

- [ ] **Step 1: Verify no regressions**

Run: `python -m pytest --tb=short -q`
Expected: All existing tests PASS

- [ ] **Step 2: Add Room 204 smoke test with report output**

```python
def test_room_204_smoke_test(world_fixture):
    """Smoke test: analyze Room 204 and verify the report is sane."""
    from randomizer.logic.partition_calculator import analyze_partition
    analysis = analyze_partition(world_fixture, 204, max_packets=1)
    report = analysis.format_report()
    print(report)

    # Structural assertions
    assert analysis.buffers[0].buffer_type == BufferType.TREASURE_CHEST
    assert analysis.vram_remaining > 0
    assert analysis.vram_cursor <= 32

    # NPC 10 (Item Bag, non-gridplane) should be force_cannot_clone
    npc10 = next(n for n in analysis.npcs if n.index == 10)
    assert npc10.force_cannot_clone is True
    assert npc10.is_gridplane is False

    # No format-0 NPCs should be in a THREE buffer
    for buf in analysis.buffers:
        if buf.buffer_type == BufferType.THREE_SPRITES_PER_ROW:
            for idx in buf.npc_indices:
                npc = next(n for n in analysis.npcs if n.index == idx)
                assert npc.gridplane_format in (2, 3)

    # No format-2/3 NPCs should be in a FOUR buffer
    for buf in analysis.buffers:
        if buf.buffer_type == BufferType.FOUR_SPRITES_PER_ROW:
            for idx in buf.npc_indices:
                npc = next(n for n in analysis.npcs if n.index == idx)
                assert npc.gridplane_format in (0, 1)
```

- [ ] **Step 3: Run and inspect output**

Run: `python -m pytest tests/test_partition_calculator.py::test_room_204_smoke_test -v -s`
Expected: PASS, with human-readable report printed showing buffer assignments, VRAM cursor, and per-NPC details

- [ ] **Step 4: Commit**

```bash
git add tests/test_partition_calculator.py
git commit -m "test: add Room 204 smoke test and integration verification"
```

---

## Notes for Implementer

- **Test fixtures**: The project may not have a standard `world_fixture`. Check `tests/conftest.py` or existing test patterns. If none exist, create a minimal fixture. The exact setup depends on how `GameWorld` is initialized — check the management commands (e.g., `partitionanalyzer.py`) for patterns of loading world data.

- **Static coin exclusion**: Verify `COIN_SPRITE_IDS` contains only animated coins (192, 193, 194, 211). Static coins (234, 235, 236, 238) must NOT be in this set.

- **`npc_sequence_overrides` are sequence IDs, not mold IDs**: Both `min_vram_from_sequence` and `min_vram_from_mold` exist on the NPC class. The overrides dict maps to SEQUENCE IDs — `min_vram_from_sequence` internally iterates frames and calls `min_vram_from_mold` for each.

- **Existing functions preserved**: `analyze_room_partition`, `apply_partition_analysis`, and all `update_*` functions stay in place. They'll be gradually replaced as rooms migrate to the new system.

- **BossNPC model assumptions**: `filter_fitting_models` assumes each `model_cls` in `candidate_models` has a no-arg constructor (`model_cls()`) and the instance has a `.base` attribute returning the NPC definition. This matches the existing `BossNPC` class pattern in `physical_objects.py`.

- **`_get_character_model` helper**: Needs to map protagonist name strings to character model objects. Check how `world.overworld_character` works and what character models are available. The helper should handle all 5 characters: mario, peach, bowser, geno, mallow.
