
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

script = AnimationScriptBlock(expected_size=14, expected_beginning=0x350000, script=[
	DefineObjectQueue(["ally_behaviour_pointers"], identifier="command_0x350000"),
	DefineObjectQueue(["command_0x350402", "command_0x350412", "command_0x350422", "command_0x350432", "command_0x350442", "command_0x350402"], identifier="ally_behaviour_pointers")
])
