"""Randomize the ROM."""
from copy import deepcopy

from randomizer.types.world import GameWorld, Settings
from randomizer.types.patch import Patch
from randomizer.types.sprites import SpriteCollection

from randomizer.scripts.event import event_controller
from randomizer.scripts.action import action_script_bank
from randomizer.scripts.animation import (
    collection_0x02xxxx,
    collection_0x35xxxx,
    collection_0x3Axxxx,
)
from randomizer.scripts.monster import monster_script_bank
from randomizer.entities.dialogs.overworld_dialogs import dialog_table
from randomizer.entities.enemies import enemy_table
from randomizer.entities.battles import formations, packs
from randomizer.entities.characters import character_table, spotted_table
from randomizer.entities.items import item_table
from randomizer.entities.spells import spell_table
from randomizer.entities.shops import shop_table
from randomizer.entities.rooms import rooms
from randomizer.entities.progress_locations import (
    boss_star_pieces_table,
    bosses_table,
    character_spell_slots_table,
    characters_recruited_table,
    characters_spotted_table,
    item_location_table,
    flag_locations_table,
)


def randomize(
    seed: int, settings_string: str, cosmetics_string: str, debug: bool = False
) -> Patch:
    """Generate a randomized ROM patch."""
    settings = Settings(
        debug_mode=debug, flag_string=settings_string, cosmetics_string=cosmetics_string
    )
    world = GameWorld(
        seed=seed,
        settings=settings,
        event_scripts=deepcopy(event_controller),
        action_scripts=deepcopy(action_script_bank),
        flower_bonus_and_toad_tutorial_animation_scripts=deepcopy(collection_0x02xxxx),
        monsters_attacks_and_items_animation_scripts=deepcopy(collection_0x35xxxx),
        battle_event_animation_scripts=deepcopy(collection_0x3Axxxx),
        monster_scripts=deepcopy(monster_script_bank),
        dialogs=deepcopy(dialog_table),
        enemies=enemy_table,
        formations=deepcopy(formations),
        packs=deepcopy(packs),
        characters=character_table,
        spotted_characters=spotted_table,
        items=item_table,
        spells=spell_table,
        shops=shop_table,
        rooms=deepcopy(rooms),
        item_locations=item_location_table + flag_locations_table,
        boss_locations=bosses_table,
        boss_star_pieces=boss_star_pieces_table,
        character_spotted_locations=characters_spotted_table,
        character_recruit_locations=characters_recruited_table,
        character_spell_slots=character_spell_slots_table,
        sprites=SpriteCollection(),
    )
