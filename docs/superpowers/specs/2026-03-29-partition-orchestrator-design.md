# Partition Orchestrator Design

Replaces `update_shuffed_boss_partitions` with a generalized, snapshot-and-diff orchestrator that detects rooms with changed NPC models and recalculates their partitions using the new `analyze_partition`/`apply_partition` API.

## Approach: Snapshot-and-Diff

Before any NPC shuffling, snapshot every room's NPC sprite IDs. After shuffling, diff against current state. Recalculate partitions only for rooms where NPCs changed.

## New Public API

### `snapshot_vanilla_room_states(world: GameWorld) -> None`

Iterates all rooms with partitions. For each NPC, records a `VanillaNPCState` (sprite_id, is_gridplane, gridplane_format, is_coin). Stores the result in `world._vanilla_room_states: dict[int, VanillaRoomState]`.

Called once, before the `.render()` loop in `apply.py` (~line 349).

### `update_changed_room_partitions(world: GameWorld) -> None`

Replaces `update_shuffed_boss_partitions`. Called from `apply.py` at the same location (line 549).

Internal call order:

1. **Diff** — compare `world._vanilla_room_states` against current NPC sprite IDs to produce a set of changed room IDs.
2. **Animation VRAM pre-pass** — run declarative animation overrides to set `min_vram_size` on NPCs before partition recalculation.
3. **Partition recalculation** — for each changed room: extract preservation params, run `analyze_partition`, overlay preserved `BufferSpace`, run `apply_partition`.
4. **Slot machine support check** — for all chest rooms, log `can_room_support_slots` results (debug output only).

## Detailed Design

### 1. Snapshot Phase

`snapshot_vanilla_room_states` iterates `world.rooms._rooms`. For each room with a partition, it builds a `VanillaRoomState` containing a `VanillaNPCState` per NPC object (skipping Clones). Uses the existing `VanillaNPCState` and `VanillaRoomState` dataclasses already defined in `partition_calculator.py`.

Stores result on `world._vanilla_room_states`.

### 2. Change Detection

For each room in the snapshot, compare each NPC's current `sprite_id` against the snapshotted value. If any NPC differs, the room is "changed" and enters the recalculation pipeline.

### 3. Animation VRAM Pre-Pass

A declarative registry of animation-to-room mappings:

```python
@dataclass
class AnimationVramOverride:
    location_class: type        # e.g., InnerMinesBossFight
    room_id: int                # room where NPC appears
    npc_id: AreaObject          # which NPC in the room
    animation_attr: str         # e.g., "mines_punch", "tower_bullet", "statue_peck"
```

For each override where the room is in the changed set:

1. Look up `world.locations[location_class].prize`
2. Get the boss NPC model via `prize.get_npc_for_slot(world, 4096)` (permissive max_vram to get the actual placed model)
3. Check `boss.animations.<animation_attr>` for a sequence ID
4. Compute `min_vram_from_sequence_for_sprite(world, sprite_id, sequence_id)`
5. Set `npc_obj.set_min_vram_size(min_vram)` on the room NPC

New animation overrides are added by appending to the registry list. No new functions needed.

Initially populated with `mines_punch` for room 289 / NPC_0. Other overrides (tower_bullet, statue_peck) can be added as their locations are identified.

### 4. Partition Recalculation with Preservation

For each changed room:

#### 4a. Extract preservation params from existing partition

- `allow_extra_sprite_buffer`: from `partition.allow_extra_sprite_buffer`
- `max_packets`: from `partition.extra_sprite_buffer_size`
- `water`: `not partition.full_palette_buffer`
- **Buffer space map**: for each of the 3 existing buffers, if `main_buffer_space` is non-zero, record `{buffer_type: max(buffer_space)}` keyed by buffer type. If multiple buffers share a type, take the max.

#### 4b. Run `analyze_partition`

Pass the preserved `allow_extra_sprite_buffer`, `max_packets`, and `water` parameters. Do NOT pass `protagonist` — ally buffer was already set by `update_partition_by_protagonist`.

