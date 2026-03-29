# ASM Trace Skill — Design Spec

## Overview

An SMRPG-specific 65816 ASM analysis skill for Claude Code, enabling static ROM analysis, disassembly, execution tracing, reference lookup, and patch generation. Designed for a user who doesn't know assembly — Claude interprets everything in plain English.

Bundled at `~/.claude/skills/asm-trace/` so it's available from any project directory.

## Core Operations

| Operation | Description |
|-----------|-------------|
| **Read** | Dump raw hex bytes at a ROM/SNES address or range |
| **Disassemble** | Decode 65816 instructions at an address, showing mnemonics, operands, and addressing modes |
| **Trace** | Follow execution flow from an address through JSR/JMP/branches, building a call graph |
| **Lookup** | Search reference docs for a RAM address, function, or keyword |
| **Patch** | Generate an IPS patch or raw byte sequence to modify specific ROM addresses |
| **Explain** | Given an address range, produce a human-readable explanation of what the code does |

## Components

### 1. Skill Definition (`SKILL.md`)

The main skill file that Claude loads when the skill is invoked. Contains:

- Trigger conditions (when to activate)
- Instructions for approaching ASM tasks
- Operation descriptions and usage patterns
- Rules for when to use summaries vs. original docs
- Guidance on when to suggest bsnes-plus debugger for runtime analysis

### 2. Python ROM Reader (`rom_reader.py`)

A CLI tool callable via the Bash tool. Hardcoded ROM path: `/mnt/d/smrpg.sfc`.

**Commands:**

```
python3 rom_reader.py read <snes_addr> [--length N]
    Hex dump N bytes (default 16) starting at SNES address.
    Output: address | hex bytes | ASCII representation

python3 rom_reader.py disasm <snes_addr> [--count N] [--m8] [--x8]
    Disassemble N instructions (default 20) starting at SNES address.
    --m8/--x8 flags set initial accumulator/index register width (default 16-bit).
    Output: address | raw bytes | mnemonic operand | notes

python3 rom_reader.py find <hex_pattern> [--start ADDR] [--end ADDR]
    Search ROM for a byte sequence. Returns all matching SNES addresses.

python3 rom_reader.py write-patch <snes_addr> <hex_bytes> -o <output.ips>
    Generate an IPS patch file that writes the given bytes at the given address.

python3 rom_reader.py info <snes_addr>
    Look up what region/data type an address falls in based on the ROM offset map.
```

**Technical details:**

- Handles LoROM address mapping (SNES bank:offset <-> ROM file offset)
- SMRPG uses LoROM with SA-1 mapping for banks 00-3F
- SA-1 memory mapping: banks $00-$1F map to ROM $000000-$0FFFFF, $80-$9F mirror, $C0-$CF map via SA-1 MMC registers
- Disassembler tracks M/X flag state through SEP/REP instructions to correctly decode 8-bit vs 16-bit operands
- Output is clean text, designed for Claude to parse and interpret

### 3. Pre-Digested Reference Summaries

Stored in `~/.claude/skills/asm-trace/ref/`. These are condensed, structured extracts of the source material optimized for fast loading into context.

| File | Contents | Primary Sources |
|------|----------|-----------------|
| `ref-ram-map.md` | RAM address ranges, purposes, key variables, object structures ($6000+), hardware registers | `ref/smrpg_docs_old/doc_ram-addr.txt`, `ref/smrpg_docs_new/.../doc_ram-addr.txt`, datacrystal wiki |
| `ref-functions.md` | Known function addresses with signatures, parameters, return values, call contexts | `ref/smrpg_docs_old/doc_functions.txt`, `ref/smrpg_docs_new/.../doc_functions.txt` |
| `ref-data-structures.md` | Binary layouts for monsters, items, spells, sprites, formations, partitions, NPCs — extracted from LazyShell source | `C:\Users\pidge\code\LAZYSHELL-UPDATED\LAZYSHELL\Editor.*\*.cs`, `ref/smrpg_docs_*/doc_offsets.txt` |
| `ref-battle-engine.md` | Battle system overview: entry points, turn flow, damage calculation, timing windows, Lucky/flower bonus mechanics, minigame triggers | `ref/smrpg_docs_new/.../asm_bank-c2.txt`, LazyShell `DamageCalculator.cs`, `Monster.cs` (FlowerBonus/FlowerOdds fields) |
| `ref-rom-layout.md` | ROM offset map organized by system (code banks, graphics, data tables, text, sound) with address ranges and descriptions | `ref/smrpg_docs_*/doc_offsets.txt` |
| `ref-65816.md` | 65816 instruction set quick reference: all mnemonics, addressing modes, flag effects, cycle counts | https://wiki.superfamicom.org/65816-reference |
| `ref-sprite-system.md` | Sprite/VRAM system: partition tables, NPC properties, sprite pointer tables, buffer allocation, SA-1 communication | `ref/smrpg_vram_system.md` |

### 4. Topic Index (`INDEX.md`)

Maps keywords and topics to both summary files and original source locations. Structured as a lookup table Claude consults first.

Format:
```
## Battle System
- **damage calculation**: ref-battle-engine.md -> ref/smrpg_docs_new/.../asm_bank-c2.txt L4200-L4350
- **Lucky bonus / flower bonus**: ref-battle-engine.md -> ref/smrpg_docs_new/.../asm_bank-c2.txt, LazyShell Monster.cs (FlowerBonus)
- **turn order / speed**: ref-battle-engine.md -> ref/smrpg_docs_new/.../asm_bank-c2.txt
```

Includes explicit rule: **"When a summary seems incomplete, uncertain, or you need exact byte-level detail, read the original source file directly."**

## Workflow

1. User asks a question or requests a patch
2. Skill activates — Claude consults `INDEX.md` to find relevant references
3. Claude loads the appropriate summary for fast context
4. Claude uses `rom_reader.py` to read/disassemble actual ROM bytes at referenced addresses
5. If the summary is insufficient, Claude reads the original source docs at the indexed file + line range
6. Claude explains findings in plain English with ASM shown alongside
7. For patching: Claude identifies target bytes, explains the change, generates the patch
8. When static analysis is insufficient (indirect jumps, runtime state, need to observe behavior): Claude tells the user exactly what to set up in **bsnes-plus v05 debugger** (breakpoints, watchpoints, trace log settings) and interprets results the user pastes back

## Debugger Escalation

When static analysis can't resolve something (e.g. indirect jump targets, self-modifying code, runtime register state), the skill instructs the user to:

1. Open the ROM in bsnes-plus v05
2. Set specific breakpoints/watchpoints with exact addresses
3. Run to the breakpoint and capture the trace log or register state
4. Paste the output back into the conversation

Claude then interprets the debugger output and continues the analysis.

## File Layout

```
~/.claude/skills/asm-trace/
  SKILL.md              # Skill definition
  rom_reader.py         # Python CLI tool
  INDEX.md              # Topic -> reference mapping
  ref/
    ref-ram-map.md
    ref-functions.md
    ref-data-structures.md
    ref-battle-engine.md
    ref-rom-layout.md
    ref-65816.md
    ref-sprite-system.md
```

## Constraints

- ROM path hardcoded: `/mnt/d/smrpg.sfc`
- Static analysis only — no emulation
- SMRPG-specific (LoROM + SA-1 mapping)
- Python 3, no external dependencies beyond standard library
- Reference summaries are digests — original source docs are the authority
