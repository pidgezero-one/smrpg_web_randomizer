from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2426_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_2426_remove_object_at_70A8_from_current_level_1',
        "command": 'remove_object_at_70A8_from_current_level'
    },
    {
        "identifier": 'EVENT_2426_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2426_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2426_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2426_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2426_run_dialog_6',
        "command": 'run_dialog',
        "args": [3213, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2426_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2426_put_inventory_8',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_2426_unfreeze_all_npcs_9',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_2426_ret_10',
        "command": 'ret'
    }
]
