"""Belome 3 spell-block + Enduring Brooch ASM hook.

Adapted from the community ASM patch in
``randomizer/patches/asm_ref/{belome3,eb}.asm``. Both behaviors are always
active. Only the Belome 3 blocked-spell list shrinks when the
``InfuseSpellElements`` flag is enabled — those infused spells become
elemental, and Belome 3's rule is to nullify only NON-elemental spells.

Behaviors
---------

* **Belome 3 immunity to non-elemental magic.** Whenever Belome 3
  (monster_id 201, byte $C9) is in enemy slot 1 and a living Bowser Copy S
  (monster_id 125, byte $7D) is in slot 2 or 3, the listed spells are
  nullified before the damage actually applies.

* **Enduring Brooch (item 73 / $49).** The wearer survives at 1 HP the
  first time a hit would have KO'd them in a battle. The repurposes byte
  $7E:001F + slot_offset (vanilla unused per-character byte) as a
  per-battle "already activated" flag. Cleared every time a character is
  selected to act (hook at $C2:972E) so the flag is per-battle, not
  per-turn.

ROM hooks
---------

Four short JSL trampolines are written into the battle engine:

* ``$C2:C55E`` — entry of the apply-damage routine. Replaces 4 bytes
  (``REP #$20`` + ``LDX $CA``) with a JSL; the helper restores those
  instructions before RTL.
* ``$C2:972E`` — start of "begin a character's defense turn". Replaces 6
  bytes (``LDA $BA`` / ``AND #$00FF`` / ``TAY``) with JSL + 2 NOPs; the
  helper clears the brooch-active flag for all 3 allies and restores the
  displaced LDA/AND/TAY.
* ``$C2:CA73`` — entry of the perfect-block path. Replaces 5 bytes with
  JSL + RTS; the helper handles the perfect-block effect itself
  (including undoing the brooch activation if a perfect block landed).
* ``$C2:C9FE`` — entry of the timed-block path. Replaces 5 bytes
  (``LDA $C2`` / ``LSR`` / ``STA $C2``) with JSL + NOP; the helper applies
  half damage conditionally and resets the inter-handler scratch words.

Free ROM region
---------------

The four helper routines are laid out back-to-back starting at SNES
``$CF:F7B0`` (ROM offset ``0x0FF7B0``). Vanilla SMRPG has 2128 zero bytes
at ``$0F:F7B0``-``$0F:FFFF``; ``open_mode.ips`` does not touch this
region; SA-1 can JSL into bank ``$CF`` (verified by the source ROM hack
this is adapted from). The total payload is well under the available
space.
"""

from typing import Iterable

from randomizer.data.nmi_hook import Asm65816


# -----------------------------------------------------------------------
# Hook addresses (ROM offsets, HiROM mapping: SNES $C2:xxxx → ROM $02xxxx)
# -----------------------------------------------------------------------
HOOK_APPLY_DAMAGE_ROM_OFFSET = 0x02C55E
HOOK_ZERO_BROOCH_ROM_OFFSET = 0x02972E
HOOK_PERFECT_BLOCK_ROM_OFFSET = 0x02CA73
HOOK_TIMED_BLOCK_ROM_OFFSET = 0x02C9FE

# Free ROM region for the four helper routines.
FREE_ROM_ROM_OFFSET = 0x0FF7B0          # ROM offset
FREE_ROM_SNES_ADDR = 0xCFF7B0           # SNES address (HiROM bank $CF)
FREE_ROM_AVAILABLE_BYTES = 0x100000 - FREE_ROM_ROM_OFFSET  # ~2128 bytes

# -----------------------------------------------------------------------
# IDs
# -----------------------------------------------------------------------
BELOME_3_ENEMY_ID = 0xC9         # randomizer monster_id 201
BOWSER_COPY_S_ENEMY_ID = 0x7D    # randomizer monster_id 125
ENDURING_BROOCH_ITEM_ID = 0x49   # randomizer item_id 73

