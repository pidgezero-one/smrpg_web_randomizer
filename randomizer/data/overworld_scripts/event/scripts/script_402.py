# E0402_SHYSTER_HARASSING_EASTERN_GUARD
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *
from ....variables.event_palette_names import *

script = EventScript([
	SetBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0051_HENCHMAN_CONTAINER_1),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),

	Set7000ToCurrentLevel(),
	PauseActionScript(NPC_9),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R191_MUSHROOM_KINGDOM_OUTSIDE, ["e402_unoccupied_guard"]),

	
    RemoveObjectFromSpecificLevel(NPC_5, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE),
    RemoveObjectFromCurrentLevel(NPC_5),
    RemoveObjectFromSpecificLevel(NPC_10, R191_MUSHROOM_KINGDOM_OUTSIDE),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=17, y=113, z=4, direction=EAST),
		A_FaceSouthwest()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
        A_VisibilityOn(),
		A_TransferToXYZF(x=17, y=114, z=4, direction=EAST),
		A_FaceNortheast(),
        A_SetSolidityBits(cant_walk_through=True)
	]),
    Jmp(["E402_converge"]),
	
	StartAsyncEmbeddedActionScript(target=NPC_11, prefix=0xF1, subscript=[
        A_VisibilityOff(),
	], identifier="e402_unoccupied_guard"),
	RemoveObjectFromSpecificLevel(NPC_5, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromSpecificLevel(NPC_10, R191_MUSHROOM_KINGDOM_OUTSIDE),
    RemoveObjectFromSpecificLevel(NPC_11, R191_MUSHROOM_KINGDOM_OUTSIDE),
    RemoveObjectFromCurrentLevel(NPC_11),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=17, y=113, z=4, direction=EAST),
		A_FaceSouthwest()
	]),
    SummonObjectToCurrentLevel(NPC_9),
    SummonObjectToSpecificLevel(NPC_9, R191_MUSHROOM_KINGDOM_OUTSIDE),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
        A_VisibilityOn(),
		A_TransferToXYZF(x=17, y=114, z=4, direction=EAST),
		A_FaceNortheast(),
	]),


	
	SetBit(TEMP_7049_6, identifier="E402_converge"),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FadeInFromBlack(sync=False),
	Pause(30),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
    SetBit(KINGDOM_BOUNCER_FREED),
	Return()
])
