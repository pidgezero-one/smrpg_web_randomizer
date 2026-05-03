# Uncap Max FP — Design

**Date:** 2026-05-03
**Status:** Approved, ready for implementation plan
**Type:** Feature flag

## Summary

Add a new boolean flag, `UncapMaxFP`, that lets allies' max FP exceed the vanilla 99 cap (capping at 255 instead — the storage field is strictly 1 byte). The vanilla event-script command `Add7000ToMaxFP` (`0xFD 0x57`) hardcodes a cap of 99; this feature replaces that cap with 255 via small inline ASM patches, gated on the flag.

When the flag is off, vanilla behaviour is preserved exactly.

## Motivation

The randomizer offers various FP-modifying mechanics (level-up grants, prize-table effects, restorative items). Players have asked for an "uncap" option analogous to the existing `UncapSuperJumps` flag — a power-mode toggle that removes a hard ceiling. Max FP is a natural fit because the storage byte already supports 0–255 and the cap is enforced in only two places.

## Storage constraints (researched)

Both max-FP RAM locations are strictly 1 byte:

- `$7F:F8B2` — Max FP (save data). Followed by `$7F:F8B3` = Current Frog Coins (2 bytes). No room to widen.
- `$7E:FA0D` — Max FP (battle copy). Followed by `$7E:FA0E` = monster formation byte. No room to widen.

Therefore the absolute ceiling is 255, not 65535. "Unlimited" is not feasible without a substantial RAM-layout change, which is out of scope.

## Where the cap is enforced (ASM trace findings)

### Event-script handler `Add7000ToMaxFP` — `$C0:C4C5`

```
C0/C4C5  AF B2 F8 7F   LDA $7F:F8B2     ; load max FP
C0/C4C9  18            CLC
C0/C4CA  65 70         ADC $70          ; add $7000 (low byte)
C0/C4CC  C9 63         CMP #$63         ; ← cap starts: compare to 99
C0/C4CE  90 02         BCC +2           ;
C0/C4D0  A9 63         LDA #$63         ; ← cap ends: force 99
C0/C4D2  8F B2 F8 7F   STA $7F:F8B2     ; store max FP
C0/C4D6  60            RTS
```

The 6 bytes at `$C0:C4CC..C4D1` (ROM offset `0xC4CC`) are the cap.

### Battle bump-max-FP handler — `$C2:C148`

Same hardcoded 99 cap structure:

```
C2/C148  AF 0D FA 7E   LDA $7E:FA0D     ; load max FP (battle)
C2/C14C  18            CLC
C2/C14D  65 FB         ADC $FB          ; add direct-page heal/grant
C2/C14F  C9 63         CMP #$63         ; ← cap starts
C2/C151  30 02         BMI +2
C2/C153  A9 63         LDA #$63         ; ← cap ends
C2/C155  8F 0D FA 7E   STA $7E:FA0D     ; store max FP (battle)
C2/C159  8F 0C FA 7E   STA $7E:FA0C     ; also set current FP = new max
C2/C15D  60            RTS
```

The 6 bytes at `$C2:C14F..C154` (ROM offset `0x2C14F`) are the cap.

### Other FP routines that do NOT need patching

- **`$C2:C040` — Royal-Syrup-style additive heal.** Caps current at max FP via `CMP / BMI / LDA $7E:FA0D` at `$C2:C059..C062`. Worked through the 8-bit math: with Royal Syrup heal=50, the BMI signed/unsigned ambiguity does not produce wrong results for any max in the realistic range (≥ ~64). No patch needed.
- **`$C2:C13F` — set current FP = max FP (RestoreAllFP-style).** Pure copy, no cap math, no wrap risk. Already correct for any max value.
- **Battle current-FP CMP at `$C2:C059`, `$C2:C13F` reads** — comparisons only, no cap to remove.

### `STA $7F:F8B2` writes in the ROM

A full-ROM search for `8F B2 F8 7F` returned exactly one hit: `$C0:C4D2`. So the event-script handler is the only code path that writes save-data max FP. The battle handler writes only to the battle copy `$7E:FA0D`. No third site is hiding.

## Design

### Flag

New class in `randomizer/types/flags.py`, modelled on `UncapSuperJumps`:

```python
class UncapMaxFP(BooleanFlag):
    _name = "Uncap maximum FP"
    _description = "If enabled, allies' max FP threshold can exceed 99 (capped at 255)."
    _id = "uncapfp"
```

Register in `CharacterStatsSpellsSubcategory._flags` next to `UncapSuperJumps` — both are "remove a hard cap" toggles in the same domain. The category's `_size` field is purely a Bootstrap column-count for layout, so adding a flag has no capacity implication.

