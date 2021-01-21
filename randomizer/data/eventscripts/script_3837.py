from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3837_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3837_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3837_pause_0']
    },
    {
        "identifier": 'EVENT_3837_set_bit_2',
        "command": 'set_bit',
        "args": [0x705e, 6]
    },
    {
        "identifier": 'EVENT_3837_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3837_enable_controls_4',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3837_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3837_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 128]
    },
    {
        "identifier": 'EVENT_3837_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3837_ret_13',
        "command": 'ret'
    }
]
