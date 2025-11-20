
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *

script = AnimationScriptBlock(expected_size=74, expected_beginning=0x358271, script=[
	DefineObjectQueue(["command_0x3582BB", "command_0x3582BB", "command_0x3582BB", "command_0x3582BE", "command_0x3582C0", "command_0x3582C0", "command_0x3582C0", "command_0x3582C3", "command_0x3582C5", "command_0x3582C8", "command_0x3582CA", "command_0x3582CA", "command_0x3582CA", "command_0x3582CA", "command_0x3582CA", "command_0x3582CD", "command_0x3582CF", "command_0x3582CF", "command_0x3582D2", "command_0x3582D4", "command_0x3582D4", "command_0x3582D7", "command_0x3582D9", "command_0x3582D9", "command_0x3582D9", "command_0x3582D9", "command_0x3582DC", "command_0x3582DE", "command_0x3582DE", "command_0x3582DE", "command_0x3582DE", "command_0x3582E1", "command_0x3582E3", "command_0x3582E6", "command_0x3582E8", "command_0x3582E8", "command_0x3582E8"], identifier="weapon_sounds_pointer_table")
])
