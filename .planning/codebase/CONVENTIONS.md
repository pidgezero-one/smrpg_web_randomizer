# Coding Conventions

**Analysis Date:** 2026-03-20

## Naming Patterns

**Files:**
- Lowercase with underscores: `validation.py`, `placement.py`, `allied.py`
- Type definition files in `randomizer/types/` directory: `flags.py`, `settings.py`, `ally.py`, `item.py`, `enemy.py`
- Data files in `randomizer/data/` organized by category: `items/items.py`, `enemies/enemies.py`, `spells/spells.py`
- Event scripts follow pattern `script_NNNN.py` where N is numeric ID: `script_1936.py`, `script_1937.py`

**Classes:**
- PascalCase: `SettingsValidationError`, `Flag`, `Settings`, `GameWorld`, `Ally`, `Item`
- Base classes use suffix: `Item` (extends `ItemBase`), `Ally` (extends `AllyBase`)
- Enum classes extend standard enum types: `class SpriteAnimationState(str, Enum)`
- Exception classes use `Error` suffix and inherit from `Exception`: `SettingsValidationError(Exception)`, `FlagError(ValueError)`

**Functions:**
- snake_case: `validate_settings()`, `mutate_normal()`, `_validate_character_requirements()`, `debug_time()`
- Private/internal functions prefixed with single underscore: `_validate_character_requirements()`, `_add_desc_fields()`
- Properties use `@property` decorator without underscore prefix

**Variables:**
- snake_case for local variables: `gating_required_characters`, `disabled_char_names`, `all_required_characters`
- CONSTANT_CASE for module-level constants: `VERSION = '9.0.0'`, `B64_TABLE`
- Underscore prefix for private attributes: `_flags`, `_override`, `_debug_mode`, `_description`, `_default`

**Types:**
- PascalCase: `Settings`, `Flag`, `Ally`, `Item`, `Enemy`
- TypeVar suffix `T`: `FlagT = TypeVar("FlagT", bound=Flag)`
- Enum members use UPPERCASE: `FIRE`, `ICE`, `MALLOW`, `MARIO` (imported from external libs)

## Code Style

**Formatting:**
- No explicit formatter configured in repo
- Consistent 4-space indentation observed
- Line length varies; no strict limit visible
- Type hints used throughout modern code

**Linting:**
- No `.eslintrc`, `.flake8`, or `pylint` config detected
- Project has `.vscode/` settings directory
- Type hints present in most files: `def function(param: Type) -> ReturnType`

## Import Organization

**Order:**
1. Future imports: `from __future__ import annotations`
2. Standard library imports: `import sys`, `import time`, `import random`, `from typing import TYPE_CHECKING`
3. External library imports: `import grpc`, `import Wii`, `import nlzss`
4. Framework imports: `from django.db import models`, `from django.http import JsonResponse`
5. Third-party packages: `from smrpgpatchbuilder.datatypes.items.classes import Item`
6. Local relative imports: `from ..types.flags import Flag`, `from .models import Seed`

**Type Checking Guards:**
```python
if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
```
Used to avoid circular imports while maintaining type hints.

**Path Aliases:**
- Module structure uses relative imports: `from ..types.settings import Settings`
- No path aliases configured in `sys.path` modifications visible (except temporary in test utilities)

## Error Handling

**Patterns:**
- Custom exceptions defined with docstrings: `class SettingsValidationError(Exception): """Raised when settings have an invalid combination."""`
- Explicit exception raising with descriptive messages: `raise SettingsValidationError("...")`
- Type-specific exception inheritance: `FlagError(ValueError)` for validation errors
- Empty except blocks avoided; instead return `None` or use specific exception types
- Functions catch and convert gRPC exceptions to return `None` (test utilities): `except Exception as e: return None`
- No silent failures - errors should propagate or be logged

## Logging

**Framework:**
- Python `logging` module used in Django views: `logger = logging.getLogger(__name__)`
- Called with descriptive messages in view handlers

**Patterns:**
- Logger instance created once per module: `logger = logging.getLogger(__name__)`
- Not used extensively in core logic; mainly in view layer (`randomizer/views.py`)

## Comments

**When to Comment:**
- Complex algorithms get descriptive docstrings (e.g., `mutate_normal()`)
- Magic numbers explained inline
- Import statements may have inline comments for clarity: `# holy shit i cannot deal with how slow pylance is, fuck it just import everything` (actual code)
- Generally minimal inline comments; code is self-documenting

**Docstrings/TSDoc:**
- Functions use docstring format with Args, Returns, Raises sections:
```python
def validate_settings(settings: Settings) -> None:
    """Validate that settings combinations are valid.

    This should be called before shuffle_items to catch invalid settings early.

    Args:
        settings: The settings object to validate

    Raises:
        SettingsValidationError: If settings have an invalid combination
    """
```
- Multi-line docstrings use triple quotes: `"""..."""`
- Class docstrings describe purpose: `"""Extended Ally class with _sprites_primary and _sprites_secondary support."""`

## Function Design

**Size:**
- Functions range from ~10 to 1000+ lines (see `randomizer/logic/apply.py` at 2000+ lines)
- Larger functions broken into logical sections with helper functions prefixed with `_`

**Parameters:**
- Type hints on all parameters: `def function(param: Type, other: int | None = None) -> ReturnType`
- Optional parameters use `| None` union type notation: `p3: int = 0`
- Callbacks typed: `progress_callback: Callable[[str, int], None] | None = None`

**Return Values:**
- Explicit return types in function signature
- Functions return specific types or `None`: `-> bool | None`, `-> dict`, `-> bytes | None`
- Errors raised as exceptions rather than returning error codes

## Module Design

**Exports:**
- No explicit `__all__` declarations observed
- Files export classes, functions, and constants directly
- Top-level constants exported: `VERSION = '9.0.0'` in `main.py`

**Barrel Files:**
- Not used; each file imported explicitly: `from randomizer.types.flags import Flag`
- Type imports use full paths: `from ..types.ally import SpriteAnimationState`

**Circular Import Prevention:**
- Uses `TYPE_CHECKING` guards for type hints
- Imports placed at function/method level when circular dependency unavoidable (CLAUDE.md warns against this, but example exists in `randomizer/logic/validation.py` line 44)

---

*Convention analysis: 2026-03-20*
