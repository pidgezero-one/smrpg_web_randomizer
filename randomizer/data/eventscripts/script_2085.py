from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2085_pause_0',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_store_character_equipment_7000_1',
        "command": 'store_character_equipment_7000',
        "args": [PlayableCharacters.MARIO, EquipSlots.ACCESSORY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 89, 'EVENT_2085_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_run_dialog_3',
        "command": 'run_dialog',
        "args": [3012, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_pause_4',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2081_run_dialog_93'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_run_dialog_6',
        "command": 'run_dialog',
        "args": [3011, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_pause_7',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2085_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2081_run_dialog_93'],
        "subscript": []
    },
]