# -----------------------------------------------------------------------
# Battle WRAM addresses
# -----------------------------------------------------------------------
ENEMY_1_STATUS = 0x7EFC00
ENEMY_1_ID = 0x7EFC01
ENEMY_2_STATUS = 0x7EFC80
ENEMY_2_ID = 0x7EFC81
ENEMY_3_STATUS = 0x7EFD00
ENEMY_3_ID = 0x7EFD01

ALLY_1_FREE_BYTE = 0x7EFA9F
ALLY_2_FREE_BYTE = 0x7EFB1F
ALLY_3_FREE_BYTE = 0x7EFB9F

# These are base addresses indexed by X (X holds an ally-slot offset
# such as $FA80 / $FB00 / $FB80). LDA $7E001E, X reads the accessory byte
# of whichever ally slot the current target offset selects.
ALLY_ACCESSORY_BASE = 0x7E001E   # ally accessory byte
ALLY_BROOCH_FLAG_BASE = 0x7E001F # repurposed unused byte (high bit = activated)
ALLY_HP_BASE = 0x7E0011          # current HP (16-bit)
ALLY_DAMAGE_DISPLAY_BASE = 0x7E0045
ALLY_FLAGS_BASE = 0x7E0041       # status / "perfect block" eligibility bits
ALLY_FLAGS2_BASE = 0x7E0000      # bit-7 cleared on certain perfect-block paths
ALLY_F30_BASE = 0x7E0030
ALLY_F33_BASE = 0x7E0033
ALLY_F35_BASE = 0x7E0035
ALLY_F40_BASE = 0x7E0040
ALLY_F43_BASE = 0x7E0043

# Inter-handler scratch (BW-RAM mirror, safe across the apply-damage
# → perfect-block / timed-block sequence within a single defense turn).
SCRATCH_HP_BEFORE = 0x7F0000
SCRATCH_DAMAGE = 0x7F0010
SCRATCH_BROOCH_ACTIVE_THIS_TURN = 0x7F0020
SCRATCH_HALF_DAMAGE = 0x7F0030

# -----------------------------------------------------------------------
# Spell IDs that Belome 3 nullifies (per the source patch, validated
# against the randomizer's spell index file).
# -----------------------------------------------------------------------
# Always blocked — these spells are non-elemental even with InfuseSpellElements.
SPELLS_ALWAYS_BLOCKED: tuple[int, ...] = (
    0x0C,  # Terrorize
    0x0D,  # Poison Gas
    0x12,  # Geno Whirl
    0x13,  # Geno Blast
    0x1A,  # Star Rain
)
# Blocked only when InfuseSpellElements is OFF — these become elemental
# under InfuseSpellElements and so should NOT be blocked then.
SPELLS_BLOCKED_WHEN_NOT_INFUSED: tuple[int, ...] = (
    0x0B,  # Psych Bomb (becomes Fire)
    0x0E,  # Crusher    (becomes Jump/Earth)
    0x0F,  # Bowser Crush (becomes Jump/Earth)
    0x10,  # Geno Beam  (becomes Ice)
    0x14,  # Geno Flash (becomes Fire)
)


# -----------------------------------------------------------------------
# Asm65816 extension with the ops this patch needs.
# -----------------------------------------------------------------------

class _Asm(Asm65816):
    """Asm65816 plus a handful of ops (DP loads/stores/branches) the
    base class doesn't expose."""

    def lda_dp(self, dp: int) -> None:
        self.emit(0xA5, dp & 0xFF)

    def cmp_dp(self, dp: int) -> None:
        self.emit(0xC5, dp & 0xFF)

    def sta_dp(self, dp: int) -> None:
        self.emit(0x85, dp & 0xFF)

    def ldx_dp(self, dp: int) -> None:
        self.emit(0xA6, dp & 0xFF)

    def sbc_dp(self, dp: int) -> None:
        self.emit(0xE5, dp & 0xFF)

    def adc_dp(self, dp: int) -> None:
        self.emit(0x65, dp & 0xFF)

    def tax(self) -> None:
        self.emit(0xAA)

    def tay(self) -> None:
        self.emit(0xA8)

    def clc(self) -> None:
        self.emit(0x18)

    def sec(self) -> None:
        self.emit(0x38)

    def lsr_a(self) -> None:
        self.emit(0x4A)

    def rtl(self) -> None:
        self.emit(0x6B)

    def rts(self) -> None:
        self.emit(0x60)

    def nop(self) -> None:
        self.emit(0xEA)

    def bmi(self, target: str) -> None:
        self._branch(0x30, target)

    def bpl(self, target: str) -> None:
        self._branch(0x10, target)

    def bit_imm16(self, val: int) -> None:
        self.emit(0x89, val & 0xFF, (val >> 8) & 0xFF)

    def sbc_imm16(self, val: int) -> None:
        self.emit(0xE9, val & 0xFF, (val >> 8) & 0xFF)

    def and_imm16(self, val: int) -> None:
        self.emit(0x29, val & 0xFF, (val >> 8) & 0xFF)

    def trb_abs(self, addr: int) -> None:
        self.emit(0x1C, addr & 0xFF, (addr >> 8) & 0xFF)

    def sbc_long(self, addr: int) -> None:
        self.emit(
            0xEF,
            addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF,
        )


