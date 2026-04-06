# Prize Offset Slider Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dev-only slider that deterministically rotates boss fight prizes, slot machine placements, and invisible flag selections by a configurable offset, with real-time preview.

**Architecture:** A single ordered-list provider in `randomizer/debug/` computes the canonical orderings for boss locations, boss prizes, eligible chest rooms, and invisible flag locations. The Django view embeds these as JSON for client-side preview. At randomization time, the same provider computes offset assignments which feed into the existing pre-placement mechanism.

**Tech Stack:** Python/Django backend, jQuery/Bootstrap frontend, localforage for persistence

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `randomizer/debug/offset_preview.py` | Create | Ordered list provider + offset assignment computation |
| `randomizer/forms.py` | Modify | Add `prize_offset` form field |
| `randomizer/views.py` | Modify | Pass ordered lists to template, read `prize_offset` from form |
| `randomizer/types/settings.py` | Modify | Add `prize_offset` property |
| `randomizer/templates/randomizer/_rom_settings.html` | Modify | Slider UI, toggle, preview table, JS |
| `randomizer/logic/setup/prize_locations.py` | Modify | Apply offset for invisible flags |
| `randomizer/logic/shufflers/items.py` | Modify | Apply offset for boss fights and slots |

---

### Task 1: Ordered List Provider

**Files:**
- Create: `randomizer/debug/offset_preview.py`

This is the single source of truth for all ordered lists and offset computations. Both frontend (via JSON) and backend (at randomization time) use this.

- [ ] **Step 1: Create `randomizer/debug/offset_preview.py` with `get_ordered_lists()`**

