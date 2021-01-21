from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3151_set_short_0',
        "command": 'set_short',
        "args": [0x700e, 0x0014]
    },
    {
        "identifier": 'EVENT_3151_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [17]
    },
    {
        "identifier": 'EVENT_3151_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3151_ret_6']
    },
    {
        "identifier": 'EVENT_3151_add_3',
        "command": 'add',
        "args": [0x70ae, 0x01]
    },
    {
        "identifier": 'EVENT_3151_jmp_if_var_not_equals_byte_4',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70ae, 25, 'EVENT_3151_ret_6']
    },
    {
        "identifier": 'EVENT_3151_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 439]
    },
    {
        "identifier": 'EVENT_3151_ret_6',
        "command": 'ret'
    }
]
