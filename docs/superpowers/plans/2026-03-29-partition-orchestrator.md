# Partition Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `update_shuffed_boss_partitions` with a generalized snapshot-and-diff orchestrator that detects rooms with changed NPC models and recalculates their partitions.

**Architecture:** Snapshot vanilla NPC sprite IDs before shuffling, diff after, then run `analyze_partition`/`apply_partition` only on changed rooms with BufferSpace preservation. Final pass logs slot machine support for chest rooms.

**Tech Stack:** Python, existing `partition_calculator.py` primitives (`analyze_partition`, `apply_partition`, `can_room_support_slots`)

**Spec:** `docs/superpowers/specs/2026-03-29-partition-orchestrator-design.md`

---

### Task 1: Add `_vanilla_room_states` field to GameWorld

**Files:**
- Modify: `randomizer/types/gameworld.py:287-288`

- [ ] **Step 1: Add the field**

In `randomizer/types/gameworld.py`, after the `_slot_dummy_indices` and `_flag_dummy_index` fields (around line 288), add:

```python
    # Vanilla room NPC states for change detection during partition recalculation
    # Populated by snapshot_vanilla_room_states() before NPC shuffling begins
    _vanilla_room_states: dict[int, "VanillaRoomState"] | None = None
```

Also add the TYPE_CHECKING import. Find the existing `if TYPE_CHECKING:` block in the file and add:

```python
from randomizer.logic.partition_calculator import VanillaRoomState
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/types/gameworld.py
git commit -m "feat: add _vanilla_room_states field to GameWorld"
```

---

### Task 2: Implement `snapshot_vanilla_room_states`

**Files:**
- Modify: `randomizer/logic/partition_calculator.py:58-90` (near the dataclass definitions)

- [ ] **Step 1: Add the snapshot function**

In `randomizer/logic/partition_calculator.py`, after the `VanillaRoomState` dataclass (after line 90), add:

```python
def snapshot_vanilla_room_states(world: GameWorld) -> None:
    """Capture vanilla NPC sprite states for all rooms with partitions.

    Must be called AFTER update_partition_by_protagonist but BEFORE any
    NPC model shuffling (.render() calls). Stores result on
    world._vanilla_room_states for later change detection.
    """
    from .partition_calculator import _get_npc_gridplane_info
    states: dict[int, VanillaRoomState] = {}

    for room_id, room in enumerate(world.rooms._rooms):
        if room is None or not hasattr(room, 'partition') or room.partition is None:
            continue

        npc_states: list[VanillaNPCState] = []
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            sprite_id = obj._npc.sprite_id
            is_gridplane, gridplane_format = _get_npc_gridplane_info(world, sprite_id)
            is_coin = sprite_id in COIN_SPRITE_IDS
            npc_states.append(VanillaNPCState(
                sprite_id=sprite_id,
                is_gridplane=is_gridplane,
                gridplane_format=gridplane_format,
                is_coin=is_coin,
            ))

        chest_states: list[VanillaChestState] = []
        states[room_id] = VanillaRoomState(npcs=npc_states, chests=chest_states)

    world._vanilla_room_states = states
```

Note: this function lives in `partition_calculator.py` but references itself — remove the self-import line (`from .partition_calculator import _get_npc_gridplane_info`) since `_get_npc_gridplane_info` is already in the same module. Just call it directly.

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "feat: implement snapshot_vanilla_room_states"
```

---

### Task 3: Implement `AnimationVramOverride` and pre-pass

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`

- [ ] **Step 1: Add the dataclass and registry**

After the `snapshot_vanilla_room_states` function, add:

```python
@dataclass
class AnimationVramOverride:
    """Declarative animation-based min_vram override for NPC objects.

    Before partition recalculation, if the boss placed at location_class
    has the named animation, compute min_vram from its sequence and set it
    on the room NPC.
    """
    location_class: type    # e.g., InnerMinesBossFight
    room_id: int            # room where NPC appears
    npc_id: AreaObject      # which NPC in the room
    animation_attr: str     # attribute name on boss.animations, e.g. "mines_punch"


# Registry of animation overrides. Add new entries here as needed.
# Each override is processed before partition recalculation for changed rooms.
ANIMATION_VRAM_OVERRIDES: list[AnimationVramOverride] = []
```

- [ ] **Step 2: Populate with mines_punch override**

The `ANIMATION_VRAM_OVERRIDES` list needs to be populated after the import of `InnerMinesBossFight` is available. Since `InnerMinesBossFight` is in `randomizer/progression/prizelocations.py` and importing it at module level would create a circular import, populate the list lazily inside the pre-pass function. Add the helper:

