from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_263_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 5, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_263_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_263_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_263_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_263_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_263_action_queue_async_3_SUBSCRIPT_shift_f_direction_pixels_1',
                "command": 'shift_f_direction_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_263_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
