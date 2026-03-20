# Concerns

## Critical: No Test Coverage

- `randomizer/tests.py` is an empty stub (60 bytes)
- Zero unit tests for placement algorithm, progression validation, shufflers, or any core logic
- No integration tests for the generation pipeline
- No CI/CD pipeline to run tests even if they existed

## Large / Monolithic Files

| File | Size | Concern |
|---|---|---|
| `randomizer/progression/prizelocations.py` | 591K | Largest file — progression data |
| `randomizer/progression/prizes.py` | 412K | Prize progression data |
| `randomizer/types/prizelocation.py` | 161K | All prize location definitions |
| `randomizer/types/flags.py` | 111K | Every flag/option in one file |
| `randomizer/types/gameworld.py` | 82K | Central orchestrator — god object |
| `randomizer/logic/apply.py` | 66K | All randomization application |
| `randomizer/logic/renders.py` | 59K | All rendering logic |
| `randomizer/logic/shufflers/items.py` | 60K | Item shuffling algorithm |
| `randomizer/logic/partition_calculator.py` | 41K | Sprite partition calculations |
| `randomizer/data/nmi_hook.py` | 35K | NMI hook data |

## God Object: GameWorld

`randomizer/types/gameworld.py` (82K) is the central orchestrator that:
- Takes 20+ deep-copied collection parameters in its constructor
- Manages all randomization state
- Coordinates shufflers, setup, placement, validation, and rendering
- Handles too many responsibilities for a single class

## Error Handling Issues

### Bare except clause
- `randomizer/logic/apply.py:724` — Bare `except:` catches all exceptions silently, masking real errors

### Debug print statements
- ~80 `print()` calls scattered across `randomizer/` source files
- Mixed with production code — no separation of debug output
- Should use `logging` module (which is configured in `settings.py` but underutilized)

### TODO/FIXME markers
- `randomizer/types/gameworld.py` — 3 TODOs
- `randomizer/progression/prizelocations.py` — 2 TODOs
- `randomizer/logic/apply.py` — 1 TODO
- `randomizer/data/sprites/objects/sprite_146.py` — 1 TODO

## Sprite/Partition Fragility

`debug_notes` (270 lines) documents extensive visual rendering bugs:
- Sprite partition system has numerous documented issues
- Boss replacement causes graphical glitches
- VRAM constraints in battle scenes are tight
- `partition_calculator.py` (41K) manages limited SNES sprite resources

This appears to be the most fragile subsystem based on the volume of documented issues.

## Performance Concerns

- `create()` in `randomizer/main.py` does `deepcopy()` on 20+ large data collections per seed generation
- No caching layer — every seed generation builds from scratch
- Placement algorithm in `randomizer/logic/placement.py` uses retry loops
- `progression/prizelocations.py` (591K) and `progression/prizes.py` (412K) loaded in memory
- `DATA_UPLOAD_MAX_MEMORY_SIZE` set to 25MB for WAD packing

## Debug Artifacts Committed to Repository

- `debug_notes` (270 lines) — Debug notes tracking sprite/partition bugs
- `debug_patches/` — Debug output directory
- `spoiler.json`, `spoiler_after_replacements.json` — Spoiler files (~106K each)
- `repeated_sequences_report.txt` (3.5MB) — Large analysis report
- `event_script_audit.txt` (19K) — Audit file
- `unreferenced_dialogs.txt` (61K) — Analysis output
- `smrpg.sfc` (4MB) — ROM file (potential copyright concern)
- `db.sqlite3` (644K) — Development database

## Security Considerations

- `smrpg.sfc` ROM file committed to repo (copyright concern)
- `.env` and `.env.dev` files are tracked (contain dev defaults, not secrets)
- `SECRET_KEY` falls back to `"change-me"` if no env var or local_settings
- No rate limiting on seed generation endpoints
- No input validation on API beyond Django form validation

## Missing Infrastructure

- No CI/CD pipeline (no `.github/workflows/`)
- No linting configuration
- No pre-commit hooks
- No monitoring or error tracking in production
- No automated deployment process
