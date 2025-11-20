
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

script = AnimationScriptBlock(expected_size=80, expected_beginning=0x350402, script=[
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x350488", "command_0x3504AB", "command_0x3504CE", "command_0x3504F1", "command_0x350502"], identifier="command_0x350402"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x35048F", "command_0x3504B2", "command_0x3504D5", "command_0x3504F1", "command_0x350502"], identifier="command_0x350412"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x350496", "command_0x3504B9", "command_0x3504DC", "command_0x3504F1", "command_0x350502"], identifier="command_0x350422"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x35049D", "command_0x3504C0", "command_0x3504E3", "command_0x3504F1", "command_0x350502"], identifier="command_0x350432"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x3504A4", "command_0x3504C7", "command_0x3504EA", "command_0x3504F1", "command_0x350502"], identifier="command_0x350442")
])
