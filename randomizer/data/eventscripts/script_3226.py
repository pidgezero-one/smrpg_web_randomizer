from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3226_close_dialog_0',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3226_set_7000_to_current_level_1',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 160, 'EVENT_3226_apply_tile_mod_8']
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 162, 'EVENT_3226_apply_tile_mod_14']
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 163, 'EVENT_3226_apply_tile_mod_16']
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 165, 'EVENT_3226_apply_tile_mod_18']
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 167, 'EVENT_3226_apply_tile_mod_25']
    },
    {
        "identifier": 'EVENT_3226_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 172, 'EVENT_3226_apply_tile_mod_27']
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._160_SUNKEN_SHIP_AREA_01, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_set_9',
        "command": 'set',
        "args": [0x70df, 34]
    },
    {
        "identifier": 'EVENT_3226_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3226_jmp_to_event_13']
    },
    {
        "identifier": 'EVENT_3226_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": [0x2e92]
    },
    {
        "identifier": 'EVENT_3226_set_bit_12',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_14',
        "command": 'apply_tile_mod',
        "args": [Rooms._162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_15',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._163_SUNKEN_SHIP_PUZZLE_ROOM_2, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_17',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_23',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_24',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_26',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3226_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._172_SUNKEN_SHIP_PUZZLE_ROOM_5, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3226_jmp_to_event_28',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