# -----------------------------------------------------------------------
# apply_damage hook: Belome 3 nullification + Enduring Brooch arming.
# -----------------------------------------------------------------------

def _build_apply_damage(infuse_spell_elements: bool) -> bytes:
    """Hook installed at $C2:C55E.

    Entry register state (vanilla): M=1 (8-bit A), X=0 (16-bit X). DBR
    is set up so DP loads of $CA-$CD reach the battle scratch holding
    the current target offset and the last-skill-id byte.
    """
    a = _Asm(base_addr=0)

    # ===== Belome 3 spell-block =====
    # Slot-1 enemy must be Belome 3.
    a.lda_long(ENEMY_1_ID)
    a.cmp_imm8(BELOME_3_ENEMY_ID)
    a.bne("return_to_apply_damage")

    # Target must be enemy slot 1 ($7E:FC00). Read the 16-bit target
    # offset byte-by-byte while still in M=1 mode.
    a.lda_dp(0xCA)
    a.cmp_imm8(0x00)
    a.bne("return_to_apply_damage")
    a.lda_dp(0xCB)
    a.cmp_imm8(0xFC)
    a.bne("return_to_apply_damage")

    # A Bowser Copy S clone must be present (slot 2 or slot 3).
    a.lda_long(ENEMY_2_ID)
    a.cmp_imm8(BOWSER_COPY_S_ENEMY_ID)
    a.beq("check_valid_enemy2")
    a.lda_long(ENEMY_3_ID)
    a.cmp_imm8(BOWSER_COPY_S_ENEMY_ID)
    a.beq("check_valid_enemy3")
    a.bra("return_to_apply_damage")

    a.label("check_valid_enemy2")
    a.lda_long(ENEMY_2_STATUS)
    a.cmp_imm8(0x00)
    a.beq("skill_check")
    a.bra("return_to_apply_damage")

    a.label("check_valid_enemy3")
    a.lda_long(ENEMY_3_STATUS)
    a.cmp_imm8(0x00)
    a.beq("skill_check")
    a.bra("return_to_apply_damage")

    # Last skill used must be one of the listed non-elemental spells.
    a.label("skill_check")
    a.lda_dp(0xCD)
    blocked: list[int] = list(SPELLS_ALWAYS_BLOCKED)
    if not infuse_spell_elements:
        blocked.extend(SPELLS_BLOCKED_WHEN_NOT_INFUSED)
    blocked.sort()
    for spell_id in blocked:
        a.cmp_imm8(spell_id)
        a.beq("nullify")
    a.bra("return_to_apply_damage")

    a.label("nullify")
    a.lda_imm8(0x00)
    a.sta_dp(0xC2)
    a.sta_dp(0xC3)
    a.bra("finish")

    # ===== Enduring Brooch arming =====
    a.label("return_to_apply_damage")
    a.rep(0x20)                                 # M=0
    a.lda_dp(0xCA)                              # 16-bit target offset
    a.cmp_imm16(0xFA80)
    a.beq("slot_accessory_check")
    a.cmp_imm16(0xFB00)
    a.beq("slot_accessory_check")
    a.cmp_imm16(0xFB80)
    a.beq("slot_accessory_check")
    a.bra("finish")

    a.label("slot_accessory_check")
    a.tax()
    a.sep(0x20)
    a.lda_long_x(ALLY_ACCESSORY_BASE)
    a.cmp_imm8(ENDURING_BROOCH_ITEM_ID)
    a.bne("finish")

    a.lda_long_x(ALLY_BROOCH_FLAG_BASE)
    a.bmi("finish")                              # already activated this battle

    # Would this hit drop HP to <=0? Vanilla pattern: CLC + SBC = subtract
    # damage and an extra 1, BMI fires when damage >= HP (KO threshold).
    a.rep(0x20)
    a.clc()
    a.lda_long_x(ALLY_HP_BASE)
    a.sbc_dp(0xC2)
    a.bmi("activate_brooch")
    a.bra("finish")

    a.label("activate_brooch")
    a.sep(0x20)
    a.lda_imm8(0x80)
    a.sta_long_x(ALLY_BROOCH_FLAG_BASE)         # mark used
    a.rep(0x20)
    a.lda_dp(0xC2)
    a.sta_long(SCRATCH_DAMAGE)
    a.lda_imm16(0x0001)
    a.sta_long(SCRATCH_BROOCH_ACTIVE_THIS_TURN)
    a.lda_long_x(ALLY_HP_BASE)
    a.sta_long(SCRATCH_HP_BEFORE)
    a.sec()
    a.sbc_imm16(0x0001)                          # damage = HP-1 → leaves 1 HP
    a.sta_dp(0xC2)

    # Finish: replay the original two displaced bytes (REP #$20 / LDX $CA)
    # and RTL back to the byte after the JSL.
    a.label("finish")
    a.rep(0x20)
    a.ldx_dp(0xCA)
    a.rtl()
    return a.finalize()


