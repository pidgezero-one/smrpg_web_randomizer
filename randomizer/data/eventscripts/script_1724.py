from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1724_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1724_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1724_pause_0']
    },
    {
        "identifier": 'EVENT_1724_fade_out_to_black_sync_duration_2',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1724_pause_script_until_effect_done_3',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_1724_db_4',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_1724_run_event_at_return_5',
        "command": 'run_event_at_return',
        "args": [1727]
    },
    {
        "identifier": 'EVENT_1724_ret_6',
        "command": 'ret'
    }
]
