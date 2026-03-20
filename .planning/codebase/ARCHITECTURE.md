# Architecture

**Analysis Date:** 2026-03-20

## Pattern Overview

**Overall:** Django-based ROM randomizer with plugin architecture

**Key Characteristics:**
- Central `GameWorld` class manages all game state and data collections
- Multi-phase randomization pipeline: setup → shuffle → apply → render
- Settings-driven flag system controls all randomization parameters
- Plugin pattern for data loading from smrpgpatchbuilder library
- Stateless randomization functions that operate on deep copies
- BPS patch generation as final output format

## Layers

**Web Server (Django):**
- Purpose: HTTP request routing, form validation, response handling
- Location: `randomizer/views.py`, `randomizer/urls.py`, `randomizer/forms.py`
- Contains: View classes (TemplateView, FormView), API endpoints, form validators
- Depends on: Models (Seed, Patch), Settings, Randomizer logic
- Used by: Frontend (HTML templates), API consumers

**Data Models (Django ORM):**
- Purpose: Persistent storage of generated seeds and patch data
- Location: `randomizer/models.py`
- Contains: Seed (seed value, hash, flags, metadata), Patch (region-specific patch bytes)
- Depends on: Django ORM
- Used by: Views for caching and replay of previous seeds

**Randomizer Logic (Core):**
- Purpose: Transform game world based on settings/flags
- Location: `randomizer/types/`, `randomizer/logic/`
- Contains: GameWorld state machine, shufflers, validators
- Depends on: Data collections, smrpgpatchbuilder types
- Used by: Views for seed generation

**Data Collections (Game Content):**
- Purpose: ROM data structures organized by game system
- Location: `randomizer/data/`
- Contains: Enemies, items, spells, dialogs, rooms, NPCs, sprites, palettes
- Depends on: smrpgpatchbuilder (external library providing collection classes)
- Used by: GameWorld initialization, shufflers for modifications

**Type System (Domain Models):**
- Purpose: Game-specific abstractions over raw ROM data
- Location: `randomizer/types/`
- Contains: GameWorld, Settings, PrizeLocation, Prize, Room, Enemy, Item, Ally
- Depends on: smrpgpatchbuilder types, data collections, progression definitions
- Used by: Shufflers, applies, validation logic

**Progression/Logic (Randomization Rules):**
- Purpose: Define constraints, randomization strategies, validation rules
- Location: `randomizer/progression/`, `randomizer/logic/`
- Contains: Prize locations, boss placement rules, item quality tiers, difficulty scaling
- Depends on: Types, data collections, settings/flags
- Used by: Shufflers and validators

## Data Flow

**Seed Generation Request:**

1. **HTTP Request** → GenerateView or APIGenerateView
   - Receive: seed value, flags string, cosmetics string, debug/race mode flags
   - Validate: Form validation with GenerateForm

2. **Settings Parsing** → Settings.set_from_flag_string()
   - Parse flag string into enabled flags
   - Build Settings object with all flag values
   - Validate: FlagError if invalid flag combination

3. **GameWorld Creation** → randomizer.main.create()
   - Deep copy all data collections (allies, enemies, items, dialogs, sprites, etc.)
   - Initialize GameWorld with copies + seed + settings
   - Establish empty prize locations mapping

4. **Pre-Shuffle Setup** → apply_shuffler_independent_settings()
   - Apply cosmetic settings (music, palettes, character names)
   - Apply enemy stat tweaks and difficulty scaling
   - Apply equipment restrictions and level-up modifications
   - Set minigame-specific parameters

5. **Location Setup** → set_locations()
   - Enable/disable prize locations based on settings
   - Initialize invisible item location markers
   - Pre-allocate dummy NPCs for slot/flag mechanics

6. **Prize Shuffling Pipeline** → shuffle_prizes()
   - Quality-tier allocation of items to location types
   - Bias-based distribution (favor harder locations with better items)
   - Character spell assignment (SpellsAnywhere mode)
   - Constraint satisfaction (key items, required progression)

7. **Remaining Shuffles** (parallel/sequential):
   - Enemies: randomize_enemy_stats, randomize_enemy_attacks_and_spells, randomize_enemy_drops, randomize_enemy_formations
   - Shops: shuffle_shops with item quality tier rebalancing
   - Characters: randomize_character_stats, randomize_levelup_xps, randomize_character_spell_stats
   - Bosses: conditional on ShuffledBosses flag, stat scaling

8. **Post-Shuffle Cleanup** → post_shuffle_cleanup()
   - Validate item distribution integrity
   - Resolve conflicts (duplicates, missing items)
   - Update shop prices for rare items

9. **Apply Shuffler Results** → apply_shuffler_results_to_game_data()
   - Write shuffled prizes to TreasureChestLocation, StandingLocation, etc.
   - Update NPC dialogue with prize locations
   - Modify room objects with chest states
   - Update boss formations and AI scripts

10. **Render to Patch** → GameWorld.get_patch()
    - smrpgpatchbuilder renders all modified collections to ROM addresses
    - Patch data aggregated as {address: bytes} dictionary
    - Optional: debug BPS patches for individual render stages