```python
"""Ordered list provider for the prize offset slider.

Computes canonical orderings of boss locations, boss prizes, eligible chest rooms,
and invisible flag locations. Used by both the Django view (JSON for frontend preview)
and the randomization backend (applying offset assignments).
"""

from randomizer.progression.prizelocations import (
    # === 47 BossFightLocation / MimicFightLocation subclasses, in game order ===
    MushrooomWayBossFight,
    MushroomKingdomBossFight,
    BanditsWayBossFight,
    Mimic1BossFight,
    KeroSewersBossFight,
    ForestMazeBossFight,
    OuterMinesBossFight,
    InnerMinesBossFight,
    InnerMinesPostgameBossFight,
    BoosterTowerIndoorBossFight,
    BoosterTowerIndoorBossFightRemake,
    BoosterTowerBalconyBossFight,
    MarrymoreBossFight,
    MarrymoreBossFightRemake,
    SeasideBeachBossFight,
    ShipPasswordBossFight,
    Mimic2BossFight,
    ShipFinalBossFight,
    ShipPostgameBossFight,
    LandsEndCloudBoss,
    TempleBossFight,
    TempleBossFightPostgame,
    DojoFirstFight,
    DojoSecondFight,
    DojoThirdFight,
    DojoFourthFight,
    DojoFifthFight,
    MonstroSealedDoorBossFight,
    MonstroSealedDoorBossFightPostgame,
    Mimic3BossFight,
    BeanValleyPlanterBossFight,
    StatueRoomBossFight,
    GiantEggBossFight,
    NimbusFinalBossFight,
    VolcanoBridgeBossFight,
    VolcanoExitBossFight,
    ObstacleCourseFinalFight,
    KeepAfterObstaclesBossFight,
    KeepChandelierBossFight,
    KeepFinalBossFight,
    FactoryEntranceBossFight,
    FactoryTransitionBossFight,
    InnerFactoryFirstFight,
    InnerFactorySecondFight,
    InnerFactoryThirdFight,
    InnerFactoryFourthFight,
    FinalBossFight,
)
from randomizer.progression.prizes import ALL_BOSS_FIGHTS, SlotsPrize1, SlotsPrize2, SlotsPrize3
from randomizer.types.prizelocation import TreasureChestLocationRow, InvisibleFlagLocation
from randomizer.types.prize import SlotsPrize


BOSS_LOCATIONS: list[type] = [
    MushrooomWayBossFight,
    MushroomKingdomBossFight,
    BanditsWayBossFight,
    Mimic1BossFight,
    KeroSewersBossFight,
    ForestMazeBossFight,
    OuterMinesBossFight,
    InnerMinesBossFight,
    InnerMinesPostgameBossFight,
    BoosterTowerIndoorBossFight,
    BoosterTowerIndoorBossFightRemake,
    BoosterTowerBalconyBossFight,
    MarrymoreBossFight,
    MarrymoreBossFightRemake,
    SeasideBeachBossFight,
    ShipPasswordBossFight,
    Mimic2BossFight,
    ShipFinalBossFight,
    ShipPostgameBossFight,
    LandsEndCloudBoss,
    TempleBossFight,
    TempleBossFightPostgame,
    DojoFirstFight,
    DojoSecondFight,
    DojoThirdFight,
    DojoFourthFight,
    DojoFifthFight,
    MonstroSealedDoorBossFight,
    MonstroSealedDoorBossFightPostgame,
    Mimic3BossFight,
    BeanValleyPlanterBossFight,
    StatueRoomBossFight,
    GiantEggBossFight,
    NimbusFinalBossFight,
    VolcanoBridgeBossFight,
    VolcanoExitBossFight,
    ObstacleCourseFinalFight,
    KeepAfterObstaclesBossFight,
    KeepChandelierBossFight,
    KeepFinalBossFight,
    FactoryEntranceBossFight,
    FactoryTransitionBossFight,
    InnerFactoryFirstFight,
    InnerFactorySecondFight,
    InnerFactoryThirdFight,
    InnerFactoryFourthFight,
    FinalBossFight,
]

BOSS_PRIZES: list[type] = list(ALL_BOSS_FIGHTS)

SLOTS_PRIZES: list[type] = [SlotsPrize1, SlotsPrize2, SlotsPrize3]


def _get_eligible_chest_rooms() -> list[type]:
    """Get TreasureChestLocationRow subclasses eligible for SlotsPrize, one per room.

    Iterates all TreasureChestLocationRow subclasses in definition order.
    A location is eligible if SlotsPrize is not in its _blacklist.
    Only the first location per room set is included (deduplication).
    """
    from randomizer.progression import prizelocations
    import inspect

    eligible = []
    seen_rooms: set[frozenset[int]] = set()

    # Get all classes from prizelocations in definition order (by line number)
    classes = inspect.getmembers(prizelocations, inspect.isclass)
    # Sort by source line to preserve definition order
    def _source_line(cls):
        try:
            return inspect.getsourcelines(cls)[1]
        except (OSError, TypeError):
            return float('inf')

    classes.sort(key=lambda pair: _source_line(pair[1]))

    for _name, cls in classes:
        if not issubclass(cls, TreasureChestLocationRow) or cls is TreasureChestLocationRow:
            continue
        # Check blacklist
        blacklist = getattr(cls, '_blacklist', None) or []
        if any(issubclass(b, SlotsPrize) if isinstance(b, type) else b is SlotsPrize for b in blacklist):
            continue
        # Deduplicate by room set
        rooms = frozenset(getattr(cls, '_rooms', []))
        if rooms in seen_rooms:
            continue
        seen_rooms.add(rooms)
        eligible.append(cls)

    return eligible


def _get_invisible_flag_locations() -> list[type]:
    """Get all InvisibleFlagLocation subclasses in definition order."""
    from randomizer.progression import prizelocations
    import inspect

    classes = inspect.getmembers(prizelocations, inspect.isclass)

    def _source_line(cls):
        try:
            return inspect.getsourcelines(cls)[1]
        except (OSError, TypeError):
            return float('inf')

    classes.sort(key=lambda pair: _source_line(pair[1]))

    return [
        cls for _name, cls in classes
        if issubclass(cls, InvisibleFlagLocation) and cls is not InvisibleFlagLocation
    ]


def get_ordered_lists() -> dict:
    """Return all ordered lists needed for offset computation and frontend preview.

    Returns dict with keys:
        boss_locations: list of class name strings (47 items)
        boss_prizes: list of class name strings (47 items)
        eligible_chests: list of class name strings (one per room, SlotsPrize-eligible)
        invisible_flags: list of class name strings
    """
    eligible_chests = _get_eligible_chest_rooms()
    invisible_flags = _get_invisible_flag_locations()

    return {
        "boss_locations": [cls.__name__ for cls in BOSS_LOCATIONS],
        "boss_prizes": [cls.__name__ for cls in BOSS_PRIZES],
        "eligible_chests": [cls.__name__ for cls in eligible_chests],
        "invisible_flags": [cls.__name__ for cls in invisible_flags],
    }


def compute_offset_assignments(offset: int) -> dict:
    """Compute prize assignments for a given offset.

    Returns dict with keys:
        bosses: list of (location_class_name, prize_class_name) tuples
        slots: list of (chest_class_name, slots_prize_class_name) tuples (3 items)
        flags: list of flag_class_name strings (3 items)
        boss_overrides: dict of {location_class_name: prize_class} for pre-placement
        slot_overrides: list of (chest_class, slots_prize_class) for pre-placement
        flag_classes: list of 3 flag location classes for pre-placement
    """
    eligible_chests = _get_eligible_chest_rooms()
    invisible_flags = _get_invisible_flag_locations()
    num_bosses = len(BOSS_LOCATIONS)
    num_chests = len(eligible_chests)
    num_flags = len(invisible_flags)

    # Boss assignments: location[i] -> prize[(i + offset) % 47]
    boss_assignments = []
    boss_overrides = {}
    for i, loc_cls in enumerate(BOSS_LOCATIONS):
        prize_cls = BOSS_PRIZES[(i + offset) % num_bosses]
        boss_assignments.append((loc_cls.__name__, prize_cls.__name__))
        boss_overrides[loc_cls.__name__] = prize_cls

    # Slots assignments: 3 slots prizes placed at consecutive eligible chests
    slot_start = (offset * 3) % num_chests
    slot_assignments = []
    slot_overrides = []
    for j in range(3):
        chest_cls = eligible_chests[(slot_start + j) % num_chests]
        slots_prize_cls = SLOTS_PRIZES[j]
        slot_assignments.append((chest_cls.__name__, slots_prize_cls.__name__))
        slot_overrides.append((chest_cls, slots_prize_cls))

    # Flag assignments: 3 consecutive flags starting at (3 * offset)
    flag_start = (3 * offset) % num_flags
    flag_assignments = []
    flag_classes = []
    for k in range(3):
        flag_cls = invisible_flags[(flag_start + k) % num_flags]
        flag_assignments.append(flag_cls.__name__)
        flag_classes.append(flag_cls)

    return {
        "bosses": boss_assignments,
        "slots": slot_assignments,
        "flags": flag_assignments,
        "boss_overrides": boss_overrides,
        "slot_overrides": slot_overrides,
        "flag_classes": flag_classes,
    }
```

