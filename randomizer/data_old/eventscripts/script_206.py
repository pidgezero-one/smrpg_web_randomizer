
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_206_check_gating",
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 0,  "EVENT_206_ret"]
    },
    {
        "identifier": "EVENT_206_skip",
        "command": 'jmp_if_var_equals_const',
        "args": [0x70D5, 4,  'EVENT_206_set_bit_399']
    },
    {
        "identifier": "EVENT_206_ret",
        "command": "jmp_to_event",
        "args": [207]
    },
    {
        "identifier": 'EVENT_206_set_bit_399',
        "command": 'set_bit',
        "args": [0x7067, 4]
    },
    {
        "identifier": 'EVENT_206_set_bit_399_',
        "command": 'set_bit',
        "args": [0x706F, 3]
    },
    {
        "identifier": 'EVENT_206_run_dialog_104',
        "command": 'run_dialog',
        "args": [2261, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": "EVENT_206_ret_",
        "command": "jmp_to_event",
        "args": [207]
    }
]