```python
def _get_animation_vram_overrides() -> list[AnimationVramOverride]:
    """Build the animation VRAM override registry.

    Imports are deferred to avoid circular dependencies with prizelocation modules.
    """
    from ..progression.prizelocations import InnerMinesBossFight

    return [
        AnimationVramOverride(
            location_class=InnerMinesBossFight,
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            npc_id=NPC_0,
            animation_attr="mines_punch",
        ),
    ]


def _apply_animation_vram_overrides(world: GameWorld, changed_rooms: set[int]) -> None:
    """Apply animation-based min_vram overrides to NPCs in changed rooms.

    For each override whose room is in the changed set, look up the boss
    model's animation sequence and compute the min_vram requirement.
    Must run BEFORE partition recalculation.
    """
    from ..utils.npcs import min_vram_from_sequence_for_sprite
    from ..types.prize import BossFightPrize

    overrides = _get_animation_vram_overrides()

    for override in overrides:
        if override.room_id not in changed_rooms:
            continue

        location = world.locations.get(override.location_class)
        if location is None:
            continue

        assert isinstance(location.prize, BossFightPrize)
        npc_model = location.prize.get_npc_for_slot(world, 4096)
        boss = npc_model()

        if boss.animations is None:
            continue
        animation = getattr(boss.animations, override.animation_attr, None)
        if animation is None:
            continue

        sequence_id = animation.sequence_id
        sprite_id = boss.base.sprite_id
        min_vram = min_vram_from_sequence_for_sprite(world, sprite_id, sequence_id)

        room = world.rooms._rooms[override.room_id]
        assert room is not None
        npc_obj = room.get_npc_by_target_id(override.npc_id)
        npc_obj.set_min_vram_size(min_vram)
```

- [ ] **Step 3: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "feat: add AnimationVramOverride registry and pre-pass"
```

---

### Task 4: Implement change detection helper

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`

- [ ] **Step 1: Add `_detect_changed_rooms`**

After the animation override functions, add:

```python
def _detect_changed_rooms(world: GameWorld) -> set[int]:
    """Compare current NPC sprite IDs against vanilla snapshot.

    Returns set of room IDs where at least one NPC's sprite_id differs
    from the snapshot taken before shuffling.
    """
    assert world._vanilla_room_states is not None, (
        "snapshot_vanilla_room_states() must be called before change detection"
    )

    changed: set[int] = set()
    for room_id, vanilla_state in world._vanilla_room_states.items():
        room = world.rooms._rooms[room_id]
        if room is None:
            continue

        # Enumerate current non-Clone NPCs
        current_sprites: list[int] = []
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            current_sprites.append(obj._npc.sprite_id)

        # Compare against snapshot
        if len(current_sprites) != len(vanilla_state.npcs):
            # NPC count changed (e.g., dummies added) — mark as changed
            changed.add(room_id)
            continue

        for current_sprite_id, vanilla_npc in zip(current_sprites, vanilla_state.npcs):
            if current_sprite_id != vanilla_npc.sprite_id:
                changed.add(room_id)
                break

    return changed
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "feat: implement _detect_changed_rooms for snapshot diff"
```

---

### Task 5: Implement partition recalculation with BufferSpace preservation

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`

- [ ] **Step 1: Add `_recalculate_room_partition`**

After `_detect_changed_rooms`, add:

```python
def _recalculate_room_partition(world: GameWorld, room_id: int) -> None:
    """Recalculate and apply a room's partition, preserving BufferSpace values.

    Steps:
    1. Extract preservation params from existing partition
    2. Run analyze_partition with preserved params
    3. Overlay preserved BufferSpace values onto the analysis result
    4. Apply the partition
    """
    room = world.rooms._rooms[room_id]
    assert room is not None
    assert room.partition is not None

    existing = room.partition

    # --- Extract preservation params ---
    allow_extra = existing.allow_extra_sprite_buffer
    max_packets = existing.extra_sprite_buffer_size
    water = not existing.full_palette_buffer

    # Build buffer space preservation map: {buffer_type: max BufferSpace}
    # Also track per-index for the "same role" fallback
    preserved_by_type: dict[BufferType, BufferSpace] = {}
    preserved_by_index: list[BufferSpace] = []
    for buf in existing.buffers:
        space = buf.main_buffer_space
        preserved_by_index.append(space)
        if space != BufferSpace.BYTES_0:
            btype = buf.buffer_type
            if btype not in preserved_by_type or space.value > preserved_by_type[btype].value:
                preserved_by_type[btype] = space

    # --- Run analyze_partition ---
    # Do NOT pass protagonist — ally buffer already set by update_partition_by_protagonist
    analysis = analyze_partition(
        world,
        room_id,
        max_packets=max_packets,
        allow_extra_sprite_buffer=allow_extra,
        water=water,
    )

    # --- Preserve ally buffer size from existing partition ---
    # update_partition_by_protagonist already computed the correct value
    analysis.ally_buffer_size = existing.ally_sprite_buffer_size

    # --- Overlay preserved BufferSpace ---
    for i, assignment in enumerate(analysis.buffers):
        computed_space = assignment.buffer_space

        # Check 1: type match in preservation map
        type_preserved = preserved_by_type.get(assignment.buffer_type, BufferSpace.BYTES_0)

        # Check 2: same-index fallback (buffer type changed but same role)
        index_preserved = preserved_by_index[i] if i < len(preserved_by_index) else BufferSpace.BYTES_0

        # Take the max of: what analysis computed, type-matched preservation, index-based preservation
        best = max(computed_space, type_preserved, index_preserved, key=lambda s: s.value)
        assignment.buffer_space = best

    # --- Apply ---
    apply_partition(world, room_id, analysis)
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "feat: implement _recalculate_room_partition with BufferSpace preservation"
```

---

### Task 6: Implement slot machine support check

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`

