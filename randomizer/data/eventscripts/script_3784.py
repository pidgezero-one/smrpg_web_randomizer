from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3784_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._378_BEAN_VALLEY_BEANSTALKS_AREA_01, RadialDirections.NORTHEAST, 5, 118, 23, [_0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3784_set_bit_1',
        "command": 'set_bit',
        "args": [0x704b, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3784_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 977],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3784_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3784_action_queue_sync_3_SUBSCRIPT_floating_on_5',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3784_pause_4',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3784_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3784_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
