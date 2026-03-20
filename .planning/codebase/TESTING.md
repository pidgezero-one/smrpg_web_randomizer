# Testing

## Current State

**Test coverage is essentially nonexistent.** The project has `pytest==8.3.5` in requirements but no meaningful test files.

### Existing Test Files

- `randomizer/tests.py` — Stub file, contains only `from django.test import TestCase` (60 bytes)
- No `test_*.py` or `*_test.py` files found anywhere in the project
- No `conftest.py` files
- No test fixtures or factories

### Test Framework

- **pytest** (8.3.5) — Listed in `requirements.txt` but unused
- **Django TestCase** — Imported in stub but no tests written
- No `pytest.ini`, `setup.cfg`, or `pyproject.toml` test configuration
- `pyrightconfig.json` exists for type checking but is minimal

## What Needs Testing

### Critical Logic (No Tests)

| Component | File | Risk |
|---|---|---|
| Prize placement algorithm | `randomizer/logic/placement.py` (14K) | Core correctness — determines if seeds are completable |
| Progression validation | `randomizer/progression/prizelocations.py` (591K) | Ensures required items are reachable |
| Item shuffling | `randomizer/logic/shufflers/items.py` (60K) | Largest shuffler, most complex logic |
| GameWorld orchestration | `randomizer/types/gameworld.py` (82K) | Central coordinator, integrates all systems |
| Flag parsing/serialization | `randomizer/types/flags.py` (111K) | User-facing configuration |
| Settings deserialization | `randomizer/types/settings.py` (29K) | Converts flag strings to settings objects |
| Partition calculator | `randomizer/logic/partition_calculator.py` (41K) | Sprite VRAM allocation — fragile |
| VRAM calculator | `randomizer/logic/battle_vram_calculator.py` (8K) | Battle scene resource management |
| Validation checks | `randomizer/logic/validation.py` (8K) | Post-generation validation |

### Web Layer (No Tests)

| Component | File | Risk |
|---|---|---|
| Seed generation endpoint | `randomizer/views.py` | Core user-facing functionality |
| API endpoints | `randomizer/views.py` (APIGenerateView, APIFlags) | External consumers |
| Hash-based seed lookup | `randomizer/views.py` (HashView) | URL-based seed sharing |
| WAD packing | `randomizer/views.py` (PackingView) | File processing |

## Testing Patterns to Follow

### Recommended Structure

```
randomizer/
  tests/
    __init__.py
    test_placement.py        # Placement algorithm
    test_flags.py            # Flag parsing and serialization
    test_settings.py         # Settings from flag strings
    test_gameworld.py        # GameWorld creation and orchestration
    test_views.py            # Web endpoints
    test_api.py              # API endpoints
    test_shufflers/
      __init__.py
      test_items.py          # Item shuffling
      test_enemies.py        # Enemy shuffling
      test_shops.py          # Shop shuffling
    test_progression/
      __init__.py
      test_completability.py # Seed completability validation
```

### Test Priorities

1. **Placement algorithm** — Can a seed be completed? Regression tests for known-broken seeds
2. **Flag serialization** — Round-trip: flags string -> Settings -> flags string
3. **Seed generation** — End-to-end: given seed + flags, does `create()` succeed?
4. **API endpoints** — POST /api/v1/generate returns valid response
5. **Progression validation** — Required items are always reachable

### Testing Challenges

- **Deep copy overhead**: `create()` deep-copies 20+ collections — tests need fresh copies per run
- **ROM dependency**: Patch generation may need actual ROM data or mocks
- **Large data files**: `progression/prizelocations.py` (591K) and `progression/prizes.py` (412K) are huge
- **Non-deterministic output**: Randomizer uses `random` module — tests need fixed seeds
- **No dependency injection**: `GameWorld` takes 20+ constructor args with concrete data

## CI/CD

- No CI/CD pipeline exists (no `.github/workflows/` directory)
- No pre-commit hooks configured
- No linting (no `.flake8`, ruff, or pylint config)
- `pyrightconfig.json` exists but minimal
