from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1548_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1548_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1548_action_queue_async_0_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1548_action_queue_async_0_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_1548_action_queue_async_0_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._085_FLOWER, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1548_set_1',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1548_add_max_FP_7000_2',
        "command": 'add_max_FP_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1548_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1548_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
