import statistics
from typing import List, Tuple, Type, Optional
from randomizer.entities.enemies.enemies import (
    AxemRangers,
    BandanaBlue,
    Belome2,
    Cloaker,
    Culex,
    Dodo,
    Domino,
    EarthCrystal,
    Earthlink,
    Exor,
    FireCrystal,
    Johnny,
    KingCalamari,
    LeftEye,
    MadAdder,
    MarioClone,
    Megasmilax,
    PeachClone,
    RightEye,
    WaterCrystal,
    WindCrystal,
)
from randomizer.types.numbers.classes import ByteField, BitMapSet
from randomizer.types.battles.battle_music.classes import Music
from randomizer.types.battles.battle_music.music import NormalBattleMusic
from randomizer.types.battles.formations.constants.misc import (
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_FORMATIONS,
)
from randomizer.types.bosses.enums import BattleMusic, Battlefields
from randomizer.types.enemies.classes import Enemy
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.patch.classes import Patch


class FormationMember:
    """Class representing a single enemy in a formation with metadata."""

    _hidden_at_start: bool
    _enemy: Type[Enemy]
    _x_pos: UInt8
    _y_pos: UInt8
    _anchor: bool
    _include_in_stat_totaling: bool

    @property
    def hidden_at_start(self) -> bool:
        return self._hidden_at_start

    def set_hidden_at_start(self, hidden_at_start: bool) -> None:
        self._hidden_at_start = hidden_at_start

    @property
    def enemy(self) -> Type[Enemy]:
        return self._enemy

    def set_enemy(self, enemy: Type[Enemy]) -> None:
        self._enemy = enemy

    @property
    def x_pos(self) -> UInt8:
        return self._x_pos

    def set_x_pos(self, x_pos: int) -> None:
        self._x_pos = UInt8(x_pos)

    @property
    def y_pos(self) -> UInt8:
        return self._y_pos

    def set_y_pos(self, y_pos: int) -> None:
        self._y_pos = UInt8(y_pos)

    @property
    def anchor(self) -> bool:
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        self._anchor = anchor

    @property
    def include_in_stat_totaling(self) -> bool:
        return self._include_in_stat_totaling

    def set_include_in_stat_totaling(self, include_in_stat_totaling: bool) -> None:
        self._include_in_stat_totaling = include_in_stat_totaling

    def __init__(
        self,
        enemy: Type[Enemy],
        x_pos: int,
        y_pos: int,
        hidden_at_start: bool = False,
        anchor: bool = False,
        include_in_stat_totaling: bool = True,
    ) -> None:
        self.set_enemy(enemy)
        self.set_x_pos(x_pos)
        self.set_y_pos(y_pos)
        self.set_hidden_at_start(hidden_at_start)
        self.set_anchor(anchor)
        self.set_include_in_stat_totaling(include_in_stat_totaling)


