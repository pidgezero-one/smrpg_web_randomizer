# E3948_EMPTY

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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3948_enter_area_385"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_3948_enter_area_389"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_3948_enter_area_393"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_3948_enter_area_397"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_3948_enter_area_401"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_3948_enter_area_405"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_3948_enter_area_409"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 18, ["EVENT_3948_enter_area_413"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_3948_enter_area_417"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_3948_enter_area_421"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_3948_enter_area_425"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 26, ["EVENT_3948_enter_area_429"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_3948_enter_area_433"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_3948_enter_area_437"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 31, ["EVENT_3948_enter_area_441"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_3948_enter_area_445"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 34, ["EVENT_3948_enter_area_449"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 35, ["EVENT_3948_enter_area_453"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 36, ["EVENT_3948_enter_area_457"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 37, ["EVENT_3948_enter_area_461"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 38, ["EVENT_3948_enter_area_465"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 39, ["EVENT_3948_enter_area_469"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 40, ["EVENT_3948_enter_area_473"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_3948_enter_area_477"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 42, ["EVENT_3948_enter_area_481"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 43, ["EVENT_3948_enter_area_485"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 48, ["EVENT_3948_enter_area_489"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 55, ["EVENT_3948_enter_area_493"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 56, ["EVENT_3948_enter_area_497"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 57, ["EVENT_3948_enter_area_501"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 58, ["EVENT_3948_enter_area_505"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 59, ["EVENT_3948_enter_area_509"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 60, ["EVENT_3948_enter_area_513"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 61, ["EVENT_3948_enter_area_517"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 62, ["EVENT_3948_enter_area_521"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_3948_enter_area_525"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_3948_enter_area_529"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 66, ["EVENT_3948_enter_area_533"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 67, ["EVENT_3948_enter_area_537"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 72, ["EVENT_3948_enter_area_541"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 73, ["EVENT_3948_enter_area_545"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_3948_enter_area_549"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 75, ["EVENT_3948_enter_area_553"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 76, ["EVENT_3948_enter_area_557"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 77, ["EVENT_3948_enter_area_561"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 78, ["EVENT_3948_enter_area_565"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 79, ["EVENT_3948_enter_area_569"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 80, ["EVENT_3948_enter_area_573"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_3948_enter_area_577"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 82, ["EVENT_3948_enter_area_581"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 83, ["EVENT_3948_enter_area_585"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 84, ["EVENT_3948_enter_area_589"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 85, ["EVENT_3948_enter_area_593"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 86, ["EVENT_3948_enter_area_597"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 87, ["EVENT_3948_enter_area_601"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 92, ["EVENT_3948_enter_area_605"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3948_enter_area_609"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 94, ["EVENT_3948_enter_area_613"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 95, ["EVENT_3948_enter_area_617"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 96, ["EVENT_3948_enter_area_621"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 97, ["EVENT_3948_enter_area_625"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 98, ["EVENT_3948_enter_area_629"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 100, ["EVENT_3948_enter_area_633"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 101, ["EVENT_3948_enter_area_637"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 102, ["EVENT_3948_enter_area_641"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 103, ["EVENT_3948_enter_area_645"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 107, ["EVENT_3948_enter_area_649"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 108, ["EVENT_3948_enter_area_653"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 109, ["EVENT_3948_enter_area_657"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 110, ["EVENT_3948_enter_area_661"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 111, ["EVENT_3948_enter_area_665"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 112, ["EVENT_3948_enter_area_669"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 113, ["EVENT_3948_enter_area_673"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 114, ["EVENT_3948_enter_area_677"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 115, ["EVENT_3948_enter_area_681"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 116, ["EVENT_3948_enter_area_685"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 117, ["EVENT_3948_enter_area_689"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 118, ["EVENT_3948_enter_area_693"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 119, ["EVENT_3948_enter_area_697"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 120, ["EVENT_3948_enter_area_701"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_3948_enter_area_705"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 122, ["EVENT_3948_enter_area_709"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 123, ["EVENT_3948_enter_area_713"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 124, ["EVENT_3948_enter_area_717"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_3948_enter_area_721"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 126, ["EVENT_3948_enter_area_725"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 127, ["EVENT_3948_enter_area_729"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3948_enter_area_733"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 129, ["EVENT_3948_enter_area_737"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 130, ["EVENT_3948_enter_area_741"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 131, ["EVENT_3948_enter_area_745"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 132, ["EVENT_3948_enter_area_749"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 133, ["EVENT_3948_enter_area_753"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 134, ["EVENT_3948_enter_area_757"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 135, ["EVENT_3948_enter_area_761"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 136, ["EVENT_3948_enter_area_765"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 137, ["EVENT_3948_enter_area_769"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 138, ["EVENT_3948_enter_area_773"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 139, ["EVENT_3948_enter_area_777"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 141, ["EVENT_3948_enter_area_781"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 142, ["EVENT_3948_enter_area_785"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 143, ["EVENT_3948_enter_area_789"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_3948_enter_area_793"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 152, ["EVENT_3948_enter_area_797"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_3948_enter_area_801"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 155, ["EVENT_3948_enter_area_805"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 158, ["EVENT_3948_enter_area_809"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 159, ["EVENT_3948_enter_area_813"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 160, ["EVENT_3948_enter_area_817"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 161, ["EVENT_3948_enter_area_821"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 162, ["EVENT_3948_enter_area_825"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 163, ["EVENT_3948_enter_area_829"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 164, ["EVENT_3948_enter_area_833"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 165, ["EVENT_3948_enter_area_837"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 166, ["EVENT_3948_enter_area_841"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 167, ["EVENT_3948_enter_area_845"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 168, ["EVENT_3948_enter_area_849"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 169, ["EVENT_3948_enter_area_853"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 170, ["EVENT_3948_enter_area_857"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 171, ["EVENT_3948_enter_area_861"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 172, ["EVENT_3948_enter_area_865"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 173, ["EVENT_3948_enter_area_869"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 174, ["EVENT_3948_enter_area_873"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 175, ["EVENT_3948_enter_area_877"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 176, ["EVENT_3948_enter_area_881"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 177, ["EVENT_3948_enter_area_885"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 178, ["EVENT_3948_enter_area_889"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 179, ["EVENT_3948_enter_area_893"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 180, ["EVENT_3948_enter_area_897"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 181, ["EVENT_3948_enter_area_901"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 182, ["EVENT_3948_enter_area_905"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 183, ["EVENT_3948_enter_area_909"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 184, ["EVENT_3948_enter_area_913"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 185, ["EVENT_3948_enter_area_917"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 186, ["EVENT_3948_enter_area_921"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 187, ["EVENT_3948_enter_area_925"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 188, ["EVENT_3948_enter_area_929"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 189, ["EVENT_3948_enter_area_933"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_3948_enter_area_937"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_3948_enter_area_941"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_3948_enter_area_945"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 193, ["EVENT_3948_enter_area_949"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 194, ["EVENT_3948_enter_area_953"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 195, ["EVENT_3948_enter_area_957"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 196, ["EVENT_3948_enter_area_961"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 197, ["EVENT_3948_enter_area_965"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 198, ["EVENT_3948_enter_area_969"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_3948_enter_area_973"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 200, ["EVENT_3948_enter_area_977"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 201, ["EVENT_3948_enter_area_981"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 202, ["EVENT_3948_enter_area_985"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 203, ["EVENT_3948_enter_area_989"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 204, ["EVENT_3948_enter_area_993"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 205, ["EVENT_3948_enter_area_997"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 206, ["EVENT_3948_enter_area_1001"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 207, ["EVENT_3948_enter_area_1005"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 208, ["EVENT_3948_enter_area_1009"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 217, ["EVENT_3948_enter_area_1013"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 220, ["EVENT_3948_enter_area_1017"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 221, ["EVENT_3948_enter_area_1021"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 222, ["EVENT_3948_enter_area_1025"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 223, ["EVENT_3948_ret_1029"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 224, ["EVENT_3948_enter_area_1030"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 225, ["EVENT_3948_enter_area_1034"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 226, ["EVENT_3948_enter_area_1038"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 227, ["EVENT_3948_enter_area_1042"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 228, ["EVENT_3948_enter_area_1046"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 229, ["EVENT_3948_enter_area_1050"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 230, ["EVENT_3948_enter_area_1054"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 231, ["EVENT_3948_enter_area_1058"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_3948_enter_area_1062"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 233, ["EVENT_3948_enter_area_1066"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_3948_enter_area_1070"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 235, ["EVENT_3948_enter_area_1074"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 236, ["EVENT_3948_enter_area_1078"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 237, ["EVENT_3948_enter_area_1082"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 238, ["EVENT_3948_enter_area_1086"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 239, ["EVENT_3948_enter_area_1090"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_3948_enter_area_1094"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 251, ["EVENT_3948_enter_area_1098"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 252, ["EVENT_3948_enter_area_1102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 253, ["EVENT_3948_enter_area_1106"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 254, ["EVENT_3948_enter_area_1108"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_3948_enter_area_1112"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 256, ["EVENT_3948_enter_area_1116"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 259, ["EVENT_3948_enter_area_1120"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 262, ["EVENT_3948_enter_area_1124"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 263, ["EVENT_3948_enter_area_1128"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 264, ["EVENT_3948_enter_area_1132"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 265, ["EVENT_3948_enter_area_1136"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 266, ["EVENT_3948_enter_area_1140"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 267, ["EVENT_3948_enter_area_1144"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 268, ["EVENT_3948_enter_area_1148"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 270, ["EVENT_3948_enter_area_1152"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 272, ["EVENT_3948_enter_area_1156"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 273, ["EVENT_3948_enter_area_1160"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 274, ["EVENT_3948_enter_area_1164"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 275, ["EVENT_3948_enter_area_1168"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 276, ["EVENT_3948_enter_area_1172"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 277, ["EVENT_3948_enter_area_1176"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 278, ["EVENT_3948_enter_area_1180"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 279, ["EVENT_3948_enter_area_1184"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 280, ["EVENT_3948_enter_area_1188"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 281, ["EVENT_3948_enter_area_1192"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 282, ["EVENT_3948_enter_area_1196"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 283, ["EVENT_3948_enter_area_1200"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 284, ["EVENT_3948_enter_area_1204"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 285, ["EVENT_3948_enter_area_1208"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 286, ["EVENT_3948_enter_area_1212"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 287, ["EVENT_3948_enter_area_1216"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 288, ["EVENT_3948_enter_area_1220"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 289, ["EVENT_3948_enter_area_1224"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 290, ["EVENT_3948_enter_area_1228"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 301, ["EVENT_3948_enter_area_1232"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 302, ["EVENT_3948_enter_area_1236"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 303, ["EVENT_3948_enter_area_1240"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 313, ["EVENT_3948_enter_area_1244"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 314, ["EVENT_3948_enter_area_1248"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 316, ["EVENT_3948_enter_area_1252"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 317, ["EVENT_3948_enter_area_1256"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 318, ["EVENT_3948_enter_area_1260"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 319, ["EVENT_3948_enter_area_1264"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 321, ["EVENT_3948_enter_area_1268"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_3948_enter_area_1272"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 323, ["EVENT_3948_enter_area_1276"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 324, ["EVENT_3948_enter_area_1280"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 325, ["EVENT_3948_enter_area_1284"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 326, ["EVENT_3948_ret_1288"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 327, ["EVENT_3948_enter_area_1289"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 328, ["EVENT_3948_enter_area_1293"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 329, ["EVENT_3948_enter_area_1297"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 330, ["EVENT_3948_enter_area_1301"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 331, ["EVENT_3948_enter_area_1305"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 332, ["EVENT_3948_enter_area_1309"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 333, ["EVENT_3948_enter_area_1313"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 334, ["EVENT_3948_enter_area_1317"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 335, ["EVENT_3948_enter_area_1321"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 337, ["EVENT_3948_enter_area_1325"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 339, ["EVENT_3948_enter_area_1329"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 341, ["EVENT_3948_enter_area_1333"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 342, ["EVENT_3948_enter_area_1337"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 343, ["EVENT_3948_enter_area_1341"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 344, ["EVENT_3948_enter_area_1345"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 345, ["EVENT_3948_enter_area_1349"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 346, ["EVENT_3948_enter_area_1353"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 347, ["EVENT_3948_enter_area_1357"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 348, ["EVENT_3948_enter_area_1361"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 349, ["EVENT_3948_enter_area_1365"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 350, ["EVENT_3948_enter_area_1369"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_3948_enter_area_1373"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 353, ["EVENT_3948_enter_area_1377"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 354, ["EVENT_3948_enter_area_1381"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 355, ["EVENT_3948_enter_area_1385"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 356, ["EVENT_3948_enter_area_1389"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 357, ["EVENT_3948_enter_area_1393"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 358, ["EVENT_3948_enter_area_1397"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 359, ["EVENT_3948_enter_area_1401"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 360, ["EVENT_3948_enter_area_1405"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 361, ["EVENT_3948_enter_area_1409"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 362, ["EVENT_3948_enter_area_1413"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 363, ["EVENT_3948_enter_area_1417"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 364, ["EVENT_3948_enter_area_1421"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 365, ["EVENT_3948_enter_area_1425"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 366, ["EVENT_3948_enter_area_1429"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 367, ["EVENT_3948_enter_area_1433"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 368, ["EVENT_3948_enter_area_1437"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 369, ["EVENT_3948_enter_area_1441"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 370, ["EVENT_3948_enter_area_1445"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 371, ["EVENT_3948_enter_area_1449"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 372, ["EVENT_3948_enter_area_1453"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 373, ["EVENT_3948_enter_area_1457"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 374, ["EVENT_3948_enter_area_1461"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 376, ["EVENT_3948_enter_area_1465"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 377, ["EVENT_3948_enter_area_1469"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 378, ["EVENT_3948_enter_area_1473"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_3948_enter_area_1477"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 380, ["EVENT_3948_enter_area_1481"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 381, ["EVENT_3948_enter_area_1485"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 383, ["EVENT_3948_enter_area_1489"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 384, ["EVENT_3948_enter_area_1493"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 385, ["EVENT_3948_enter_area_1497"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 386, ["EVENT_3948_enter_area_1501"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 387, ["EVENT_3948_enter_area_1505"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 388, ["EVENT_3948_enter_area_1509"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 389, ["EVENT_3948_enter_area_1513"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 390, ["EVENT_3948_enter_area_1517"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 391, ["EVENT_3948_enter_area_1521"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 392, ["EVENT_3948_enter_area_1525"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 393, ["EVENT_3948_ret_1529"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 394, ["EVENT_3948_enter_area_1530"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 395, ["EVENT_3948_enter_area_1534"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 397, ["EVENT_3948_enter_area_1538"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 398, ["EVENT_3948_enter_area_1542"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 399, ["EVENT_3948_enter_area_1546"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 400, ["EVENT_3948_enter_area_1550"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 401, ["EVENT_3948_enter_area_1554"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 402, ["EVENT_3948_enter_area_1558"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 403, ["EVENT_3948_enter_area_1562"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 404, ["EVENT_3948_enter_area_1566"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 405, ["EVENT_3948_enter_area_1570"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 406, ["EVENT_3948_enter_area_1574"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 407, ["EVENT_3948_enter_area_1578"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 408, ["EVENT_3948_enter_area_1582"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 409, ["EVENT_3948_enter_area_1586"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 410, ["EVENT_3948_enter_area_1590"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 411, ["EVENT_3948_enter_area_1594"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 412, ["EVENT_3948_enter_area_1598"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 413, ["EVENT_3948_enter_area_1602"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 414, ["EVENT_3948_enter_area_1606"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 415, ["EVENT_3948_enter_area_1610"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 416, ["EVENT_3948_enter_area_1614"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 417, ["EVENT_3948_enter_area_1618"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 419, ["EVENT_3948_enter_area_1622"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 420, ["EVENT_3948_enter_area_1626"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_3948_enter_area_1630"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_3948_enter_area_1634"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 424, ["EVENT_3948_enter_area_1638"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_3948_enter_area_1642"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 426, ["EVENT_3948_enter_area_1646"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 428, ["EVENT_3948_enter_area_1650"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 430, ["EVENT_3948_enter_area_1654"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 431, ["EVENT_3948_enter_area_1658"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 433, ["EVENT_3948_enter_area_1662"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 434, ["EVENT_3948_enter_area_1666"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 435, ["EVENT_3948_enter_area_1670"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 436, ["EVENT_3948_enter_area_1674"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 437, ["EVENT_3948_enter_area_1678"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 438, ["EVENT_3948_enter_area_1682"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 439, ["EVENT_3948_enter_area_1686"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 440, ["EVENT_3948_enter_area_1690"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 442, ["EVENT_3948_enter_area_1694"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_3948_enter_area_1698"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 444, ["EVENT_3948_enter_area_1702"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 445, ["EVENT_3948_enter_area_1706"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_3948_enter_area_1710"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 447, ["EVENT_3948_enter_area_1714"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 448, ["EVENT_3948_enter_area_1718"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 449, ["EVENT_3948_enter_area_1722"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 450, ["EVENT_3948_enter_area_1726"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 451, ["EVENT_3948_enter_area_1730"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 452, ["EVENT_3948_enter_area_1734"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 453, ["EVENT_3948_enter_area_1738"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 454, ["EVENT_3948_enter_area_1742"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_3948_enter_area_1746"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 456, ["EVENT_3948_enter_area_1750"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_3948_enter_area_1754"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_3948_enter_area_1758"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 459, ["EVENT_3948_enter_area_1762"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 460, ["EVENT_3948_enter_area_1766"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 461, ["EVENT_3948_enter_area_1770"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 462, ["EVENT_3948_enter_area_1774"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 463, ["EVENT_3948_enter_area_1778"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 464, ["EVENT_3948_enter_area_1782"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 465, ["EVENT_3948_enter_area_1786"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 466, ["EVENT_3948_enter_area_1790"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 467, ["EVENT_3948_enter_area_1794"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 468, ["EVENT_3948_enter_area_1798"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 469, ["EVENT_3948_ret_1802"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 470, ["EVENT_3948_enter_area_1803"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 471, ["EVENT_3948_enter_area_1807"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 472, ["EVENT_3948_enter_area_1811"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 473, ["EVENT_3948_enter_area_1815"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 474, ["EVENT_3948_enter_area_1819"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 475, ["EVENT_3948_enter_area_1823"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 476, ["EVENT_3948_enter_area_1827"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 477, ["EVENT_3948_enter_area_1831"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 478, ["EVENT_3948_enter_area_1835"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 479, ["EVENT_3948_enter_area_1839"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 480, ["EVENT_3948_enter_area_1843"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 481, ["EVENT_3948_enter_area_1847"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 482, ["EVENT_3948_enter_area_1851"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 483, ["EVENT_3948_enter_area_1855"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 487, ["EVENT_3948_enter_area_1859"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 490, ["EVENT_3948_enter_area_1863"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 491, ["EVENT_3948_enter_area_1867"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_3948_enter_area_1871"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 493, ["EVENT_3948_enter_area_1875"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 496, ["EVENT_3948_jmp_1879"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 497, ["EVENT_3948_enter_area_1880"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 498, ["EVENT_3948_enter_area_1884"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 499, ["EVENT_3948_enter_area_1888"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 500, ["EVENT_3948_enter_area_1892"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 501, ["EVENT_3948_enter_area_1896"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 507, ["EVENT_3948_enter_area_1900"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 508, ["EVENT_3948_enter_area_1904"]),
	EnterArea(room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_385"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0610_MARRYMORE_OCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R007_MARRYMORE_INN_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_389"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0611_MARRYMORE_INN_LOBBY_LOADER),
	EnterArea(room_id=R009_MARRYMORE_INN_REGULAR_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_393"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0935_MARRYMORE_INN_REGULAR_ROOM_LOADER),
	EnterArea(room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_397"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0613_MARRYMORE_SUITE_LOADER),
	EnterArea(room_id=R010_BOWSERS_KEEP_1ST_TIME_AREA_04_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_401"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R016_MARIOS_PAD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_405"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1408_MARIOS_PAD_EXTERIOR_LOADER),
	EnterArea(room_id=R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_409"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0320_MUSHROOM_KINGDOM_MAIN_HALL_LOADER),
	EnterArea(room_id=R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_413"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0322_MUSHROOM_KINGDOM_THRONE_ROOM_LOADER),
	EnterArea(room_id=R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_417"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0347_TOADSTOOLS_ROOM_LOADER),
	EnterArea(room_id=R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_421"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3280_SHIP_LOWER_HENCHMAN_ROOM_LOADER),
	EnterArea(room_id=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_425"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3281_SHIP_UPPER_HENCHMAN_ROOM_LOADER),
	EnterArea(room_id=R026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_429"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_433"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_437"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3282_SHIP_BOSS_ROOM_LOADER),
	EnterArea(room_id=R031_MUSHROOM_KINGDOM_CASTLE_VAULT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_441"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_445"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0455_RESUMMON_PIPE_VAULT_ENEMIES),
	EnterArea(room_id=R034_YOSTER_ISLE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_449"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3824_YOSTER_ISLE_LOADER),
	EnterArea(room_id=R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_453"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2315_TOWER_PARACHUTE_ROOM_LOADER),
	EnterArea(room_id=R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_457"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2344_TOWER_THWOMP_SEESAW_ROOM_LOADER),
	EnterArea(room_id=R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_461"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2348_TOWER_BULLET_BILL_ROOM_LOADER),
	EnterArea(room_id=R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_465"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_469"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_473"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2417_TOWER_CHOMP_STAIRWAY_LOADER),
	EnterArea(room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_477"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1295_TOWER_CHECKERBOARD_ROOM_LOADER),
	EnterArea(room_id=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_481"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2576_TOWER_8BIT_ROOM_LOADER),
	EnterArea(room_id=R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_485"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1312_TOWER_LOBBY_LOADER),
	EnterArea(room_id=R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_489"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R055_PIPE_VAULT_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_493"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0455_RESUMMON_PIPE_VAULT_ENEMIES),
	EnterArea(room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_497"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_501"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_505"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_509"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_513"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R061_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA_RIGHT_BEFORE_FIGHT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_517"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_521"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R064_MARRYMORE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_525"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0670_MARRYMORE_UNOCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_529"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0677_MARRYMORE_UNOCCUPIED_SANCTUARY_LOADER),
	EnterArea(room_id=R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_533"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3917_ROSE_WAY_BACK_ENTRANCE_LOADER),
	EnterArea(room_id=R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_537"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3486_MIDAS_RIVER_BASE_AREA_LOADER),
	EnterArea(room_id=R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_541"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3484_MIDAS_RIVER_BOTTOM_LEFT_LOADER),
	EnterArea(room_id=R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_545"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3485_MIDAS_RIVER_BOTTOM_RIGHT_LOADER),
	EnterArea(room_id=R074_TADPOLE_POND_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_549"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1072_MELODY_BAY_LOADER),
	EnterArea(room_id=R075_TADPOLE_POND_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_553"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1104_TADPOLE_POND_LOADER),
	EnterArea(room_id=R076_BANDITS_WAY_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_557"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1714_BANDITS_WAY_1_LOADER),
	EnterArea(room_id=R077_BANDITS_WAY_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_561"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1713_BANDITS_WAY_3_LOADER),
	EnterArea(room_id=R078_BANDITS_WAY_AREA_04, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_565"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1698_BANDITS_WAY_4_LOADER),
	EnterArea(room_id=R079_ROSE_WAY_MAIN_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_569"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3148_ROSE_WAY_MAIN_ROOM_LOADER),
	EnterArea(room_id=R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_573"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_577"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R082_ROSE_WAY_WINDING_PATH_WCROOKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_581"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_585"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0529_ROSE_TOWN_OCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R084_ROSE_TOWN_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_589"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0556_ROSE_TOWN_LIBERATED_LOADER),
	EnterArea(room_id=R085_ROSE_TOWN_DURING_BOWYER_INN_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_593"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0512_ROSE_TOWN_OCCUPIED_INN_LOADER),
	EnterArea(room_id=R086_ROSE_TOWN_INN_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_597"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	EnterArea(room_id=R087_ROSE_TOWN_ITEM_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_601"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	EnterArea(room_id=R092_GRATE_GUYS_CASINO_INSIDE_CASINO, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_605"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2633_CASINO_INTERIOR_LOADER),
	EnterArea(room_id=R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_609"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0580_ROSE_TOWN_OCCUPIED_TREASURE_HOUSE_1F_LOADER),
	EnterArea(room_id=R094_ROSE_TOWN_TREASURE_HOUSE_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_613"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0575_ROSE_TOWN_LIBERATED_COUPLES_HOUSE_LOADER),
	EnterArea(room_id=R095_ROSE_TOWN_DURING_BOWYER_INN_2F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_617"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0531_ROSE_TOWN_OCCUPIED_INN_2F_LOADER),
	EnterArea(room_id=R096_ROSE_TOWN_INN_2F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_621"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0561_PLACE_LINK_IN_ROSE_TOWN),
	EnterArea(room_id=R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_625"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0537_ROSE_TOWN_TREASURE_HOUSE_2F_LOADER),
	EnterArea(room_id=R098_ROSE_TOWN_TREASURE_HOUSE_2F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_629"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0537_ROSE_TOWN_TREASURE_HOUSE_2F_LOADER),
	EnterArea(room_id=R100_BOOSTER_PASS_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_633"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2308_BOOSTER_PASS_1ST_ROOM_LOADER),
	EnterArea(room_id=R101_BOOSTER_PASS_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_637"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3919_BOOSTER_PASS_BACK_ENTRANCE_LOADER),
	EnterArea(room_id=R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_641"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1644_MOLEVILLE_OCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_645"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1893_ABYSS_BOSS_2_ROOM_LOADER),
	EnterArea(room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_649"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_653"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1649_MOLEVILLE_LIBERATED_EXTERIOR_LOADER),
	EnterArea(room_id=R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_657"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3670_NIMBUS_CASTLE_MAIN_HALL_LOADER),
	EnterArea(room_id=R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_661"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2112_NIMBUS_CASTLE_STATUE_GAME_ROOM_LOADER),
	EnterArea(room_id=R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_665"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3712_NIMBUS_CASTLE_BRIDGE_ROOM_NPC_ANIMATIONS),
	EnterArea(room_id=R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_669"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2108_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_LOADER),
	EnterArea(room_id=R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_673"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0828_NIMBUS_CASTLE_SINGLE_BIRD_STATUE_ROOM_LOADER),
	EnterArea(room_id=R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_677"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3703_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOADER),
	EnterArea(room_id=R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_681"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3730_NIMBUS_CASTLE_OCCUPIED_4_PATH_ROOM_LOADER),
	EnterArea(room_id=R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_685"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3696_NIMBUS_CASTLE_WEST_LOWER_HALL_LOADER),
	EnterArea(room_id=R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_689"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3714_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_LOADER),
	EnterArea(room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_693"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3704_NIMBUS_CASTLE_OCCUPIED_5_DOOR_ROOM_LOADER),
	EnterArea(room_id=R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_697"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3701_NIMBUS_CASTLE_LEFT_SHAMAN_ROOM_LOADER),
	EnterArea(room_id=R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_701"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3729_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_LOADER),
	EnterArea(room_id=R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_705"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3732_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_LOADER),
	EnterArea(room_id=R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_709"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3726_NIMBUS_CASTLE_ANTECHAMBER_LOADER),
	EnterArea(room_id=R123_PIPE_VAULT_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_713"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0435_PIPE_VAULT_ROOM_1_LOADER),
	EnterArea(room_id=R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_717"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
	EnterArea(room_id=R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_721"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3604_PIPE_VAULT_TRIPLE_CHEST_ROOM_LOADER),
	EnterArea(room_id=R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_725"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0434_PIPE_VAULT_RED_ROOM_LOADER),
	EnterArea(room_id=R127_PIPE_VAULT_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_729"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0428_PIPE_VAULT_THWOMP_ROOM_LOADER),
	EnterArea(room_id=R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_733"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0443_PIPE_VAULT_CHOMPWEED_ROOM_LOADER),
	EnterArea(room_id=R129_PIPE_VAULT_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_737"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0467_PIPE_VAULT_PLATFORMING_ROOM_LOADER),
	EnterArea(room_id=R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_741"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R131_SEA_AREA_04_BUNCH_OF_ZEOSTARS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_745"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_749"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3920_SEA_SAVE_ROOM_LOADER),
	EnterArea(room_id=R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_753"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3285_SEA_SINGLE_CHEST_ROOM_LOADER),
	EnterArea(room_id=R134_SEA_AREA_03_SUPER_STAR_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_757"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R135_SEA_AREA_01_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_761"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3285_SEA_SINGLE_CHEST_ROOM_LOADER),
	EnterArea(room_id=R136_SEA_AREA_07_SMALL_UNDERWATER_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_765"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R137_LANDS_END_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_769"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3819_LANDS_END_FIRST_ROOM_LOADER),
	EnterArea(room_id=R138_LANDS_END_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_773"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1567_LANDS_END_2_LOADER),
	EnterArea(room_id=R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_777"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1561_LANDS_END_GECKIT_CANNON_ROOM_LOADER),
	EnterArea(room_id=R141_LANDS_END_AREA_04_ROTATING_FLOWERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_781"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1780_LANDS_END_FLOWER_LOADER),
	EnterArea(room_id=R142_LANDS_END_AREA_05_SKY_BRIDGE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_785"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1722_SKY_BRIDGE_ROOM_LOADER),
	EnterArea(room_id=R143_PIPE_VAULT_GOOMBATHUMPING_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_789"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0454_GOOMBA_THUMPIN_ROOM_LOADER),
	EnterArea(room_id=R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_793"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_797"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0729_SEVERAL_MARRYMORE_ROOM_LOADERS),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_801"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0600_MARRYMORE_OCCUPIED_CHAPEL_LOADER),
	EnterArea(room_id=R155_MARRYMORE_CHAPEL_KITCHEN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_805"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0628_MARRYMORE_KITCHEN_LOADER),
	EnterArea(room_id=R158_STAR_HILL_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_809"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2526_STAR_HILL_1ST_ROOM_LOADER),
	EnterArea(room_id=R159_STAR_HILL_AREA_04, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_813"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2405_STAR_HILL_FINAL_AREA_LOADER),
	EnterArea(room_id=R160_SUNKEN_SHIP_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_817"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R161_SUNKEN_SHIP_AREA_03_GREAPERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_821"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_825"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R163_SUNKEN_SHIP_PUZZLE_ROOM_2, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_829"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R164_SUNKEN_SHIP_AREA_02_FROM_ENTRANCE_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_833"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3921_SHIP_FIRST_SAVE_ROOM_LOADER),
	EnterArea(room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_837"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R166_SUNKEN_SHIP_PUZZLE_ROOM_1, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_841"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3222_SHIP_TROOPA_PUZZLE_LOADER),
	EnterArea(room_id=R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_845"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R168_SUNKEN_SHIP_PUZZLE_ROOM_3, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_849"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3211_SHIP_3D_MAZE_ROOM_LOADER),
	EnterArea(room_id=R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_853"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R170_SUNKEN_SHIP_AREA_14_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_857"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R171_SUNKEN_SHIP_PUZZLE_ROOM_4, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_861"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R172_SUNKEN_SHIP_PUZZLE_ROOM_5, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_865"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3226_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_869"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0879_SHIP_TRAMPOLINE_LOADER_OVERRIDE),
	EnterArea(room_id=R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_873"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_877"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_881"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3284_SHIP_SAVE_ROOMS_LOADER),
	EnterArea(room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_885"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3224_SHIP_PASSWORD_ROOM_LOADER),
	EnterArea(room_id=R178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_889"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3292_LOWER_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_893"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3227_SHIP_CLONE_ROOM_LOADER),
	EnterArea(room_id=R180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_897"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3292_LOWER_SHIP_GENERIC_LOADER),
	EnterArea(room_id=R181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_901"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_905"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_909"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_913"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3284_SHIP_SAVE_ROOMS_LOADER),
	EnterArea(room_id=R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_917"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_921"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_925"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_929"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R189_MARIOS_PIPEHOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_933"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1392_MARIOS_HOUSE_INTERIOR_LOADER),
	EnterArea(room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_937"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0376_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R191_MUSHROOM_KINGDOM_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_941"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0723_MUSHROOM_KINGDOM_UNOCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_945"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1359_CURTAIN_GAME_ROOM_LOADER),
	EnterArea(room_id=R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_949"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0793_TOWER_FIRST_BOBOMB_STAIRCASE_LOADER),
	EnterArea(room_id=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_953"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1344_TOWER_HENCHMAN_2_ROOM_LOADER),
	EnterArea(room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_957"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1339_PORTRAIT_GAME_ROOM_LOADER),
	EnterArea(room_id=R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_961"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2335_TOWER_FIRST_STAIRCASE_LOADER),
	EnterArea(room_id=R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_965"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2340_TOWER_SEESAW_CHEST_ROOM_LOADER),
	EnterArea(room_id=R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_969"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2805_TOWER_APPRENTICE_ROOM_LOADER),
	EnterArea(room_id=R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_973"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2364_TOWER_TOP_FLOOR_CHEST_ROOM_LOADER),
	EnterArea(room_id=R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_977"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1341_ELDER_KEY_PRIZE_ROOM_LOADER),
	EnterArea(room_id=R201_BOOSTER_TOWER_6F_AREA_01_SMALL_ROOM_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_981"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2445_TOWER_SMALL_SAVE_ROOM_LOADER),
	EnterArea(room_id=R202_BOOSTER_TOWER_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_985"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1328_TOWER_EXTERIOR_LOADER),
	EnterArea(room_id=R203_MUSHROOM_WAY_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_989"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1427_MUSHROOM_WAY_1_LOADER),
	EnterArea(room_id=R204_MUSHROOM_WAY_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_993"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1423_MUSHROOM_WAY_2_LOADER),
	EnterArea(room_id=R205_MUSHROOM_WAY_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_997"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2814_MUSHROOM_WAY_3_LOADER),
	EnterArea(room_id=R206_BANDITS_WAY_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1001"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_AddConstToVar(X_COORD_2, 65532),
		A_AddConstToVar(Y_COORD_2, 65520),
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1708_BANDITS_WAY_5_LOADER),
	EnterArea(room_id=R207_BANDITS_WAY_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1005"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1702_BANDITS_WAY_2_LOADER),
	EnterArea(room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1009"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1119_SEASIDE_OCCUPIED_EXTERIOR_LOADER),
	EnterArea(room_id=R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1013"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1129_SEASIDE_OCCUPIED_ACCESSORY_SHOP_LOADER),
	EnterArea(room_id=R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1017"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2359_ABYSS_1ST_SAVE_ROOM_LOADER),
	EnterArea(room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1021"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2361_ABYSS_AMEBOID_BUTTON_ROOM_LOADER),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1025"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2362_ABYSS_FOUR_BOLT_ROOM_LOADER),
	Return(identifier="EVENT_3948_ret_1029"),
	EnterArea(room_id=R224_FOREST_MAZE_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1030"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3918_FOREST_MAZE_ENTRANCE_LOADER),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1034"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1552_FOREST_TREE_TRUNK_AREA_LOADER),
	EnterArea(room_id=R226_FOREST_MAZE_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1038"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1554_FOREST_FIRST_WIGGLER_ROOM_LOADER),
	EnterArea(room_id=R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1042"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2430_FOREST_PREMAZE_SAVE_ROOM_LOADER),
	EnterArea(room_id=R228_FOREST_MAZE_AREA_04, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1046"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2806_FOREST_MAZE_ROOM_BEFORE_TRUNK_ROOM_LOADER),
	EnterArea(room_id=R229_FOREST_MAZE_AREA_06, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1050"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1557_FOREST_MAZE_PAST_TRUNK_AREA_ROOM_LOADER),
	EnterArea(room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1054"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2431_FOREST_MAZE_AREA_LOADER),
	EnterArea(room_id=R231_FOREST_MAZE_SECRET_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1058"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2598_FOREST_SECRET_ENTRANCE_LOADER),
	EnterArea(room_id=R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1062"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0774_FOREST_MAZE_BOSS_ROOM_LOADER),
	EnterArea(room_id=R233_FOREST_MAZE_AREA_03_UNDERGROUND, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1066"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2418_FOREST_UNDERGROUND_1_LOADER),
	EnterArea(room_id=R234_FOREST_MAZE_SECRET, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1070"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2425_FOREST_MAZE_SECRET_LOADER),
	EnterArea(room_id=R235_FOREST_MAZE_AREA_08_UNDERGROUND, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1074"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2418_FOREST_UNDERGROUND_1_LOADER),
	EnterArea(room_id=R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1078"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2418_FOREST_UNDERGROUND_1_LOADER),
	EnterArea(room_id=R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1082"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2595_ABYSS_SAVE_ROOM_WITH_CHEST_LOADER),
	EnterArea(room_id=R238_SMITHY_FACTORY_FALL_FROM_LUGNUT_ROOMS_AREA_06_PRIOR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1086"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2360_ABYSS_1ST_TRAMPOLINE_CATCHER_LOADER),
	EnterArea(room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1090"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2409_ABYSS_ROOM_BEFORE_1ST_BOSS_LOADER),
	EnterArea(room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1094"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2418_FOREST_UNDERGROUND_1_LOADER),
	EnterArea(room_id=R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1098"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2476_BEAN_VALLEY_5_PIPE_AREA_LOADER),
	EnterArea(room_id=R252_BEAN_VALLEY_MAIN_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1102"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2466_BEAN_VALLEY_1ST_ROOM_LOADER),
	EnterArea(room_id=R202_BOOSTER_TOWER_ENTRANCE, face_direction=SOUTHWEST, x=5, y=114, z=15, identifier="EVENT_3948_enter_area_1106"),
	JmpToEvent(E1328_TOWER_EXTERIOR_LOADER),
	EnterArea(room_id=R254_BEAN_VALLEY_SMILAX_AREA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1108"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2555_BEAN_VALLEY_BOSS_ROOM_LOADER),
	EnterArea(room_id=R255_MONSTRO_TOWN_JINXS_DOJO, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1112"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2064_DOJO_LOADER),
	EnterArea(room_id=R256_FOREST_MAZE_SMALL_AREA_WTREE_TRUNK_UNUSED, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1116"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R259_BOOSTER_TOWER_3F_AREA_01_GREEN_SWITCH_FOR_BP_SECRET, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1120"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2338_TOWER_BUTTON_ROOM_LOADER),
	EnterArea(room_id=R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1124"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1795_LANDS_END_UNDERGROUND_LOWER_LEVEL_LOADER),
	EnterArea(room_id=R263_LANDS_END_UNDERGROUND_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1128"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1779_LANDS_END_UNDERGROUND_1_LOADER),
	EnterArea(room_id=R264_LANDS_END_UNDERGROUND_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1132"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1791_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER),
	EnterArea(room_id=R265_LANDS_END_UNDERGROUND_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1136"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1792_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER),
	EnterArea(room_id=R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1140"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2208_KEEP_1ST_BOSS_ROOM_LOADER),
	EnterArea(room_id=R267_MONSTRO_TOWN_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1144"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2090_MONSTRO_ENTRANCE_LOADER),
	EnterArea(room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1148"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1771_TEMPLE_BOSS_ROOM_LOADER),
	EnterArea(room_id=R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1152"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1676_LANDS_END_GROTTO_ROOM_1_LOADER),
	EnterArea(room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1156"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1160"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0776_MINES_TRAMPOLINE_ROOM_LOADER),
	EnterArea(room_id=R274_MOLEVILLE_MINES_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1164"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1168"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1172"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3184_MINES_FIRST_ROOM_LOADER),
	EnterArea(room_id=R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1176"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0778_MINES_LEFT_OF_TRAMPOLINE_ROOM_LOADER),
	EnterArea(room_id=R278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1180"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1184"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0784_MINES_SMALL_NORTH_ROOM_IN_MINIBOSS_PATH_LOADER),
	EnterArea(room_id=R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1188"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1192"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0782_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_LOADER),
	EnterArea(room_id=R282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1196"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1200"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0786_MINES_LONG_ROOM_IN_MINIBOSS_PATH_LOADER),
	EnterArea(room_id=R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1204"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3156_MINECART_ROOM_LOADER),
	EnterArea(room_id=R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1208"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1212"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1216"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1220"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3167_MINES_FINAL_SAVE_ROOM_LOADER),
	EnterArea(room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1224"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0592_MINES_BOSS_ROOM_LOADER_BEFORE_DEFEAT),
	EnterArea(room_id=R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1228"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3182_MINECART_PAID_LOBBY_ROOM_LOADER),
	EnterArea(room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1232"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R302_KERO_SEWERS_AREA_08_BELOMES_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1236"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0773_KERO_SEWERS_BELOME_ROOM_LOADER_CONTAINER),
	EnterArea(room_id=R303_KERO_SEWERS_AREA_08_BELOMES_ROOM_AFTER_DEFEAT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1240"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R313_SEASIDE_TOWN_ACCESSORY_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1244"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1161_SEASIDE_LIBERATED_ACCESSORY_SHOP_LOADER),
	EnterArea(room_id=R314_SEASIDE_TOWN_SHED, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1248"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1162_SEASIDE_LIBERATED_SHED_LOADER),
	EnterArea(room_id=R316_SEASIDE_TOWN_BEACH, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1252"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1163_SEASIDE_LIBERATED_BEACH),
	EnterArea(room_id=R317_LANDS_END_DESERT_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1256"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1782_LANDS_END_DESERT_1_LOADER),
	EnterArea(room_id=R318_LANDS_END_DESERT_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1260"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1787_LANDS_END_DESERT_1_RIGHT_WHIRLPOOL_SUBROUTINE),
	EnterArea(room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1264"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER),
	EnterArea(room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1268"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1824_KEEP_SET_PLATFORM_PROPERTIES),
	EnterArea(room_id=R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1272"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER),
	EnterArea(room_id=R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1276"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0764_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ANTECHAMBER_LOADER),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1280"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	Return(),
	EnterArea(room_id=R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1284"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0371_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_LOADER),
	Return(identifier="EVENT_3948_ret_1288"),
	EnterArea(room_id=R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1289"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0391_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_LOADER),
	EnterArea(room_id=R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1293"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0382_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_LOADER),
	EnterArea(room_id=R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1297"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0767_MUSHROOM_KINGDOM_OCCUPIED_EAST_HALL_LOADER),
	EnterArea(room_id=R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1301"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1305"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1309"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0384_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_LOADER),
	EnterArea(room_id=R333_KERO_SEWERS_ENTRANCE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1313"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
	EnterArea(room_id=R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1317"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2489_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_LOADER),
	EnterArea(room_id=R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1321"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2544_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_LOADER),
	EnterArea(room_id=R337_MOLEVILLE_INN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1325"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1616_MOLEVILLE_INN_LOADER),
	EnterArea(room_id=R339_MOLEVILLE_FIREWORKS_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1329"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1871_FIREWORKS_HOUSE_LOADER),
	EnterArea(room_id=R341_NIMBUS_LAND_GARROS_HOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1333"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0737_GARROS_HOUSE_LOADER),
	EnterArea(room_id=R342_NIMBUS_LAND_LOWER_HOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1337"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R343_NIMBUS_LAND_INN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1341"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3616_NIMBUS_INN_LOADER_FROM_DOOR),
	EnterArea(room_id=R344_NIMBUS_LAND_ITEM_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1345"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3624_NIMBUS_SHOP_LOADER),
	EnterArea(room_id=R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1349"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0724_NIMBUS_CROCO_HOUSE_LOADER),
	EnterArea(room_id=R346_NIMBUS_LAND_INN_BEDROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1353"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3617_NIMBUS_INN_BEDROOM_LOADER),
	EnterArea(room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1357"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2541_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER),
	EnterArea(room_id=R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1361"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2543_BEAN_VALLEY_BOTTOM_LEFT_PIPE_BASEMENT_LOADER),
	EnterArea(room_id=R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1365"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2549_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_LOADER),
	EnterArea(room_id=R350_SMITHY_FACTORY_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1369"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2399_ABYSS_ROOM_1_LOADER),
	EnterArea(room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1373"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3330_VOLCANO_1ST_BOSS_ROOM_LOADER),
	EnterArea(room_id=R353_VOLCANO_AREA_18_HINO_MART, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1377"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2096_HINO_MART_LOADER),
	EnterArea(room_id=R354_VOLCANO_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1381"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3323_VOLCANO_1ST_ROOM_LOADER),
	EnterArea(room_id=R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1385"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3333_VOLCANO_GENERIC_LOADER_2),
	EnterArea(room_id=R356_VOLCANO_AREA_08, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1389"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R357_VOLCANO_POSTCD_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1393"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3332_VOLCANO_1ST_BOSS_PATH_ROOM_LOADER),
	EnterArea(room_id=R358_VOLCANO_AREA_11, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1397"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3333_VOLCANO_GENERIC_LOADER_2),
	EnterArea(room_id=R359_VOLCANO_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1401"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3328_VOLCANO_GENERIC_LOADER_1),
	EnterArea(room_id=R360_VOLCANO_AREA_04_BUNCH_OF_STEPS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1405"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R361_VOLCANO_AREA_09, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1409"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3333_VOLCANO_GENERIC_LOADER_2),
	EnterArea(room_id=R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1413"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3336_CORKPEDITE_ROOM_LOADER),
	EnterArea(room_id=R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1417"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3336_CORKPEDITE_ROOM_LOADER),
	EnterArea(room_id=R364_VOLCANO_AREA_14, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1421"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R365_VOLCANO_POSTCD_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1425"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R366_VOLCANO_AREA_13_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1429"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3923_VOLCANO_SAVE_ROOM_LOADER),
	EnterArea(room_id=R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1433"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R368_NIMBUS_LAND_ROYAL_BUS_STATION, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1437"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3677_ROYAL_BUS_PLATFORM_LOADER),
	EnterArea(room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1441"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3761_NIMBUS_MEZZANINE_LOADER),
	EnterArea(room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1445"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3753_HOT_SPRINGS_LOBBY_LOADER),
	EnterArea(room_id=R371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1449"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1453"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1457"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1461"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1465"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2180_KEEP_CHEWY_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1469"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2185_KEEP_SPARKY_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R378_BEAN_VALLEY_BEANSTALKS_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1473"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3770_BEAN_VALLEY_1ST_VINE_ROOM_LOADER),
	EnterArea(room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1477"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1481"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1485"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1489"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3328_VOLCANO_GENERIC_LOADER_1),
	EnterArea(room_id=R384_VOLCANO_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1493"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R385_VOLCANO_AREA_06, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1497"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R386_VOLCANO_AREA_12_ERUPTING_STUMPET, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1501"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3325_STUMPET_ROOM_LOADER),
	EnterArea(room_id=R387_VOLCANO_AREA_19_FROM_HINO_MART_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1505"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3923_VOLCANO_SAVE_ROOM_LOADER),
	EnterArea(room_id=R388_VOLCANO_POSTCD_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1509"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3339_VOLCANO_2ND_BOSS_PATH_ROOM_LOADER),
	EnterArea(room_id=R389_VOLCANO_AREA_20_JUMPING_PYROSPHERES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1513"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3328_VOLCANO_GENERIC_LOADER_1),
	EnterArea(room_id=R390_VOLCANO_AREA_16_ERUPTING_STUMPET, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1517"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3325_STUMPET_ROOM_LOADER),
	EnterArea(room_id=R391_VOLCANO_POSTCD_AREA_04, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1521"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3341_VOLCANO_SMALL_BOSS_PATH_ROOM_LOADER),
	EnterArea(room_id=R392_VOLCANO_POSTCD_AREA_06, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1525"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0841_VOLCANO_FINAL_PRE_EXIT_ROOM_LOADER),
	Return(identifier="EVENT_3948_ret_1529"),
	EnterArea(room_id=R394_VOLCANO_POSTCD_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1530"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3342_VOLCANO_5TH_BOSS_PATH_ROOM_LOADER),
	EnterArea(room_id=R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1534"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2057_MONSTROMAMA_HOUSE_1F_LOADER),
	EnterArea(room_id=R397_MONSTRO_TOWN_SUPERJUMPING_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1538"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2049_MONSTRO_SUPER_JUMP_HOUSE_LOADER),
	EnterArea(room_id=R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1542"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2051_MONSTRO_SHOP_LOADER),
	EnterArea(room_id=R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1546"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2080_MUSTY_FEARS_ROOM_LOADER),
	EnterArea(room_id=R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1550"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2224_KEEP_FINAL_BOSS_ROOM_LOADER),
	EnterArea(room_id=R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1554"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1590_SEWER_PIPE_TO_LANDS_END_SUBROUTINE),
	EnterArea(room_id=R402_LANDS_END_DESERT_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1558"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1784_LANDS_END_DESERT_1_LEFT_WHIRLPOOL_SUBROUTINE),
	EnterArea(room_id=R403_LANDS_END_DESERT_AREA_05, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1562"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE),
	EnterArea(room_id=R404_LANDS_END_DESERT_AREA_04, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1566"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE),
	EnterArea(room_id=R405_BOOSTER_PASS_SECRET, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1570"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2570_BOOSTER_PASS_SECRET_LOADER),
	EnterArea(room_id=R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1574"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT),
	EnterArea(room_id=R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1578"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1777_LANDS_END_CLIFF_LOADER),
	EnterArea(room_id=R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1582"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3702_NIMBUS_CASTLE_RIGHT_SHAMAN_ROOM_LOADER),
	EnterArea(room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1586"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3679_NIMBUS_CASTLE_EGG_ROOM_LOADER),
	EnterArea(room_id=R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1590"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3707_NIMBUS_CASTLE_WEST_STAIRCASE_LOADER),
	EnterArea(room_id=R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1594"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3927_NIMBUS_CASTLE_EXIT_HALLWAY_SAVE_ROOM_LOADER),
	EnterArea(room_id=R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1598"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3725_NIMBUS_CASTLE_NOTE_HALLWAY_LOADER),
	EnterArea(room_id=R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1602"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3811_NIMBUS_INNER_CELLAR_LOADER),
	EnterArea(room_id=R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1606"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3724_NIMBUS_CASTLE_OUTER_CELLAR_LOADER),
	EnterArea(room_id=R415_NIMBUS_LAND_SMALL_PLATFORM_AFTER_NIMBUS_CASTLE_THRONE_PATHS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1610"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3737_NIMBUS_CASTLE_BACK_EXIT_LOADER),
	EnterArea(room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1614"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3642_NIMBUS_EXTERIOR_OCCUPIED_LOADER),
	EnterArea(room_id=R417_GARDENERS_HOUSE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1618"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2316_GARDENER_EXTERIOR_LOADER),
	EnterArea(room_id=R419_LAZY_SHELL_CLOUD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1622"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2317_GARDENER_CLOUD_LOADER),
	EnterArea(room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1626"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1688_TEMPLE_FORTUNE_HEADS_ROOM_LOADER),
	EnterArea(room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1630"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1770_TEMPLE_FORTUNE_RESULTS_ROOM_LOADER),
	EnterArea(room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1634"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1810_TEMPLE_VAULT_LOADER),
	EnterArea(room_id=R424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1638"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER),
	EnterArea(room_id=R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1642"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1811_TEMPLE_FOUR_CHEST_ROOM_LOADER),
	EnterArea(room_id=R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1646"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER),
	EnterArea(room_id=R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1650"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER),
	EnterArea(room_id=R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1654"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0738_NIMBUS_LAND_FINAL_BOSS_FIGHT_TOWN_SQUARE_LOADER),
	EnterArea(room_id=R431_BOWSERS_KEEP_6DOOR_PUZZLE_ROOMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1658"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R433_SMITHY_FACTORY_AREA_01_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1662"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3925_FACTORY_SAVE_ROOM_LOADERS),
	EnterArea(room_id=R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1666"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1888_ABYSS_AXEM_PIT_ROOM_LOADER),
	EnterArea(room_id=R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1670"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R436_SMITHY_FACTORY_AREA_01_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1674"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1678"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3736_NIMBUS_CASTLE_FINAL_HALLWAY_LOADER),
	EnterArea(room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1682"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3673_NIMBUS_LIBERATED_TOWN_SQUARE_LOADER),
	EnterArea(room_id=R439_BOWSERS_KEEP_OUTSIDE_TALK_TO_EXOR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1686"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1690"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3740_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_LOADER),
	EnterArea(room_id=R442_SMITHY_FACTORY_AREA_11_CONVEYOR_BELTS_SPAWNING_DRILL_BITS_AND_MACKS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1694"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1698"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1890_DETERMINE_SIDE_TREASURE_ROOM_TO_LOAD),
	EnterArea(room_id=R444_SMITHY_FACTORY_AREA_09_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1702"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R445_SMITHY_FACTORY_AREA_10_FALL_FROM_AREA_09, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1706"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1889_ABYSS_SIDE_TREASURE_ROOMS_LOADER),
	EnterArea(room_id=R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1710"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R447_NIMBUS_LAND_HOT_SPRINGS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1714"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3756_HOT_SPRINGS_LOADER),
	EnterArea(room_id=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1718"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3924_KEEP_1ST_SAVE_ROOM_LOADER),
	EnterArea(room_id=R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1722"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3373_KEEP_THWOMP_ROOM_LOADER),
	EnterArea(room_id=R450_BOWSERS_KEEP_AREA_12_CROCOS_SHOP_2_AFTER_MAGIKOOPAS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1726"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1730"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R452_BOWSERS_KEEP_AREA_06_SAVE_POINT_WCROCO_SHOP, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1734"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3924_KEEP_1ST_SAVE_ROOM_LOADER),
	EnterArea(room_id=R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1738"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2228_KEEP_DARK_ROOM_LOADER),
	EnterArea(room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1742"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3376_KEEP_6_DOOR_LOBBY_LOADER),
	EnterArea(room_id=R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1746"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1825_KEEP_ROTATING_ROOM_LOADER),
	EnterArea(room_id=R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1750"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1836_KEEP_DONKEY_ROOM_LOADER),
	EnterArea(room_id=R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1754"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1835_KEEP_CANNONBALL_ROOM_LOADER),
	EnterArea(room_id=R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1758"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER),
	EnterArea(room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1762"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2160_KEEP_TERRA_COTTA_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1766"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2165_KEEP_ALLEY_RAT_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1770"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2170_KEEP_BOBOMB_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1774"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2175_KEEP_GOOMBA_BATTLE_ROOM_LOADER),
	EnterArea(room_id=R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1778"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3354_KEEP_BARREL_COUNT_LOADER),
	EnterArea(room_id=R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1782"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1786"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3357_KEEP_BUTTON_GAME_LOADER),
	EnterArea(room_id=R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1790"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3364_KEEP_LOGIC_GAME_LOADER),
	EnterArea(room_id=R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1794"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1798"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3778_BALL_SOLITAIRE_SET_PUZZLE),
	Return(identifier="EVENT_3948_ret_1802"),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1803"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2601_FACTORY_4TH_ROOM_LOADER),
	EnterArea(room_id=R471_FACTORY_GROUNDS_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1807"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2617_FACTORY_2ND_ROOM_LOADER),
	EnterArea(room_id=R472_FACTORY_GROUNDS_AREA_03, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1811"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2621_FACTORY_3RD_ROOM_LOADER),
	EnterArea(room_id=R473_SMITHY_FACTORY_AREA_13_BOWYERS_FALLING_DOWN_CONVEYOR_BELTS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1815"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1819"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1897_ABYSS_UPPER_MACHINE_YARID_ROOM_LOADER),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1823"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1891_ABYSS_BIG_CONVEYOR_ROOM_LOADER),
	EnterArea(room_id=R476_BOWSERS_KEEP_2ND_TIME_AREA_01, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1827"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2233_KEEP_1ST_ROOM_LOADER),
	EnterArea(room_id=R477_BOWSERS_KEEP_2ND_TIME_AREA_02, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1831"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2144_KEEP_2ND_ROOM_LOADER),
	EnterArea(room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1835"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2145_KEEP_DONUT_BRIDGE_ROOM_LOADER),
	EnterArea(room_id=R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1839"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E2147_KEEP_ORIGINAL_THRONE_ROOM_LOADER),
	EnterArea(room_id=R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1843"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0393_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F_LOADER),
	EnterArea(room_id=R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1847"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0409_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_LOADER),
	EnterArea(room_id=R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1851"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0339_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_LOADER),
	EnterArea(room_id=R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1855"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0404_MUSHROOM_KINGDOM_OCCUPIED_SHOP_LOADER),
	EnterArea(room_id=R487_MUSHROOM_KINGDOM_DURING_MACK_RUNNING_KIDS_HOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1859"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	EnterArea(room_id=R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1863"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0344_MUSHROOM_KINGDOM_RAZ_RAINI_HOUSE_LOADER),
	EnterArea(room_id=R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1867"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	EnterArea(room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1871"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3831_MUSHROOM_KINGDOM_SHOP_CELLAR_MOD),
	EnterArea(room_id=R493_MUSHROOM_KINGDOM_INN_1F, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1875"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0265_OCCUPIED_MK_INN_LOADER),
	Jmp(["EVENT_3797_jmp_if_bit_set_9"], identifier="EVENT_3948_jmp_1879"),
	EnterArea(room_id=R497_NIMBUS_CASTLE_AREA_06_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1880"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0833_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_LOADER),
	EnterArea(room_id=R498_NIMBUS_CASTLE_AREA_10_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1884"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3703_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOADER),
	EnterArea(room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1888"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3762_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_LOADER),
	EnterArea(room_id=R500_NIMBUS_CASTLE_AREA_04_DUMMY, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1892"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3769_NIMBUS_CASTLE_LIBERATED_BRIDGE_ROOM_LOADER),
	EnterArea(room_id=R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1896"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E0837_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_LOADER),
	EnterArea(room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1900"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E1892_ABYSS_BOSS_1_DEFEATED_TEMP_ROOM_LOADER),
	EnterArea(room_id=R508_SMITHY_FACTORY_AREA_14_WSAVE_POINT, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3948_enter_area_1904"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferTo70167018()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_TransferTo70167018()
	]),
	JmpToEvent(E3925_FACTORY_SAVE_ROOM_LOADERS)
])
