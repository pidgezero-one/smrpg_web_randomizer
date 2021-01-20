from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3166_set_7010_to_object_xyz_0',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7010, 22, 'EVENT_3166_action_queue_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7012, 74, 'EVENT_3166_action_queue_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3166_action_queue_async_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3166_action_queue_async_3_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3166_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3166_set_7010_to_object_xyz_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3166_action_queue_async_6_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3166_action_queue_async_6_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3166_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3166_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3166_set_7010_to_object_xyz_0'],
        "subscript": []
    },
]
