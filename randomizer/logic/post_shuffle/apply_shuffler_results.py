"""Apply the results of the shuffler"""

from __future__ import annotations
from typing import (TYPE_CHECKING)


from randomizer.logic.post_shuffle.steps.assemble_hint_system import apply_hint_text
from randomizer.logic.post_shuffle.steps.calculate_boss_stats import apply_boss_stat_scaling
from randomizer.logic.post_shuffle.steps.apply_character_spells import (apply_character_spells, apply_godmode_spells)
from randomizer.logic.post_shuffle.steps.calibrate_character_base_stats import (calibrate_character_base_stats)
from randomizer.logic.post_shuffle.steps.build_room_granter_scripts import (build_room_granter_scripts)
from randomizer.logic.post_shuffle.steps.adjust_recruitment_graphics import (apply_booster_tower_gating_graphics, apply_protagonist_sprite_swaps, apply_recruitment_palette_adjustments)
from randomizer.logic.post_shuffle.steps.set_fight_run_away_flags import (set_fight_run_away_flags)
from randomizer.logic.post_shuffle.steps.adjust_win_condition_scripts import (adjust_win_condition_scripts)

from randomizer.logic.partition_calculator import (update_changed_room_partitions)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def apply_shuffler_results_to_game_data(world: GameWorld) -> None:
    apply_character_spells(world)
    calibrate_character_base_stats(world)
    apply_godmode_spells(world)
    build_room_granter_scripts(world)
    apply_booster_tower_gating_graphics(world)

    # Apply boss stat scaling after all prizes are set
    apply_boss_stat_scaling(world)

    set_fight_run_away_flags(world)
    apply_protagonist_sprite_swaps(world)
    # Update partition buffers for rooms with shuffled sprites.
    # MUST run after the per-character protagonist sprite remap above, since
    # the orchestrator reads sprite data at slots 31-37 for VRAM calculations
    # — those slots are empty placeholders until cosmetics writes them.
    update_changed_room_partitions(world)

    apply_recruitment_palette_adjustments(world)
    
    adjust_win_condition_scripts(world)


    apply_hint_text(world)


