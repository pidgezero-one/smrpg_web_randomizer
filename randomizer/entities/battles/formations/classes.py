"""Base class for formations, and battle packs, consisting of 3 formations."""

from random import choices
import statistics
from typing import List, Tuple, Type, Optional, Dict


from smrpgpatchbuilder.datatypes.battles.enums import BattleMusic, Battlefields
from smrpgpatchbuilder.datatypes.enemies.classes import Enemy
from smrpgpatchbuilder.datatypes.numbers.classes import (
    ByteField,
    BitMapSet,
    UInt16,
    UInt8,
)

from smrpgpatchbuilder.datatypes.battles.ids.misc import (
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_FORMATIONS,
    PACK_BASE_ADDRESS,
)


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
        """If true, this enemy will be hidden when the battle begins."""
        return self._hidden_at_start

    def set_hidden_at_start(self, hidden_at_start: bool) -> None:
        """If true, this enemy will be hidden when the battle begins."""
        self._hidden_at_start = hidden_at_start

    @property
    def enemy(self) -> Type[Enemy]:
        """The class of the enemy being included in the formation."""
        return self._enemy

    def set_enemy(self, enemy: Type[Enemy]) -> None:
        """Set the class of the enemy being included in the formation."""
        self._enemy = enemy

    @property
    def x_pos(self) -> UInt8:
        """The X coordinate that the enemy will be stationed at."""
        return self._x_pos

    def set_x_pos(self, x_pos: int) -> None:
        """Set the X coordinate that the enemy will be stationed at."""
        self._x_pos = UInt8(x_pos)

    @property
    def y_pos(self) -> UInt8:
        """The Y coordinate that the enemy will be stationed at."""
        return self._y_pos

    def set_y_pos(self, y_pos: int) -> None:
        """Set the Y coordinate that the enemy will be stationed at."""
        self._y_pos = UInt8(y_pos)

    @property
    def anchor(self) -> bool:
        """(deprecated)"""
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        """(deprecated)"""
        self._anchor = anchor

    @property
    def include_in_stat_totaling(self) -> bool:
        """true by default. if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
        return self._include_in_stat_totaling

    def set_include_in_stat_totaling(self, include_in_stat_totaling: bool) -> None:
        """if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
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
    """A subclass that defines an arrangement of enemies in a battle."""

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
        """A list of containers including info about enemies and their positioning."""
        return self._members

    def set_members(self, members: List[Optional[FormationMember]]) -> None:
        """Overwrite the list of containers including info about enemies and their positioning."""
        self._members = members
        self._members.extend([None] * (8 - len(self._members)))

    @property
    def run_event_at_load(self) -> Optional[UInt8]:
        """the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        return self._run_event_at_load

    def set_run_event_at_load(self, run_event_at_load: Optional[int]) -> None:
        """set the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        if run_event_at_load is None:
            self._run_event_at_load = run_event_at_load
        else:
            self._run_event_at_load = UInt8(run_event_at_load)

    @property
    def music(self) -> BattleMusic:
        """The battle music that should accompany this formation."""
        return self._music

    def set_music(self, music: BattleMusic) -> None:
        """Set the battle music that should accompany this formation."""
        self._music = music

    @property
    def can_run_away(self) -> bool:
        """If false, running away from this formation is impossible."""
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        """If false, running away from this formation is impossible."""
        self._can_run_away = can_run_away

    @property
    def unknown_bit(self) -> bool:
        """(unknown)"""
        return self._unknown_bit

    def set_unknown_bit(self, unknown_bit: bool) -> None:
        """(unknown)"""
        self._unknown_bit = unknown_bit

    @property
    def battlefield_override(self) -> Optional[Battlefields]:
        """if set, forces this formation to always load with the given battlefield,
        regardless of where in the world it is encountered."""
        return self._battlefield_override

    def set_battlefield_override(
        self, battlefield_override: Optional[Battlefields]
    ) -> None:
        """force this formation to always load with the given battlefield,
        regardless of where in the world it is encountered."""
        self._battlefield_override = battlefield_override

    @property
    def additional_enemies_to_scale(self) -> List[Type[Enemy]]:
        """if this formation is used in a boss fight, its stats will change depending on
        which location it is shuffled to inhabit. this property specifies enemies that are
        not included in the formation itself whose stats should also be scaled similarly to
        the enemies in this formation.

        an example of this is when valentina occupies the mushroom kingdom. valentina and dodo
        will have their stats scaled to roughly match mack's original stats. however, valentina
        also brings bluebird henchmen with her who occupy the mushroom kingdom exterior, despite
        not appearing in battle in the same formation as her. those bluebirds should also be
        roughly scaled to match stats suitable to the mushroom kingdom, so you would
        specify bluebirdhenchmen in this list to make sure their stats stay appropriately
        relative to Valentina's, no matter where she ends up."""
        return self._additional_enemies_to_scale

    def set_additional_enemies_to_scale(
        self, additional_enemies_to_scale: List[Type[Enemy]]
    ) -> None:
        """if this formation is used in a boss fight, its stats will change depending on
        which location it is shuffled to inhabit. this property specifies enemies that are
        not included in the formation itself whose stats should also be scaled similarly to
        the enemies in this formation.

        an example of this is when valentina occupies the mushroom kingdom. valentina and dodo
        will have their stats scaled to roughly match mack's original stats. however, valentina
        also brings bluebird henchmen with her who occupy the mushroom kingdom exterior, despite
        not appearing in battle in the same formation as her. those bluebirds should also be
        roughly scaled to match stats suitable to the mushroom kingdom, so you would
        specify bluebirdhenchmen in this list to make sure their stats stay appropriately
        relative to Valentina's, no matter where she ends up."""
        self._additional_enemies_to_scale = additional_enemies_to_scale

    @property
    def additional_enemies_for_stat_count(self) -> List[Type[Enemy]]:
        """calculating the stats that a boss location should confer onto the boss inhabiting it
        via shuffling is based on the stats of the boss that inhabited that location in the original
        game, and takes into account which enemies absolutely must be defeated in order
        to end the fight. sometimes, an enemy formation does not perfectly define the whole
        list of enemies that need to be defeated.

        for example, the megasmilax fight requires you to defeat 8 smilaxes, but the formation
        only includes five, three of which are re-summoned during battle.

        this property would be used to contain three more smilaxes, so that the total hp
        conferred by the bean valley boss location is equivalent to megasmilax plus 8 smilaxes
        instead of five."""
        return self._additional_enemies_for_stat_count

    def set_additional_enemies_for_stat_count(
        self, additional_enemies_for_stat_count: List[Type[Enemy]]
    ) -> None:
        """calculating the stats that a boss location should confer onto the boss inhabiting it
        via shuffling is based on the stats of the boss that inhabited that location in the original
        game, and takes into account which enemies absolutely must be defeated in order
        to end the fight. sometimes, an enemy formation does not perfectly define the whole
        list of enemies that need to be defeated.

        for example, the megasmilax fight requires you to defeat 8 smilaxes, but the formation
        only includes five, three of which are re-summoned during battle.

        this property would be used to contain three more smilaxes, so that the total hp
        conferred by the bean valley boss location is equivalent to megasmilax plus 8 smilaxes
        instead of five."""
        self._additional_enemies_for_stat_count = additional_enemies_for_stat_count

    def get_summed_stats(self) -> Tuple[int, int, int, int, int, int, int, int, int]:
        """calculates the stats that this fight's original location should confer onto whichever
        boss fight inhabits it via the shuffler, if the player's settings require relative
        stat scaling."""
        stat_counted_enemy_classes = [
            m.enemy
            for m in self.members
            if m is not None and m.include_in_stat_totaling
        ]
        stat_counted_enemy_classes.extend(self.additional_enemies_for_stat_count)
        stat_counted_enemies = [m() for m in stat_counted_enemy_classes]

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
        """A list of the class definitions of enemies which are included in scaling."""
        returned_enemy_classes = [m.enemy for m in self.members if m is not None]
        returned_enemy_classes.extend(self.additional_enemies_to_scale)
        return list(set(returned_enemy_classes))

    def get_members_by_enemy_classes(self, *cls: Type[Enemy]) -> List[FormationMember]:
        """returns all of the enemy containers in this formation if the enemy class
        matches an entry in the given list."""
        return [m for m in self.members if m is not None and type(m) in cls]

    def randomize_coords(self, valid_coordinates: List[Tuple[int, int]]) -> None:
        """randomizes the coordinates of each formation member.\n
        Should not result in overlap."""
        valid_members = [m for m in self.members if m is not None]
        coords = choices(valid_coordinates, k=len(valid_members))
        for member, coord in zip(valid_members, coords):
            member.set_x_pos(coord[0])
            member.set_y_pos(coord[1])

    def __init__(
        self,
        members: List[Optional[FormationMember]],
        run_event_at_load: Optional[int] = None,
        music: BattleMusic = BattleMusic.NORMAL_MUSIC,
        can_run_away: bool = True,
        unknown_bit: bool = True,
        battlefield_override: Optional[Battlefields] = None,
        additional_enemies_to_scale: Optional[List[Type[Enemy]]] = None,
        additional_enemies_for_stat_count: Optional[List[Type[Enemy]]] = None,
    ) -> None:
        if additional_enemies_to_scale is None:
            additional_enemies_to_scale = []
        if additional_enemies_for_stat_count is None:
            additional_enemies_for_stat_count = []
        self.set_members(members)
        self.set_run_event_at_load(run_event_at_load)
        self.set_music(music)
        self.set_can_run_away(can_run_away)
        self.set_unknown_bit(unknown_bit)
        self.set_battlefield_override(battlefield_override)
        self.set_additional_enemies_to_scale(additional_enemies_to_scale)
        self.set_additional_enemies_for_stat_count(additional_enemies_for_stat_count)

    def render(self, formation_index: int) -> Dict[int, bytearray]:
        """Get formation data in `{0x123456: bytearray([0x00])}` format."""
        assert 0 <= formation_index < TOTAL_FORMATIONS
        patch: Dict[int, bytearray] = {}
        data = bytearray()

        # monsters present bitmap.
        monsters_present = [
            7 - index for (index, enemy) in enumerate(self.members) if enemy is not None
        ]
        data += BitMapSet(1, monsters_present).as_bytes()

        # monsters hidden bitmap.
        monsters_hidden = [
            7 - index
            for (index, enemy) in enumerate(self.members)
            if enemy is not None and enemy.hidden_at_start
        ]
        data += BitMapSet(1, monsters_hidden).as_bytes()

        # monster data.
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
        patch[base_addr] = data

        # add formation metadata.
        data = bytearray()
        data += ByteField(
            self.run_event_at_load if self.run_event_at_load is not None else 0xFF
        ).as_bytes()
        music_byte = (
            self.music.value + ((not self.can_run_away) * 0x02) + self.unknown_bit
        )
        data += ByteField(music_byte).as_bytes()

        base_addr = BASE_FORMATION_META_ADDRESS + formation_index * 3 + 1
        patch[base_addr] = data

        return patch


