from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2335_set_bit_0',
        "command": 'set_bit',
        "args": [0x709a, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708d, 2, 'EVENT_2335_remove_from_level_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2335_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_set_bit_15',
        "command": 'set_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_set_bit_16',
        "command": 'set_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_set_bit_17',
        "command": 'set_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_set_7000_to_object_coord_18',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 17, 'EVENT_2335_run_background_event_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_run_background_event_20',
        "command": 'run_background_event',
        "args": [2336, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_2335_run_event_as_subroutine_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_run_background_event_23',
        "command": 'run_background_event',
        "args": [2337, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_fade_in_from_black_async_24',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_run_event_as_subroutine_25',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_jmp_if_bit_clear_26',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2335_clear_bit_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 2, 'EVENT_2335_clear_bit_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_play_sound_29',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2335_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
