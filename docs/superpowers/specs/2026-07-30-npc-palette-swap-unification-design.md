# NPC Palette-Swap Sprite Unification

Date: 2026-07-30
Status: design approved, not yet planned

## Problem

A VRAM clone buffer holds tile data for exactly one `sprite_id`. A room has three
buffers. Every distinct sprite beyond the third must be `cannot_clone=True` and
take a dedicated allocation from the packed cursor `$6D`.

That cursor has a hard ceiling nothing enforces. Clone buffer bases are literals
in the engine — `$C0:8E98`-`$C0:8EB7` loads `#$40`, `#$80`, `#$C0` for buffers A,
B and C — and `$C0:8F83` writes that base into the same object field (`$18,X`) the
dedicated path fills from `$6D`. So dedicated NPCs own packed `$00`-`$3F` and
nothing more. The only guard (`$C0:8ED4`-`$C0:8EFD`) stops a block straddling
packed `$20` or `$30`; both sit below `$40`. A cursor that walks past `$40`
silently allocates on top of buffer A.

Room 315 in seed `9d58504ba469c08df5381ae0d15d8bc3_747523943` does exactly that.
Boss shuffle placed Culex, giving six distinct sprite ids across nine objects:

| obj | sprite | what | cannot_clone | min_vram |
|-----|--------|------|--------------|----------|
| 0 | 838 | Fire crystal | False, buffer A | 0 |
| 1 | 840 | Water crystal | False, buffer B | 0 |
| 2 | 842 | Earth crystal | True | 0 |
| 3 | 844 | Wind crystal | True | 0 |
| 4,5 | 263 | Piranha Plant | False, buffer C | 0 |
| 6,7 | 633 | Culex small | True | 1 |
| 8 | 263 | Piranha Plant | True | 0 |

Five dedicated NPCs. The cursor walks `$04` → `$10` → `$14` (realigned to `$20`)
→ `$30` → `$40`, landing object 8 on buffer A, where object 0 lives. Reported as
"NPC 6/7/8 partially overwrite NPC 0".

Fewer distinct sprite ids per room is the general fix. Many sprites are already
byte-identical recolours of each other, so collapsing them costs nothing but the
recolour, and the recolour is recoverable.

## Scope

**In scope:** merging sprites whose definitions are byte-identical apart from
`palette_offset`.

**Out of scope, deliberately:** consolidating sprites whose tiles genuinely
differ (the four Culex crystals — `AnimationPack(397)` vs `(440)`) onto one sprite
carrying several molds. That is the room 422 `_SHARED_MOLD_ROOM` pattern and
belongs in a follow-up spec that reuses the stub plumbing built here.

## Data

Hashing every sprite definition with `palette_offset` stripped, keeping only
sprites that have real graphics and a `palette_id` other than `SPAL000_NOTHING`
(866 of 1024):

- **125 palette-swap classes**, 322 sprite ids, **197 removable**.
- **26 classes / 32 ids are pure duplicates** — same `palette_offset`, so merging
  is sprite_id aliasing and nothing else. Includes `[263, 386]` Piranha Plant,
  `[511, 694]` Culex, `[496, 497]` Croco, `[505, 691]` Johnny 2,
  `[455, 456, 687, 693]` Belome, `[397, 415, 416, 429]` Bob-omb.
- **99 classes / 165 ids are offset-shifted** — merging needs a CGRAM row bump.

Bandanas straddle both: `[267, 331, 380]` at offsets `[0, 1, 0]`. 380 is a free
duplicate of 267; 331 needs a bump of +1.

The counts above are a **class-level** tally, which lumps every member of a mixed
class into whichever bucket the class falls in. Classified **per member** — which is
what the generated table does, and what the merge pass needs — the same 197 ids split
**42 pure / 155 shifted**. The gap is the 9 mixed classes, contributing 10 pure
members and 17 shifted ones. Both readings describe identical data; quote the
per-member figures when talking about the table.

