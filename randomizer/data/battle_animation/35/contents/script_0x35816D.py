# pyright: reportWildcardImportFromLibrary=false
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

script = AnimationScriptBlock(expected_size=74, expected_beginning=0x35816D, script=[
	DefineObjectQueue(["command_0x3581B7", "command_0x3581B9", "command_0x3581B9", "command_0x3581BC", "command_0x3581C1", "command_0x3581C6", "command_0x3581CB", "command_0x3581D0", "command_0x3581D5", "command_0x3581DA", "command_0x3581DC", "command_0x3581DF", "command_0x3581E4", "command_0x3581E9", "command_0x3581EE", "command_0x3581F3", "command_0x3581F8", "command_0x3581FA", "command_0x3581FD", "command_0x358202", "command_0x358207", "command_0x35820C", "command_0x358217", "command_0x35821C", "command_0x358221", "command_0x358226", "command_0x358231", "command_0x358236", "command_0x35823B", "command_0x35823D", "command_0x35823D", "command_0x358240", "command_0x358242", "command_0x358245", "command_0x35824A", "command_0x35824F", "command_0x358251"], identifier="weapon_misses_pointer_table")
])
