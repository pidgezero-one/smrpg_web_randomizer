# Logic module for matching overworld sprites to area bosses.
import math

locations_with_replaceable_sprites = ["HammerBros", "Croco1", "Mack", "Belome1", "Bowyer", "Croco2", "Punchinello", "KingCalamari", "Booster", "Bundt", "Johnny", "Yaridovich",
                                      "Belome2", "Jagger", "Jinx3", "MegaSmilax", "Dodo", "Valentina", "Magikoopa", "Boomer", "CzarDragon", "AxemRangers", "Countdown", "Clerk", "Manager", "Director", "Gunyolk"]
locations_using_huge_sprites = ["Belome1", "Belome2", "Dodo"]


def approximate_dimension(num):
    base = max(num - 0x20, 0)
    return 0x20 + math.ceil(base / 8) * 8


def patch_overworld_bosses(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        ???

    """

    for location in [l for l in world.boss_locations if l.name in locations_with_replaceable_sprites]:
        shuffled_boss = None
        for enemy in location.pack.common_enemies:
            if enemy.overworld_sprite is not None:
                shuffled_boss = enemy

        if shuffled_boss is not None:
            # determine sprite to use
            battle_sprite_fits_height = approximate_dimension(
                shuffled_boss.sprite_height) <= approximate_dimension(location.sprite_height)
            battle_sprite_fits_width = approximate_dimension(shuffled_boss.sprite_width) <= approximate_dimension(
                location.sprite_width)
            battle_sprite_fits_overworld = battle_sprite_fits_height and battle_sprite_fits_width
            battle_sprite_fits_large_room = shuffled_boss.sprite_height < 80 and shuffled_boss.sprite_width < 48

            use_battle_sprite = location.name is not "Gunyolk" and (battle_sprite_fits_overworld or (
                battle_sprite_fits_large_room and location.name in locations_using_huge_sprites))

            if use_battle_sprite:
                #consider changing these to belong to objects tied to sprites instead of being direct properties
                sprite = shuffled_boss.battle_sprite
                sequence = shuffled_boss.battle_sequence
                plus = shuffled_boss.battle_sprite_plus
                freeze = shuffled_boss.battle_freeze
                sesw_only = shuffled_boss.battle_sesw_only or shuffled_boss.battle_freeze
                invert_se_sw = shuffled_boss.battle_invert_se_sw
                extra_sequence = shuffled_boss.battle_extra_sequence
                push_sequence = shuffled_boss.battle_push_sequence
                push_length = shuffled_boss.battle_push_length
                if shuffled_boss.battle_sprite == shuffled_boss.overworld_sprite:
                    overworld_is_skinny = shuffled_boss.overworld_is_skinny
                    solidity = shuffled_boss.overworld_solidity
                    y_shift = shuffled_boss.overworld_y_shift
                    shadow = shuffled_boss.shadow
                else:
                    overworld_is_skinny = False
                    solidity = shuffled_boss.battle_solidity
                    y_shift = shuffled_boss.battle_y_shift
                    shadow = 3
                    belome_shadow_off = True
                if shuffled_boss.battle_sprite == shuffled_boss.overworld_sprite:
                    overworld_is_empty = shuffled_boss.overworld_is_empty
                else:
                    overworld_is_empty = False
                statue_mold = shuffled_boss.statue_mold
            else:
        else:
            raise "What boss is this?"
