# Partition Calculator Redesign

**Date:** 2026-03-29
**Location:** `randomizer/logic/partition_calculator.py`
**Replaces:** `analyze_room_partition`, `apply_partition_analysis`, and the manual one-off functions called from `update_shuffed_boss_partitions`

## Problem

The current partition system uses a collection of manual per-room/per-boss update functions (`update_statue_room_partitions`, `update_kitchen_partitions`, etc.) that each handle buffer type changes for specific shuffled NPCs. This approach:

- Doesn't scale as more shuffle types are added
- Doesn't account for all the factors that determine a correct partition (protagonist, sequences, packet sprites, format compatibility)
- Has led to visual corruption bugs when buffer types don't match NPC gridplane formats

## Solution

Two functions that replace all manual partition logic:

1. **`analyze_partition`** — Pure computation. Examines all NPCs in a room, determines optimal buffer layout, ally buffer size, and cannot_clone flags. Returns a `PartitionAnalysis` result object with no side effects.

2. **`apply_partition`** — Takes an analysis and writes it to the room: sets the partition, sets cannot_clone on each NPC.

Callers run `analyze_partition` on any room after shuffle results are applied, inspect/log the result if needed, then call `apply_partition`.

## Key Domain Rules

### Buffer type / gridplane format compatibility

| Buffer Type | Tile width per slot | Compatible formats |
|-------------|--------------------|--------------------|
| FOUR_SPRITES_PER_ROW | 3 tiles (24px) | Format 0-1 only |
| THREE_SPRITES_PER_ROW | 4 tiles (32px) | Format 2-3 only |

Mismatches cause visual corruption:
- Format 0-1 in THREE buffer: game reads 4 tiles but sprite has 3 -> shows adjacent sprite's tiles
- Format 2-3 in FOUR buffer: game reads 3 tiles but sprite has 4 -> rightmost column cut off

### Buffer slot constraints

- Buffer A (index 0): TREASURE_CHEST if any chests exist
- Buffer C (index 2): COINS if any animated coins exist (sprite IDs 192, 193, 194, 211). Static coin sprites (234, 235, 236, 238) do NOT require a COINS buffer.
- Remaining slots: gridplane types or EMPTY_3

### When force_cannot_clone is computed

The `force_cannot_clone` field on `NPCAnalysis` is a **computed output** of the analysis. It is distinct from `cannot_clone`, which is the **input value** read from the NPC or room-object definition.

| Condition | `force_cannot_clone` |
|-----------|---------------------|
| NPC's mold 0 is non-gridplane | `True` — cannot be in any gridplane buffer |
| NPC's gridplane format has no available buffer slot | `True` — overflow to dedicated VRAM |
| NPC's gridplane format matches an available buffer | `False` — assigned to that buffer |

`apply_partition` uses `force_cannot_clone` (not the input `cannot_clone`) to set the room-object-level override.

### Non-gridplane sequences and buffer space

A gridplane NPC (mold 0 is gridplane) may use animation sequences whose frames reference non-gridplane molds. This does NOT set `force_cannot_clone`. Instead, it increases the buffer's `main_buffer_space`.

Two levels of calculation:

1. **Per-mold cost:** `min_vram_from_mold(mold_id)` — returns 0 for gridplane molds; for non-gridplane molds returns `ceil(max(0, truthy_subtiles - 16) / 16)` where each unit = 256 bytes = one `BufferSpace` step.

2. **Per-sequence cost:** `min_vram_from_sequence(seq_id)` = `max(min_vram_from_mold(frame.mold_id) for frame in sequence.frames)`

3. **Per-NPC cost:** `max_sequence_vram` = `max(min_vram_from_sequence(seq_id) for seq_id in npc's specified sequences)`, or 0 if no sequences specified.

