
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 1,
    "allow_extra_sprite_buffer": True,
    "extra_sprite_buffer_size": 1,
    "buffer_a": {
      "type": PartitionBufferTypes.TREASURE_CHEST,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes._4_SPRITES_PER_ROW,
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
  "music": Music._00_CURRENT,
  "entrance_event": 15,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 27,
      "y": 71,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
      "show_message": False,
      "destination_props": {
        "x": 26,
        "y": 15,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.CHEST,
      "initiator": Initiator.HIT_FROM_BELOW,
      "model": 94,
      "event_script": 172,
      "action_script": 14,
      "speed": 0,
      "star_offset": 10,
      "item_offset": 4,
      "visible": True,
      "x": 29,
      "y": 67,
      "z": 3,
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
      "cant_pass_npcs": False,
      "byte3_bit5": False,
      "cant_walk_through": True,
      "byte3_bit7": False,
      "slidable_along_walls": True,
      "cant_move_if_in_air": False,
      "byte7_upper2": 0x03,
      "clones": []
    }
  ]
}
