from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1568_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1568_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1568_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1568_action_queue_async_2_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1568_run_event_at_return_3',
        "command": 'run_event_at_return',
        "args": [1571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1568_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