#### 4c. Overlay preserved `BufferSpace`

After analysis, for each buffer in the result:

1. If the analysis already computed a non-zero `buffer_space` (from `min_vram_size` on NPCs), keep it if it's >= the preserved value.
2. Otherwise, look up the buffer's type in the preservation map. If found and the preserved value is larger, apply it.
3. If the buffer type changed (e.g., THREE_SPRITES_PER_ROW -> FOUR_SPRITES_PER_ROW) but occupies the same buffer index as an original buffer that had non-zero space, carry the preserved `BufferSpace` forward — the replacement NPC serves the same role.

Priority: `max(analysis_computed_space, preserved_space)`.

#### 4d. Apply partition

Call `apply_partition(world, room_id, analysis)` which sets the room partition and `cannot_clone` flags on NPCs.

### 5. Slot Machine Support Check (Final Pass)

After all partition recalculation is complete, iterate all rooms that contain chest NPCs (identified by having any NPC with `ChestNPC` type or sprite ID matching `CHEST_SPRITE_ID`).

For each chest room:

1. Check if the last 5 objects have sprite IDs matching the slot dummy sprite (`EMPTY_NPC_3`'s sprite ID).
2. If yes: temporarily swap those 5 NPCs to use `EMPTY_NPC` (SPR1023_EMPTY), run `can_room_support_slots`, then restore the originals.
3. If no slot dummies present: run `can_room_support_slots` directly.
4. Log: room ID, True/False result, `bitmap_slots_remaining` from the analysis.

This is debug output only — no blacklist enforcement. The output informs manual blacklist decisions.

## Integration Points

### apply.py changes

1. **Before `.render()` loop** (~line 349): insert `snapshot_vanilla_room_states(world)`.
2. **Replace line 549**: `update_shuffed_boss_partitions(world)` → `update_changed_room_partitions(world)`.

### gameworld.py changes

Add `_vanilla_room_states: dict[int, VanillaRoomState] | None = None` field.

### partition_calculator.py changes

**Add:**
- `AnimationVramOverride` dataclass
- `ANIMATION_VRAM_OVERRIDES` registry list
- `snapshot_vanilla_room_states(world)`
- `update_changed_room_partitions(world)` (the orchestrator)
- Helper: `_detect_changed_rooms(world)` → set of room IDs
- Helper: `_apply_animation_vram_overrides(world, changed_rooms)`
- Helper: `_recalculate_room_partition(world, room_id)` (extract, analyze, overlay, apply)
- Helper: `_log_slot_machine_support(world)`

**Delete:**
- `update_shuffed_boss_partitions`
- `update_statue_room_partitions`
- `update_mines_henchman_room_partitions`
- `update_protagonist_room_partition`
- `update_kitchen_partitions`
- `update_johnny_room_partition`
- `update_mushroom_kingdom_partitions`
- `update_chapel_partition`
- `update_arrow_partitions`
- `update_mines_inner_henchman_room_partition`
- `update_seaside_partitions`
- `update_credits_partitions`
- `_update_buffer_by_room_object`
- `_buffer_by_room_object`
- `_buffer_by_sprite_format`

**Keep:**
- `_get_npc_gridplane_info` (used by `_analyze_npc`)
- All `analyze_partition` / `apply_partition` / `filter_fitting_models` / `can_room_support_slots` functions
- `VanillaNPCState`, `VanillaRoomState`, `VanillaChestState` dataclasses

## Ordering Guarantees

1. `update_partition_by_protagonist` runs on all rooms first (already in gameworld.py).
2. `snapshot_vanilla_room_states` captures state after protagonist updates but before any shuffling.
3. `.render()` loop performs all NPC model swaps.
4. `update_changed_room_partitions`:
   - Animation VRAM pre-pass runs before any partition recalculation.
   - Partition recalculation runs for all changed rooms.
   - Slot machine check runs last, after all partitions are finalized.
