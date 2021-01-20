from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3219_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 336],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3219_action_queue_sync_2_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3219_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3219_action_queue_sync_2_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3219_action_queue_sync_2_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3219_action_queue_sync_2_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3219_add_3',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 2, 'EVENT_3219_action_queue_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3219_action_queue_async_6_SUBSCRIPT_inc_palette_row_by_0',
                "command": 'inc_palette_row_by',
                "args": [255]
            },
        ]
    },
    {
        "identifier": 'EVENT_3219_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 338],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 5, 'EVENT_3219_action_queue_sync_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_set_short_9',
        "command": 'set_short',
        "args": [0x7010, 0x0011],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_set_short_10',
        "command": 'set_short',
        "args": [0x7012, 0x0012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_set_short_11',
        "command": 'set_short',
        "args": [0x7014, 0x0015],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_db_12',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_pause_13',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_create_packet_event_at_coords_jmp_if_null_14',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._038_MUSHROOM_JUMPS, 0x0c05, 'EVENT_3219_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3219_action_queue_sync_15_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3219_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 336],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 336],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3219_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
