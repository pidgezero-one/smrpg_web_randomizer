# Architecture

**Analysis Date:** 2026-03-20

## Pattern Overview

**Overall:** Django web application with a complex game randomization engine

**Key Characteristics:**
- Django monolithic web server handling HTTP requests and form submission
- Core randomization logic decoupled in `GameWorld` class that processes ROM patches
- Data-driven design with extensive game data definitions (enemies, items, spells, rooms)
- Multi-stage randomization pipeline: setup → validation → shuffling → rendering → BPS patch generation
- Event-based streaming response generation for long-running operations
- Database persistence of seed results and patches for reproducibility

## Layers

**Presentation Layer:**
- Purpose: Handle HTTP requests, render templates, manage client-side flag UI
- Location: `randomizer/views.py`, `randomizer/templates/`, `randomizer/static/`
- Contains: Django CBVs (TemplateView, FormView), form handling, template rendering
- Depends on: Django ORM, core randomization logic, settings
- Used by: Browser clients via URL routing

**API Layer:**
- Purpose: Expose JSON endpoints for programmatic seed generation and flag queries
- Location: `randomizer/views.py` (APIGenerateView, APIFlags)
- Contains: REST endpoints with JSON serialization
- Depends on: Core randomization, flag system
- Used by: External tools, web UI via AJAX

**Core Randomization Engine:**
- Purpose: Generate randomized game state by modifying ROM data
- Location: `randomizer/main.py` (entry point), `randomizer/types/gameworld.py` (orchestrator)
- Contains: GameWorld class that coordinates all randomization logic
- Depends on: Data layer, shufflers, setup modules
- Used by: Views, API endpoints

**Shuffler Modules:**
- Purpose: Implement domain-specific randomization logic
- Location: `randomizer/logic/shufflers/` (items.py, enemies.py, shops.py, characters.py, equipment.py, minigames.py)
- Contains: Shuffle algorithms for prizes, enemy stats/drops/formations, shop contents, character stats, equipment properties
- Depends on: GameWorld state, type definitions, validation rules
- Used by: GameWorld.__init__() and _shuffle_items()

**Setup Modules:**
- Purpose: Apply fixed transformations before shuffling begins
- Location: `randomizer/logic/setup/` (pre_shuffler_settings.py, enemy_tweaks.py, equipment_setup.py, thresholds.py, cosmetics.py, prize_locations.py)
- Contains: Early-stage modifications like gate logic, stat adjustments, minigame setup, palette selection
- Depends on: GameWorld, flag values, data collections
- Used by: GameWorld.__init__()

**Data Layer:**
- Purpose: Store immutable game data (enemies, items, spells, rooms, dialogs, etc.)
- Location: `randomizer/data/` (enemies, items, spells, rooms, dialogs, overworld_scripts, battle_animation, etc.)
- Contains: Collections of game entities defined via `smrpgpatchbuilder` datatypes
- Depends on: None (data only)
- Used by: main.py (deep copied), GameWorld, shufflers

**Type System:**
- Purpose: Define domain models and their relationships
- Location: `randomizer/types/` (gameworld.py, flags.py, prizelocation.py, prize.py, item.py, enemy.py, etc.)
- Contains: GameWorld, Flag hierarchy, PrizeLocation subtypes, Item/Prize/Spell wrappers, Settings
- Depends on: smrpgpatchbuilder datatypes, data definitions
- Used by: All layers

**Persistence Layer:**
- Purpose: Cache seeds and patches for reproducibility
- Location: `randomizer/models.py` (Seed, Patch)
- Contains: Django ORM models for database storage
- Depends on: Django ORM
- Used by: Views for hash lookups and patch caching

**Patch Generation:**
- Purpose: Convert randomized game state to ROM patch format
- Location: `randomizer/logic/renders.py`, `randomizer/logic/apply.py`
- Contains: BPS (Binary Patch System) patch generation, ROM offset calculations
- Depends on: GameWorld state, smrpgpatchbuilder serialization
- Used by: GameWorld after shuffling complete

## Data Flow

**Seed Generation Request:**