class FormationPack:
    """Base class for an arrangement of enemies in battle."""

    _formation_ids: List[UInt16] = []

    @property
    def formation_ids(self) -> List[UInt16]:
        """a list of all formation ids included in this battle pack.
        If all three formations are the same, it will just return one ID."""
        if self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]:
            return [self.formation_id]
        assert len(self._formation_ids) == 3
        return self._formation_ids

    @property
    def formation_id(self) -> "UInt16":
        """returns one formation id. it will fail if all three formation
        IDs are not the same in this pack."""
        assert self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]
        return self.formation_ids[0]

    def set_formation_ids(self, *formation_ids: int) -> None:
        """Overwrites the formation IDs in this pack."""
        assert len(formation_ids) == 3
        pids = list(formation_ids)
        for form_id in pids:
            assert form_id < TOTAL_FORMATIONS
        self._formation_ids = [UInt16(id) for id in pids]

    def set_formation_id(self, formation_id: int) -> None:
        """overwrites all three formation ids in this pack with the one
        id given as an argument to this function. in effect, this means
        all three formations will be the same and the pack will always load
        the same battle."""
        assert formation_id < TOTAL_FORMATIONS
        self.set_formation_ids(formation_id, formation_id, formation_id)

    def __init__(self, *formation_ids: int) -> None:
        if len(formation_ids) == 1:
            self.set_formation_ids(formation_ids[0], formation_ids[0], formation_ids[0])
        else:
            self.set_formation_ids(*formation_ids)

    def render(self, pack_index: int) -> Dict[int, bytearray]:
        """Get pack data in `{0x123456: bytearray([0x00])}` format."""
        assert UInt8(pack_index)
        assert len(self._formation_ids) == 3

        patch: Dict[int, bytearray] = {}
        data = bytearray()
        hi_num = False

        for formation_id in self.formation_ids:
            val = formation_id
            if val > 255:
                hi_num = True
                val -= 256
            data += ByteField(val).as_bytes()

        # high bank indicator.
        val = 7 if hi_num else 0
        data += ByteField(val).as_bytes()

        base_addr = PACK_BASE_ADDRESS + (pack_index * 4)
        patch[base_addr] = data

        return patch