11. **Compute Hash** → seed hash from spoiler
    - Hash used as unique identifier for seed
    - Enables replay of identical generation via hash lookup

12. **Response** → JSON with patch data
    - GenerateView: Immediate response with full patch
    - GenerateStreamView: SSE stream with progress updates
    - GenerateFromHashView: Replay from database

**State Management:**

- **Immutable during generation**: Seed, Settings, flag strings
- **Mutable during generation**: GameWorld and all collections (deep copied per seed)
- **Cached per seed**: Generated patches in database (Seed, Patch models)
- **Progress tracking**: Optional progress_callback during long-running generation

## Key Abstractions

**GameWorld:**
- Purpose: Central state container representing the entire randomized game
- Examples: `randomizer/types/gameworld.py` (2000+ lines, ~40 properties)
- Pattern: Builder pattern - initialized with collections, modified via get_*/update_* methods
- Responsibilities:
  - Provides access to all game data (items, enemies, dialogs, etc.)
  - Maintains prize location registry and placement cache
  - Generates final patch via smrpgpatchbuilder renders
  - Computes hash and spoiler log

**PrizeLocation:**
- Purpose: Represent a logical location where a prize can be placed
- Examples: `randomizer/types/prizelocation.py` (TreasureChestLocation, StandingLocation, BossFightLocation, etc.)
- Pattern: Polymorphic hierarchy with location-specific metadata
- Responsibilities:
  - Define where a prize appears in the game (room ID, NPC index, etc.)
  - Control visibility based on settings (isflag_enabled checks)
  - Track placed prize and notify GameWorld

**Settings & Flags:**
- Purpose: User-configurable options for randomization behavior
- Examples: `randomizer/types/flags.py` (110KB), `randomizer/types/settings.py`
- Pattern: Hierarchical flag system with dependencies and requirements
- Responsibilities:
  - Parse flag strings from UI or API
  - Track enabled flags and their values
  - Provide is_flag_enabled() checks throughout shufflers

**Shuffler Functions:**
- Purpose: Transform specific game systems based on settings
- Examples: `randomizer/logic/shufflers/items.py`, `enemies.py`, `shops.py`
- Pattern: Pure functions receiving GameWorld, returning nothing (mutate in place)
- Responsibilities:
  - Implement randomization logic for one domain
  - Respect enabled flags and constraints
  - Coordinate with other shufflers via GameWorld state

**Patch:**
- Purpose: Represent binary ROM modifications as address→data map
- Examples: `randomizer/types/patch.py`
- Pattern: Additive data structure with merging support
- Responsibilities:
  - Accumulate patch data from all shuffler operations
  - Serialize to JSON for network transmission
  - Support debug mode overlap detection

## Entry Points

**Web Application:**
- Location: `manage.py`
- Triggers: `python manage.py runserver` or gunicorn
- Responsibilities: Django WSGI startup

**Seed Generation:**
- Location: `randomizer/main.py:create()`
- Triggers: FormView.form_valid() or API client POST to /seed or /seed/stream
- Responsibilities: Orchestrate the full randomization pipeline

**Hash Replay:**
- Location: `randomizer/views.py:GenerateFromHashView.get()`
- Triggers: GET /hash/<hash>/<region> or reverse lookup from database
- Responsibilities: Retrieve previously generated seed from cache

**WAD Packing:**
- Location: `randomizer/views.py:PackingView.post()`
- Triggers: POST /pack with ROM + WAD file uploads
- Responsibilities: Embed randomized ROM into Wii WAD package

**Management Commands:**
- Location: `randomizer/management/commands/`
- Triggers: `python manage.py [command]`
- Responsibilities: Database maintenance, bulk operations

## Error Handling

**Strategy:** Exception-based with specific error types

**Patterns:**
- `FlagError`: Flag parsing/validation fails → HTTP 400 with error message
- `RandomizerSettingsException`: Settings logic error → HTTP 500 with details
- `WorldBuildingException`: GameWorld construction fails → HTTP 500 with details
- `ValidationError`: Prize distribution invalid → Logged, generation fails gracefully
- Generic Exception: Catch-all logging in views with full context (seed, flags)

**Database Integrity:**
- Atomic transactions on seed/patch save with conflict resolution (delete existing by hash)
- No cascading deletes from UI level - only through Django ORM on_delete=CASCADE

## Cross-Cutting Concerns

**Logging:**
- Use `logging.getLogger(__name__)` in all modules
- Views log FormView and validation errors with full context
- Shufflers and validation logic rarely log (rely on exception propagation)

**Validation:**
- Flag validation: FlagError before world creation
- Settings validation: RandomizerSettingsException during Settings construction
- Prize distribution: validate_settings() post-shuffle with detailed error messages
- Room/object state: Asserts in get_* methods (no silent failures)

**Authentication:**
- @csrf_exempt on APIs (PackingView, APIGenerateView)
- No per-user tracking or authentication in core logic
- Race mode suppresses spoiler log

**Concurrency:**
- GenerateStreamView uses threading.Thread for background generation
- Thread-safe queue.Queue for progress updates
- No thread-local storage or global state mutations during generation

---

*Architecture analysis: 2026-03-20*
