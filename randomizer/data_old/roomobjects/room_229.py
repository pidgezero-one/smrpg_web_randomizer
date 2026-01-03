
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 2,
    "allow_extra_sprite_buffer": False,
    "extra_sprite_buffer_size": 0,
    "buffer_a": {
      "type": PartitionBufferTypes._4_SPRITES_PER_ROW,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes._3_SPRITES_PER_ROW,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_c": {
      "type": PartitionBufferTypes.COINS,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "full_palette_buffer": True,
  },
  "music": Music._26_FOREST_MAZE,
  "entrance_event": 1557,
  "event_tiles": [
    {
      "event": 2440,
      "x": 20,
      "y": 108,
      "z": 2,
      "f": Edge.SOUTHEAST,
      "length": 1,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "byte_8_bit_4": False,
    }
  ],
  "exit_fields": [
    {
      "x": 25,
      "y": 119,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA,
      "show_message": False,
      "destination_props": {
        "x": 2,
        "y": 68,
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
      "type": ObjectType.OBJECT,
      "initiator": Initiator.NONE,
      "model": 127,
      "event_script": 1551,
      "action_script": 160,
      "speed": 0,
      "npc_id_offset": 0,
      "event_offset": 0,
      "action_offset": 0,
      "visible": False,
      "x": 22,
      "y": 113,
      "z": 0,
      "z_half": False,
      "direction": RadialDirection.NORTHWEST,
      "face_on_trigger": False,
      "cant_enter_doors": True,
      "byte2_bit5": False,
      "set_sequence_playback": True,
      "cant_float": False,
      "cant_walk_up_stairs": False,
      "cant_walk_under": True,
      "cant_pass_walls": False,
      "cant_jump_through": False,
      "cant_pass_npcs": False,
      "byte3_bit5": False,
      "cant_walk_through": False,
      "byte3_bit7": False,
      "slidable_along_walls": True,
      "cant_move_if_in_air": True,
      "byte7_upper2": 0x03,
      "clones": [
        {
          "id": 1,
          "npc_id_offset": 2,
          "event_offset": 0,
          "action_offset": 0,
          "visible": False,
          "x": 22,
          "y": 113,
          "z": 0,
          "z_half": False,
          "direction": RadialDirection.NORTHWEST
        },
        {
          "id": 2,
          "npc_id_offset": 2,
          "event_offset": 0,
          "action_offset": 0,
          "visible": False,
          "x": 22,
          "y": 113,
          "z": 0,
          "z_half": False,
          "direction": RadialDirection.NORTHWEST
        },
        {
          "id": 3,
          "npc_id_offset": 2,
          "event_offset": 0,
          "action_offset": 0,
          "visible": False,
          "x": 22,
          "y": 113,
          "z": 0,
          "z_half": False,
          "direction": RadialDirection.NORTHWEST
        }
      ]
    }
  ]
}
