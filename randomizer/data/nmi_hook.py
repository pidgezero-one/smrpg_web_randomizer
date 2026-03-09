"""NMI Cooperative Hook for FxPakPro Archipelago Support.

Patches the ROM with a cooperative NMI hook that bridges WRAM (inaccessible
from FxPakPro on SA-1 games) to BW-RAM (accessible via SRAM $E0xxxx).

The hook runs on the SNES CPU every frame during NMI:
  - Copies music + battle state from WRAM to BW-RAM mailbox (per-frame)
  - Checks a BW-RAM inbox for commands from the AP client
  - Processes commands: give items, set coins, heal, dump inventory state
  - Jumps to the original WRAM NMI handler when done

Architecture:
  AP Client <--USB--> FxPakPro <--SRAM--> BW-RAM Mailbox <--NMI Hook--> WRAM
"""

# =============================================================================
# ROM patch addresses
# =============================================================================

# NMI vectors in ROM header — BOTH must be patched because SMRPG switches
# the SNES CPU between native and emulation mode (title screen vs gameplay).
NMI_VECTOR_ROM_OFFSET = 0x7FEA       # Native mode NMI (SNES $00:FFEA)
NMI_VECTOR_NEW = bytes([0xE0, 0xFF])  # Point to $FFE0 (trampoline)
EMU_NMI_VECTOR_ROM_OFFSET = 0x7FFA   # Emulation mode NMI (SNES $00:FFFA)
EMU_NMI_VECTOR_NEW = bytes([0xE0, 0xFF])  # Same trampoline

# JML trampoline in unused native vector entry at $00:FFE0 (ROM $7FE0).
# NOTE: In SA-1, $00:8xxx maps to ROM $0xxx (game code), NOT ROM $8xxx
# (antipiracy space at $C0:8xxx). The only safe executable space in bank $00
# is the SNES header area at $00:FFC0-$FFFF = ROM $7FC0-$7FFF.
TRAMPOLINE_ROM_OFFSET = 0x7FE0
TRAMPOLINE_CODE = bytes([0x5C, 0x00, 0xF0, 0xD5])  # JML $D5:F000

# Hook code location ($D5:F000 = ROM offset $15F000)
# Documented free space at $15EFEB-$15FFFF (doc_offsets.txt).
# Must NOT be in animation banks $02/$35/$3A — those are overwritten by
# battle animation script rendering.
HOOK_ROM_OFFSET = 0x15F000

# Original NMI handler (in WRAM, set up by game during init)
ORIGINAL_NMI_ADDR = 0x000008

# NMITIMEN ($4200) patches — enable VBlank NMI during gameplay.
# SMRPG's gameplay engine (bank C0) writes $01 to $4200, which has bit 7=0
# (NMI disabled). The game delegates VBlank work to the SA-1 coprocessor instead.
# Our hook needs NMI enabled to run, so we patch $01 → $81 (NMI on + joypad on).
# The SNES CPU's gameplay NMI handler ($C0:0283) is a no-op, so this is safe.
NMITIMEN_PATCHES: list[tuple[int, int, int]] = [
    # (rom_offset, old_value, new_value)
    (0x0008A0, 0x01, 0x81),  # LDA #$01 → LDA #$81 at $C0:88A0
    (0x00094A, 0x01, 0x81),  # LDA #$01 → LDA #$81 at $C0:894A
]

# =============================================================================
# Mailbox addresses — BW-RAM offset $3F00-$3F84
# =============================================================================
# Access via BMAPS=1 window: $00:6000-$7FFF → BW-RAM $2000-$3FFF.
# BW-RAM $3F00 = SNES $7F00 (with BMAPS=1) = FxPakPro SRAM $E03F00.
#
# NOTE: BW-RAM $3E00 is actively cleared by the SA-1 during gameplay
# (confirmed by write/readback test). $3F00 is safe.
# Inbox is at $80-$84 (not $F0) to avoid conflicting with AP counter at $3FF0.

MAILBOX_SNES_BASE = 0x3F00  # BW-RAM offset
MAILBOX_FXPAK_BASE = 0xE03F00

