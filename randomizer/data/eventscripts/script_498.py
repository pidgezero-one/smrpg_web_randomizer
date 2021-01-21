from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_498_start_battle_0',
        "command": 'start_battle',
        "args": [0x0006, 21]
    },
    {
        "identifier": 'EVENT_498_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1008_set_temp_action_script_sync_7']
    },
    {
        "identifier": 'EVENT_498_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0']
    },
    {
        "identifier": 'EVENT_498_remove_object_at_70A8_from_current_level_3',
        "command": 'remove_object_at_70A8_from_current_level'
    },
    {
        "identifier": 'EVENT_498_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_498_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_498_ret_6',
        "command": 'ret'
    }
]
