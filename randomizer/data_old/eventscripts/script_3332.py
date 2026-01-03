
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3332_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._357_VOLCANO_POSTCD_AREA_01]
    },
    {
        "identifier": 'EVENT_3332_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_set_155',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3332_ret_158']
    },
    {
        "identifier": 'EVENT_3332_play_music_default_volume_156',
        "command": 'play_music_default_volume',
        "args": [Music._63_AXEM_RANGERS_DROP_IN]
    },
    {
        "identifier": 'EVENT_3332_ret_158',
        "command": 'ret'
    }
]
