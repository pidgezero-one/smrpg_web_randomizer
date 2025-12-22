from .types.gameworld import GameWorld, Settings
from .types.patch import Patch
from .data.allies.allies import ally_collection
from .data.battle_animation._02.export import bank as bank02
from .data.battle_animation._35.export import bank as bank35
from .data.battle_animation._3A.export import bank as bank3A
from .data.battle_dialogs.battle_dialogs import collection as battle_dialog_collection
from .data.dialogs.dialogs import data as dialog_collection
from .data.enemies.enemies import ENEMIES
from .data.enemy_attacks.attacks import collection as enemy_attack_collection
from .data.items.items import ITEMS
from .data.monster_ai.monster_scripts import monster_scripts
from .data.overworld_scripts.event.events import events
from .data.overworld_scripts.animation.actionqueues import actions
from .data.packets.packets import ALL_PACKETS
from .data.packs.pack_collection import pack_collection
from .data.rooms.rooms import room_collection
from .data.shops.shops import shop_collection
from .data.spells.spells import ALL_SPELLS
from .data.sprites.sprites import sprites
from .data.world_map_locations.world_map_locations import world_map_location_collection

# Current version number
VERSION = '9.0.0'

def create(seed: int | str, settings: Settings ) -> GameWorld:
    """Create a patch for the given seed."""
    return GameWorld(
        seed, 
        VERSION,
        settings, 
        ally_collection,
        {
            0x02: bank02,
            0x35: bank35,
            0x3A: bank3A,
        },
        battle_dialog_collection,
        dialog_collection,
        ENEMIES,
        enemy_attack_collection,
        ITEMS,
        monster_scripts,
        events,
        actions,
        ALL_PACKETS,
        pack_collection,
        room_collection,
        shop_collection,
        ALL_SPELLS,
        sprites,
        world_map_location_collection,
    )