def _build_zero_out_brooch() -> bytes:
    """Hook installed at $C2:972E (start of a character's defense turn).

    Clears the per-battle "brooch already used" flag for all three ally
    slots, then replays the displaced ``LDA $BA / AND #$00FF / TAY`` so
    control returns to vanilla code unchanged.
    """
    a = _Asm(base_addr=0)
    a.sep(0x20)
    a.lda_imm8(0x00)
    a.sta_long(ALLY_1_FREE_BYTE)
    a.sta_long(ALLY_2_FREE_BYTE)
    a.sta_long(ALLY_3_FREE_BYTE)
    a.rep(0x20)
    a.lda_dp(0xBA)
    a.and_imm16(0x00FF)
    a.tay()
    a.rtl()
    return a.finalize()


def _build_brooch_perfect_block() -> bytes:
    """Hook installed at $C2:CA73 (perfect-block path).

    If the brooch armed THIS turn but the player landed a perfect block,
    the damage is fully avoided so the brooch use should be refunded.
    Then run the vanilla perfect-block effect.
    """
    a = _Asm(base_addr=0)
    a.rep(0x20)
    a.lda_dp(0xCA)
    a.cmp_imm16(0xFA80)
    a.beq("slot_accessory_check_perfect")
    a.cmp_imm16(0xFB00)
    a.beq("slot_accessory_check_perfect")
    a.cmp_imm16(0xFB80)
    a.beq("slot_accessory_check_perfect")
    a.bra("finish_perfect")

    a.label("slot_accessory_check_perfect")
    a.sep(0x20)
    a.lda_long(SCRATCH_BROOCH_ACTIVE_THIS_TURN)
    a.beq("finish_perfect")
    a.lda_imm8(0x00)
    a.sta_long_x(ALLY_BROOCH_FLAG_BASE)         # refund the brooch use

    # Vanilla perfect-block effect (preserved verbatim from the asm
    # reference). The "brooch_bit_test" path covers a special-status
    # branch in the original routine; we keep the original logic intact
    # so we don't change non-brooch perfect-block behavior.
    a.label("finish_perfect")
    a.rep(0x20)
    a.lda_long_x(ALLY_FLAGS_BASE)
    a.bit_imm16(0x0080)
    a.bne("brooch_bit_test")
    a.lda_long_x(ALLY_HP_BASE)
    a.clc()
    a.adc_dp(0xC2)
    a.sta_long_x(ALLY_HP_BASE)
    a.lda_imm16(0x0000)
    a.sta_long_x(ALLY_DAMAGE_DISPLAY_BASE)
    a.rtl()

    a.label("brooch_bit_test")
    a.lda_long_x(ALLY_F35_BASE)
    a.sta_long_x(ALLY_HP_BASE)
    a.lda_imm16(0x0000)
    a.sta_long_x(ALLY_DAMAGE_DISPLAY_BASE)
    a.lda_long_x(ALLY_FLAGS2_BASE)
    a.and_imm16(0xFF3F)
    a.sta_long_x(ALLY_FLAGS2_BASE)
    a.lda_long_x(ALLY_F30_BASE)
    a.sta_long_x(ALLY_F40_BASE)
    a.lda_long_x(ALLY_F33_BASE)
    a.sta_long_x(ALLY_F43_BASE)
    a.lda_imm16(0x0002)
    a.trb_abs(0x0700)
    a.lda_imm16(0x8000)
    a.trb_abs(0x0708)
    a.rtl()
    return a.finalize()


