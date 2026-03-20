# Testing Patterns

**Analysis Date:** 2026-03-20

## Test Framework

**Runner:**
- Not detected - Django's default `TestCase` available via import
- Two standalone test scripts exist: `tools/sni_test.py` and `tools/sni_mailbox_test.py`
- No pytest, unittest, or vitest configuration files found

**Assertion Library:**
- Django `TestCase` class imported in `randomizer/tests.py`
- Standard Python assertions used in test scripts (e.g., `assert readback[0] == 0xAA`)

**Run Commands:**
```bash
python manage.py test                    # Django test discovery (empty test file exists)
python tools/sni_test.py                 # SNI direct read tests
python tools/sni_mailbox_test.py         # NMI hook mailbox tests
```

## Test File Organization

**Location:**
- Django test file at `randomizer/tests.py` (currently empty placeholder)
- Standalone utility tests in `tools/` directory as executable scripts
- Not co-located with source code

**Naming:**
- Django convention: `tests.py` at app level
- Utility scripts: `sni_test.py`, `sni_mailbox_test.py` (prefix convention for test detection)

**Structure:**
```
randomizer/
├── tests.py          # Django TestCase imports (empty)

tools/
├── sni_test.py       # SNI hardware integration tests
└── sni_mailbox_test.py  # NMI mailbox integration tests
```

## Test Structure

**Suite Organization:**

The test utilities use modular test functions rather than class-based test suites. Example from `sni_test.py`:

```python
async def test_wram(channel: str, uri: str, verbose: bool) -> dict:
    """Test WRAM reads via FxPakPro address space."""
    print("=" * 60)
    print("Test 1: WRAM via FxPakPro Address Space")
    print("=" * 60)
    results = {}

    # Test specific operation
    print("\n  Reading character stats ($7F:F800, 0xB9 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF6F800, 0xB9)
    if data is None:
        print("  FAIL: Read returned None (gRPC error)")
        results["character_stats"] = False
    else:
        validity = data_looks_valid(data)
        results["character_stats"] = "OK" in validity
        print(f"  Result: {validity}")

    print()
    return results
```

**Patterns:**
- Setup: Connection and device discovery in `test_connection()` before other tests run
- Test organization: Multiple test functions called sequentially from `main()`
- Teardown: None; tests clean up resources via context managers (gRPC channels)
- Assertions: Boolean result dictionaries returned: `results["test_name"] = True/False`

## Mocking

**Framework:**
- Not used in existing tests
- Real hardware integration tests (SNI communication with actual FxPakPro device)

**Patterns:**
- Test functions are async and communicate with real gRPC servers
- No mock objects; uses real device URIs returned from SNI device enumeration
- Optional retry logic for flaky hardware: `for attempt in range(retries): ...`

**What to Mock:**
- (Not applicable - integration tests only)

**What NOT to Mock:**
- Hardware communication (intentionally tests real device)
- gRPC responses (tests expect real SNI protocol)

## Fixtures and Factories

**Test Data:**
- Hardcoded test addresses and memory regions in test functions
- Example from `sni_test.py`:
```python
test_addrs = [
    (0xE00000, 0x100, "SRAM base $E00000 (first 256 bytes)"),
    (0xE01040, 0x60,  "SRAM $E01040 (BW-RAM offset $1040 = $7040-$6000)"),
    (0xE07040, 0x60,  "SRAM $E07040 (SA-1 addr $7040 direct)"),
    # ...
]
```
- Hardcoded character names: `CHARACTER_NAMES.get(i, f"Unknown({i})")`
- Hardcoded game mode mappings: `mode_names = {0xC0: "overworld", 0xC3: "menu", 0xC1: "battle setup"}`

**Location:**
- Test data defined in test functions themselves
- Device enumeration happens via SNI at runtime (not fixtures)

## Coverage

**Requirements:**
- Not detected - no coverage configuration files found

**View Coverage:**
- Not applicable (integration tests only)

## Test Types

**Unit Tests:**
- None currently implemented
- Single placeholder file with Django TestCase import
- Core logic lacks unit test coverage

**Integration Tests:**
- `sni_test.py` - Tests SNI protocol with real FxPakPro hardware
  - Tests WRAM, BW-RAM, IRAM memory regions
  - Tests event flag parsing
  - Tests multiple address spaces (FxPakPro, SnesABus, Raw)
  - Tests data validity heuristics and coherency

- `sni_mailbox_test.py` - Tests NMI cooperative hook via mailbox
  - Tests hook alive detection
  - Tests state dump command
  - Tests item giving, coin setting, character recruitment
  - Tests spell learning and healing commands
  - Diagnostic functions for hook failure investigation

**E2E Tests:**
- Not used - integration tests serve as E2E verification

## Common Patterns

**Async Testing:**
```python
async def main():
    # ... setup ...
    all_results = {}
    all_results.update(await test_wram(channel, uri, args.verbose))
    all_results.update(await test_bwram_snes_abus(channel, uri, args.verbose))
    # ... collect all results ...
```

Async functions used for hardware I/O; results aggregated in dictionaries.

**Error Testing:**
```python
if data is None:
    print("  FAIL: Read returned None")
    results["event_flags_abus"] = False
else:
    validity = data_looks_valid(data)
    results["event_flags_abus"] = "OK" in validity
```

Tests check for `None` returns as error condition; helper function `data_looks_valid()` detects bad data patterns:
- All zeros (uninitialized/unmapped)
- All 0xFF (unmapped/bus noise)
- Insufficient unique values
- Invalid ranges for parsed values

**Retry Logic:**
```python
def read_mailbox(host: str, uri: str, offset: int = 0, size: int = 0x100, retries: int = 3) -> bytes | None:
    """Read from the mailbox region in FxPakPro SRAM space."""
    addr = MAILBOX_FXPAK_BASE + offset
    for attempt in range(retries):
        try:
            # ... read operation ...
            return bytes(response.response.data)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(0.5)
            else:
                print(f"  Read error at ${addr:06X}: {e}")
    return None
```

Retries on hardware communication failures with sleep between attempts.

**Polling/Timeout Patterns:**
```python
for _ in range(20):
    time.sleep(0.05)
    data = read_mailbox(host, uri, INBOX_COMMAND, 1)
    if data and data[0] == 0x00:
        # Command complete
        result = read_mailbox(host, uri, OUTBOX_RESULT, 1)
        if result:
            return result[0]
        return None
print("  Timeout waiting for command to complete!")
return None
```

Hardware tests poll for state changes with timeout; return `None` on timeout.

---

*Testing analysis: 2026-03-20*
