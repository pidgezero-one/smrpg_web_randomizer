
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 1,
    "allow_extra_sprite_buffer": False,
    "extra_sprite_buffer_size": 0,
    "buffer_a": {
      "type": PartitionBufferTypes.EMPTY_3,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes.EMPTY_3,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_c": {
      "type": PartitionBufferTypes.EMPTY_3,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "full_palette_buffer": True,
  },
  "music": Music._32_AND_MY_NAMES_BOOSTER,
  "entrance_event": 2417,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 11,
      "y": 127,
      "z": 5,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS,
      "show_message": False,
      "destination_props": {
        "x": 11,
        "y": 81,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.SOUTHEAST,
        "x_bit_7": False
      }
    },
    {
      "x": 16,
      "y": 125,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
      "show_message": False,
      "destination_props": {
        "x": 21,
        "y": 21,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.SOUTHEAST,
        "x_bit_7": False
      }
    }
  ],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.BATTLE,
      "initiator": Initiator.ANYTHING_EXCEPT_PRESS_A,
      "model": 278,
      "battle_pack": 50,
      "after_battle": 0,
      "action_script": 703,
      "speed": 0,
      "action_offset": 0,
      "pack_offset": 0,
      "visible": True,
      "x": 14,
      "y": 119,
      "z": 2,
      "z_half": False,
      "direction": RadialDirection.SOUTHWEST,
      "face_on_trigger": False,
      "cant_enter_doors": False,
      "byte2_bit5": False,
      "set_sequence_playback": True,
      "cant_float": False,
      "cant_walk_up_stairs": False,
      "cant_walk_under": False,
      "cant_pass_walls": False,
      "cant_jump_through": False,
      "cant_pass_npcs": True,
      "byte3_bit5": False,
      "cant_walk_through": True,
      "byte3_bit7": False,
      "slidable_along_walls": True,
      "cant_move_if_in_air": False,
      "byte7_upper2": 0x03,
      "clones": [
        {
          "id": 1,
          "action_offset": 0,
          "pack_offset": 0,
          "visible": True,
          "x": 14,
          "y": 117,
          "z": 4,
          "z_half": False,
          "direction": RadialDirection.SOUTHEAST
        },
        {
          "id": 2,
          "action_offset": 0,
          "pack_offset": 0,
          "visible": True,
          "x": 11,
          "y": 122,
          "z": 5,
          "z_half": False,
          "direction": RadialDirection.NORTHEAST
        }
      ]
    }
  ]
}
