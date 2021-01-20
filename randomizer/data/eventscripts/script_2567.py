from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2567_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708d, 0, 'EVENT_2567_fade_in_from_black_async_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2567_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2567_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2567_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 0, 'EVENT_2567_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2567_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
