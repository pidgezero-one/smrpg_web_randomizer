#A0879_MONSTRO_GOOMBETTE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(3, identifier="ACTION_879_pause_0"),
	JmpIfRandom1of2(["ACTION_879_pause_0"]),
	Set700CToObjectCoord(object=NPC_1, coord=COORD_F, pixel=True),
	FaceEast7C(),
	Pause(1),
	Jmp(["ACTION_879_pause_0"])
])
