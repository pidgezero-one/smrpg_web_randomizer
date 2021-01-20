from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_449_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._066_KICK_BALL_SHELL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 210],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 421],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_add_short_5',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_run_dialog_7',
        "command": 'run_dialog',
        "args": [835, AreaObjects.MARIO, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_449_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