# Outbox (hook writes, AP client reads) — per-frame updates
OUTBOX_MUSIC = 0x00       # 1B: current music track ($7E:1D04)
OUTBOX_BATTLE = 0x01      # 1B: battle state ($7E:3021), 0=not in battle
OUTBOX_FRAME_CTR = 0x02   # 2B: frame counter (LE), incremented each NMI
OUTBOX_VERSION = 0x04     # 1B: hook version (0x01)
OUTBOX_RESULT = 0x05      # 1B: last command result

# Outbox state dump (populated by command CMD_STATE_DUMP)
OUTBOX_CONSUMABLES = 0x10  # 30B: consumable inventory (29 usable + Waste Basket)
OUTBOX_EQUIPMENT = 0x2E    # 30B: equipment inventory
OUTBOX_KEY_ITEMS = 0x4C    # 30B: key item inventory (expanded by randomizer)
OUTBOX_COINS = 0x6A        # 2B: coins (LE)
# NOTE: WRAM layout is coins(2) → FP_cur(1) → FP_max(1) → frog_coins(2).
# Outbox must match this order since we MVN the 6 bytes contiguously.
OUTBOX_CURRENT_FP = 0x6C   # 1B: current FP
OUTBOX_MAX_FP = 0x6D       # 1B: max FP
OUTBOX_FROG_COINS = 0x6E   # 2B: frog coins (LE)
OUTBOX_CUR_HP = 0x70       # 10B: current HP (5 chars × 2B)
OUTBOX_MAX_HP = 0x7A       # 10B: max HP (5 chars × 2B)

# Inbox (AP client writes, hook reads)
# Starts at $88 to avoid overlap with expanded outbox (ends at $82).
# Must stay below $F0 to avoid AP counter at BW-RAM $3FF0.
INBOX_COMMAND = 0x88   # 1B: command byte (0=idle)
INBOX_PARAM1 = 0x89    # 1B: item type (0=consumable, 1=equip, 2=key)
INBOX_PARAM2 = 0x8A    # 1B: item ID / amount
INBOX_PARAM3 = 0x8B    # 2B: amount (LE) for coins/frog coins

# Commands
CMD_IDLE = 0x00
CMD_GIVE_ITEM = 0x01
CMD_SET_COINS = 0x02
CMD_SET_FROG_COINS = 0x03
CMD_ADD_FP = 0x04
CMD_HEAL = 0x05
CMD_STATE_DUMP = 0x09

# Results
RESULT_NONE = 0x00
RESULT_OK = 0x01
RESULT_INV_FULL = 0x02

# Hook protocol version
HOOK_VERSION = 0x01

# =============================================================================
# WRAM source addresses (for hook copies)
# =============================================================================

WRAM_MUSIC = 0x7E1D04
WRAM_BATTLE = 0x7E3021
WRAM_CONSUMABLES = 0x7FF882   # 30 bytes (29 usable + Waste Basket)
WRAM_EQUIPMENT = 0x7FF864     # 30 bytes
WRAM_KEY_ITEMS = 0x7FF8F0     # 30 bytes (randomizer expands from $F8A0 to $F8F0)
WRAM_COINS = 0x7FF8AF         # 2 bytes (LE)
WRAM_CURRENT_FP = 0x7FF8B1    # 1 byte
WRAM_MAX_FP = 0x7FF8B2        # 1 byte
WRAM_FROG_COINS = 0x7FF8B3    # 2 bytes (LE)

# Character stat offsets in $7F:F800, stride $14 (20 bytes) per character
# Layout per char: level(1) HP_cur(2) HP_max(2) spd(1) atk(1) def(1) matk(1) mdef(1)
#                  exp(2) weapon(1) armor(1) accessory(1) unused(1) spells(4)
# +$01 = current HP (2B), +$03 = max HP (2B)
CHAR_STAT_BASE = 0x7FF800
CHAR_STAT_STRIDE = 0x14
CHAR_HP_CUR_OFF = 0x01
CHAR_HP_MAX_OFF = 0x03


# =============================================================================
# Mini 65816 assembler with label/branch support
# =============================================================================

