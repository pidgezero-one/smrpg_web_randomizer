"""Battle VRAM calculator for SMRPG formations.

Computes VRAM usage per formation based on unique enemy sprite data.
Each unique sprite contributes its animation.properties.vram_size to the total.
Duplicate enemies (same sprite ID) share VRAM and don't add to the total.

Key findings from vanilla analysis:
- All formations (inc. bosses): max unique VRAM = 24576 bytes
  (Pack 184: Cloaker+Domino+MadAdder, 3 x 8192)
- Non-boss formations only (no hidden_at_start): max unique VRAM = 14336 bytes
  85% of non-boss formations fit within 8192, 100% fit within 14336
- Boss formations: max unique VRAM = 24576 bytes (with hidden members)
- The shuffler's MAX_VRAM_SIZE=8192 is overly conservative and prevents many
  valid formations. The correct limit for shuffled (non-boss) formations is 14336.

SNES VRAM reference:
- Total SNES VRAM: 64KB
- OBJ tiles: up to 32KB (two 16KB banks)
- Battle engine allocates portions for player sprites, enemy sprites, and effects
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from collections import Counter

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
        Formation,
        FormationPack,
    )

# Based on vanilla analysis: max unique VRAM across all formations
VANILLA_MAX_UNIQUE_VRAM = 24576
# Max unique VRAM across non-boss formations (no hidden_at_start members).
# This is the correct limit for the enemy shuffler to use.
VANILLA_MAX_NONBOSS_UNIQUE_VRAM = 14336
# Default fallback if sprite lookup fails
DEFAULT_VRAM_SIZE = 2048


@dataclass
class EnemySpriteInfo:
    """VRAM information for a single enemy type in a formation."""

    enemy_name: str
    monster_id: int
    sprite_id: int
    vram_size: int
    instance_count: int


@dataclass
class FormationVRAMAnalysis:
    """VRAM analysis for a single formation."""

    formation_id: int | None
    member_count: int
    unique_sprites: list[EnemySpriteInfo]
    unique_vram_total: int
    instance_vram_total: int
    has_hidden_members: bool

    @property
    def unique_sprite_count(self) -> int:
        return len(self.unique_sprites)

    @property
    def utilization_pct(self) -> float:
        """Percentage of vanilla max VRAM used."""
        return (self.unique_vram_total / VANILLA_MAX_UNIQUE_VRAM) * 100

    def format_report(self) -> str:
        lines = [f"Formation {self.formation_id}: {self.member_count} members, "
                 f"{self.unique_sprite_count} unique sprites"]
        lines.append(f"  Unique VRAM: {self.unique_vram_total} / {VANILLA_MAX_UNIQUE_VRAM} "
                     f"({self.utilization_pct:.0f}%)")
        if self.unique_vram_total != self.instance_vram_total:
            lines.append(f"  Instance VRAM: {self.instance_vram_total} "
                         f"(shared sprites save {self.instance_vram_total - self.unique_vram_total} bytes)")
        if self.has_hidden_members:
            lines.append("  [has hidden members]")
        for sprite in self.unique_sprites:
            lines.append(f"    {sprite.enemy_name} (#{sprite.monster_id}): "
                         f"sprite {sprite.sprite_id}, {sprite.vram_size} bytes"
                         + (f" x{sprite.instance_count}" if sprite.instance_count > 1 else ""))
        return "\n".join(lines)


@dataclass
class PackVRAMAnalysis:
    """VRAM analysis for a formation pack (1-3 formations)."""

    pack_id: int
    formations: list[FormationVRAMAnalysis]
    warnings: list[str] = field(default_factory=list)

    @property
    def max_unique_vram(self) -> int:
        """Worst-case unique VRAM across all formations in the pack."""
        if not self.formations:
            return 0
        return max(f.unique_vram_total for f in self.formations)

    def format_report(self) -> str:
        lines = [f"=== Pack {self.pack_id} ==="]
        lines.append(f"Max unique VRAM: {self.max_unique_vram}")
        for formation in self.formations:
            lines.append(formation.format_report())
        if self.warnings:
            lines.append("Warnings:")
            for w in self.warnings:
                lines.append(f"  ! {w}")
        return "\n".join(lines)


def _get_enemy_vram_size(world: GameWorld, enemy_type: type) -> int:
    """Get the VRAM size for an enemy type's sprite.

    Enemy sprite IDs are monster_id + 256.
    """
    enemy = world.enemies.get_by_type(enemy_type)
    sprite_id = enemy.monster_id + 256
    try:
        sprite = world.get_sprite(sprite_id)
        return sprite.animation.properties.vram_size
    except (IndexError, AttributeError):
        return DEFAULT_VRAM_SIZE


def analyze_formation(world: GameWorld, formation: Formation) -> FormationVRAMAnalysis:
    """Analyze VRAM usage for a single formation.

    Computes unique sprite VRAM (shared sprites counted once) and
    per-instance VRAM (each enemy counted separately).
    """
    members = [m for m in formation.members if m is not None]
    has_hidden = any(m.hidden_at_start for m in members)

    # Group by enemy type to find unique sprites
    type_counts = Counter(m.enemy for m in members)

    unique_sprites: list[EnemySpriteInfo] = []
    for enemy_type, count in type_counts.items():
        enemy = world.enemies.get_by_type(enemy_type)
        sprite_id = enemy.monster_id + 256
        vram = _get_enemy_vram_size(world, enemy_type)
        unique_sprites.append(EnemySpriteInfo(
            enemy_name=type(enemy).__name__,
            monster_id=enemy.monster_id,
            sprite_id=sprite_id,
            vram_size=vram,
            instance_count=count,
        ))

    unique_vram = sum(s.vram_size for s in unique_sprites)
    instance_vram = sum(s.vram_size * s.instance_count for s in unique_sprites)

    return FormationVRAMAnalysis(
        formation_id=formation._formation_id,
        member_count=len(members),
        unique_sprites=unique_sprites,
        unique_vram_total=unique_vram,
        instance_vram_total=instance_vram,
        has_hidden_members=has_hidden,
    )


def analyze_pack(world: GameWorld, pack_id: int) -> PackVRAMAnalysis:
    """Analyze VRAM usage for a formation pack."""
    pack = world.battle_packs.packs[pack_id]
    warnings: list[str] = []

    formation_analyses = []
    for formation in pack.formations:
        members = [m for m in formation.members if m is not None]
        if not members:
            continue
        analysis = analyze_formation(world, formation)
        formation_analyses.append(analysis)

        if analysis.unique_vram_total > VANILLA_MAX_UNIQUE_VRAM:
            warnings.append(
                f"Formation {analysis.formation_id}: unique VRAM {analysis.unique_vram_total} "
                f"exceeds vanilla max {VANILLA_MAX_UNIQUE_VRAM}"
            )

    return PackVRAMAnalysis(
        pack_id=pack_id,
        formations=formation_analyses,
        warnings=warnings,
    )


def scan_all_formations(world: GameWorld) -> list[PackVRAMAnalysis]:
    """Scan all packs and return analyses sorted by max unique VRAM (descending)."""
    results = []
    for pack_id in range(len(world.battle_packs.packs)):
        analysis = analyze_pack(world, pack_id)
        if analysis.formations:
            results.append(analysis)
    results.sort(key=lambda a: a.max_unique_vram, reverse=True)
    return results


def format_vram_summary(analyses: list[PackVRAMAnalysis]) -> str:
    """Format a summary of all formation VRAM usage."""
    if not analyses:
        return "No formations to analyze."

    total = len(analyses)
    max_vram = analyses[0].max_unique_vram if analyses else 0

    # Count by threshold
    thresholds = [8192, 12288, 16384, 20480, VANILLA_MAX_UNIQUE_VRAM]
    lines = [f"=== Battle VRAM Summary ({total} packs) ==="]
    lines.append(f"Highest unique VRAM: {max_vram} bytes")
    lines.append("")

    for threshold in thresholds:
        count = sum(1 for a in analyses if a.max_unique_vram <= threshold)
        lines.append(f"  <= {threshold:5d} bytes: {count:3d} / {total} ({count * 100 // total}%)")

    over_vanilla = [a for a in analyses if a.max_unique_vram > VANILLA_MAX_UNIQUE_VRAM]
    if over_vanilla:
        lines.append(f"\n{len(over_vanilla)} packs exceed vanilla max:")
        for a in over_vanilla[:10]:
            lines.append(f"  Pack {a.pack_id}: {a.max_unique_vram} bytes")

    return "\n".join(lines)
