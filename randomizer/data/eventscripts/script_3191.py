from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3191_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_3191_ret_9']
    },
    {
        "identifier": 'EVENT_3191_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3191_action_queue_sync_1_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3191_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3191_action_queue_sync_1_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3191_action_queue_sync_1_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3191_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [1394]
    },
    {
        "identifier": 'EVENT_3191_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3191_action_queue_async_3_SUBSCRIPT_shift_east_steps_0',
                "command": 'shift_east_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3191_close_dialog_4',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3191_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3190_stop_all_background_events_0']
    },
    {
        "identifier": 'EVENT_3191_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3191_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3191_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3191_ret_9',
        "command": 'ret'
    }
]