1. User submits form to `GenerateView` (views.py) with seed and flag selections
2. View creates `Settings` object from POST data
3. View calls `main.create(seed, settings)` which instantiates GameWorld
4. GameWorld.__init__() executes in phases:
   - Parse settings and validate combinations
   - Apply setup modules (gates, stat tweaks, cosmetics)
   - Build item impact categories and item→prize mappings
   - Retry loop for item shuffling (handles placement failures)
   - Shuffle other domains (enemies, shops, characters)
   - Render ROM patches via renders.py
5. GameWorld returns fully randomized game state
6. View serializes result to JSON/database and returns to client
7. Client downloads BPS patches via StreamingHttpResponse

**State Management:**

- `GameWorld` instance is the central state container holding all game collections
- Prize locations cache (`_prize_type_to_location`) tracks placement for dependency resolution
- Rooms snapshot enables shuffle retries without data accumulation
- Settings object immutable for reproducibility given seed + flag string
- Each request creates fresh GameWorld with deep copies of data (no shared state)

## Key Abstractions

**GameWorld:**
- Purpose: Central orchestrator holding all game state and coordinating randomization
- Examples: `randomizer/types/gameworld.py` (2000+ lines)
- Pattern: Singleton-per-request with deep-copied data; uses composition for collections

**PrizeLocation and subtypes:**
- Purpose: Abstract different ways items can be placed (chests, NPC drops, spell slots, etc.)
- Examples: `TreasureChestLocation`, `NPCLocationRow`, `SpellSlotLocation`, `BoosterHillLocation`
- Pattern: Polymorphism with type-based dispatch in shufflers

**Flag system:**
- Purpose: User-facing randomization options with dependencies and validation
- Examples: `randomizer/types/flags.py` (BooleanFlag, RangeFlag, SelectOneFlag, CategorizationFlag)
- Pattern: Class hierarchy with metadata (requires_all, requires_any, disabled_if_all, modes)

**Shuffler pattern:**
- Purpose: Domain-specific randomization algorithms
- Examples: `shuffle_prizes()`, `randomize_enemy_stats()`, `shuffle_shops()`
- Pattern: Functions taking GameWorld, modifying state in-place, with validation

**Settings:**
- Purpose: Immutable configuration object created from flag selections
- Examples: `randomizer/types/settings.py`
- Pattern: Dict-like access to flag values with isflag_enabled(FlagClass) and is_flag_value(FlagClass, value)

## Entry Points

**Web Request:**
- Location: `randomizer/views.py` (GenerateView, APIGenerateView)
- Triggers: HTTP POST to /seed or /api/v1/generate
- Responsibilities: Parse request, create Settings, call main.create(), serialize response

**Stream Generation:**
- Location: `randomizer/views.py` (GenerateStreamView)
- Triggers: HTTP GET to /seed/stream with query params
- Responsibilities: Long-running seed generation with SSE progress updates

**Patch Reconstruction:**
- Location: `randomizer/views.py` (GenerateFromHashView)
- Triggers: HTTP GET to /hash/{hash}/{region}
- Responsibilities: Look up cached seed by hash, regenerate specific region patch

**Management Commands:**
- Location: `randomizer/management/commands/`
- Triggers: `python manage.py [command]`
- Responsibilities: Bulk operations (debug, testing, data migration)

## Error Handling

**Strategy:** Fail-fast with specific exceptions, retry on placement failures

**Patterns:**
- Settings validation in GameWorld.__init__() catches impossible flag combinations early
- PlacementException triggers shuffle retry with fresh room state (max 5 retries per failure count)
- WorldBuildingException raised after exhausting retries, indicates unsolvable settings
- RandomizerSettingsException for user-provided invalid flag data
- Form validation in GenerateForm catches basic client errors

## Cross-Cutting Concerns

**Logging:** Configured in settings.py with StreamHandler; randomizer logger at ERROR level in development

**Validation:**
- Settings validation in `randomizer/logic/validation.py`
- Prize placement validation in `randomizer/logic/placement.py`
- Form validation in `randomizer/forms.py`

**Authentication:** None (stateless HTTP, seed hash is not authentication)

**Caching:**
- Prize location cache for quick lookups during shuffling
- Cached patches in database (Seed.hash, Patch model)
- Seed snapshot for deterministic retry

---

*Architecture analysis: 2026-03-20*
