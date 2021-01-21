from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_781_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 0, 'ACTION_781_play_sound_12']
    },
    {
        "identifier": 'ACTION_781_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_781_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_781_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_781_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_781_db_5',
        "command": 'db',
        "args": [0xc8, 0x91]
    },
    {
        "identifier": 'ACTION_781_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_781_run_away_shift_7',
        "command": 'run_away_shift'
    },
    {
        "identifier": 'ACTION_781_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_781_set_vram_priority_9',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_781_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_781_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_781_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._034_SQUIRM_WRITHE, 4]
    },
    {
        "identifier": 'ACTION_781_jump_to_height_silent_13',
        "command": 'jump_to_height_silent',
        "args": [48]
    },
    {
        "identifier": 'ACTION_781_run_away_shift_14',
        "command": 'run_away_shift'
    },
    {
        "identifier": 'ACTION_781_ret_15',
        "command": 'ret'
    }
]
