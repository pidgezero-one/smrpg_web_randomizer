from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_279_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_279_add_coins_1',
        "command": 'add_coins',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_279_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_279_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 470],
        "subscript": []
    },
    {
        "identifier": 'EVENT_279_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