4. **Per-buffer cost:** `main_buffer_space` = `max(npc.max_sequence_vram for npc in NPCs assigned to that buffer)`, capped at 7 (the `BufferSpace` enum max). Note: not all NPCs use their extra sequences simultaneously — the buffer only needs space for the largest single NPC's sequence requirement, not the sum. This is already handled by using `max()` rather than `sum()`.

### VRAM overflow check

```
cursor  = ally_buffer_size * 4          (rows for player character)
cursor += extra_sprite_buffer_size      (rows for packet sprites; = max_packets directly)
cursor += sum(buffer.main_buffer_space for buffer in 3 buffers)
cursor += sum(npc.max_sequence_vram for npc in force_cannot_clone NPCs)
# Max ~32 rows. Warn if exceeded.
```

`max_packets` maps directly to `extra_sprite_buffer_size` — each packet sprite takes 1 cursor row. The parameter value IS the cursor cost.

## Data Structures

```python
@dataclass
class NPCAnalysis:
    index: int                     # Position in room's objects list
    sprite_id: int
    vram_store: VramStore
    min_vram: int                  # From mold 0 baseline (NPC definition or room override)
    max_sequence_vram: int         # Max min_vram across specified sequences (for buffer space)
    cannot_clone: bool             # INPUT: from NPC/room-object definition (read-only)
    is_chest: bool
    is_coin: bool                  # Animated coins only (192, 193, 194, 211)
    is_gridplane: bool             # Mold 0 gridplane status
    gridplane_format: int | None   # 0-3 or None
    buffer_type: BufferType        # Computed: FOUR, THREE, TREASURE_CHEST, COINS, EMPTY_3
    clone_count: int               # Consecutive Clone objects after this NPC
    force_cannot_clone: bool       # COMPUTED OUTPUT: True when mold 0 non-gridplane OR no buffer slot


@dataclass
class BufferAssignment:
    buffer_type: BufferType
    buffer_space: BufferSpace
    npc_indices: list[int]


@dataclass
class PartitionAnalysis:
    room_id: int
    npcs: list[NPCAnalysis]
    ally_buffer_size: int
    allow_extra_sprite_buffer: bool
    extra_buffer_size: int
    buffers: list[BufferAssignment]   # Always exactly 3
    full_palette: bool
    warnings: list[str]

    def to_partition(self) -> Partition: ...
    def format_report(self) -> str: ...

    @property
    def vram_cursor(self) -> int:
        """Total VRAM rows consumed by this partition."""
        ...

    @property
    def vram_remaining(self) -> int:
        """VRAM rows available for additional NPCs (32 - vram_cursor)."""
        ...
```

## Function Signatures

```python
def analyze_partition(
    world: GameWorld,
    room_id: int,
    *,
    protagonist: str | None = None,
    max_packets: int = 0,
    allow_extra_sprite_buffer: bool | None = None,  # Default: True if max_packets > 0
    water: bool = False,
    npc_sequence_overrides: dict[int, list[int]] | None = None,
) -> PartitionAnalysis:
    """Analyze a room and compute optimal partition configuration.

    Args:
        world: GameWorld with loaded sprite data.
        room_id: Room index to analyze.
        protagonist: Character name ("mario", "peach", "bowser", "geno", "mallow")
            for ally buffer sizing. Uses room's extra_sprite_actions to determine
            if additional animation states require larger ally buffer. Default None
            uses ally_buffer_size=1.
        max_packets: Maximum packet sprites active simultaneously (chest pickups,
            EXP stars, flower bonuses). Sets extra_sprite_buffer_size directly
            (1 packet = 1 cursor row).
        allow_extra_sprite_buffer: Whether packet sprites can be created. Defaults
            to True when max_packets > 0, False otherwise. Can be set True with
            max_packets=0 (valid but unknown runtime effect).
        water: If True, sets full_palette_buffer=False (5 NPC palette slots
            instead of 9). Default False (full palette, no water).
        npc_sequence_overrides: Per-NPC sequence IDs that the NPC is known to use.
            {npc_object_index: [sequence_id, ...]}. Used to compute buffer space
            needs from non-gridplane molds in those sequences.

    Returns:
        PartitionAnalysis with computed partition, buffer assignments, and
        force_cannot_clone recommendations. Deterministic for identical inputs.
    """


def apply_partition(
    world: GameWorld,
    room_id: int,
    analysis: PartitionAnalysis,
) -> None:
    """Apply a computed partition analysis to a room.

    Sets the room's partition and force_cannot_clone flags on each parent NPC.
    Clones are skipped (they inherit from parent). No preserve flags — the
    analysis computes all values. If the caller needs to override something,
    modify the analysis object before calling apply.

    Args:
        world: GameWorld instance.
        room_id: Room index to update.
        analysis: Result from analyze_partition().
    """
```