- [ ] **Step 1: Add `_log_slot_machine_support`**

After `_recalculate_room_partition`, add:

```python
def _log_slot_machine_support(world: GameWorld) -> None:
    """Log can_room_support_slots results for all rooms with chests.

    For rooms with slot machine dummy NPCs (last 5 objects with EMPTY_NPC_3
    sprite ID), temporarily swaps them to EMPTY_NPC before checking.
    Debug output only — does not modify any state.
    """
    import logging
    logger = logging.getLogger(__name__)

    from ..data.rooms.npcs import EMPTY_NPC

    slot_dummy_sprite_id = SPR1023_EMPTY

    for room_id, room in enumerate(world.rooms._rooms):
        if room is None or room.partition is None:
            continue

        # Check if room has chests
        has_chest = False
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            if isinstance(obj, ChestNPC) or obj._npc.sprite_id == CHEST_SPRITE_ID:
                has_chest = True
                break

        if not has_chest:
            continue

        # Check if last 5 objects are slot dummies (all have EMPTY sprite)
        objects = room.objects
        has_dummies = (
            len(objects) >= 5
            and all(
                objects[len(objects) - 5 + j]._npc.sprite_id == slot_dummy_sprite_id
                for j in range(5)
            )
        )

        saved_npcs = []
        if has_dummies:
            # Temporarily swap dummy NPCs to EMPTY_NPC
            for j in range(5):
                idx = len(objects) - 5 + j
                saved_npcs.append(objects[idx]._npc)
                objects[idx]._npc = EMPTY_NPC

        try:
            result = can_room_support_slots(world, room_id)
            # Run a quick analysis to get bitmap_slots_remaining
            analysis = analyze_partition(world, room_id)
            logger.info(
                "Slot check room %d: support=%s bitmap_remaining=%d vram_remaining=%d",
                room_id, result, analysis.bitmap_slots_remaining, analysis.vram_remaining,
            )
        finally:
            # Restore original dummy NPCs
            if has_dummies:
                for j in range(5):
                    idx = len(objects) - 5 + j
                    objects[idx]._npc = saved_npcs[j]
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "feat: implement _log_slot_machine_support debug output"
```

---

### Task 7: Implement the main orchestrator and wire up integration

**Files:**
- Modify: `randomizer/logic/partition_calculator.py`
- Modify: `randomizer/logic/apply.py:13,349,549`

- [ ] **Step 1: Add `update_changed_room_partitions` orchestrator**

After `_log_slot_machine_support`, add:

```python
def update_changed_room_partitions(world: GameWorld) -> None:
    """Recalculate partitions for rooms where NPC models changed.

    Replaces update_shuffed_boss_partitions. Call order:
    1. Detect changed rooms via snapshot diff
    2. Apply animation VRAM overrides (min_vram_size pre-pass)
    3. Recalculate partition for each changed room
    4. Log slot machine support for all chest rooms
    """
    import logging
    logger = logging.getLogger(__name__)

    changed_rooms = _detect_changed_rooms(world)
    logger.info("Partition orchestrator: %d rooms changed", len(changed_rooms))

    # Pre-pass: animation VRAM overrides
    _apply_animation_vram_overrides(world, changed_rooms)

    # Recalculate partitions
    for room_id in sorted(changed_rooms):
        _recalculate_room_partition(world, room_id)

    # Final pass: slot machine support check (all chest rooms, not just changed)
    _log_slot_machine_support(world)
```

- [ ] **Step 2: Update apply.py import**

In `randomizer/logic/apply.py`, change line 13 from:

```python
from randomizer.logic.partition_calculator import update_shuffed_boss_partitions
```

to:

```python
from randomizer.logic.partition_calculator import snapshot_vanilla_room_states, update_changed_room_partitions
```

- [ ] **Step 3: Insert snapshot call before .render() loop**

In `randomizer/logic/apply.py`, before the loop that starts around line 349 (`for place in world.locations.values():`), insert:

