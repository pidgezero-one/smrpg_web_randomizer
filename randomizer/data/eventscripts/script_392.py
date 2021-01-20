from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_392_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._053_BOUNCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 136],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 133],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_pause_4',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 133],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_pause_7',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_392_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_392_pause_action_script_2'],
        "subscript": []
    }
]