## Algorithm: analyze_partition

### Step 1: Enumerate NPCs

Iterate room objects. For each parent NPC (not a Clone):
- Count consecutive Clones following it
- Detect sprite properties: gridplane status (mold 0), format, min_vram from mold 0
- If `npc_sequence_overrides` includes this NPC index, compute `max_sequence_vram`:
  - For each specified sequence, call `min_vram_from_sequence(seq_id)` which returns `max(min_vram_from_mold(frame.mold_id) for frame in sequence.frames)`
  - `max_sequence_vram` = max across all specified sequences
- Classify: chest (sprite 94 or ChestNPC), animated coin (sprite 192/193/194/211), gridplane format 0-1 (FOUR), gridplane format 2-3 (THREE), or non-gridplane (EMPTY_3)
- Non-gridplane NPCs (mold 0 non-gridplane): set `force_cannot_clone=True`

### Step 2: Compute ally buffer size

If protagonist is specified:
1. Look up character model from world
2. Check DEFAULT_ANIMATION_STATES (SOUTH, FACE_NORTH, FACE_SOUTH) for min_vram
3. Check room's `extra_sprite_actions` mapped through EXTRA_ACTION_TO_ANIMATION_STATE for additional min_vram
4. If any vram values found: `ally_buffer_size = min(max(all_vram_values) + 1, 3)`
5. If no vram values found (no matching animation states): `ally_buffer_size = 1`

If protagonist is None: `ally_buffer_size = 1`.

### Step 3: Assign buffer slots

Priority order:
1. If any chests: buffer A = TREASURE_CHEST
2. If any animated coins: buffer C = COINS
3. Determine which gridplane formats are present among clonable NPCs (those with `force_cannot_clone=False`)
4. Assign FOUR and/or THREE to remaining empty slots
5. If both formats exist but only one slot remains: assign the majority format, mark minority format NPCs `force_cannot_clone=True`
6. Fill remaining empty slots with EMPTY_3

### Step 4: Compute buffer space

For each gridplane buffer (FOUR or THREE):
- Collect all NPCs assigned to it (those with matching format and `force_cannot_clone=False`)
- `main_buffer_space = max(npc.max_sequence_vram for npc in assigned)`, capped at 7
- Map to BufferSpace enum

### Step 5: Overflow check

Sum cursor consumption:
```
cursor  = ally_buffer_size * 4
cursor += extra_sprite_buffer_size
cursor += sum(buffer.main_buffer_space for buffer in 3 buffers)
cursor += sum(npc.max_sequence_vram for npc in force_cannot_clone NPCs)
```
If > 32: add warning. The caller may need to reduce NPC count or adjust parameters.

### Step 6: Build result

Return PartitionAnalysis with all computed values.

## Algorithm: apply_partition

1. `partition = analysis.to_partition()`
2. `room._partition = partition`
3. For each NPC analysis:
   - Skip if Clone
   - If `force_cannot_clone=True`: `obj.set_cannot_clone(True)`
   - Else if assigned to a buffer: `obj.set_cannot_clone(False)`