- [ ] **Step 2: Verify the module imports correctly**

Run:
```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -c "
from randomizer.debug.offset_preview import get_ordered_lists, compute_offset_assignments
lists = get_ordered_lists()
print(f'Boss locations: {len(lists[\"boss_locations\"])}')
print(f'Boss prizes: {len(lists[\"boss_prizes\"])}')
print(f'Eligible chests: {len(lists[\"eligible_chests\"])}')
print(f'Invisible flags: {len(lists[\"invisible_flags\"])}')
print()
assignments = compute_offset_assignments(0)
print(f'Boss assignments: {len(assignments[\"bosses\"])}')
print(f'First 3 bosses: {assignments[\"bosses\"][:3]}')
print(f'Slot assignments: {assignments[\"slots\"]}')
print(f'Flag assignments: {assignments[\"flags\"]}')
print()
assignments1 = compute_offset_assignments(1)
print(f'Offset 1 first 3 bosses: {assignments1[\"bosses\"][:3]}')
print(f'Offset 1 slots: {assignments1[\"slots\"]}')
print(f'Offset 1 flags: {assignments1[\"flags\"]}')
"
```

Expected: 47 boss locations, 47 boss prizes, some number of eligible chests and invisible flags. Offset 0 and 1 should show different assignments.

- [ ] **Step 3: Commit**

