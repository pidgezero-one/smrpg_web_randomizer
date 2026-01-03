
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_247_room_9_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 9, "EVENT_247_room_9_logic"]
    },
    {
        "identifier": "EVENT_247_room_17_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 17, "EVENT_247_room_17_325_logic"]
    },
    {
        "identifier": "EVENT_247_room_24_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 24, "EVENT_247_room_24_logic"]
    },
    {
        "identifier": "EVENT_247_room_31_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 31, "EVENT_247_room_31_logic"]
    },
    {
        "identifier": "EVENT_247_room_33_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 33, "EVENT_247_room_33_logic"]
    },
    {
        "identifier": "EVENT_247_room_35_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 35, "EVENT_247_room_35_logic"]
    },
    {
        "identifier": "EVENT_247_room_36_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 36, "EVENT_247_room_36_logic"]
    },
    {
        "identifier": "EVENT_247_room_48_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 48, "EVENT_247_room_48_logic"]
    },
    {
        "identifier": "EVENT_247_room_59_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 59, "EVENT_247_room_59_logic"]
    },
    {
        "identifier": "EVENT_247_room_60_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 60, "EVENT_247_room_60_logic"]
    },
    {
        "identifier": "EVENT_247_room_77_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 77, "EVENT_247_room_77_logic"]
    },
    {
        "identifier": "EVENT_247_room_78_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 78, "EVENT_247_room_78_logic"]
    },
    {
        "identifier": "EVENT_247_room_80_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 80, "EVENT_247_room_80_logic"]
    },
    {
        "identifier": "EVENT_247_room_81_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 81, "EVENT_247_room_81_logic"]
    },
    {
        "identifier": "EVENT_247_room_87_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 87, "EVENT_247_room_87_logic"]
    },
    {
        "identifier": "EVENT_247_room_93_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 93, "EVENT_247_room_93_94_logic"]
    },
    {
        "identifier": "EVENT_247_room_94_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 94, "EVENT_247_room_93_94_logic"]
    },
    {
        "identifier": "EVENT_247_room_97_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 97, "EVENT_247_room_97_98_logic"]
    },
    {
        "identifier": "EVENT_247_room_98_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 98, "EVENT_247_room_97_98_logic"]
    },
    {
        "identifier": "EVENT_247_room_100_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 100, "EVENT_247_room_100_logic"]
    },
    {
        "identifier": "EVENT_247_room_111_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 111, "EVENT_247_room_111_500_logic"]
    },
    {
        "identifier": "EVENT_247_room_113_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 113, "EVENT_247_room_113_logic"]
    },
    {
        "identifier": "EVENT_247_room_114_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 114, "EVENT_247_room_114_498_logic"]
    },
    {
        "identifier": "EVENT_247_room_118_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 118, "EVENT_247_room_118_logic"]
    },
    {
        "identifier": "EVENT_247_room_121_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 121, "EVENT_247_room_121_logic"]
    },
    {
        "identifier": "EVENT_247_room_125_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 125, "EVENT_247_room_125_logic"]
    },
    {
        "identifier": "EVENT_247_room_128_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 128, "EVENT_247_room_128_logic"]
    },
    {
        "identifier": "EVENT_247_room_132_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 132, "EVENT_247_room_132_logic"]
    },
    {
        "identifier": "EVENT_247_room_133_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 133, "EVENT_247_room_133_logic"]
    },
    {
        "identifier": "EVENT_247_room_134_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 134, "EVENT_247_room_134_logic"]
    },
    {
        "identifier": "EVENT_247_room_137_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 137, "EVENT_247_room_137_logic"]
    },
    {
        "identifier": "EVENT_247_room_138_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 138, "EVENT_247_room_138_logic"]
    },
    {
        "identifier": "EVENT_247_room_141_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 141, "EVENT_247_room_141_logic"]
    },
    {
        "identifier": "EVENT_247_room_144_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 144, "EVENT_247_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_247_room_167_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 167, "EVENT_247_room_167_logic"]
    },
    {
        "identifier": "EVENT_247_room_169_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 169, "EVENT_247_room_169_logic"]
    },
    {
        "identifier": "EVENT_247_room_175_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 175, "EVENT_247_room_175_logic"]
    },
    {
        "identifier": "EVENT_247_room_179_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 179, "EVENT_247_room_179_logic"]
    },
    {
        "identifier": "EVENT_247_room_183_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 183, "EVENT_247_room_183_logic"]
    },
    {
        "identifier": "EVENT_247_room_184_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 184, "EVENT_247_room_184_logic"]
    },
    {
        "identifier": "EVENT_247_room_185_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 185, "EVENT_247_room_185_logic"]
    },
    {
        "identifier": "EVENT_247_room_196_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 196, "EVENT_247_room_196_logic"]
    },
    {
        "identifier": "EVENT_247_room_199_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 199, "EVENT_247_room_199_logic"]
    },
    {
        "identifier": "EVENT_247_room_203_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 203, "EVENT_247_room_203_logic"]
    },
    {
        "identifier": "EVENT_247_room_204_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 204, "EVENT_247_room_204_logic"]
    },
    {
        "identifier": "EVENT_247_room_206_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 206, "EVENT_247_room_206_logic"]
    },
    {
        "identifier": "EVENT_247_room_207_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 207, "EVENT_247_room_207_logic"]
    },
    {
        "identifier": "EVENT_247_room_224_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 224, "EVENT_247_room_224_logic"]
    },
    {
        "identifier": "EVENT_247_room_227_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 227, "EVENT_247_room_227_logic"]
    },
    {
        "identifier": "EVENT_247_room_228_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 228, "EVENT_247_room_228_logic"]
    },
    {
        "identifier": "EVENT_247_room_234_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 234, "EVENT_247_room_234_logic"]
    },
    {
        "identifier": "EVENT_247_room_237_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 237, "EVENT_247_room_237_logic"]
    },
    {
        "identifier": "EVENT_247_room_239_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 239, "EVENT_247_room_239_logic"]
    },
    {
        "identifier": "EVENT_247_room_242_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 242, "EVENT_247_room_242_logic"]
    },
    {
        "identifier": "EVENT_247_room_251_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 251, "EVENT_247_room_251_logic"]
    },
    {
        "identifier": "EVENT_247_room_252_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 252, "EVENT_247_room_252_logic"]
    },
    {
        "identifier": "EVENT_247_room_262_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 262, "EVENT_247_room_262_logic"]
    },
    {
        "identifier": "EVENT_247_room_263_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 263, "EVENT_247_room_263_logic"]
    },
    {
        "identifier": "EVENT_247_room_266_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 266, "EVENT_247_room_266_logic"]
    },
    {
        "identifier": "EVENT_247_room_267_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 267, "EVENT_247_room_267_logic"]
    },
    {
        "identifier": "EVENT_247_room_270_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 270, "EVENT_247_room_270_logic"]
    },
    {
        "identifier": "EVENT_247_room_280_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 280, "EVENT_247_room_280_logic"]
    },
    {
        "identifier": "EVENT_247_room_285_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 285, "EVENT_247_room_285_logic"]
    },
    {
        "identifier": "EVENT_247_room_288_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 288, "EVENT_247_room_288_logic"]
    },
    {
        "identifier": "EVENT_247_room_301_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 301, "EVENT_247_room_301_logic"]
    },
    {
        "identifier": "EVENT_247_room_321_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 321, "EVENT_247_room_321_logic"]
    },
    {
        "identifier": "EVENT_247_room_322_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 322, "EVENT_247_room_322_logic"]
    },
    {
        "identifier": "EVENT_247_room_325_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 325, "EVENT_247_room_17_325_logic"]
    },
    {
        "identifier": "EVENT_247_room_331_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 331, "EVENT_247_room_331_logic"]
    },
    {
        "identifier": "EVENT_247_room_334_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 334, "EVENT_247_room_334_logic"]
    },
    {
        "identifier": "EVENT_247_room_335_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 335, "EVENT_247_room_335_logic"]
    },
    {
        "identifier": "EVENT_247_room_344_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 344, "EVENT_247_room_344_logic"]
    },
    {
        "identifier": "EVENT_247_room_348_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 348, "EVENT_247_room_348_logic"]
    },
    {
        "identifier": "EVENT_247_room_349_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 349, "EVENT_247_room_349_logic"]
    },
    {
        "identifier": "EVENT_247_room_355_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 355, "EVENT_247_room_355_logic"]
    },
    {
        "identifier": "EVENT_247_room_366_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 366, "EVENT_247_room_366_logic"]
    },
    {
        "identifier": "EVENT_247_room_367_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 367, "EVENT_247_room_367_logic"]
    },
    {
        "identifier": "EVENT_247_room_372_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 372, "EVENT_247_room_372_logic"]
    },
    {
        "identifier": "EVENT_247_room_373_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 373, "EVENT_247_room_373_logic"]
    },
    {
        "identifier": "EVENT_247_room_379_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 379, "EVENT_247_room_379_logic"]
    },
    {
        "identifier": "EVENT_247_room_384_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 384, "EVENT_247_room_384_logic"]
    },
    {
        "identifier": "EVENT_247_room_385_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 385, "EVENT_247_room_385_logic"]
    },
    {
        "identifier": "EVENT_247_room_401_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 401, "EVENT_247_room_401_logic"]
    },
    {
        "identifier": "EVENT_247_room_405_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 405, "EVENT_247_room_405_logic"]
    },
    {
        "identifier": "EVENT_247_room_410_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 410, "EVENT_247_room_410_logic"]
    },
    {
        "identifier": "EVENT_247_room_419_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 419, "EVENT_247_room_419_logic"]
    },
    {
        "identifier": "EVENT_247_room_420_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 420, "EVENT_247_room_420_logic"]
    },
    {
        "identifier": "EVENT_247_room_421_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 421, "EVENT_247_room_421_logic"]
    },
    {
        "identifier": "EVENT_247_room_425_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 425, "EVENT_247_room_425_logic"]
    },
    {
        "identifier": "EVENT_247_room_434_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 434, "EVENT_247_room_434_logic"]
    },
    {
        "identifier": "EVENT_247_room_443_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 443, "EVENT_247_room_443_logic"]
    },
    {
        "identifier": "EVENT_247_room_446_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 446, "EVENT_247_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_247_room_451_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 451, "EVENT_247_room_451_logic"]
    },
    {
        "identifier": "EVENT_247_room_453_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 453, "EVENT_247_room_453_logic"]
    },
    {
        "identifier": "EVENT_247_room_455_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 455, "EVENT_247_room_455_logic"]
    },
    {
        "identifier": "EVENT_247_room_457_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 457, "EVENT_247_room_457_logic"]
    },
    {
        "identifier": "EVENT_247_room_458_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 458, "EVENT_247_room_458_logic"]
    },
    {
        "identifier": "EVENT_247_room_475_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 475, "EVENT_247_room_475_logic"]
    },
    {
        "identifier": "EVENT_247_room_492_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 492, "EVENT_247_room_492_logic"]
    },
    {
        "identifier": "EVENT_247_room_498_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 498, "EVENT_247_room_114_498_logic"]
    },
    {
        "identifier": "EVENT_247_room_499_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 499, "EVENT_247_room_499_logic"]
    },
    {
        "identifier": "EVENT_247_room_500_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 500, "EVENT_247_room_111_500_logic"]
    },
    {
        "identifier": "EVENT_247_cancel",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_247_room_9_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_17_325_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_24_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_31_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_31_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_33_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_35_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_36_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_48_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_59_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_60_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_77_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": 'EVENT_247_room_78_logic',
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_80_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_81_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_87_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_93_94_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_97_98_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_100_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_111_500_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_113_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_114_498_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_118_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_121_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_125_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_128_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_132_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_133_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_134_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_137_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_138_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_141_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_144_446_logic",
        "command": "set_var_to_const",
        "args": [0x70A7, 32]
    },
    {
        "identifier": "EVENT_247_room_141_logic_2",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_167_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_167_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_169_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_169_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_175_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_175_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_179_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_183_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_184_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_185_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_196_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_199_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_203_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_203_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_204_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_206_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_207_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_224_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_227_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_228_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_234_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_237_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_239_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_242_logic",
        "command": "set_var_to_const",
        "args": [0x70A7, 108]
    },
    {
        "identifier": "EVENT_247_room_242_logic_",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_251_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_252_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_262_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_263_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_266_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_266_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_267_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_270_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_280_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_280_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_285_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_288_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_301_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_321_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_322_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_331_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_331_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_334_logic",
        "command": 'jmp_to_event',
        "args": [2490]
    },
    {
        "identifier": "EVENT_247_room_335_logic",
        "command": 'jmp_to_event',
        "args": [2493]
    },
    {
        "identifier": "EVENT_247_room_344_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_348_logic",
        "command": 'jmp_to_event',
        "args": [2491]
    },
    {
        "identifier": "EVENT_247_room_349_logic",
        "command": 'jmp_to_event',
        "args": [2492]
    },
    {
        "identifier": "EVENT_247_room_355_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_366_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_367_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_367_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_372_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_373_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_379_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_384_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_385_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_401_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_405_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_410_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_419_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_420_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_420_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_421_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_425_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_434_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_443_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_451_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_247_room_451_logic_2",
        "command": 'jmp_to_event',
        "args": [3074]
    },
    {
        "identifier": "EVENT_247_room_453_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_455_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_457_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_458_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_475_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_247_room_492_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_247_room_499_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
]