## Special-case rooms in existing code

The existing code has several room lists with hardcoded overrides:

- **`SPECIAL_CASE_ROOMS`** (triple EMPTY_3 forced): Rooms with complicated sequences (e.g., Spikey spinning in R205) or specific engine quirks. These rooms should continue to use their hand-tuned partitions — callers should NOT run `analyze_partition` on them unless the shuffle actually changed their NPCs.

- **`ALWAYS_REQUIRES_COIN_BUFFER`** (Midas River rooms): Coins are spawned by game scripts, not by NPC objects. The analyzer won't detect them. Callers must pass the appropriate parameters or handle these rooms separately.

- **`TRIPLE_EMPTY_EX1_ROOMS` / `TRIPLE_EMPTY_EX0_ROOMS`** (Bowser's Keep battle rooms, Booster Tower): All-non-gridplane rooms where every NPC is `cannot_clone`. The analyzer handles this correctly — all NPCs get `force_cannot_clone=True`, all buffers become EMPTY_3.

- **`CLOSE_CHEST_ROOMS`**: Rooms where multiple chests can be opened before packets despawn. Callers should set `max_packets=2` (or higher) for these rooms.

These lists remain as caller-side knowledge. The analyzer is general-purpose; the caller decides which rooms to run it on and with what parameters.

## Migration

The new functions replace:
- `analyze_room_partition` (dead code, never called)
- `apply_partition_analysis` (dead code, never called)
- Individual `update_*` functions called from `update_shuffed_boss_partitions` (gradually, as rooms are migrated to the new system)

The old `update_*` functions can remain temporarily for rooms not yet migrated. The caller builds a list of rooms that had model-changing shuffles and runs `analyze_partition` + `apply_partition` on each.

## Boss Model Selection Helper

For boss fight rooms, callers need to know which NPC models fit within the VRAM budget before choosing one. The `PartitionAnalysis.vram_remaining` property exposes the headroom after partition calculation.

```python
def filter_fitting_models(
    world: GameWorld,
    room_id: int,
    npc_index: int,
    candidate_models: list,
    *,
    prefer_largest: bool = True,
    **analyze_kwargs,
) -> list:
    """Filter and rank NPC models that fit in a room's VRAM budget.

    For each candidate model, temporarily substitutes it into the room's NPC
    slot, runs analyze_partition, and checks whether vram_remaining >= 0.

    Args:
        world: GameWorld instance.
        room_id: Room to test against.
        npc_index: Object index where the boss NPC sits.
        candidate_models: List of NPC model objects (from prize._npc_models).
        prefer_largest: If True (default), returns models sorted largest VRAM
            first. If False, returns sorted smallest first (for tight rooms).
        **analyze_kwargs: Passed through to analyze_partition (protagonist,
            max_packets, water, npc_sequence_overrides).

    Returns:
        List of (model, analysis) tuples for models that fit, sorted by
        VRAM consumption (descending if prefer_largest, ascending otherwise).
        Empty list if nothing fits.
    """
```

Usage on BossFightLocation:
```python
fitting = filter_fitting_models(
    world, room_id, boss_npc_index,
    prize._npc_models,
    protagonist="mario",
    max_packets=1,
    prefer_largest=True,       # default: pick biggest that fits
    # prefer_largest=False,    # for tight rooms: pick smallest
)
if fitting:
    chosen_model, analysis = fitting[0]
    # apply the model, then apply the partition
    apply_partition(world, room_id, analysis)
```

## Open Questions

- **Vanilla asymmetry**: In vanilla Room 204, format-3 Sky Troopas render correctly in a FOUR buffer despite the format mismatch. The cause is unknown. The calculator takes the conservative approach: strict format matching, with `force_cannot_clone` as the fallback.
- **`allow_extra_sprite_buffer` with size 0**: Valid combination but runtime effect is unclear. Exposed as a parameter for callers who need it.
