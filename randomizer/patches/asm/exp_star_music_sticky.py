"""EXP-star music - keep it sticky across room transitions.

Symptom
-------
With the EXP-star music decider (event 357) routing problem-BGM rooms
through PlayMusicAtCurrentVolume (SPC command $05) instead of
StopMusicFDA0 (command $08), the Invincible Star music stops the
moment the player walks into a new room - the new room's BGM takes over.
In vanilla the star music overrides room BGM until the EXP star expires.

Root cause
----------
$00:0338 is the "suppress pending music change" flag. The per-frame
music handler at $C0:F303 does LDA $0338 / BEQ apply - when the
flag is set the queued room BGM ($0332) is discarded; when clear it
is applied. $C0:F436 keeps the flag alive across rooms as long as the
queued music $0330 is the Invincible Star (CMP #$08).

StopMusicFDA0 sets $0338 = 1 - that is the whole cross-room
mechanism. But PlayMusicAtCurrentVolume runs through $C0:F36B,
which unconditionally **clears** $0338 (LDA #$00 / STA $0338 at
$C0:F387). So the decider's problem-room branch never engages the
suppression and the room BGM wins.

No event-script opcode can write $0338 (the Store* family only
reaches $0248 / $0334 / $0335 and the $704x / $708x
event-flag banks), so this must be fixed in ASM.

Fix
---
Replace the unconditional $0338 clear inside $C0:F36B with a JSL
to a helper that sets $0338 = 1 when the music being started is the
Invincible Star (ID $08) and clears it (vanilla behaviour) for any
other track::

    helper @ $CF:FF10 :
        LDA $80          ; effective music ID (already resolved by $F36B)
        CMP #$08         ; Invincible Star == EXP-star music
        BEQ +            ; -> set
        LDA #$00         ; any other track: vanilla clear
        BRA ++
      + LDA #$01         ; Invincible Star: set the suppress flag
     ++ STA $000338
        RTL

$C0:F436 then keeps the flag sticky for free (it preserves $0338
while $0330 == 8), and the flag is cleared again the moment any
non-star track is played through $F36B, so it cannot get stuck.
Track $08 is the Invincible Star, used only for the EXP-star effect,
so generalising "playing the Invincible Star -> sticky" is exactly the
intended behaviour and affects nothing else.

The accumulator is 8-bit at $C0:F387 (vanilla LDA #$00 is a
2-byte immediate) and $80 resolves through the same direct page the
music engine already uses for it, so the helper needs no mode/DP setup.
The JSL is balanced by RTL; after it the two NOP pad bytes run
and execution falls into the vanilla $C0:F38D (LDA $82).

ROM sites
---------
* $00F387 (SNES $C0:F387, 6 bytes) - hook, JSL $CF:FF10 + 2 NOP.
* $0FFF10 (SNES $CF:FF10, 17 bytes) - helper, in free space.
"""


# -----------------------------------------------------------------------
# Hook: $C0:F387 -- replace LDA #$00 / STA $0338 (A9 00 8F 38 03 00, the
# unconditional $0338 clear inside $C0:F36B) with a JSL to the helper.
# JSL is 4 bytes; pad the remaining 2 with NOP.
# -----------------------------------------------------------------------
HOOK_ROM_OFFSET = 0x00F387
HOOK_BYTES = bytes([0x22, 0x10, 0xFF, 0xCF, 0xEA, 0xEA])  # JSL $CF:FF10 / NOP / NOP

# -----------------------------------------------------------------------
# Helper @ $CF:FF10 (ROM $0FFF10) -- conditional $0338 set.
#   A5 80         LDA $80          ; effective music ID
#   C9 08         CMP #$08         ; Invincible Star?
#   F0 04         BEQ +4 ($CF:FF1A)
#   A9 00         LDA #$00         ; other track -> clear (vanilla)
#   80 02         BRA +2 ($CF:FF1C)
#   A9 01         LDA #$01         ; Invincible Star -> set
#   8F 38 03 00   STA $000338
#   6B            RTL
# -----------------------------------------------------------------------
HELPER_ROM_OFFSET = 0x0FFF10
HELPER_BYTES = bytes(
    [0xA5, 0x80, 0xC9, 0x08, 0xF0, 0x04, 0xA9, 0x00,
     0x80, 0x02, 0xA9, 0x01, 0x8F, 0x38, 0x03, 0x00, 0x6B]
)


def get_patch() -> dict[int, bytes]:
    """Return {rom_offset: bytes} for the EXP-star sticky-music fix."""
    return {
        HOOK_ROM_OFFSET: HOOK_BYTES,
        HELPER_ROM_OFFSET: HELPER_BYTES,
    }
