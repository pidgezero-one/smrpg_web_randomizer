# Structure

## Top-Level Layout

```
smrpg_web_randomizer/
├── smrpg_web_randomizer/     # Django project config (settings, urls, wsgi)
├── randomizer/               # Main Django app (all game logic)
│   ├── data/                 # Game data definitions (21 entity type dirs)
│   ├── logic/                # Core randomization algorithms
│   ├── types/                # Type definitions and core classes
│   ├── progression/          # Progression validation
│   ├── utils/                # Utility functions
│   ├── debug/                # Debug tools
│   ├── management/           # Django management commands
│   ├── migrations/           # Database migrations
│   ├── patches/              # ROM patch data
│   ├── scripts/              # Standalone scripts
│   ├── static/               # CSS, JS, images
│   ├── templates/            # Django HTML templates
│   └── templatetags/         # Custom template tags
├── tools/                    # Development/analysis tools
├── lazyshell/                # LazyShell editor reference data
├── ref/                      # Reference files
├── scripts/                  # Project-level scripts
├── nginx/                    # Nginx config (production)
├── debug_patches/            # Debug output patches
└── patchvenv/                # Python venv with smrpgpatchbuilder
```

## Key Directories

### `randomizer/data/` — Game Data (21 subdirectories)
Each subdirectory represents a game entity type with Python data definitions:
- `allies/` — Party member data
- `battle_animation/` — Battle animation banks (`_02/`, `_35/`, `_3A/`)
- `battle_dialogs/` — In-battle text
- `credits/` — End credits data
- `dialogs/` — Overworld dialog text
- `enemies/` — Enemy stats and properties
- `enemy_attacks/` — Enemy attack definitions
- `items/` — Item stats and properties
- `minigames/` — Minigame configuration
- `monster_ai/` — Monster AI scripts
- `overworld_scripts/` — Event scripts and action queues (`event/`, `animation/`)
- `packets/` — Data packets
- `packs/` — Pack collections
- `palettes/` — Event and sprite color palettes
- `physical_objects/` — Physical map objects
- `rooms/` — Room definitions
- `shops/` — Shop inventories
- `spells/` — Spell definitions
- `sprites/` — Sprite data and objects
- `variables/` — Game variables
- `world_map_locations/` — Overworld map locations

### `randomizer/logic/` — Randomization Engine
- `setup/` — Pre-shuffle configuration (9 files)
  - `prize_locations.py` (59K) — Prize location setup
  - `cosmetics.py` (32K) — Cosmetic randomization
  - `pre_shuffler_settings.py` (25K) — Pre-shuffler configuration
- `shufflers/` — Core shuffling algorithms (7 files)
  - `items.py` (60K) — Item shuffling
  - `shops.py` (28K) — Shop shuffling
  - `enemies.py` (25K) — Enemy shuffling
  - `equipment.py` (15K) — Equipment shuffling
  - `minigames.py` (13K) — Minigame shuffling
  - `characters.py` (6K) — Character shuffling
- `apply.py` (66K) — Applies all randomization to ROM data
- `renders.py` (59K) — Renders game world to patch data
- `placement.py` (14K) — Item/prize placement algorithm
- `partition_calculator.py` (41K) — Sprite partition calculations
- `battle_vram_calculator.py` (8K) — Battle VRAM management
- `validation.py` (8K) — Validation checks

### `randomizer/types/` — Core Type Definitions
- `gameworld.py` (82K) — Central `GameWorld` class, orchestrates everything
- `prizelocation.py` (161K) — `PrizeLocation` definitions (largest file)
- `flags.py` (111K) — Flag system (all user-configurable options)
- `prize.py` (37K) — Prize definitions
- `settings.py` (29K) — Settings/configuration types
- `physical_objects.py` (26K) — Physical object types
- Smaller types: `ally.py`, `enemy.py`, `item.py`, `room.py`, `spell.py`, etc.

### `randomizer/progression/` — Progression Validation
- Validates that seeds are completable
- Ensures required items are reachable

## Key Files

| File | Purpose |
|---|---|
| `randomizer/main.py` | Entry point — `create()` function, VERSION constant |
| `randomizer/views.py` | All web views and API endpoints |
| `randomizer/models.py` | Django models (Seed, Patch) |
| `randomizer/urls.py` | URL routing |
| `randomizer/forms.py` | Django forms |
| `randomizer/types/gameworld.py` | Central GameWorld orchestrator class |
| `randomizer/types/flags.py` | Full flag/option system |
| `randomizer/types/prizelocation.py` | Prize location definitions |
| `randomizer/logic/apply.py` | Applies randomization passes |
| `randomizer/logic/renders.py` | Renders world to ROM patches |
| `randomizer/logic/placement.py` | Prize placement algorithm |
| `smrpg_web_randomizer/settings.py` | Django settings |
| `manage.py` | Django management entry point |

## Naming Conventions

- **Python files**: `snake_case.py`
- **Directories**: lowercase, often plural nouns for data collections (`enemies/`, `items/`)
- **Classes**: `PascalCase` (`GameWorld`, `PrizeLocation`, `BooleanFlag`)
- **Functions/methods**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE` (`VERSION`, `ENEMIES`, `ALL_PACKETS`)
- **Data exports**: Module-level constants or collections, imported by `main.py`
- **Script files**: `script_NNNN.py` pattern in `overworld_scripts/`
- **Sprite objects**: `sprite_NNN.py` pattern in `sprites/objects/`
