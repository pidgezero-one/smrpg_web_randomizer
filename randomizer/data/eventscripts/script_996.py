from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_996_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._123_PIPE_VAULT_AREA_01, RadialDirections.SOUTH, 12, 83, 0, []]
    },
    {
        "identifier": 'EVENT_996_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_996_action_queue_async_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_996_display_intro_title_2',
        "command": 'display_intro_title',
        "args": [12, IntroTitles.IN]
    },
    {
        "identifier": 'EVENT_996_fade_in_from_black_sync_duration_3',
        "command": 'fade_in_from_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_996_pause_script_until_effect_done_4',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_996_pause_5',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_996_fade_out_to_black_sync_duration_6',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_996_pause_script_until_effect_done_7',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_996_ret_8',
        "command": 'ret'
    }
]