The unfiltered numbers (129 classes / 349 removable) are wrong — they collapse
the empty protagonist-remap slots (sprites 31-37, 847-927, 997-1023, all
`SPAL000_NOTHING`) into one 119-member false class. The filter is load-bearing.

## Mechanism

Two separate things, both required for an offset-shifted merge:

- **Residency** — `extra_palette_source_offset` and `extra_palette_row_count`
  make the palette rows available in the level. Settable as a room-object
  override; the room 54 barrels do exactly this
  (`extra_palette_source_offset=1, extra_palette_row_count=1`).
- **Application** — `A_IncPaletteRowBy(n)` moves the object onto the row. It
  requires residency to already be set. Same pairing as room 422, where
  `SHARED_ITEM_BASE` loads the rows and `A_IncPaletteRowBy(2)` recolours the
  frog coins.

Residency alone does not recolour. Application alone does not work.

### Where the bump goes

96 event scripts named `*_SHUFFLED_NPC_ANIMATION_LOADER` exist. All 96 are empty
(`Return()` only) and all 96 are already invoked from their room's loader. Room
315's is `RunEventAsSubroutine(E0802_...)` at `script_1146.py:67`, inside the
boss-available branch, reached from `E1145` via the `"EVENT_1146_action_queue_0"`
label.

Because these are pre-wired subroutine calls rather than tail jumps, they sidestep
both the `reference_room_loader_e0015_ordering` landmine and the hand-editing of
room loaders that room 422 needed.

### CGRAM row budget

`green_switch_glow.npc_palette_rows` gives the layout:

```python
row = PROTAGONIST_PALETTE_ROW + partition.ally_sprite_buffer_size   # 8 + ally
for obj in room.objects:
    palette = world.get_sprite(sprite_id).palette_id
    if palette == protagonist_palette or palette in rows: continue
    extra = obj._npc.extra_palette_row_count if override is None else override
    rows[palette] = row
    row += 1 + extra
```

Rows are allocated **per distinct `palette_id`**, one each plus
`extra_palette_row_count` more. `PROTAGONIST_PALETTE_ROW = 8` and sprite CGRAM
runs to row 15, so a room has `15 - (8 + ally_sprite_buffer_size)` rows — seven at
ally 1. Every extra row shifts each later palette up by one, and per
`reference_effects_npc_palette_row` some effects records target hardcoded rows.
Residency growth is a scarce shared budget, not a free knob.

Note the `if palette in rows: continue`: only the **first** object in room order
carrying a palette sets its row count. Residency declared on a later merged object
is silently ignored. This is the most likely place to get the implementation
subtly wrong.

## Architecture

### Generated class table

A management command emits `randomizer/data/sprites/palette_swap_classes.py`:

```python
PURE:    dict[int, int]              # 386 -> 263       alias only
SHIFTED: dict[int, tuple[int, int]]  # 331 -> (267, 1)  canonical, pack offset
```

A test regenerates and diffs, so the table cannot drift silently when sprite data
changes.

### Generated stub map

A second command emits `randomizer/data/rooms/sprite_loader_events.py` mapping
room id to stub event id. Built by locating each stub's call site, then the room
whose entrance chain reaches it. Naive reachability is ambiguous — traversing
shared hub events returns five candidate stubs for room 315 — so the generator
resolves by nearest caller and **raises at build time** on any stub mapping to
zero or more than one room. Ambiguity is settled once, by hand, at generation
time, never at seed time.

### Merge pass

`_merge_palette_swaps()` in `partition_calculator.py`, called from
`_recalculate_room_partition` **before Step 3**. Step 3 is where "one buffer per
unique sprite ID" is decided, so merging earlier is what actually buys the buffer.

Per room, per class with two or more distinct sprite ids present:

