"""Fix the hardcoded sprite in ending star-piece sequence #8.

The credits cutscene at ``$C3:5516`` originally does
``LDX #$0184; STX $74`` to load sprite ``$0184`` (388). In v9 sprite 388
moved into the enemy-reserved range and now renders Poundette. Redirect
the load to sprite 725 (Geno Redemption), which is the intended visual.

Patches the 2-byte LDX immediate operand at ROM ``$03:5517``.
"""

from randomizer.data.variables.sprite_names import SPR0725_GENO_REDEMPTION


def get_patch() -> dict[int, bytes]:
    return {
        0x035517: bytes([
            SPR0725_GENO_REDEMPTION & 0xFF,
            (SPR0725_GENO_REDEMPTION >> 8) & 0xFF,
        ]),
    }
