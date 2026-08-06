"""UncapMaxFP: lift the 99 cap on max FP so it can grow up to 255.

Multiple sites participate:

1. Two Add7000ToMaxFP handlers - overworld at $C0:C4CC and battle
   at $C2:C14F - replace the 99-cap with a 255-cap. BCS catches
   8-bit ADC overflow so a wrap cannot regress max FP.

2. The X-menu MAIN-menu "Flowers" line ($C3:1621-$C3:163E) widens
   from 2-digit to 3-digit by switching its converter
   $C3:78D2 -> $C3:78EC and shifting its destination LDX 2 tiles
   left ($4630 -> $462C). New layout: cur h/t/o at $462C/$462E/$4630,
   slash at $4632, max h/t/o at $4634/$4636/$4638 (max-ones at vanilla
   $4638). All three Flowers renderers use the same vanilla-minus-2-tile
   shift so they align identically with their box borders.

3. The X-menu Special-menu "Flowers" line at $C3:35EA: cur and max use
   the converter via the shared inner routine $C3:35FF (call sites at
   $C3:3605 and $C3:3615), with the field starting at tilemap slot
   $44B2. The inner routine has no separate LDX for the slash or max -
   both ride on $62, which each subroutine advances (2-digit converter
   += 4, slash writer += 2, 3-digit converter += 6). Switching both
   converters to 3-digit widens the field, so we shift the LDX start 2
   tiles left ($44B2 -> $44AE) so max-ones lands at the vanilla position
   $44BA (flush with the box border), matching the other Flowers lines.

   New layout: cur h/t/o at $44AE/$44B0/$44B2, slash at $44B4, max
   h/t/o at $44B6/$44B8/$44BA.

4. The X-menu item-submenu Flowers display ($C3:2CC0) - third call site
   that targets the same shared inner subroutine ($C3:35FF), so the JSR
   target swaps above already make this site emit 3-digit. Shift the
   LDX dest pointer 2 tiles left ($4694 -> $4690) so max-ones lands at
   vanilla $469C (flush with the description box's right border).

5. The battle spell-menu FP header (bank $C1) widens to 3 digits.

   The vanilla renderer at $C1:62F6 (26 bytes) printed 2-digit cur/max
   via two JSR $C1:6378 calls, then STX/STA to the tilemap
   mirror at $702C/$702E (cur) and $7032/$7034 (max), with a static
   slash at $7030 supplied by the MVN template at $C1:639D. The 11-tile
   window $7020-$7034 is shared with the spell list (which begins at
   $7040) and the per-spell FP cost renderer (which writes $7024/$7026
   each frame), so we cannot widen past $7034.

   We rewrite the renderer in place to call a small converter in free
   ROM at $C1:C6C0, which reuses the proven battle HP 3-digit converter
   at $C1:5D6A (it writes 3 tiles itself via STA $7000,X with X =
   offset + $8C, applying leading-zero suppression and the $2400 tile
   attribute). The converter:

   * saves and restores BOTH $8C (the dialog-text tilemap cursor used
     by $C1:25D2 / $C1:2610, which doubles as the partition base $5D6A
     reads) and $8E (dialog scratch / $5D6A's value-stash) on the
     STACK, so no zero-page state leaks past the call; and
   * STZ $8C so the partition base is 0 and Y is treated as a plain
     offset from $7000.

   New tilemap layout in the existing 11-tile $7020-$7034 window::

       $7020 F | $7022 P | $7024-$7026 spell cost (untouched)
       $7028-$702C cur FP (3 digits) | $702E '/' (static) |
       $7030-$7034 max FP (3 digits)

   The static MVN template at $C1:639D moves the slash from $7030 to
   $702E and blanks the digit slots. Highest write is $7034 (vanilla
   parity, no DMA changes).

   CRITICAL - trampoline location: the converter MUST live at $C1:C6C0
   (or another genuinely-free region such as $C1:9570-$C1:9D50). The
   region $C1:9564-$C1:956F is reserved in the patched ROM and the
   chest-packet allocator patch can land in $C1:95xx on some seeds.
   Placing the converter at $C1:9564 corrupted battle/HUD state and
   produced sprite/tile/palette artifacts even when the converter body
   was a functional no-op - bisecting that down (Test A clean with no
   trampoline; Tests B-G all dirty sharing the $C1:9564 location; Test
   F a no-op trampoline still dirty) is what pinned the location as the
   root cause. The per-spell FP cost renderer at $C1:635B is NOT
   modified - spell costs stay capped at 99.

6. The item RESTORE_FP handler ($C2:C040) is made 8-bit-overflow safe.

   Vanilla adds the item's heal amount to current FP with an 8-bit ADC,
   never checks the carry, and clamps with a *signed* BMI::

       LDA $7EFA0C / CLC / ADC $FB / CMP $7EFA0D / BMI + / LDA $7EFA0D
       STA $7EFA0C

   Both shortcuts hold only while max FP and every heal amount stay <= 99
   (so cur + amount <= 198 cannot wrap, and |cur + amount - max|
   cannot exceed 127). Raising max FP to 255 breaks both:

   * cur + 255 (Royal Syrup) wraps to cur - 1, carry is ignored,
     and the wrapped value is stored - the heal *removes* 1 FP.
   * whenever max - (cur + amount) > 127 the signed compare takes the
     branch backwards, so e.g. Honey Syrup at 0/255 FP restores all 255.

   This is also the overworld menu's FP restore: the item menu applies
   effects by JSL-ing into the battle engine ($C3:2C4F -> JSL $C2A012 ->
   the byte-16 dispatch at $C2:BD45), so $C2:C040 is the only code in the
   ROM that adds a heal amount to current FP.

   Fix, in place and byte-exact (the tail from $C2:C067 keeps its vanilla
   addresses, so $C2:C074 - the next dispatch target - is untouched)::

       LDY $C6 / LDX $02,y        ; folds INY / INY / LDX $00,y, freeing 2
       ... damage-flag writes unchanged ...
       LDA $7EFA0C / CLC / ADC $FB
       BCS clamp                  ; NEW: 8-bit overflow saturates to max
       CMP $7EFA0D
       BCC store                  ; was BMI: unsigned compare
       clamp: LDA $7EFA0D
       store: STA $7EFA0C

   LDX $02,y reads the same effective address as the vanilla
   INY / INY / LDX $00,y (D + 2 + Y), and Y is dead afterwards - unlike
   RESTORE_HP, this handler does not loop over targets (FP is party-global,
   not per-actor), so it never writes Y back to $C6.

   Result is min(cur + amount, max) for every value in 0-255. The green
   heal popup ($7E0045/$7E0046) is left alone: it shows the item's raw
   amount, so Royal Syrup pops "255" exactly like vanilla Max Mushroom
   (also a 255 "recover all" item) does.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # --- FP caps (storage) ---
        # Add7000ToMaxFP handler ($C0:C4CC): replace 99-cap with 255-cap.
        # BCS catches 8-bit ADC overflow so a wrap cannot regress max FP.
        0xC4CC: bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]),
        # Battle bump-max-FP handler ($C2:C14F): same fix, identical bytes.
        0x2C14F: bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]),

        # --- Item RESTORE_FP handler ($C2:C040-$C2:C066, 39 bytes) ---
        # Overflow-safe rewrite; see item 6 in the module docstring. Ends at
        # $C2:C066 so the popup-number tail at $C2:C067 stays byte-identical.
        0x2C040: bytes([
            0xA4, 0xC6,              # LDY $C6
            0xB6, 0x02,              # LDX $02,y
            0xBF, 0x44, 0x00, 0x7E,  # LDA $7E0044,x
            0x29, 0xBF,              # AND #$BF
            0x09, 0x80,              # ORA #$80
            0x9F, 0x44, 0x00, 0x7E,  # STA $7E0044,x
            0xAF, 0x0C, 0xFA, 0x7E,  # LDA $7EFA0C     ; cur FP
            0x18,                    # CLC
            0x65, 0xFB,              # ADC $FB         ; + heal amount
            0xB0, 0x06,              # BCS $C05F       ; overflow -> clamp
            0xCF, 0x0D, 0xFA, 0x7E,  # CMP $7EFA0D     ; vs max FP
            0x90, 0x04,              # BCC $C063       ; under max -> keep sum
            0xAF, 0x0D, 0xFA, 0x7E,  # LDA $7EFA0D     ; clamp to max FP
            0x8F, 0x0C, 0xFA, 0x7E,  # STA $7EFA0C
        ]),

        # --- X-menu MAIN-menu FP display ($C3:1621-$C3:163E) ---
        # 2-digit print ($C3:78D2) -> 3-digit ($C3:78EC); LDX $4630 -> $462C
        # (vanilla - 2 tiles), max-ones at vanilla $4638.
        0x31622: bytes([0x2C]),
        0x3162F: bytes([0xEC]),
        0x3163F: bytes([0xEC]),

        # --- X-menu Special-menu Flowers line ($C3:35EA / shared $C3:35FF) ---
        # LDX $44B2 -> $44AE (vanilla - 2 tiles), max-ones at vanilla $44BA.
        0x335EB: bytes([0xAE]),
        0x33606: bytes([0xEC]),
        0x33616: bytes([0xEC]),

        # --- X-menu item-submenu Flowers display ($C3:2CC0) ---
        0x32CC1: bytes([0x90]),

        # --- Battle spell-menu FP header: 3-digit cur/max ---
        # Static MVN template ($C1:639D, 22 bytes): slash $7030 -> $702E,
        # digit slots blank.
        #   $7020 F | $7022 P | $7024-$702C blanks | $702E '/' |
        #   $7030-$7034 blanks
        0x1639D: bytes([
            0x14, 0x24, 0x15, 0x24, 0x00, 0x24, 0x00, 0x24,
            0x00, 0x24, 0x00, 0x24, 0x00, 0x24, 0x16, 0x24,
            0x00, 0x24, 0x00, 0x24, 0x00, 0x24,
        ]),
        # Renderer rewrite ($C1:62F6, 26 bytes). The converter writes the
        # 3 tiles itself, so no STX/STA here.
        #   REP #$30
        #   LDA $FA0C / LDY #$0028 / JSR $C6C0   ; cur FP -> $7028+
        #   LDA $FA0D / LDY #$0030 / JSR $C6C0   ; max FP -> $7030+
        #   NOP x6 (pad; falls through to $C1:6310 F-tile animator)
        0x162F6: bytes([
            0xC2, 0x30,
            0xAD, 0x0C, 0xFA, 0xA0, 0x28, 0x00, 0x20, 0xC0, 0xC6,
            0xAD, 0x0D, 0xFA, 0xA0, 0x30, 0x00, 0x20, 0xC0, 0xC6,
            0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA,
        ]),
        # --- Battle spell-cast eligibility check (signed-comparison bug) ---
        # Per-spell eligibility check at $C1:669B-$C1:66A4 runs in m8 mode
        # (entered via SEP #$20 at $C1:6686 and reached either by fall-through
        # from $C1:6698 or by BEQ from $C1:668D):
        #   LDA $FA0C / SEC / SBC $7090,Y / BPL +3 / STA $70E0,Y
        # In m8, A holds the cur FP byte. For max FP >= 128 the cur FP byte
        # for "full FP" is also >= 128, which has bit 7 set; BPL treats that
        # as negative and never branches, so STA $70E0,Y always stores a
        # shortage and every spell is greyed out.
        # Fix: change BPL ($10) to BCS ($B0) -- the unsigned branch using
        # the carry flag from SBC. Result is correct for all cur/cost in
        # 0-255 unsigned. Single byte patch at $C1:66A2.
        0x166A2: bytes([0xB0]),

        # Converter at $C1:C6C0 (29 bytes; free ROM). Reuses HP 3-digit
        # converter $C1:5D6A with stack save/restore of $8C and $8E.
        # Stack after the 3 saves: $1,S=$8E, $3,S=$8C, $5,S=A_FP.
        #   PHA                 ; save A_FP
        #   LDA $8C / PHA       ; save $8C:$8D (dialog cursor / part. base)
        #   LDA $8E / PHA       ; save $8E:$8F (dialog scratch / value-stash)
        #   STZ $8C             ; partition base = 0 for $5D6A
        #   LDA $5,S            ; peek A_FP
        #   AND #$00FF          ; mask high byte (Y still = offset)
        #   JSR $5D6A           ; HP 3-digit converter writes 3 tiles
        #   LDA $1,S / STA $8E  ; restore $8E:$8F
        #   LDA $3,S / STA $8C  ; restore $8C:$8D
        #   PLY x3              ; drain $8E, $8C, A_FP
        #   RTS
        0x1C6C0: bytes([
            0x48,
            0xA5, 0x8C, 0x48,
            0xA5, 0x8E, 0x48,
            0x64, 0x8C,
            0xA3, 0x05,
            0x29, 0xFF, 0x00,
            0x20, 0x6A, 0x5D,
            0xA3, 0x01,
            0x85, 0x8E,
            0xA3, 0x03,
            0x85, 0x8C,
            0x7A, 0x7A, 0x7A,
            0x60,
        ]),
    }
