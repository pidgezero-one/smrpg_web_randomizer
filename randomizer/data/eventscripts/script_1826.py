from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1826_set_short_0',
        "command": 'set_short',
        "args": [0x7038, 0x1080]
    },
    {
        "identifier": 'EVENT_1826_set_short_1',
        "command": 'set_short',
        "args": [0x703a, 0x3980]
    },
    {
        "identifier": 'EVENT_1826_set_short_2',
        "command": 'set_short',
        "args": [0x703c, 0x0200]
    },
    {
        "identifier": 'EVENT_1826_run_background_event_3',
        "command": 'run_background_event',
        "args": [1828, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1826_run_background_event_4',
        "command": 'run_background_event',
        "args": [1831, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1826_run_background_event_5',
        "command": 'run_background_event',
        "args": [1832, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_1826_priority_set_6',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]]
    },
    {
        "identifier": 'EVENT_1826_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1826_play_sound_10']
    },
    {
        "identifier": 'EVENT_1826_set_8',
        "command": 'set',
        "args": [0x70cb, 10]
    },
    {
        "identifier": 'EVENT_1826_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7095, 4]
    },
    {
        "identifier": 'EVENT_1826_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 6]
    },
    {
        "identifier": 'EVENT_1826_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 822]
    },
    {
        "identifier": 'EVENT_1826_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 822]
    },
    {
        "identifier": 'EVENT_1826_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 822]
    },
    {
        "identifier": 'EVENT_1826_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [1829]
    }
]