```bash
git add randomizer/debug/offset_preview.py
git commit -m "Add ordered list provider for prize offset slider"
```

---

### Task 2: Form and Settings

**Files:**
- Modify: `randomizer/forms.py:8-15`
- Modify: `randomizer/types/settings.py:15-28`

- [ ] **Step 1: Add `prize_offset` to the Django form**

In `randomizer/forms.py`, add after line 14 (`debug_bps_patches`):

```python
    prize_offset = forms.IntegerField(required=False, initial=None, min_value=0, max_value=46)
```

The full form should look like:

```python
class GenerateForm(forms.Form):
    seed = forms.Field(required=False)
    mode = forms.ChoiceField(required=False, choices=MODES, initial='open')
    flags = forms.Field(required=False, initial='')
    cosmetics = forms.Field(required=False, initial='')
    debug_mode = forms.BooleanField(required=False, initial=False)
    debug_bps_patches = forms.BooleanField(required=False, initial=False)
    race_mode = forms.BooleanField(required=False, initial=False)
    prize_offset = forms.IntegerField(required=False, initial=None, min_value=0, max_value=46)
```

- [ ] **Step 2: Add `prize_offset` to Settings**

In `randomizer/types/settings.py`, add after line 16 (`_debug_mode: bool = False`):

```python
    _prize_offset: int | None = None
```

And add after the `debug_mode` setter (after line 28):

```python
    @property
    def prize_offset(self) -> int | None:
        """Prize offset for deterministic placement (dev-only). None means disabled."""
        return self._prize_offset

    @prize_offset.setter
    def prize_offset(self, value: int | None) -> None:
        self._prize_offset = value
```

- [ ] **Step 3: Commit**

```bash
git add randomizer/forms.py randomizer/types/settings.py
git commit -m "Add prize_offset field to form and Settings"
```

---

### Task 3: Views — Pass Data and Read Offset

**Files:**
- Modify: `randomizer/views.py:185-192` (context data)
- Modify: `randomizer/views.py:275-286` (GenerateView form_valid)
- Modify: `randomizer/views.py:405-427` (GenerateStreamView)

- [ ] **Step 1: Pass ordered lists JSON to template context**

In `randomizer/views.py`, in the `get_context_data` method (around line 188), add after `context["debug_enabled"] = settings.DEBUG`:

```python
        if settings.DEBUG:
            from randomizer.debug.offset_preview import get_ordered_lists
            context["offset_preview_data"] = json.dumps(get_ordered_lists())
```

Also ensure `json` is imported at the top of `views.py` (it likely already is; if not, add `import json`).

- [ ] **Step 2: Read prize_offset in GenerateView.form_valid**

In `randomizer/views.py`, in `GenerateView.form_valid` around line 275-286, after `debug_mode = bool(data["debug_mode"])` (line 275), add:

```python
        prize_offset = data.get("prize_offset")
        if not settings.DEBUG:
            prize_offset = None
```

Then after `s.debug_mode = debug_mode` (line 286), add:

```python
            s.prize_offset = prize_offset
```

- [ ] **Step 3: Read prize_offset in GenerateStreamView**

In `randomizer/views.py`, in `GenerateStreamView` around line 405, after `debug_mode = bool(data["debug_mode"])` (line 405), add:

```python
            prize_offset = data.get("prize_offset")
            if not settings.DEBUG:
                prize_offset = None
```

Then after `s.debug_mode = debug_mode` (line 424), add:

```python
                    s.prize_offset = prize_offset
```

- [ ] **Step 4: Verify the server starts without errors**

Run:
```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python manage.py check
```

Expected: No errors.

