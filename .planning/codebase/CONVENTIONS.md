# Coding Conventions

**Analysis Date:** 2026-03-20

## Naming Patterns

**Files:**
- `snake_case.py` for all Python files
- Example: `randomizer/views.py`, `randomizer/main.py`, `randomizer/forms.py`
- Type/class files grouped by domain: `randomizer/types/patch.py`, `randomizer/types/flags.py`, `randomizer/types/logic.py`

**Functions and Methods:**
- `snake_case()` for function/method names
- Private methods prefixed with `_`: `_build_flag_json_data()`, `_serialize_requirements()`, `_get_option_text()`
- Example from `randomizer/views.py`: `def _build_flag_json_data()`, `def _serialize_requirements()`, `def get_context_data()`
- Example from `randomizer/types/patch.py`: `def add_data()`, `def get_data()`, `def for_json()`

**Variables:**
- `snake_case` for local and instance variables
- Private instance attributes prefixed with `_`: `self._data`, `self._debug_mode`, `self._name`, `self._requires_all`
- Type-hinted class attributes with explicit types: `_requires_all: list = []`, `_disabled_if_all: list = []`

**Classes:**
- `PascalCase` for class names
- Examples: `Patch`, `Flag`, `Spell`, `CharacterSpell`, `EnemySpell`, `Inventory`, `CategorizationFlag`, `GenerateForm`, `RandomizerView`
- Classes inherit from specific base classes: `class Patch:`, `class CharacterSpell(CharacterSpellBase, Spell):`

**Enums:**
- `PascalCase` for enum classes: `FlagType`, `TreasureHunterNickname`
- `UPPER_CASE` for enum values: `FlagType.BOOLEAN`, `FlagType.CATEGORIZATION`, `FlagType.RANGE`

**Type Hints:**
- Modern Python type hints used throughout: `def create(seed: int | str, settings: Settings, progress_callback: Callable[[str, int], None] | None = None) -> GameWorld:`
- Union types using `|` operator instead of `Union[]`
- `dict[K, V]` instead of `Dict[K, V]`
- `list[T]` instead of `List[T]`

## Code Style

**Formatting:**
- No explicit formatter detected (no .black, .prettier, or ruff config files)
- Lines appear to follow standard Python conventions (no enforced line length limit visible)
- Consistent 4-space indentation throughout

**Linting:**
- `pytest` is installed (`pytest==8.3.5` in requirements.txt)
- No `.flake8`, `.pylintrc`, or equivalent linting config files present
- No automated linting enforcement configured

**Line Length & Readability:**
- Long type hints broken across lines when needed
- Imports organized but not enforced by tool
- Code favors explicit type hints over implicit typing

## Import Organization

**Order:**
1. Standard library imports: `import binascii`, `import hashlib`, `import json`, `import logging`, `import os`, etc.
2. Third-party imports: `import Wii`, `import nlzss`, `from django.*`, etc.
3. Local/relative imports: `from .models import`, `from .types.flags import`, `from .main import`

**Pattern from `randomizer/views.py`:**
```python
import binascii
import hashlib
import json
import logging
import os
# ... more stdlib ...

import Wii
import nlzss

from django.conf import settings
from django.db import transaction
from django.http import (
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponse,
    HttpResponseNotFound,
    QueryDict,
    StreamingHttpResponse,
)
# ... more django imports ...

from randomizer.types.flags import CATEGORIES, PRESETS, FlagError
from randomizer.types.patch import PatchJSONEncoder

from .models import Seed, Patch
from .forms import GenerateForm
from .main import create, VERSION
from .types.settings import Settings
from .types.flags import Flag, CategorizationFlag, CategorizationFlagWithOrdinance, BooleanFlag, RangeFlag, SelectOneFlag
```

**Path Aliases:**
- No path aliases configured (no jsconfig or alias patterns observed)
- Relative imports used within Django app: `from .models`, `from .types.flags`
- Absolute imports for cross-module references: `from randomizer.types.flags import`

**Conditional Imports:**
- `TYPE_CHECKING` guard used for circular import prevention: `if TYPE_CHECKING: from .gameworld import GameWorld`
- Example from `randomizer/types/prize.py` and `randomizer/types/logic.py`