### Settings

Add `UncapMaxFP: UncapMaxFP(),` to the `_flags` dict in `Settings.__init__()` in `randomizer/types/settings.py`.

### Patch wiring

In `randomizer/types/gameworld.py`'s `get_patch()`, in the `# Misc` section near the `ShowEquips` block (~line 1916):

```python
if self.settings.isflag_enabled(UncapMaxFP):
    # Event-script Add7000ToMaxFP handler ($C0:C4CC):
    #   Original: C9 63 90 02 A9 63   CMP #$63 / BCC +2 / LDA #$63
    #   Patched:  B0 02 80 02 A9 FF   BCS +2 / BRA +2 / LDA #$FF
    # BCS-on-wrap catches the 8-bit ADC overflow case (e.g. max=200, addend=100
    # wraps to 44), so a wrap-then-store-low-byte regression cannot happen.
    patch.add_data(0xC4CC, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])

    # Battle bump-max-FP handler ($C2:C14F): identical fix, identical bytes.
    patch.add_data(0x2C14F, [0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF])
```

Each patch is a 6-byte drop-in replacement; the surrounding offsets are unchanged.

The user's stated preference is to keep these inline in `gameworld.py` for now and migrate to a dedicated module later when raw patchers are reorganised.

### Disassembly of the patched bytes

```
C0/C4CC  B0 02         BCS +2 → $C0:C4D0   ; if ADC overflowed, jump to cap
C0/C4CE  80 02         BRA +2 → $C0:C4D2   ; otherwise skip cap
C0/C4D0  A9 FF         LDA #$FF            ; cap at 255
C0/C4D2  8F B2 F8 7F   STA $7F:F8B2        ; (unchanged)
```

The same logic applies at `$C2:C14F` (the BMI in the original is replaced; semantics become unsigned-correct).

## UI display fixes (in scope, per-site fallback)

When the flag is enabled, max FP can be 100–255, which the vanilla 2-digit FP renderers do not visibly support. The implementation plan traces each of the following sites and lands the fix if it is a small tweak. If a site requires layout restructuring (shifting box positions, rewriting tilemap text windows), it is cut from this PR and tracked as a follow-up; the flag description is updated to acknowledge the visual overflow until the follow-up lands.

1. **Status menu (X menu) FP display** — bank `$C3` character-status screen showing `current / max FP`.
2. **Battle spell-selection FP display** — bank `$C2` shows `current / max FP` when picking a spell.
3. **Royal Syrup / Kerokero Cola heal-amount popup** — bank `$C2`. The popup amount in `$7E:0045,X` is the raw heal delta. For Royal Syrup (heal=50) this is always 2-digit. For Kerokero Cola the heal delta could exceed 99 if it routes through the additive path; this needs to be traced. If KKC routes through the absolute-set path (`$C2:C13F`), there is no popup-driven heal-delta number to widen.

## Implementation-plan verification steps

The plan must include the following manual or scripted verifications:

- Confirm Royal Syrup heals correctly with max FP values: 0, 50, 99, 100, 200, 255.
- Trace the Kerokero Cola item handler in bank `$C2` and confirm it does not silently regress when current+heal would wrap.
- Confirm event scripts that call `Add7000ToMaxFP` (e.g. `script_2305`, `script_2491-2492`, `script_2817`, `script_214`, `script_3072`, `script_1801`) actually push max FP above 99 in a playthrough when the flag is on.
- Confirm spell-cost gating still rejects/accepts correctly when current FP is allowed to exceed 99.
- Vanilla seed (flag off) still produces a byte-identical patch for the `Add7000ToMaxFP` regions — i.e. the new branch in `get_patch()` is dead code unless the flag is enabled.

## Out of scope

- Spell-cost arithmetic, level-up FP grants, item-restored FP amounts (other than the popup display) — all already operate on the 1-byte field correctly.
- Widening max-FP storage to 16 bits — would require RAM-layout changes incompatible with the 1-byte neighbours.
- A new dedicated patch module for FP routines — explicitly deferred per user request; raw patchers stay inline in `gameworld.py` until a future reorganisation pass.
- HUD layout restructuring beyond per-renderer 3-digit support.

## Files touched

- `randomizer/types/flags.py` — new `UncapMaxFP` class; register in `CharacterStatsSpellsSubcategory._flags`.
- `randomizer/types/settings.py` — register `UncapMaxFP` in `Settings.__init__()._flags`.
- `randomizer/types/gameworld.py` — two `patch.add_data` calls in `get_patch()`, plus any UI-display patch calls determined during implementation.
