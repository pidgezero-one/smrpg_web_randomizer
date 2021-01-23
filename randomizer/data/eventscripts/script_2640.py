from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2640_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 3, 'EVENT_2640_ret_9']
    },
    {
        "identifier": 'EVENT_2640_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2640_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2640_action_queue_sync_1_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2640_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [2644]
    },
    {
        "identifier": 'EVENT_2640_set_bit_3',
        "command": 'set_bit',
        "args": [0x7059, 3]
    },
    {
        "identifier": 'EVENT_2640_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2640_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2640_run_dialog_6',
        "command": 'run_dialog',
        "args": [3079, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2640_put_inventory_7',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_2640_inc_8',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2640_ret_9',
        "command": 'ret'
    }
]
