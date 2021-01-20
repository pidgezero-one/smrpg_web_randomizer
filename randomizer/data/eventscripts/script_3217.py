from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3217_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3217_action_queue_sync_1_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3217_action_queue_sync_1_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3217_action_queue_sync_1_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3217_action_queue_sync_1_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3217_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_dec_3',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_dec_4',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_dec_5',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_jmp_if_objects_less_than_xy_steps_apart_7',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MEM_70A8, AreaObjects.MEM_70A9, 0xc0, 0x00, 'EVENT_3217_pause_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_pause_9',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_pause_action_script_10',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_temp_action_script_sync_11',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 337],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_add_13',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 3, 'EVENT_3217_set_action_script_sync_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_add_16',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 319],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 338],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 4, 'EVENT_3217_ret_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_22',
        "command": 'set_short',
        "args": [0x7010, 0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_23',
        "command": 'set_short',
        "args": [0x7012, 0x003e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_set_short_24',
        "command": 'set_short',
        "args": [0x7014, 0x0015],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_db_25',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_pause_26',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_create_packet_event_at_coords_jmp_if_null_27',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._037_ITEM_BAG_JUMPS, 0x0cdb, 'EVENT_3217_pause_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3217_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