class Formation:

    _members: List[Optional[FormationMember]]
    _run_event_at_load: Optional[UInt8]
    _music: BattleMusic
    _can_run_away: bool
    _unknown_bit: bool
    _battlefield_override: Optional[Battlefields]
    _additional_enemies_to_scale: List[Type[Enemy]]
    _additional_enemies_for_stat_count: List[Type[Enemy]]

    @property
    def members(self) -> List[Optional[FormationMember]]:
        return self._members

    def set_members(self, members: List[Optional[FormationMember]]) -> None:
        self._members = members
        self._members.extend([None] * (8 - len(self._members)))

    @property
    def run_event_at_load(self) -> Optional[UInt8]:
        return self._run_event_at_load

    def set_run_event_at_load(self, run_event_at_load: Optional[int]) -> None:
        if run_event_at_load is None:
            self._run_event_at_load = run_event_at_load
        else:
            self._run_event_at_load = UInt8(run_event_at_load)

    @property
    def music(self) -> BattleMusic:
        return self._music

    def set_music(self, music: BattleMusic) -> None:
        self._music = music

    @property
    def can_run_away(self) -> bool:
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        self._can_run_away = can_run_away

    @property
    def unknown_bit(self) -> bool:
        return self._unknown_bit

    def set_unknown_bit(self, unknown_bit: bool) -> None:
        self._unknown_bit = unknown_bit

    @property
    def battlefield_override(self) -> Optional[Battlefields]:
        return self._battlefield_override

    def set_battlefield_override(
        self, battlefield_override: Optional[Battlefields]
    ) -> None:
        self._battlefield_override = battlefield_override

    @property
    def additional_enemies_to_scale(self) -> List[Type[Enemy]]:
        return self._additional_enemies_to_scale

    def set_additional_enemies_to_scale(
        self, additional_enemies_to_scale: List[Type[Enemy]]
    ) -> None:
        self._additional_enemies_to_scale = additional_enemies_to_scale

    @property
    def additional_enemies_for_stat_count(self) -> List[Type[Enemy]]:
        return self._additional_enemies_for_stat_count

    def set_additional_enemies_for_stat_count(
        self, additional_enemies_for_stat_count: List[Type[Enemy]]
    ) -> None:
        self._additional_enemies_for_stat_count = additional_enemies_for_stat_count

    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        stat_counted_enemy_classes = [
            m.enemy
            for m in self.members
            if m is not None and m.include_in_stat_totaling
        ]
        stat_counted_enemy_classes.extend(self.additional_enemies_for_stat_count)
        stat_counted_enemies = [m() for m in stat_counted_enemy_classes]

        e: Enemy

        hp: int = sum(e.hp for e in stat_counted_enemies)
        xp: int = sum(e.xp for e in stat_counted_enemies)
        coins: int = sum(e.coins for e in stat_counted_enemies)

        attack: int = int(
            round(statistics.mean(e.attack for e in stat_counted_enemies))
        )
        defense: int = int(
            round(statistics.mean(e.defense for e in stat_counted_enemies))
        )
        magic_attack: int = int(
            round(statistics.mean(e.magic_attack for e in stat_counted_enemies))
        )
        magic_defense: int = int(
            round(statistics.mean(e.magic_defense for e in stat_counted_enemies))
        )
        evade: int = int(round(statistics.mean(e.evade for e in stat_counted_enemies)))
        magic_evade: int = int(
            round(statistics.mean(e.magic_evade for e in stat_counted_enemies))
        )

        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )

    def get_scaled_enemy_classes(self) -> List[Type[Enemy]]:
        returned_enemy_classes = [m.enemy for m in self.members if m is not None]
        returned_enemy_classes.extend(self.additional_enemies_to_scale)
        return list(set(returned_enemy_classes))

    def get_members_by_enemy_classes(self, *cls: Type[Enemy]) -> List[FormationMember]:
        return [m for m in self.members if m is not None and type(m) in cls]

    def __init__(
        self,
        members: List[Optional[FormationMember]],
        run_event_at_load: Optional[int] = None,
        music: BattleMusic = BattleMusic.Normal,
        can_run_away: bool = True,
        unknown_bit: bool = True,
        battlefield_override: Optional[Battlefields] = None,
        additional_enemies_to_scale: List[Type[Enemy]] = [],
        additional_enemies_for_stat_count: List[Type[Enemy]] = [],
    ) -> None:
        self.set_members(members)
        self.set_run_event_at_load(run_event_at_load)
        self.set_music(music)
        self.set_can_run_away(can_run_away)
        self.set_unknown_bit(unknown_bit)
        self.set_battlefield_override(battlefield_override)
        self.set_additional_enemies_to_scale(additional_enemies_to_scale)
        self.set_additional_enemies_for_stat_count(additional_enemies_for_stat_count)

    def get_patch(self, formation_index: int) -> Patch:
        assert 0 <= formation_index < TOTAL_FORMATIONS
        patch = Patch()
        data = bytearray()

        # Monsters present bitmap.
        monsters_present = [
            7 - index for (index, enemy) in enumerate(self.members) if enemy is not None
        ]
        data += BitMapSet(1, monsters_present).as_bytes()

        # Monsters hidden bitmap.
        monsters_hidden = [
            7 - index
            for (index, enemy) in enumerate(self.members)
            if enemy is not None and enemy.hidden_at_start
        ]
        data += BitMapSet(1, monsters_hidden).as_bytes()

        # Monster data.
        for index, member in enumerate(self.members):
            if member is not None:
                data += ByteField(index).as_bytes()
                data += ByteField(member.x_pos).as_bytes()
                data += ByteField(member.y_pos).as_bytes()
            else:
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()

        base_addr = BASE_FORMATION_ADDRESS + (formation_index * 26)
        patch.add_data(base_addr, data)

        # Add formation metadata.
        data = bytearray()
        data += ByteField(
            self.run_event_at_load if self.run_event_at_load is not None else 0xFF
        ).as_bytes()
        music_byte = (
            self.music.value + ((not self.can_run_away) * 0x02) + self.unknown_bit
        )
        data += ByteField(music_byte).as_bytes()

        base_addr = BASE_FORMATION_META_ADDRESS + formation_index * 3 + 1
        patch.add_data(base_addr, data)

        return patch


class ExorBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # HP = exor plus average of two eyes
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        exor = self.get_members_by_enemy_classes(Exor)[0].enemy()
        righteye = self.get_members_by_enemy_classes(RightEye)[0].enemy()
        lefteye = self.get_members_by_enemy_classes(LeftEye)[0].enemy()
        hp = round(exor.hp + (righteye.hp + lefteye.hp) / 2)
        xp = exor.xp
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class KingCalamariBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from kc
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        kc = self.get_members_by_enemy_classes(KingCalamari)[0].enemy()
        xp = kc.xp
        coins = kc.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class CloakerDominoFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # average HP between alternating fight options
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        cloaker = self.get_members_by_enemy_classes(Cloaker)[0].enemy()
        domino = self.get_members_by_enemy_classes(Domino)[0].enemy()
        earthlink = self.get_members_by_enemy_classes(Earthlink)[0].enemy()
        madadder = self.get_members_by_enemy_classes(MadAdder)[0].enemy()
        hp = round((cloaker.hp + domino.hp) / 2 + (earthlink.hp + madadder.hp) / 2)
        # xp and coins come only from these two
        xp = cloaker.xp + domino.xp
        coins = cloaker.coins + domino.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class ValentinaBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # For Dodo/Valentina, count 40% of Dodo's HP.
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        dodo = self.get_members_by_enemy_classes(Dodo)
        hp -= round(0.6 * dodo[0].enemy().hp)
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class MegasmilaxBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        ms = self.get_members_by_enemy_classes(Megasmilax)[0].enemy()
        xp = ms.xp
        coins = ms.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class AxemBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        ar = self.get_members_by_enemy_classes(AxemRangers)[0].enemy()
        xp = ar.xp
        coins = ar.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class Belome2BossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        belome = self.get_members_by_enemy_classes(Belome2)[0].enemy()
        marioclone = self.get_members_by_enemy_classes(MarioClone)[0].enemy()
        peachclone = self.get_members_by_enemy_classes(PeachClone)[0].enemy()
        xp = belome.xp + marioclone.xp + peachclone.xp
        coins = belome.coins + marioclone.coins + peachclone.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class CulexBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        culex = self.get_members_by_enemy_classes(Culex)[0].enemy()
        fc = self.get_members_by_enemy_classes(FireCrystal)[0].enemy()
        wc = self.get_members_by_enemy_classes(WindCrystal)[0].enemy()
        ec = self.get_members_by_enemy_classes(EarthCrystal)[0].enemy()
        wac = self.get_members_by_enemy_classes(WaterCrystal)[0].enemy()
        xp = culex.xp + fc.xp + wc.xp + ec.xp + wac.xp
        coins = culex.coins + fc.coins + wc.coins + ec.coins + wac.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )


class JohnnyBossFormation(Formation):
    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = super().get_summed_stats()
        johnny = self.get_members_by_enemy_classes(Johnny)[0].enemy()
        henchmen = self.get_members_by_enemy_classes(BandanaBlue)
        xp = johnny.xp
        coins = johnny.coins
        for h in henchmen:
            henchman = h.enemy()
            xp += henchman.xp * 4
            coins += henchman.coins * 4
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        )
