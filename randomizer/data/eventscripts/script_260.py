from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_260_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x12, 0x00]
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_mem_700C_and_const_1',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_southeast_6']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 64, 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_southwest_8']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 128, 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_northwest_10']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 192, 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_northeast_12']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_260_ret_1']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_9',
                "command": 'jmp',
                "args": ['EVENT_260_ret_1']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_260_ret_1']
            },
            {
                "identifier": 'EVENT_260_action_queue_async_0_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_260_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