- [ ] **Step 5: Commit**

```bash
git add randomizer/views.py
git commit -m "Wire prize_offset through views to Settings"
```

---

### Task 4: Backend — Apply Offset for Boss Fights and Slots

**Files:**
- Modify: `randomizer/logic/shufflers/items.py:1305-1335`

The existing override block at lines 1305-1335 handles config.yml `items.override`. We add offset-based overrides that run first (so they take precedence), feeding into the same pre-placement mechanism.

- [ ] **Step 1: Add offset-based boss and slot overrides**

In `randomizer/logic/shufflers/items.py`, find the existing debug override block at line 1305:

```python
    # Apply debug overrides: place the specified prize at each override location
```

Insert BEFORE that block (before line 1305):

```python
    # Apply prize offset overrides (takes precedence over config.yml for bosses and slots)
    if world.settings.debug_mode and world.settings.prize_offset is not None:
        from randomizer.debug.offset_preview import compute_offset_assignments
        offset_result = compute_offset_assignments(world.settings.prize_offset)

        # Place boss fight prizes at offset-computed locations
        for location_name, prize_cls in offset_result["boss_overrides"].items():
            for loc in world.locations.values():
                if type(loc).__name__ == location_name:
                    loc.set_prize(prize_cls())
                    break
            # Remove one instance of this prize from the pool
            removed = False
            for tier_list in pool.values():
                for i, item in enumerate(tier_list):
                    if type(item) == prize_cls:
                        tier_list.pop(i)
                        pulled_count -= 1
                        removed = True
                        break
                if removed:
                    break

        # Place slot machine prizes at offset-computed chest locations
        for chest_cls, slots_prize_cls in offset_result["slot_overrides"]:
            for loc in world.locations.values():
                if isinstance(loc, chest_cls):
                    loc.set_prize(slots_prize_cls())
                    break
            # Remove one instance of this slots prize from the pool
            removed = False
            for tier_list in pool.values():
                for i, item in enumerate(tier_list):
                    if type(item) == slots_prize_cls:
                        tier_list.pop(i)
                        pulled_count -= 1
                        removed = True
                        break
                if removed:
                    break
```

Then modify the existing config.yml override block to skip boss/slot overrides when offset is active. Change line 1309 from:

```python
    if world.settings.debug_mode:
```

to:

```python
    if world.settings.debug_mode:
```

And inside the loop over overrides, add a skip condition. After `prize_cls = get_prize_class(prize_name)` and its validation, add:

```python
            # Skip boss/slot overrides if prize_offset is active (offset takes precedence)
            if world.settings.prize_offset is not None:
                from randomizer.types.prizelocation import BossFightLocation
                from randomizer.types.prize import SlotsPrize as SlotsPrizeBase
                if location_cls is not None and (
                    issubclass(location_cls, BossFightLocation)
                    or (prize_cls is not None and issubclass(prize_cls, SlotsPrizeBase))
                ):
                    continue
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/shufflers/items.py
git commit -m "Apply prize offset overrides for boss fights and slots"
```

---

### Task 5: Backend — Apply Offset for Invisible Flags

**Files:**
- Modify: `randomizer/logic/setup/prize_locations.py:969-983`

The existing invisible flag debug override reads from config.yml. When prize_offset is active, we override this to use the offset-computed flags instead.

- [ ] **Step 1: Add offset-based invisible flag override**

In `randomizer/logic/setup/prize_locations.py`, replace the existing debug invisible flags block (lines 969-983):

```python
        # Check for debug override of invisible flags
        debug_invisible_flags: list[type] | None = None
        if world.settings.debug_mode:
            from randomizer.debug import load_debug_config, get_location_class
            config = load_debug_config()
            flag_names = config.get("invisible_flags", [])
            if len(flag_names) == 3:
                debug_invisible_flags = []
                for name in flag_names:
                    cls = get_location_class(name)
                    if cls is not None:
                        debug_invisible_flags.append(cls)
                    else:
                        debug_invisible_flags = None
                        break
```

With:

