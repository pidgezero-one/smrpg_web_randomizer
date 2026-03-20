# Concerns

## Large File Sizes

Several files are exceptionally large and may be difficult to maintain:

| File | Size | Concern |
|---|---|---|
| `randomizer/types/prizelocation.py` | 161K | Largest file — all prize location definitions in one module |
| `randomizer/types/flags.py` | 111K | Every flag/option defined in a single file |
| `randomizer/types/gameworld.py` | 82K | Central orchestrator, god-object pattern |
| `randomizer/logic/apply.py` | 66K | All randomization application in one file |
| `randomizer/logic/renders.py` | 59K | All rendering logic in one file |
| `randomizer/logic/shufflers/items.py` | 60K | Item shuffling algorithm |
| `randomizer/logic/partition_calculator.py` | 41K | Sprite partition calculations |
| `randomizer/types/prize.py` | 37K | Prize definitions |
| `randomizer/data/nmi_hook.py` | 35K | NMI hook data |
| `randomizer/types/settings.py` | 29K | Settings type definitions |

## God Object Pattern

`GameWorld` in `randomizer/types/gameworld.py` is the central orchestrator that:
- Receives deep copies of all game data collections (20+ parameters in constructor)
- Manages all randomization state
- Coordinates shufflers, setup, placement, validation, and rendering
- At 82K, it likely handles too many responsibilities

## Test Coverage

- `randomizer/tests.py` exists but is essentially empty (60 bytes)
- No unit tests for critical logic: placement algorithm, progression validation, shufflers
- No integration tests for the generation pipeline
- `pytest` is in requirements but no test files found beyond the stub

## Technical Debt Markers

Files with TODO/FIXME markers:
- `randomizer/types/gameworld.py`
- `randomizer/logic/apply.py`
- `randomizer/progression/prizelocations.py`
- `randomizer/data/sprites/objects/sprite_146.py`

## Debug Artifacts in Repository

- `debug_notes` (14.5K) — tracked debug notes with sprite/partition bug documentation (~130+ issues)
- `debug_patches/` — debug output directory
- `spoiler.json`, `spoiler_after_replacements.json` — committed spoiler files (106K each)
- `repeated_sequences_report.txt` (3.5MB) — large analysis report committed to repo
- `event_script_audit.txt` (19K) — audit file
- `unreferenced_dialogs.txt` (61K) — analysis output
- `smrpg.sfc` (4MB) — ROM file committed to repository
- `db.sqlite3` (644K) — development database committed

## Security Considerations

- `smrpg.sfc` ROM file committed to repo (potential copyright concern)
- `.env` and `.env.dev` files are tracked (though they appear to contain non-secret dev defaults)
- `SECRET_KEY` falls back to `"change-me"` if no env var or local_settings
- `DEBUG` defaults to 0 (safe), but configured via env var cast to int

## Performance Considerations

- `create()` in `main.py` does `deepcopy()` on 20+ large data collections per seed generation
- Placement algorithm in `randomizer/logic/placement.py` uses retry loops
- No caching layer — every seed generation builds from scratch
- Streaming generation via SSE (`/seed/stream`) for long-running operations
- `DATA_UPLOAD_MAX_MEMORY_SIZE` set to 25MB for WAD packing

## Architectural Fragility

- **Sprite partition system**: `debug_notes` documents 130+ visual rendering bugs related to sprite partitions — this appears to be the most fragile subsystem
- **Event script space**: Overworld scripts have space constraints; `overworld_scripts/` has hundreds of individual script files that must fit within ROM limits
- **VRAM constraints**: `battle_vram_calculator.py` manages limited SNES VRAM — changes to battle animations can break VRAM budgets
- **Deep copy overhead**: The `create()` function's deep copy of all collections is a critical correctness mechanism — without it, concurrent generation would corrupt shared state

## Missing Infrastructure

- No CI/CD pipeline (no `.github/workflows/` found)
- No linting configuration (no `.flake8`, `pyproject.toml` linting sections, etc.)
- No type checking config beyond basic `pyrightconfig.json`
- No monitoring or error tracking in production
- No automated deployment process documented
