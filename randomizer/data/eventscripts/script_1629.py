from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1629_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 5, 'EVENT_1629_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_1629_run_dialog_1',
        "command": 'run_dialog',
        "args": [1104, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1629_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1629_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_1629_run_dialog_9']
    },
    {
        "identifier": 'EVENT_1629_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 3, 'EVENT_1629_run_dialog_9']
    },
    {
        "identifier": 'EVENT_1629_run_dialog_5',
        "command": 'run_dialog',
        "args": [1165, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1629_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1629_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1629_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1629_action_queue_async_6_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1629_set_bit_7',
        "command": 'set_bit',
        "args": [0x707b, 3]
    },
    {
        "identifier": 'EVENT_1629_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1629_run_dialog_9',
        "command": 'run_dialog',
        "args": [1117, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1629_ret_10',
        "command": 'ret'
    }
]