class Asm65816:
    """Minimal 65816 assembler for generating hook code with automatic
    branch offset calculation.

    Args:
        base_addr: The absolute address within the bank where this code
                   will be located. Used for JMP (absolute) fixups.
    """

    def __init__(self, base_addr: int = 0x2200) -> None:
        self.code = bytearray()
        self.labels: dict[str, int] = {}
        self.fixups: list[tuple[int, str]] = []     # 8-bit relative branches
        self.jmp_fixups: list[tuple[int, str]] = []  # 16-bit absolute JMPs
        self.base_addr = base_addr

    def emit(self, *args: int) -> None:
        """Emit raw bytes."""
        for b in args:
            self.code.append(b & 0xFF)

    def pos(self) -> int:
        """Current code offset."""
        return len(self.code)

    def label(self, name: str) -> None:
        """Define a label at the current position."""
        if name in self.labels:
            raise ValueError(f"Duplicate label: {name}")
        self.labels[name] = len(self.code)

    def _branch(self, opcode: int, target: str) -> None:
        self.emit(opcode)
        self.fixups.append((len(self.code), target))
        self.emit(0x00)  # placeholder

    def beq(self, target: str) -> None:
        self._branch(0xF0, target)

    def bne(self, target: str) -> None:
        self._branch(0xD0, target)

    def bcc(self, target: str) -> None:
        self._branch(0x90, target)

    def bcs(self, target: str) -> None:
        self._branch(0xB0, target)

    def bra(self, target: str) -> None:
        self._branch(0x80, target)

    # --- Common instruction helpers ---

    def rep(self, flags: int) -> None:
        self.emit(0xC2, flags)

    def sep(self, flags: int) -> None:
        self.emit(0xE2, flags)

    def lda_long(self, addr: int) -> None:
        """LDA $xxxxxx (long, 4 bytes)"""
        self.emit(0xAF, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF)

    def sta_long(self, addr: int) -> None:
        """STA $xxxxxx (long, 4 bytes)"""
        self.emit(0x8F, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF)

    def lda_long_x(self, addr: int) -> None:
        """LDA $xxxxxx,X (long indexed, 4 bytes)"""
        self.emit(0xBF, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF)

    def sta_long_x(self, addr: int) -> None:
        """STA $xxxxxx,X (long indexed, 4 bytes)"""
        self.emit(0x9F, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF)

    def lda_imm8(self, val: int) -> None:
        """LDA #$xx (8-bit immediate, requires M=1)"""
        self.emit(0xA9, val & 0xFF)

    def lda_imm16(self, val: int) -> None:
        """LDA #$xxxx (16-bit immediate, requires M=0)"""
        self.emit(0xA9, val & 0xFF, (val >> 8) & 0xFF)

    def ldx_imm16(self, val: int) -> None:
        """LDX #$xxxx (16-bit immediate, requires X=0)"""
        self.emit(0xA2, val & 0xFF, (val >> 8) & 0xFF)

    def ldy_imm16(self, val: int) -> None:
        """LDY #$xxxx (16-bit immediate, requires X=0)"""
        self.emit(0xA0, val & 0xFF, (val >> 8) & 0xFF)

    def cmp_imm8(self, val: int) -> None:
        """CMP #$xx (8-bit, requires M=1)"""
        self.emit(0xC9, val & 0xFF)

    def cpx_imm16(self, val: int) -> None:
        """CPX #$xxxx (16-bit, requires X=0)"""
        self.emit(0xE0, val & 0xFF, (val >> 8) & 0xFF)

    def mvn(self, dst_bank: int, src_bank: int) -> None:
        """MVN dst,src (block move next, 3 bytes)"""
        self.emit(0x54, dst_bank & 0xFF, src_bank & 0xFF)

    def jml(self, addr: int) -> None:
        """JML $xxxxxx (4 bytes)"""
        self.emit(0x5C, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF)

    def jmp(self, target: str) -> None:
        """JMP $xxxx (absolute within bank, 3 bytes, label resolved at finalize)"""
        self.emit(0x4C)
        self.jmp_fixups.append((len(self.code), target))
        self.emit(0x00, 0x00)  # placeholder

    def finalize(self) -> bytes:
        """Resolve all branch/JMP fixups and return the assembled bytes."""
        # 8-bit relative branches
        for offset, label_name in self.fixups:
            if label_name not in self.labels:
                raise ValueError(f"Undefined label: {label_name}")
            target = self.labels[label_name]
            rel = target - (offset + 1)
            if rel < -128 or rel > 127:
                raise ValueError(
                    f"Branch to '{label_name}' out of range: {rel} "
                    f"(from offset {offset} to {target})"
                )
            self.code[offset] = rel & 0xFF

        # 16-bit absolute JMPs (within bank)
        for offset, label_name in self.jmp_fixups:
            if label_name not in self.labels:
                raise ValueError(f"Undefined label: {label_name}")
            target = self.labels[label_name]
            abs_addr = self.base_addr + target
            self.code[offset] = abs_addr & 0xFF
            self.code[offset + 1] = (abs_addr >> 8) & 0xFF

        return bytes(self.code)


