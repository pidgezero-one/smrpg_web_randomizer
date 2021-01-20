from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1294_add_frog_coins_0',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1294_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1294_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 6]
            },
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1294_action_queue_sync_2_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1294_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
