from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_167_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_167_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_167_floating_off_2',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_167_db_3',
        "command": 'db',
        "args": [0xc8, 0x00]
    },
    {
        "identifier": 'ACTION_167_add_short_4',
        "command": 'add_short',
        "args": [0x7016, 0xf580]
    },
    {
        "identifier": 'ACTION_167_add_short_5',
        "command": 'add_short',
        "args": [0x7018, 0x0500]
    },
    {
        "identifier": 'ACTION_167_set_short_6',
        "command": 'set_short',
        "args": [0x701a, 0x0090]
    },
    {
        "identifier": 'ACTION_167_db_7',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_167_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_167_shift_northeast_steps_9',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_167_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_167_sequence_looping_on_11',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_167_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_167_pause_13',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_167_visibility_off_14',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_167_ret_15',
        "command": 'ret'
    }
]
