from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1813_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_1813_action_queue_async_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1813_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1813_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1813_action_queue_async_2_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1813_action_queue_async_2_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_1813_action_queue_async_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1813_action_queue_async_2_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1813_action_queue_async_2_SUBSCRIPT_pause_2']
            }
        ]
    },
    {
        "identifier": 'EVENT_1813_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
