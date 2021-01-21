from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1773_enable_controls_0',
        "command": 'enable_controls',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1773_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1773_set_action_script_async_2',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 363]
    },
    {
        "identifier": 'EVENT_1773_enable_controls_3',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1773_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1773_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1773_ret_6',
        "command": 'ret'
    }
]
