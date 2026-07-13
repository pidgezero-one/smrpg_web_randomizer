"""Retarget the "Victory Against Culex" fanfare at the Culex door.

The battle-end music selector at ``$C2:4C8D`` picks the victory jingle by
comparing the current formation ID against Culex's *vanilla* formation::

    C2/4C8D  AF 0E FA 7E  LDA $7EFA0E   ; current formation id
    C2/4C91  C9 5E 01     CMP #$015E    ; 350 = Culex in vanilla
    C2/4C94  D0 05        BNE +
    C2/4C96  A9 3C 00     LDA #$003C    ; song $3C "Victory Against Culex"
    C2/4C99  80 03        BRA ++
    C2/4C9B  A9 09 00     LDA #$0009    ; song $09 "Victory"
    C2/4C9E  85 E0        STA $E0       ; -> JSR $9EA5 (play song)

The randomizer renumbers every formation, so ID 350 lands on the Bowser's
Keep Greaper wave (``PACK243_OBSTACLE_GREAPER``). That fight inherits
Culex's fanfare and the real Culex never plays it.

Rewrite the CMP operand with whatever formation ends up in
``PACK216_MONSTRO_DOOR_BOSS`` so the fanfare follows the door rather than a
stale ID — it plays for whichever boss shuffle drops behind Monstro Town's
locked door.
"""

# Immediate operand of `CMP #$015E` at $C2:4C91.
CMP_OPERAND = 0x024C92


def get_patch(formation_id: int) -> dict[int, bytes]:
    assert 0 <= formation_id <= 0x1FF, f"formation id out of range: {formation_id}"
    return {CMP_OPERAND: formation_id.to_bytes(2, "little")}
