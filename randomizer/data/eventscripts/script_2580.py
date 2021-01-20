from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2580_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 4, 'EVENT_2580_ret_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2580_action_queue_async_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2580_action_queue_async_1_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
        ]
    },
    {
        "identifier": 'EVENT_2580_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2580_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2580_action_queue_sync_2_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2580_action_queue_sync_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2580_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_set_7010_to_object_xyz_5',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_add_7',
        "command": 'add',
        "args": [0x7000, 608],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_create_packet_at_7010_coords_jmp_if_null_10',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_2580_set_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_add_frog_coins_11',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_set_bit_12',
        "command": 'set_bit',
        "args": [0x708d, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_add_15',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2580_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2580_action_queue_sync_16_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
        ]
    },
    {
        "identifier": 'EVENT_2580_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
