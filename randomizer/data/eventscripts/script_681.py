from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_681_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_681_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_681_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_681_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_681_jmp_if_object_in_air_3',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_8, 'EVENT_681_pause_2']
    },
    {
        "identifier": 'EVENT_681_run_dialog_4',
        "command": 'run_dialog',
        "args": [2198, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_681_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_681_action_queue_async_5_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_681_resume_action_script_6',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_681_ret_7',
        "command": 'ret'
    }
]