def _build_brooch_timed_block() -> bytes:
    """Hook installed at $C2:C9FE (timed-block path).

    If the brooch armed this turn, recompute whether the half-damage
    timed defense would still have KO'd. If yes, keep the brooch armed
    and apply 0 damage. If no, refund the brooch use and apply the
    normal half-damage. Then reset all scratch words.
    """
    a = _Asm(base_addr=0)
    a.rep(0x20)
    a.lda_dp(0xCA)
    a.cmp_imm16(0xFA80)
    a.beq("slot_accessory_check_timed")
    a.cmp_imm16(0xFB00)
    a.beq("slot_accessory_check_timed")
    a.cmp_imm16(0xFB80)
    a.beq("slot_accessory_check_timed")
    a.bra("apply_half_damage_normal_case")

    a.label("slot_accessory_check_timed")
    a.sep(0x20)
    a.lda_long(SCRATCH_BROOCH_ACTIVE_THIS_TURN)
    a.beq("apply_half_damage_normal_case")

    # Would HP - (orig_damage / 2) still be lethal?
    a.rep(0x20)
    a.lda_long(SCRATCH_DAMAGE)
    a.lsr_a()
    a.sta_long(SCRATCH_HALF_DAMAGE)
    a.lda_long(SCRATCH_HP_BEFORE)
    a.sec()
    a.sbc_long(SCRATCH_HALF_DAMAGE)
    a.bmi("finish_timed")                       # still lethal: keep brooch armed

    # Half-damage non-lethal — refund brooch and apply real half-damage.
    a.sep(0x20)
    a.lda_imm8(0x00)
    a.sta_long_x(ALLY_BROOCH_FLAG_BASE)
    a.rep(0x20)
    a.lda_long(SCRATCH_DAMAGE)
    a.sta_dp(0xC2)
    a.sta_long_x(ALLY_DAMAGE_DISPLAY_BASE)
    a.lda_long(SCRATCH_HP_BEFORE)
    a.sec()
    a.sbc_dp(0xC2)
    a.sta_long_x(ALLY_HP_BASE)

    a.label("apply_half_damage_normal_case")
    a.rep(0x20)
    a.lda_dp(0xC2)
    a.lsr_a()
    a.sta_dp(0xC2)

    a.lda_imm16(0x0000)
    a.sta_long(SCRATCH_HP_BEFORE)
    a.sta_long(SCRATCH_DAMAGE)
    a.sta_long(SCRATCH_BROOCH_ACTIVE_THIS_TURN)
    a.sta_long(SCRATCH_HALF_DAMAGE)

    a.label("finish_timed")
    a.rtl()
    return a.finalize()


# -----------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------