## Error Handling

**Patterns:**
- Custom exception classes created for domain-specific errors: `class FlagError(ValueError): pass` in `randomizer/types/flags.py`
- Custom exceptions raised with descriptive messages: `raise FlagError(f"Option {option} is not a valid option for this flag.")`
- Try-except blocks used selectively for external library operations
- Example from `randomizer/types/gameworld.py`:
  ```python
  try:
      # attempt operation
  except IdentifierException:
      try:
          # fallback attempt
      except IdentifierException:
          raise WorldBuildingException("No battle animation banks found")
  ```
- No silent failures: CLAUDE.md explicitly states "NEVER resolve an issue by adding silent failure handling. Find the root cause instead."

**Logging Errors:**
- Logger initialized as module-level instance: `logger = logging.getLogger(__name__)` in `randomizer/views.py`
- Error logging uses descriptive messages: `logger.error("Flag error during generation: %s", e.args[0])`
- Exception context logged with `logger.exception()` for full stack traces

## Logging

**Framework:** `logging` module (stdlib)

**Patterns:**
- Module-level logger initialization: `logger = logging.getLogger(__name__)`
- Log levels used: `logger.error()` for errors, `logger.exception()` for exceptions with traceback
- Logging configuration in `smrpg_web_randomizer/settings.py`:
  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'filters': {...},
      'handlers': {'console': {...}, 'console_debug': {...}},
      'loggers': {...}
  }
  ```

## Comments

**When to Comment:**
- Docstrings on public methods and classes that need explanation
- Inline comments for non-obvious logic or algorithm choices
- TODO/FIXME comments marked with issue context

**JSDoc/TSDoc:**
- Python docstrings using triple quotes for methods/functions
- Example from `randomizer/types/patch.py`:
  ```python
  def add_data(
      self, addr: int, data: bytearray | bytes | list[int] | int | str, source: str = ""
  ) -> None:
      """Add data to the patch."""
      # Convert all types to bytes/bytearray for consistent handling
  ```
- Example from `randomizer/main.py`:
  ```python
  def create(
      seed: int | str,
      settings: Settings,
      progress_callback: Callable[[str, int], None] | None = None,
      debug_bps_patches: bool = False,
  ) -> GameWorld:
      """Create a patch for the given seed.

      Deep copies all mutable collections so modifications during randomization
      don't affect subsequent seed generations.

      Args:
          seed: The randomizer seed value.
          settings: The randomizer settings/flags.
          progress_callback: Optional callback for progress updates. Called with
              (message: str, percent: int) during generation.
          debug_bps_patches: If True, generate separate BPS patches for each render
              stage (only works in debug/development environment).
      """
  ```

## Function Design

**Size:** Functions range from single-operation to 50+ lines. Preference appears to be for focused, single-responsibility functions.

**Parameters:**
- Explicit parameter types required: `def create(seed: int | str, settings: Settings, ...)`
- Default parameters provided where sensible: `debug_mode: bool = False`
- Optional parameters use `| None` union syntax: `progress_callback: Callable[[str, int], None] | None = None`

**Return Values:**
- Explicit return type hints on all public functions: `-> GameWorld`, `-> list[int]`, `-> str`, `-> None`
- Properties used for computed attributes: `@property def addresses(self) -> list[int]:`
- Multiple return values returned as tuples or custom classes (not unpacking)

## Module Design

**Exports:**
- Classes and functions implicitly exported from modules (no `__all__` pattern observed)
- Modules organize related functionality: `randomizer/types/` directory contains type definitions, `randomizer/data/` contains game data

**Barrel Files:**
- No barrel files (index.py aggregation) used in this codebase
- Each module imports directly from its source: `from randomizer.types.flags import Flag`, `from randomizer.types.patch import Patch`

**Organization:**
- `randomizer/types/` - Type definitions and domain models (Patch, Flag, Spell, Prize, etc.)
- `randomizer/data/` - Game data and assets
- `randomizer/` - Views, forms, models, main generation logic
- `randomizer/progression/` - Randomization logic and algorithms
- `randomizer/logic/` - Game logic application
- `randomizer/management/commands/` - Django management commands

---

*Convention analysis: 2026-03-20*
