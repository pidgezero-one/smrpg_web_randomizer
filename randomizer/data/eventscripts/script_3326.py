from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3326_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_7000_to_current_level_2',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 390, 'EVENT_3326_jmp_if_object_not_in_level_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET, 'EVENT_3326_set_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_7, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET, 'EVENT_3326_set_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_8, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET, 'EVENT_3326_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_7',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_9, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET, 'EVENT_3326_set_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3326_clear_bit_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_9',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 'EVENT_3326_set_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_10',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_7, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 'EVENT_3326_set_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_11',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_8, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 'EVENT_3326_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_if_object_not_in_level_12',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_9, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 'EVENT_3326_set_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_3326_clear_bit_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_14',
        "command": 'set',
        "args": [0x70aa, 26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3326_pause_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_16',
        "command": 'set',
        "args": [0x70aa, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3326_pause_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_18',
        "command": 'set',
        "args": [0x70aa, 28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_3326_pause_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_20',
        "command": 'set',
        "args": [0x70aa, 29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_pause_21',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70aa],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_summon_object_at_70A8_to_current_level_24',
        "command": 'summon_object_at_70A8_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_bit_25',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 933],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3326_action_queue_sync_27_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x15]
            },
            {
                "identifier": 'EVENT_3326_action_queue_sync_27_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [33]
            },
            {
                "identifier": 'EVENT_3326_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3326_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3326_action_queue_sync_27_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3326_pause_28',
        "command": 'pause',
        "args": [68],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3326_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3326_clear_bit_0'],
        "subscript": []
    }
]
