from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1854_set_0',
        "command": 'set',
        "args": [0x70a9, 22]
    },
    {
        "identifier": 'EVENT_1854_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1854_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1854_jmp_if_object_not_in_level_3',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, 'EVENT_1854_summon_to_level_5']
    },
    {
        "identifier": 'EVENT_1854_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_1854_pause_2']
    },
    {
        "identifier": 'EVENT_1854_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1854_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1854_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1854_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 824]
    },
    {
        "identifier": 'EVENT_1854_pause_8',
        "command": 'pause',
        "args": [68]
    },
    {
        "identifier": 'EVENT_1854_inc_9',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1854_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1854_pause_11',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1854_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1854_jmp_if_object_in_level_13',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, 'EVENT_1854_pause_12']
    },
    {
        "identifier": 'EVENT_1854_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1854_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1854_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1854_pause_17',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1854_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1854_action_queue_sync_18_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._119_CZAR_DRAGON_ROAR, 4]
            },
            {
                "identifier": 'EVENT_1854_action_queue_sync_18_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1854_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 824]
    },
    {
        "identifier": 'EVENT_1854_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1854_jmp_if_object_in_level_21',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, 'EVENT_1854_pause_20']
    },
    {
        "identifier": 'EVENT_1854_summon_to_level_22',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70A9, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1854_set_bit_23',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1854_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1854_pause_25',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1854_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1854_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1854_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 824]
    },
    {
        "identifier": 'EVENT_1854_pause_28',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1854_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1854_set_0']
    }
]
