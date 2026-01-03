
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_246_room_31_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 31, "EVENT_246_room_31_logic"]
    },
    {
        "identifier": "EVENT_246_pandorite_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 60, "EVENT_246_room_60_logic"]
    },
    {
        "identifier": "EVENT_246_room_78_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 78, "EVENT_246_room_78_logic"]
    },
    {
        "identifier": "EVENT_246_room_81_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 81, "EVENT_246_room_81_logic"]
    },
    {
        "identifier": "EVENT_246_room_87_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 87, "EVENT_246_room_87_logic"]
    },
    {
        "identifier": "EVENT_246_room_93_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 93, "EVENT_246_room_93_94_logic"]
    },
    {
        "identifier": "EVENT_246_room_94_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 94, "EVENT_246_room_93_94_logic"]
    },
    {
        "identifier": "EVENT_246_room_100_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 100, "EVENT_246_room_100_logic"]
    },
    {
        "identifier": "EVENT_246_room_114_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 114, "EVENT_246_room_114_498_logic"]
    },
    {
        "identifier": "EVENT_246_room_121_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 121, "EVENT_246_room_121_logic"]
    },
    {
        "identifier": "EVENT_246_room_125_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 125, "EVENT_246_room_125_logic"]
    },
    {
        "identifier": "EVENT_246_room_128_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 128, "EVENT_246_room_128_logic"]
    },
    {
        "identifier": "EVENT_246_room_132_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 132, "EVENT_246_room_132_logic"]
    },
    {
        "identifier": "EVENT_246_room_138_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 138, "EVENT_246_room_138_logic"]
    },
    {
        "identifier": "EVENT_246_room_144_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 144, "EVENT_246_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_246_room_175_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 175, "EVENT_246_room_175_logic"]
    },
    {
        "identifier": "EVENT_246_hidon_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 184, "EVENT_246_room_184_logic"]
    },
    {
        "identifier": "EVENT_246_room_199_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 199, "EVENT_246_room_199_logic"]
    },
    {
        "identifier": "EVENT_246_room_203_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 203, "EVENT_246_room_203_logic"]
    },
    {
        "identifier": "EVENT_246_room_204_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 204, "EVENT_246_room_204_logic"]
    },
    {
        "identifier": "EVENT_246_room_234_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 234, "EVENT_246_room_234_logic"]
    },
    {
        "identifier": "EVENT_246_room_242_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 242, "EVENT_246_room_242_logic"]
    },
    {
        "identifier": "EVENT_246_room_252_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 252, "EVENT_246_room_252_logic"]
    },
    {
        "identifier": "EVENT_246_room_262_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 262, "EVENT_246_room_262_logic"]
    },
    {
        "identifier": "EVENT_246_room_270_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 270, "EVENT_246_room_270_logic"]
    },
    {
        "identifier": "EVENT_246_room_288_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 288, "EVENT_246_room_288_logic"]
    },
    {
        "identifier": "EVENT_246_room_301_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 301, "EVENT_246_room_301_logic"]
    },
    {
        "identifier": "EVENT_246_room_322_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 322, "EVENT_246_room_322_logic"]
    },
    {
        "identifier": "EVENT_246_room_331_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 331, "EVENT_246_room_331_logic"]
    },
    {
        "identifier": "EVENT_246_room_335_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 335, "EVENT_246_room_335_logic"]
    },
    {
        "identifier": "EVENT_246_room_349_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 349, "EVENT_246_room_349_logic"]
    },
    {
        "identifier": "EVENT_246_room_355_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 355, "EVENT_246_room_355_logic"]
    },
    {
        "identifier": "EVENT_246_room_366_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 366, "EVENT_246_room_366_logic"]
    },
    {
        "identifier": "EVENT_246_room_372_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 372, "EVENT_246_room_372_logic"]
    },
    {
        "identifier": "EVENT_246_room_373_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 373, "EVENT_246_room_373_logic"]
    },
    {
        "identifier": "EVENT_246_room_384_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 384, "EVENT_246_room_384_logic"]
    },
    {
        "identifier": "EVENT_246_room_405_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 405, "EVENT_246_room_405_logic"]
    },
    {
        "identifier": "EVENT_246_room_410_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 410, "EVENT_246_room_410_logic"]
    },
    {
        "identifier": "EVENT_246_room_419_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 419, "EVENT_246_room_419_logic"]
    },
    {
        "identifier": "EVENT_246_room_421_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 421, "EVENT_246_room_421_logic"]
    },
    {
        "identifier": "EVENT_246_room_425_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 425, "EVENT_246_room_425_logic"]
    },
    {
        "identifier": "EVENT_246_room_443_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 443, "EVENT_246_room_443_logic"]
    },
    {
        "identifier": "EVENT_246_room_446_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 446, "EVENT_246_room_144_446_logic"]
    },
    {
        "identifier": "EVENT_246_room_451_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 451, "EVENT_246_room_451_logic"]
    },
    {
        "identifier": "EVENT_246_room_455_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 455, "EVENT_246_room_455_logic"]
    },
    {
        "identifier": "EVENT_246_room_457_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 457, "EVENT_246_room_457_logic"]
    },
    {
        "identifier": "EVENT_246_room_458_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 458, "EVENT_246_room_458_logic"]
    },
    {
        "identifier": "EVENT_246_room_475_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 475, "EVENT_246_room_475_logic"]
    },
    {
        "identifier": "EVENT_246_room_492_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 492, "EVENT_246_room_492_logic"]
    },
    {
        "identifier": "EVENT_246_room_498_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 498, "EVENT_246_room_114_498_logic"]
    },
    {
        "identifier": "EVENT_246_cancel",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_246_room_31_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_60_logic",
        "command": 'jmp_to_event',
        "args": [3124]
    },
    {
        "identifier": "EVENT_246_room_78_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_81_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_81_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_87_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_93_94_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_100_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_114_498_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_121_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_125_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_128_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_128_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_132_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_138_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_144_446_logic",
        "command": "set_var_to_const",
        "args": [0x70A7, 29]
    },
    {
        "identifier": "EVENT_246_room_144_446_logic_2",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_175_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_175_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_184_logic",
        "command": 'jmp_to_event',
        "args": [3126]
    },
    {
        "identifier": "EVENT_246_room_199_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_203_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_203_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_204_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_234_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_242_logic",
        "command": "set_var_to_const",
        "args": [0x70A7, 32]
    },
    {
        "identifier": "EVENT_246_room_242_logic_",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_252_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_262_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_270_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_288_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_301_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_322_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_331_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_335_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_349_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_355_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_366_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_372_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_373_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_384_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_384_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_405_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_410_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_419_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_421_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_425_logic",
        "command": "set_var_to_const",
        "args": [0x70BC, 0]
    },
    {
        "identifier": "EVENT_246_room_425_logic_2",
        "command": 'jmp_to_event',
        "args": [3401]
    },
    {
        "identifier": "EVENT_246_room_443_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_451_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_455_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_457_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
    {
        "identifier": "EVENT_246_room_458_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_475_logic",
        "command": 'jmp_to_event',
        "args": [3089]
    },
    {
        "identifier": "EVENT_246_room_492_logic",
        "command": 'jmp_to_event',
        "args": [3072]
    },
]
