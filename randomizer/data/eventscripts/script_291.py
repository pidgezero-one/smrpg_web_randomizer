from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_291_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 20, 'EVENT_291_action_queue_sync_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_291_action_queue_sync_2_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_2_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_2_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_291_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_291_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_291_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_4_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_291_action_queue_sync_4_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_291_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_291_run_dialog_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_291_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_run_dialog_7',
        "command": 'run_dialog',
        "args": [528, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_remember_last_object_8',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_run_dialog_10',
        "command": 'run_dialog',
        "args": [603, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_run_dialog_12',
        "command": 'run_dialog',
        "args": [2230, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_291_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