```python
        # Check for debug override of invisible flags
        debug_invisible_flags: list[type] | None = None
        if world.settings.debug_mode:
            # Prize offset takes precedence over config.yml for invisible flags
            if world.settings.prize_offset is not None:
                from randomizer.debug.offset_preview import compute_offset_assignments
                offset_result = compute_offset_assignments(world.settings.prize_offset)
                debug_invisible_flags = offset_result["flag_classes"]
            else:
                from randomizer.debug import load_debug_config, get_location_class
                config = load_debug_config()
                flag_names = config.get("invisible_flags", [])
                if len(flag_names) == 3:
                    debug_invisible_flags = []
                    for name in flag_names:
                        cls = get_location_class(name)
                        if cls is not None:
                            debug_invisible_flags.append(cls)
                        else:
                            debug_invisible_flags = None
                            break
```

- [ ] **Step 2: Commit**

```bash
git add randomizer/logic/setup/prize_locations.py
git commit -m "Apply prize offset override for invisible flag selection"
```

---

### Task 6: Frontend — Slider UI and Preview

**Files:**
- Modify: `randomizer/templates/randomizer/_rom_settings.html`

This is the largest task. The slider, toggle, and preview table all go inside the existing `{% if debug_enabled %}` block.

- [ ] **Step 1: Add hidden input, toggle, slider, and preview HTML**

In `randomizer/templates/randomizer/_rom_settings.html`, after the closing `</div>` of the existing card-body (line 41), and before the `<script>` tag (line 43), insert the following new card-body section:

```html
    <div class="card-body border-top">
        <div class="row">
            <div class="col-12">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="prize-offset-toggle">
                    <label class="form-check-label" for="prize-offset-toggle">
                        <strong>Prize Offset</strong> — Deterministic boss/slot/flag placement
                    </label>
                </div>
            </div>
        </div>
        <div id="prize-offset-controls" style="display: none;" class="mt-2">
            <div class="row align-items-center">
                <div class="col-md-8">
                    <input type="range" class="form-range" id="prize-offset-slider"
                           min="0" max="46" value="0">
                </div>
                <div class="col-md-4">
                    <span>Offset: <strong id="prize-offset-value">0</strong></span>
                </div>
            </div>
            <input type="hidden" name="prize_offset" id="prize-offset-hidden" disabled>

            <div class="row mt-3">
                <div class="col-md-6">
                    <h6>Boss Fight Assignments</h6>
                    <div id="preview-bosses" style="max-height: 300px; overflow-y: auto;">
                        <table class="table table-sm table-striped">
                            <thead><tr><th>Location</th><th>Prize</th></tr></thead>
                            <tbody id="preview-bosses-body"></tbody>
                        </table>
                    </div>
                </div>
                <div class="col-md-6">
                    <h6>Slot Machine Assignments</h6>
                    <table class="table table-sm table-striped">
                        <thead><tr><th>Chest Location</th><th>Slots Prize</th></tr></thead>
                        <tbody id="preview-slots-body"></tbody>
                    </table>

                    <h6 class="mt-3">Invisible Flag Locations</h6>
                    <table class="table table-sm table-striped">
                        <thead><tr><th>#</th><th>Flag Location</th></tr></thead>
                        <tbody id="preview-flags-body"></tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
```

- [ ] **Step 2: Add the JavaScript logic**

In the same file, inside the existing `<script>` block's `$(function () { ... })`, after the debug BPS patches handler (after line 74), add:

