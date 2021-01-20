from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2552_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2552_summon_to_current_level_1',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2552_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2552_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2552_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2552_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
