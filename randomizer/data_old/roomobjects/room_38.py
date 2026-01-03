
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": None,
  "music": Music._32_AND_MY_NAMES_BOOSTER,
  "entrance_event": 15,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 10,
      "y": 80,
      "z": 0,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 7,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._040_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLINE_ROOM_AFTER_DEFEAT,
      "show_message": False,
      "destination_props": {
        "x": 11,
        "y": 125,
        "z": 5,
        "z_half": False,
        "f": RadialDirection.NORTHWEST,
        "x_bit_7": False
      }
    },
    {
      "x": 13,
      "y": 90,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 7,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP,
      "show_message": False,
      "destination_props": {
        "x": 28,
        "y": 55,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": []
}