# =============================================================================
# Hook code assembly
# =============================================================================

def _bwram(offset: int) -> int:
    """Convert a mailbox offset to a BW-RAM address via the BMAPS window.

    Uses the $00:6000-$7FFF BW-RAM window with BMAPS=1 (mapping BW-RAM
    $2000-$3FFF). The hook sets BMAPS=1 at entry.

    BW-RAM $3F00 → window address $00:7F00 (= $6000 + $3F00 - $2000).
    """
    return 0x007F00 + offset


def build_hook_code() -> bytes:
    """Assemble the NMI cooperative hook as raw 65816 machine code.

    The hook is installed at $D5:F000 (ROM offset $15F000).
    It runs every NMI frame, copies WRAM state to BW-RAM mailbox,
    processes inbox commands, then jumps to the original WRAM handler.
    """
    a = Asm65816(base_addr=0xF000)

    # =================================================================
    # ENTRY: Switch to native mode, save registers and old E flag
    # =================================================================
    # NMI can fire in native or emulation mode (via $FFEA/$FFFA).
    # CLC;XCE switches to native mode; carry = old E flag.
    # Key insight: carry is NOT affected by REP, PHA/PHX/PHY/PHB/PHD,
    # LDA, or STA. So carry survives from XCE through register saves
    # and BMAPS setup, and we can save it to the stack via ROL trick.
    a.emit(0x18)      # CLC
    a.emit(0xFB)      # XCE — native mode; carry = old E flag
    a.rep(0x30)       # REP #$30: 16-bit A/X/Y (carry preserved)
    a.emit(0x48)      # PHA (16-bit, carry preserved)
    a.emit(0xDA)      # PHX (16-bit, carry preserved)
    a.emit(0x5A)      # PHY (16-bit, carry preserved)
    a.emit(0x8B)      # PHB (carry preserved)
    a.emit(0x0B)      # PHD (carry preserved)

    a.sep(0x20)       # SEP #$20: 8-bit A (carry preserved)

    # =================================================================
    # SET UP BW-RAM ACCESS (carry still = old E flag)
    # =================================================================
    # Set BMAPS=1 so $6000-$7FFF maps to BW-RAM $2000-$3FFF (game default).
    a.lda_imm8(0x01)
    a.sta_long(0x002224)            # BMAPS = 1

    # Enable SNES CPU BW-RAM writes. Set at entry, NOT cleared at exit —
    # clearing SBWE during NMI breaks in-progress game BW-RAM operations.
    a.lda_imm8(0x80)
    a.sta_long(0x002226)            # SBWE bit 7 = 1 (enable writes)

    # Save old E flag (carry) to stack via ROL trick
    a.lda_imm8(0x00)                # A=0 (carry preserved)
    a.emit(0x2A)                    # ROL A: A = carry (old E), carry = 0
    a.emit(0x48)                    # PHA (8-bit, 1 byte: 0=native, 1=emu)

    # =================================================================
    # PER-FRAME: Copy music byte (WRAM → BW-RAM)
    # =================================================================
    a.lda_long(WRAM_MUSIC)              # LDA $7E1D04
    a.sta_long(_bwram(OUTBOX_MUSIC))    # STA $007E00

    # =================================================================
    # PER-FRAME: Copy battle state (WRAM → BW-RAM)
    # =================================================================
    a.lda_long(WRAM_BATTLE)             # LDA $7E3021
    a.sta_long(_bwram(OUTBOX_BATTLE))   # STA $007E01

    # =================================================================
    # PER-FRAME: Increment frame counter
    # =================================================================
    a.rep(0x20)                           # REP #$20: 16-bit A
    a.lda_long(_bwram(OUTBOX_FRAME_CTR))  # LDA $007E02
    a.emit(0x1A)                          # INC A
    a.sta_long(_bwram(OUTBOX_FRAME_CTR))  # STA $007E02
    a.sep(0x20)                           # SEP #$20: 8-bit A

    # =================================================================
    # PER-FRAME: Write hook version byte
    # =================================================================
    a.lda_imm8(HOOK_VERSION)              # LDA #$01
    a.sta_long(_bwram(OUTBOX_VERSION))    # STA $007E04

    # =================================================================
    # CHECK INBOX (use BNE + JMP since no_command is >127 bytes away)
    # =================================================================
    a.lda_long(_bwram(INBOX_COMMAND))     # LDA $007EF0
    a.bne("has_command")                  # If non-zero, dispatch
    a.jmp("no_command")                   # Otherwise skip (JMP for far target)
    a.label("has_command")

    # =================================================================
    # COMMAND DISPATCH (use JMP for far command handlers)
    # =================================================================
    a.cmp_imm8(CMD_GIVE_ITEM)
    a.bne("not_give_item")
    a.jmp("cmd_give_item")
    a.label("not_give_item")

    a.cmp_imm8(CMD_SET_COINS)
    a.bne("not_set_coins")
    a.jmp("cmd_set_coins")
    a.label("not_set_coins")

    a.cmp_imm8(CMD_SET_FROG_COINS)
    a.bne("not_set_frog")
    a.jmp("cmd_set_frog_coins")
    a.label("not_set_frog")

    a.cmp_imm8(CMD_ADD_FP)
    a.bne("not_add_fp")
    a.jmp("cmd_add_fp")
    a.label("not_add_fp")

    a.cmp_imm8(CMD_HEAL)
    a.bne("not_heal")
    a.jmp("cmd_heal")
    a.label("not_heal")

    a.cmp_imm8(CMD_STATE_DUMP)
    a.bne("not_state_dump")
    a.jmp("cmd_state_dump")
    a.label("not_state_dump")

    a.jmp("cmd_done")                     # Unknown command, just clear it

    # =================================================================
    # CMD $01: GIVE ITEM
    # =================================================================
    a.label("cmd_give_item")
    a.lda_long(_bwram(INBOX_PARAM1))      # item type
    a.beq("give_consumable")              # type 0
    a.cmp_imm8(0x01)
    a.beq("give_equipment")               # type 1
    a.cmp_imm8(0x02)
    a.beq("give_key_item")                # type 2
    a.jmp("cmd_fail")                     # invalid type

    # --- Give consumable: find empty slot in $7F:F882 (29 slots) ---
    a.label("give_consumable")
    a.ldx_imm16(0x0000)
    a.label("find_con_slot")
    a.lda_long_x(WRAM_CONSUMABLES)        # LDA $7FF882,X
    a.cmp_imm8(0xFF)                      # Empty?
    a.beq("found_con_slot")
    a.emit(0xE8)                          # INX
    a.cpx_imm16(0x001D)                   # 29 slots
    a.bcc("find_con_slot")
    a.jmp("cmd_fail")                     # Inventory full

    a.label("found_con_slot")
    a.lda_long(_bwram(INBOX_PARAM2))      # Item ID
    a.sta_long_x(WRAM_CONSUMABLES)        # STA $7FF882,X
    a.jmp("cmd_ok")

    # --- Give equipment: find empty slot in $7F:F864 (30 slots) ---
    a.label("give_equipment")
    a.ldx_imm16(0x0000)
    a.label("find_equ_slot")
    a.lda_long_x(WRAM_EQUIPMENT)          # LDA $7FF864,X
    a.cmp_imm8(0xFF)
    a.beq("found_equ_slot")
    a.emit(0xE8)                          # INX
    a.cpx_imm16(0x001E)                   # 30 slots
    a.bcc("find_equ_slot")
    a.jmp("cmd_fail")

    a.label("found_equ_slot")
    a.lda_long(_bwram(INBOX_PARAM2))
    a.sta_long_x(WRAM_EQUIPMENT)
    a.jmp("cmd_ok")

    # --- Give key item: find empty slot in $7F:F8A0 (16 slots) ---
    a.label("give_key_item")
    a.ldx_imm16(0x0000)
    a.label("find_key_slot")
    a.lda_long_x(WRAM_KEY_ITEMS)          # LDA $7FF8A0,X
    a.cmp_imm8(0xFF)
    a.beq("found_key_slot")
    a.emit(0xE8)                          # INX
    a.cpx_imm16(0x001E)                   # 30 slots
    a.bcc("find_key_slot")
    a.jmp("cmd_fail")

    a.label("found_key_slot")
    a.lda_long(_bwram(INBOX_PARAM2))
    a.sta_long_x(WRAM_KEY_ITEMS)
    a.jmp("cmd_ok")

    # =================================================================
    # CMD $02: SET COINS
    # =================================================================
    a.label("cmd_set_coins")
    a.rep(0x20)                           # 16-bit A
    a.lda_long(_bwram(INBOX_PARAM3))      # Amount (2B LE)
    a.sta_long(WRAM_COINS)                # STA $7FF8AF
    a.sep(0x20)                           # 8-bit A
    a.jmp("cmd_ok")

    # =================================================================
    # CMD $03: SET FROG COINS
    # =================================================================
    a.label("cmd_set_frog_coins")
    a.rep(0x20)
    a.lda_long(_bwram(INBOX_PARAM3))
    a.sta_long(WRAM_FROG_COINS)           # STA $7FF8B3
    a.sep(0x20)
    a.jmp("cmd_ok")

    # =================================================================
    # CMD $04: ADD MAX FP
    # =================================================================
    a.label("cmd_add_fp")
    a.lda_long(WRAM_MAX_FP)               # Current max FP
    a.emit(0x18)                          # CLC
    a.emit(0x6F)                          # ADC long...
    # ADC $007EF2 (long) = 6F F2 7E 00
    a.emit(_bwram(INBOX_PARAM2) & 0xFF)
    a.emit((_bwram(INBOX_PARAM2) >> 8) & 0xFF)
    a.emit((_bwram(INBOX_PARAM2) >> 16) & 0xFF)
    a.cmp_imm8(99)                        # Cap at 99
    a.bcc("fp_no_cap")
    a.lda_imm8(99)
    a.label("fp_no_cap")
    a.sta_long(WRAM_MAX_FP)               # Write max FP
    a.sta_long(WRAM_CURRENT_FP)           # Also set current = max
    a.jmp("cmd_ok")

    # =================================================================
    # CMD $05: HEAL ALL
    # =================================================================
    a.label("cmd_heal")
    a.rep(0x20)                           # 16-bit A for HP
    # Unrolled: 5 characters, stride $25, HP at +$01 (cur) and +$03 (max)
    for i in range(5):
        base = CHAR_STAT_BASE + i * CHAR_STAT_STRIDE
        a.lda_long(base + CHAR_HP_MAX_OFF)   # Max HP
        a.sta_long(base + CHAR_HP_CUR_OFF)   # → Current HP
    a.sep(0x20)                           # 8-bit A
    # Restore FP
    a.lda_long(WRAM_MAX_FP)
    a.sta_long(WRAM_CURRENT_FP)
    a.jmp("cmd_ok")

    # =================================================================
    # CMD $09: STATE DUMP
    # =================================================================
    a.label("cmd_state_dump")
    a.rep(0x30)                           # 16-bit A/X/Y

    # Consumables: 30 bytes from $7F:F882 → BW-RAM outbox
    a.lda_imm16(30 - 1)
    a.ldx_imm16(WRAM_CONSUMABLES & 0xFFFF)
    a.ldy_imm16(_bwram(OUTBOX_CONSUMABLES) & 0xFFFF)
    a.mvn(0x00, 0x7F)

    # Equipment: 30 bytes from $7F:F864 → $60:3E2D
    a.lda_imm16(30 - 1)
    a.ldx_imm16(WRAM_EQUIPMENT & 0xFFFF)
    a.ldy_imm16(_bwram(OUTBOX_EQUIPMENT) & 0xFFFF)
    a.mvn(0x00, 0x7F)

    # Key items: 30 bytes from $7F:F8F0 → BW-RAM outbox
    a.lda_imm16(30 - 1)
    a.ldx_imm16(WRAM_KEY_ITEMS & 0xFFFF)
    a.ldy_imm16(_bwram(OUTBOX_KEY_ITEMS) & 0xFFFF)
    a.mvn(0x00, 0x7F)

    # Coins(2) + CurrentFP(1) + MaxFP(1) + FrogCoins(2) = 6 contiguous bytes
    # from $7F:F8AF → $60:3E5B
    a.lda_imm16(6 - 1)
    a.ldx_imm16(WRAM_COINS & 0xFFFF)
    a.ldy_imm16(_bwram(OUTBOX_COINS) & 0xFFFF)
    a.mvn(0x00, 0x7F)

    a.sep(0x20)                           # 8-bit A (X/Y still 16-bit)

    # Character HP: unrolled, 5 chars × (2B current + 2B max)
    a.rep(0x20)                           # 16-bit A for HP values
    for i in range(5):
        base = CHAR_STAT_BASE + i * CHAR_STAT_STRIDE
        # Current HP → outbox $61 + i*2
        a.lda_long(base + CHAR_HP_CUR_OFF)
        a.sta_long(_bwram(OUTBOX_CUR_HP + i * 2))
        # Max HP → outbox $6B + i*2
        a.lda_long(base + CHAR_HP_MAX_OFF)
        a.sta_long(_bwram(OUTBOX_MAX_HP + i * 2))
    a.sep(0x20)                           # 8-bit A
    a.jmp("cmd_ok")

    # =================================================================
    # COMMAND RESULTS
    # =================================================================
    a.label("cmd_ok")
    a.lda_imm8(RESULT_OK)
    a.sta_long(_bwram(OUTBOX_RESULT))
    a.jmp("cmd_done")

    a.label("cmd_fail")
    a.lda_imm8(RESULT_INV_FULL)
    a.sta_long(_bwram(OUTBOX_RESULT))

    a.label("cmd_done")
    a.lda_imm8(0x00)
    a.sta_long(_bwram(INBOX_COMMAND))     # Clear command (signals AP client)

    # =================================================================
    # EXIT: Disable BW-RAM writes, restore registers and processor mode
    # =================================================================
    a.label("no_command")
    # Note: SBWE is NOT touched — game manages it. If SBWE=$00 when NMI
    # fires, our BW-RAM writes are silently ignored (harmless miss).

    # Restore old E flag from stack
    a.emit(0x68)       # PLA (8-bit, 1 byte: saved E flag)
    a.emit(0x4A)       # LSR A: bit 0 → carry = old E flag

    # Restore registers (none of these affect carry)
    a.emit(0x2B)       # PLD
    a.emit(0xAB)       # PLB
    a.rep(0x30)        # REP #$30: 16-bit A/X/Y (carry preserved)
    a.emit(0x7A)       # PLY (16-bit, carry preserved)
    a.emit(0xFA)       # PLX (16-bit, carry preserved)
    a.emit(0x68)       # PLA (16-bit, carry preserved)

    # Restore processor mode: carry → E flag
    a.emit(0xFB)       # XCE: carry → E (restores native or emulation)
    a.jml(ORIGINAL_NMI_ADDR)  # JML $000008

    return a.finalize()


# Pre-built hook code
NMI_HOOK_CODE = build_hook_code()
