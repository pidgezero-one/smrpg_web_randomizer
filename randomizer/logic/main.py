"""Randomize the ROM."""
from copy import deepcopy
from randomizer.logic.place_everything import shuffle_all
from randomizer.logic.randomize_item_properties import randomize_all_items
from randomizer.logic.randomize_spells import initialize_clone_spells_and_elements

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
)
from randomizer.types.world.classes import WorldBuildingException

from .finalize_location_list import finalize_location_list


def randomize(
    seed: int, settings_string: str, cosmetics_string: str, debug: bool = False
) -> Patch:
    """Generate a randomized ROM patch."""

    while True:
        try:
            settings = Settings(
                debug_mode=debug,
                flag_string=settings_string,
                cosmetics_string=cosmetics_string,
            )
            world = GameWorld(
                seed=seed,
                settings=settings,
                event_scripts=deepcopy(event_controller),
                action_scripts=deepcopy(action_script_bank),
                flower_bonus_and_toad_tutorial_animation_scripts=deepcopy(
                    collection_0x02xxxx
                ),
                monsters_attacks_and_items_animation_scripts=deepcopy(
                    collection_0x35xxxx
                ),
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
                item_locations=item_location_table,
                boss_locations=bosses_table,
                boss_star_pieces=boss_star_pieces_table,
                character_spotted_locations=characters_spotted_table,
                character_recruit_locations=characters_recruited_table,
                character_spell_slots=character_spell_slots_table,
                sprites=SpriteCollection(),
            )

            finalize_location_list(world)
            randomize_all_items(world)
            initialize_clone_spells_and_elements(world)
            shuffle_all(world)

            # Key item size patch
            # 0xC305 = 0x20
            # 0xC37F = 0x20
            # 0xC3B5 = 0x20
            # TODO might need to be larger, recount key items
            # 0xC302 = 0xF0 0xF8
            # 0xC37C = 0xF0 0xF8
            # 0xC3B2 = 0xF0 0xF8
            # 0x2BC80 = 0xF0 0xF8 0x7F
            # 0x2BC95 = 0xF0 0xF8 0x7F
            # 0x2BCA1 = 0xF0 0xF8 0x7F
            # 0x2BCB6 = 0xF0 0xF8 0x7F
            # 0x353080 = 0xF0 0xF8 0x7F

            # Postgame weapon palettes
            # 0x25894C (sage stick palette 762): 7B 37 BD 33 39 33 F7 2E F7 2A F7 22 31 26 52 22 DE 53 10 1E 8C 15 4A 15 08 11 C6 0C 63 0C
            # 0x25896A (wonder chomp palette 763): BD 6B BD 6B 5B 47 39 3B 95 1A D7 1E 74 1A EF 15 6C 0D 09 09 A6 04 A6 04 84 04 FF 7B 63 0C
            # 0x0x25DEE4 (stella palette 756): FF 7F F5 7F EA 7F E0 7F 40 7F 80 7E E0 7D 20 7D 00 69 C0 58 A0 44 60 30 40 20 00 0C 00 00




            # TODO: reconstruct item granters according to allowed tiers
        except WorldBuildingException:
            pass
        except Exception as exc:
            raise WorldBuildingException(exc) from exc