def get_patch(
    infuse_spell_elements: bool,
) -> dict[int, bytes]:
    """Return ``{rom_offset: bytes}`` for both the ASM hooks and the
    free-rom payload. Caller passes the dict to ``Patch.add_dict``.
    """
    apply_bytes = _build_apply_damage(infuse_spell_elements)
    zero_bytes = _build_zero_out_brooch()
    perfect_bytes = _build_brooch_perfect_block()
    timed_bytes = _build_brooch_timed_block()

    apply_addr = FREE_ROM_SNES_ADDR
    zero_addr = apply_addr + len(apply_bytes)
    perfect_addr = zero_addr + len(zero_bytes)
    timed_addr = perfect_addr + len(perfect_bytes)

    total = len(apply_bytes) + len(zero_bytes) + len(perfect_bytes) + len(timed_bytes)
    if total > FREE_ROM_AVAILABLE_BYTES:
        raise RuntimeError(
            f"belome3_brooch payload {total} bytes exceeds "
            f"{FREE_ROM_AVAILABLE_BYTES} bytes available at "
            f"${FREE_ROM_SNES_ADDR:06X}"
        )

    # Write each routine as its own dict entry rather than one large
    # concatenated blob. The single-blob form (~440 bytes) was observed
    # truncating mid-payload during the SSE → browser → ROM transport
    # for at least one user; smaller per-routine entries side-step it
    # cleanly. ROM layout is unchanged (each routine still lives at the
    # same SNES address; the JSL hooks below point at those addresses).
    apply_rom_offset = FREE_ROM_ROM_OFFSET
    zero_rom_offset = apply_rom_offset + len(apply_bytes)
    perfect_rom_offset = zero_rom_offset + len(zero_bytes)
    timed_rom_offset = perfect_rom_offset + len(perfect_bytes)

    out: dict[int, bytes] = {
        apply_rom_offset: apply_bytes,
        zero_rom_offset: zero_bytes,
        perfect_rom_offset: perfect_bytes,
        timed_rom_offset: timed_bytes,
    }

    # Hook 1: $C2:C55E — JSL apply_damage. Replaces the 4 displaced bytes
    # ``REP #$20`` + ``LDX $CA``; the helper restores them before RTL.
    out[HOOK_APPLY_DAMAGE_ROM_OFFSET] = bytes([
        0x22,
        apply_addr & 0xFF,
        (apply_addr >> 8) & 0xFF,
        (apply_addr >> 16) & 0xFF,
    ])

    # Hook 2: $C2:972E — JSL zero_brooch + 2 NOPs. Replaces the 6 bytes
    # ``LDA $BA`` / ``AND #$00FF`` / ``TAY``; helper restores them.
    out[HOOK_ZERO_BROOCH_ROM_OFFSET] = bytes([
        0x22,
        zero_addr & 0xFF,
        (zero_addr >> 8) & 0xFF,
        (zero_addr >> 16) & 0xFF,
        0xEA, 0xEA,
    ])

    # Hook 3: $C2:CA73 — JSL brooch_perfect + RTS. Replaces 5 bytes; the
    # helper terminates by RTL'ing back, then the RTS pops the parent.
    out[HOOK_PERFECT_BLOCK_ROM_OFFSET] = bytes([
        0x22,
        perfect_addr & 0xFF,
        (perfect_addr >> 8) & 0xFF,
        (perfect_addr >> 16) & 0xFF,
        0x60,
    ])

    # Hook 4: $C2:C9FE — JSL brooch_timed + NOP. Replaces 5 bytes
    # ``LDA $C2`` / ``LSR`` / ``STA $C2``; the helper performs them
    # conditionally, then control falls through to vanilla code at $CA03.
    out[HOOK_TIMED_BLOCK_ROM_OFFSET] = bytes([
        0x22,
        timed_addr & 0xFF,
        (timed_addr >> 8) & 0xFF,
        (timed_addr >> 16) & 0xFF,
        0xEA,
    ])

    return out


# Convenience export for direct introspection / tests.
def patched_addresses() -> Iterable[int]:
    return (
        HOOK_APPLY_DAMAGE_ROM_OFFSET,
        HOOK_ZERO_BROOCH_ROM_OFFSET,
        HOOK_PERFECT_BLOCK_ROM_OFFSET,
        HOOK_TIMED_BLOCK_ROM_OFFSET,
        FREE_ROM_ROM_OFFSET,
    )