```javascript
            // === Prize Offset Slider ===
            const offsetData = JSON.parse('{{ offset_preview_data|escapejs }}');

            function updatePreview(offset) {
                const numBosses = offsetData.boss_locations.length;
                const numChests = offsetData.eligible_chests.length;
                const numFlags = offsetData.invisible_flags.length;
                const slotsPrizes = ["SlotsPrize1", "SlotsPrize2", "SlotsPrize3"];

                // Boss fights
                let bossHtml = "";
                for (let i = 0; i < numBosses; i++) {
                    const loc = offsetData.boss_locations[i];
                    const prize = offsetData.boss_prizes[(i + offset) % numBosses];
                    bossHtml += `<tr><td>${loc}</td><td>${prize}</td></tr>`;
                }
                $("#preview-bosses-body").html(bossHtml);

                // Slots
                const slotStart = (offset * 3) % numChests;
                let slotsHtml = "";
                for (let j = 0; j < 3; j++) {
                    const chest = offsetData.eligible_chests[(slotStart + j) % numChests];
                    slotsHtml += `<tr><td>${chest}</td><td>${slotsPrizes[j]}</td></tr>`;
                }
                $("#preview-slots-body").html(slotsHtml);

                // Flags
                const flagStart = (3 * offset) % numFlags;
                let flagsHtml = "";
                for (let k = 0; k < 3; k++) {
                    const flag = offsetData.invisible_flags[(flagStart + k) % numFlags];
                    flagsHtml += `<tr><td>${k + 1}</td><td>${flag}</td></tr>`;
                }
                $("#preview-flags-body").html(flagsHtml);
            }

            // Slider input handler
            $("#prize-offset-slider").on("input", function () {
                const val = parseInt($(this).val());
                $("#prize-offset-value").text(val);
                $("#prize-offset-hidden").val(val);
                localforage.setItem("rom.prize_offset_value", val);
                updatePreview(val);
            });

            // Toggle handler
            $("#prize-offset-toggle").change(function () {
                const enabled = $(this).is(":checked");
                localforage.setItem("rom.prize_offset_enabled", enabled);
                if (enabled) {
                    $("#prize-offset-controls").show();
                    $("#prize-offset-hidden").prop("disabled", false);
                    const val = parseInt($("#prize-offset-slider").val());
                    $("#prize-offset-hidden").val(val);
                    updatePreview(val);
                } else {
                    $("#prize-offset-controls").hide();
                    $("#prize-offset-hidden").prop("disabled", true);
                }
            });

            // Restore from localStorage
            Promise.all([
                localforage.getItem("rom.prize_offset_enabled"),
                localforage.getItem("rom.prize_offset_value"),
            ]).then(([enabled, value]) => {
                if (value !== null) {
                    $("#prize-offset-slider").val(value);
                    $("#prize-offset-value").text(value);
                }
                if (enabled === true) {
                    $("#prize-offset-toggle").prop("checked", true).change();
                }
            });
```

- [ ] **Step 3: Verify the page loads without errors**

Start the dev server and load the randomizer page in a browser. Check the browser console for JavaScript errors. Verify:
- The toggle appears in the Debug Settings section
- Clicking the toggle shows/hides the slider and preview
- Moving the slider updates the preview tables in real-time
- The preview shows 47 boss rows, 3 slot rows, and 3 flag rows

- [ ] **Step 4: Commit**

```bash
git add randomizer/templates/randomizer/_rom_settings.html
git commit -m "Add prize offset slider UI with real-time preview"
```

---

### Task 7: Integration Test

**Files:** None (manual testing)

- [ ] **Step 1: End-to-end test with offset disabled**

Generate a seed with debug mode ON but prize offset toggle OFF. Verify it behaves the same as before (config.yml applies normally).

- [ ] **Step 2: End-to-end test with offset 0**

Enable the prize offset toggle, set slider to 0, and generate a seed. Verify boss fights are placed in vanilla order (MushrooomWayBossFight → HammerBrosFight, etc.).

- [ ] **Step 3: End-to-end test with offset 1**

Set slider to 1 and generate. Verify the assignments shift: MushrooomWayBossFight → Croco1BossFight, MushroomKingdomBossFight → MackBossFight, etc. (shifted by 1).

- [ ] **Step 4: End-to-end test with high offset (wrapping)**

Set slider to 46 and generate. Verify wrapping works correctly for all three categories.

- [ ] **Step 5: Commit all remaining changes if any**

```bash
git add -A
git commit -m "Prize offset slider: complete feature"
```
