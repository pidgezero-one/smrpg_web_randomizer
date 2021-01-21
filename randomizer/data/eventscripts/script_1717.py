from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1717_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1717_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1717_set_short_3']
    },
    {
        "identifier": 'EVENT_1717_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [255]
    },
    {
        "identifier": 'EVENT_1717_set_short_3',
        "command": 'set_short',
        "args": [0x700e, 0x0009]
    },
    {
        "identifier": 'EVENT_1717_start_battle_700E_4',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1717_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_1717_set_bit_6',
        "command": 'set_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_1717_set_bit_7',
        "command": 'set_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_1717_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1717_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1717_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1717_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1717_set_10',
        "command": 'set',
        "args": [0x70ab, 22]
    },
    {
        "identifier": 'EVENT_1717_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1717_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1717_unfreeze_all_npcs_13',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_1717_ret_14',
        "command": 'ret'
    }
]
