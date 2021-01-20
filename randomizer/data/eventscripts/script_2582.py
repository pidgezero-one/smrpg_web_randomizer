from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2582_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 5, 'EVENT_2582_ret_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2582_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2582_action_queue_sync_1_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2582_action_queue_sync_1_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2582_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_set_7010_to_object_xyz_4',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_add_6',
        "command": 'add',
        "args": [0x7000, 608],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_create_packet_at_7010_coords_jmp_if_null_9',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_2582_set_bit_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_add_frog_coins_10',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_set_bit_11',
        "command": 'set_bit',
        "args": [0x708d, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._252_BEAN_VALLEY_MAIN_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._252_BEAN_VALLEY_MAIN_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._252_BEAN_VALLEY_MAIN_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_add_15',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2582_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