1. Rewrite each member object to the canonical sprite.
2. Let `offs` be the pack offsets needed. On the **first object in room order
   carrying that `palette_id`**, set `extra_palette_source_offset = min(offs)` and
   `extra_palette_row_count = max(offs) - min(offs)`. That object is whichever one
   the row model reaches first — it need not be a member of the merged class, only
   a carrier of the same `palette_id`. Writing residency onto a class member that
   is not first has no effect.
3. For each object with `offset > min(offs)`, append
   `ActionQueueSync(target=NPC_n, subscript=[A_IncPaletteRowBy(offset - min(offs))])`
   to the room's stub, before its trailing `Return()`.

Tier 1 (pure duplicates) is step 1 only — no residency, no bump, no stub, no row
cost. It is independently shippable and carries no visual risk.

### Refactor included

`npc_palette_rows` moves from `green_switch_glow.py` to `logic/palette_rows.py`.
It is a general room-layout primitive living in a feature module, and it is about
to acquire a second consumer.

## Bounds

Each is a skip with a log line, never a silent truncation:

| Bound | Behaviour |
|---|---|
| `extra_palette_row_count` is 2 bits | class may only merge members spanning <= 3 pack rows; `[82..88]` (offsets 0-6) merges as subsets |
| Row budget | skip the merge if total rows would exceed 15 |
| No reachable stub | tier 2 unavailable in that room; tier 1 still applies |
| Stub map ambiguous | build-time error |
| Table drift | test failure, not seed failure |

## Ordering constraint

`apply.py`'s `sprite_palette_copies` rewrites `palette_id` when
`DifferentiateRepeatedBosses` is off, which can change class membership. The merge
pass must read post-copy palette ids. Assert this rather than relying on call
order.

## Verification gate

Two unknowns are settled **before** anything else is built. Both are cheap.

1. Do two sprites sharing a `palette_id` but differing in `palette_offset`
   currently occupy one CGRAM row or two? This decides whether merging costs a row
   and therefore how much the budget check matters. `npc_palette_rows` keys on
   `palette_id` alone, suggesting one, but that helper serves the glow feature
   specifically and should not be generalised without a look in-game.
2. Does `A_IncPaletteRowBy` count against the 10-object sprite-state limit from
   `project_room422_ten_object_sprite_state_limit`? If yes, busy rooms cap out and
   the design needs a per-room bump budget as well.

## Testing

- drift tests for both generated tables
- merge pass on a synthetic room: sprite rewrite lands, residency goes on the
  first object carrying the palette, bumps land on the rest
- rejection tests: row budget exceeded, span > 3 partial merge, room without a stub
- **regression for the originating bug** — room 315 with Culex: distinct buffered
  sprite count drops and the dedicated cursor stays below packed `$40`. Fails
  without the fix.
- headless `main.create()` smoke run

## Immediate unblock

Independent of this design and worth landing first: room 315 object 8 carries a
room-level `cannot_clone=True` in `randomizer/data/rooms/room_315.py`, a
Yaridovich-era hardcode. Under Culex its sprite 263 is already resident in buffer
C via objects 4 and 5, so it should share. Dropping that override reduces the
dedicated set to objects 2, 3, 6, 7 — 24 slots, ending at `$3F`, inside the cap.
It also removes a second defect: sprite 263's molds 6-11 carry 18 subtiles and
need `min_vram_size=1`, but the record has 0, and `$C0:8ED0` skips the bounds
check whenever `min_vram_size == 0`.

## References

- `reference_clone_buffer_hardcoded_vram_bases` — buffer bases and the `$40` cap
- `project_room315_culex_overruns_buffer_a` — the originating bug
- `reference_dedicated_vram_allocator` — per-block sizing
- `reference_npc_vram_sized_by_subtiles` — subtile vs tile packing
- `reference_room_loader_e0015_ordering` — why the stubs matter
- `reference_effects_npc_palette_row` — hardcoded CGRAM row targets
- `project_room422_ten_object_sprite_state_limit` — per-room sprite-state cap
- `apply.py:305-325` — the `_SHARED_MOLD_ROOM` precedent
