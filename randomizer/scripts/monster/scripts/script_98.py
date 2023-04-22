"""98 - Muckle"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        CastSpell(Crystal, Crystal, SpellDoNothing),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        CastSpell(Blizzard),
        Wait1TurnandRestartScript(),
    ]
)
