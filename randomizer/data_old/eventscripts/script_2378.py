
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2378_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2378_remove_from_current_level_95',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2378_play_sound_3',
        "command": 'run_event_as_subroutine',
        "args": [178]
    },
    {
        "identifier": 'EVENT_2378_ret_6',
        "command": 'ret'
    }
]
