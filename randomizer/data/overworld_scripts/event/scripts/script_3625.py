# E3625_EMPTY
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

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_3625_jmp_if_present_in_current_level_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 325, ["EVENT_3625_jmp_if_present_in_current_level_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 114, ["EVENT_3625_jmp_if_present_in_current_level_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 498, ["EVENT_3625_jmp_if_present_in_current_level_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 499, ["EVENT_3625_jmp_if_present_in_current_level_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 97, ["EVENT_3625_jmp_if_present_in_current_level_75"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 98, ["EVENT_3625_jmp_if_present_in_current_level_86"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 87, ["EVENT_3625_jmp_if_present_in_current_level_97"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_3625_jmp_if_present_in_current_level_107"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_3625_jmp_if_present_in_current_level_117"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_3625_jmp_if_present_in_current_level_127"]),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_3625_play_sound_21"]),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_0, R344_NIMBUS_LAND_ITEM_SHOP),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3625_play_sound_21"),
	SummonObjectToCurrentLevel(MEM_70A8),
	SetSyncActionScript(MEM_70A8, A0014_FLOATING_CHEST),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_4, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_25"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	DisableObjectTriggerInSpecificLevel(NPC_6, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_35"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_1, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM),
	DisableObjectTriggerInSpecificLevel(NPC_1, R498_NIMBUS_CASTLE_AREA_10_DUMMY),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_45"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_1, R498_NIMBUS_CASTLE_AREA_10_DUMMY),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_54"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_0, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_6, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_64"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	DisableObjectTriggerInSpecificLevel(NPC_6, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_75"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_2, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	DisableObjectTriggerInSpecificLevel(NPC_1, R098_ROSE_TOWN_TREASURE_HOUSE_2F),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_86"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_2, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	DisableObjectTriggerInSpecificLevel(NPC_1, R098_ROSE_TOWN_TREASURE_HOUSE_2F),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_5, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_97"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_5, R087_ROSE_TOWN_ITEM_SHOP),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_107"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_1, R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_10, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_117"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_10, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_3625_play_sound_21"], identifier="EVENT_3625_jmp_if_present_in_current_level_127"),
	JmpToSubroutine(["EVENT_3625_freeze_camera_137"]),
	SetVarToConst(ITEM_ID, HappyShellItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Inc(PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	DisableObjectTriggerInSpecificLevel(NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM),
	RememberLastObject(),
	UnfreezeCamera(),
	Return(),
	FreezeCamera(identifier="EVENT_3625_freeze_camera_137"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownSteps(2)
	]),
	Return()
])
