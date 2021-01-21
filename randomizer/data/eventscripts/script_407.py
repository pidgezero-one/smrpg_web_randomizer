from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_407_set_bit_0',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_407_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_407_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_407_start_battle_3',
        "command": 'start_battle',
        "args": [0x000b, 11]
    },
    {
        "identifier": 'EVENT_407_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [1010]
    },
    {
        "identifier": 'EVENT_407_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_405_pause_action_script_6']
    },
    {
        "identifier": 'EVENT_407_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_407_ret_7',
        "command": 'ret'
    }
]