```python
    # Snapshot vanilla NPC states before any shuffling modifies room objects
    snapshot_vanilla_room_states(world)
```

Find the line that reads:

```python
    for place in world.locations.values():
        # Construct prize granter hub events
```

Insert the snapshot call immediately before it.

- [ ] **Step 4: Replace the orchestrator call**

In `randomizer/logic/apply.py`, replace line 549:

```python
    update_shuffed_boss_partitions(world)
```

with:

```python
    update_changed_room_partitions(world)
```

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/partition_calculator.py randomizer/logic/apply.py
git commit -m "feat: wire up partition orchestrator in apply pipeline"
```

---

### Task 8: Delete old hardcoded update functions

**Files:**
- Modify: `randomizer/logic/partition_calculator.py:286-508`

- [ ] **Step 1: Delete old functions**

Remove the following from `randomizer/logic/partition_calculator.py`:

- `_buffer_by_sprite_format` (line 286)
- `_buffer_by_room_object` (line 297)
- `_update_buffer_by_room_object` (line 303)
- `update_statue_room_partitions` (line 321)
- `update_kitchen_partitions` (line 344)
- `update_mines_henchman_room_partitions` (line 350)
- `update_protagonist_room_partition` (line 377)
- `update_johnny_room_partition` (line 427)
- `update_mushroom_kingdom_partitions` (line 431)
- `update_chapel_partition` (line 446)
- `update_arrow_partitions` (line 451)
- `update_mines_inner_henchman_room_partition` (line 456)
- `update_seaside_partitions` (line 480)
- `update_credits_partitions` (line 484)
- `update_shuffed_boss_partitions` (line 490)

This is the entire block from line 286 to line 508 (the section between the "Ally Buffer Calculation" comment block and the "General-purpose partition analysis tool" comment block).

Also clean up now-unused imports. After deletion, these area_object imports are no longer needed by the old functions but check if they're still used by the new orchestrator code or other functions:

- `NPC_10`, `NPC_13`, `NPC_6` (line 27) — check if used elsewhere in file. `NPC_10` and `NPC_13` appear in `analyze_room_partition` or other functions — search before removing.
- The `NPC_0` through `NPC_8` imports (lines 42-48) — `NPC_0` is still used by `ANIMATION_VRAM_OVERRIDES`. Remove only those not referenced anywhere else in the file.

- [ ] **Step 2: Verify no remaining references to deleted functions**

Run:

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && grep -rn "update_shuffed_boss_partitions\|update_statue_room\|update_mines_henchman\|update_protagonist_room_partition\|update_kitchen\|update_johnny\|update_mushroom_kingdom\|update_chapel\|update_arrow\|update_mines_inner\|update_seaside_partitions\|update_credits_partitions\|_update_buffer_by_room_object\|_buffer_by_room_object\|_buffer_by_sprite_format" randomizer/
```

Expected: no results (all references removed).

- [ ] **Step 3: Commit**

```bash
git add randomizer/logic/partition_calculator.py
git commit -m "refactor: delete old hardcoded partition update functions"
```

---

### Task 9: Remove TYPE_CHECKING import from gameworld.py if circular

**Files:**
- Modify: `randomizer/types/gameworld.py`

- [ ] **Step 1: Verify no circular import**

Run:

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -c "from randomizer.types.gameworld import GameWorld; print('OK')"
```

If this fails with a circular import error, change the `VanillaRoomState` import in `gameworld.py` to use a string annotation instead:

```python
_vanilla_room_states: "dict[int, VanillaRoomState] | None" = None
```

And remove the import from the `TYPE_CHECKING` block if it causes issues. The field annotation can use a string literal since Python evaluates dataclass field annotations lazily with `from __future__ import annotations`.

- [ ] **Step 2: Run a basic smoke test**

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -c "from randomizer.logic.partition_calculator import snapshot_vanilla_room_states, update_changed_room_partitions; print('Imports OK')"
```

Expected: `Imports OK`

- [ ] **Step 3: Commit if changes were needed**

```bash
git add randomizer/types/gameworld.py
git commit -m "fix: resolve circular import for VanillaRoomState"
```

---

### Task 10: End-to-end verification

**Files:** None (testing only)

- [ ] **Step 1: Generate a test seed**

Run whatever the standard seed generation command is for this project. Verify it completes without errors. The logging output should show lines like:

```
Partition orchestrator: N rooms changed
Slot check room XXX: support=True/False bitmap_remaining=N vram_remaining=N
```

- [ ] **Step 2: Check for regressions**

If there are any existing tests, run them:

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -m pytest -x -v 2>&1 | head -50
```

- [ ] **Step 3: Final commit if any fixes were needed**

```bash
git add -A
git commit -m "fix: address issues found during end-to-end verification"
```
