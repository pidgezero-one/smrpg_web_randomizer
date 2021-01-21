from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2598_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7046, 1]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7064, 0]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7064, 1]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7064, 2]
    },
    {
        "identifier": 'EVENT_2598_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7064, 3]
    },
    {
        "identifier": 'EVENT_2598_set_14',
        "command": 'set',
        "args": [0x70da, 0]
    },
    {
        "identifier": 'EVENT_2598_set_15',
        "command": 'set',
        "args": [0x70db, 0]
    },
    {
        "identifier": 'EVENT_2598_set_16',
        "command": 'set',
        "args": [0x70dc, 0]
    },
    {
        "identifier": 'EVENT_2598_set_17',
        "command": 'set',
        "args": [0x70dd, 0]
    },
    {
        "identifier": 'EVENT_2598_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 0, 'EVENT_2598_fade_in_from_black_async_26']
    },
    {
        "identifier": 'EVENT_2598_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2598_action_queue_async_19_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2598_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2598_freeze_camera_21',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2598_set_action_script_async_22',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 482]
    },
    {
        "identifier": 'EVENT_2598_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2598_unfreeze_camera_24',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2598_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2598_fade_in_from_black_async_26',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2598_ret_27',
        "command": 'ret'
    }
]
