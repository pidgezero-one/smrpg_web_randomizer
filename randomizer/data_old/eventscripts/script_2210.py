
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2210_play_sound_47',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_2210_tint_layers_48',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2210_tint_layers_49',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2210_reset_priority_set_50',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_2210_restore_all_hp_51',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2210_restore_all_fp_52',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2210_ret_57',
        "command": 'ret'
    }
]
