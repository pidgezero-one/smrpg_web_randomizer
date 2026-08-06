from enum import Enum, StrEnum


class ExitType(Enum):
    FLAT = "flat"
    PIPE = "pipe"
    WHIRLPOOL = "whirlpool"
    FALL = "fall"
    SPRING = "spring"
    STALK = "stalk"


class EntranceType(StrEnum):
    FLAT = "flat"
    PIPE = "pipe"
    SPRING = "spring"
    WORLD_MAP = "world_map"
    NO_RETURN_FALL = "no_return_fall"
    WHIRLPOOL = "whirlpool"
    CLIMB = "climb"


class Entrance:
    _can_return: bool = True
    _coords: tuple[int, int, int, bool] | None = None

    @property
    def can_return(self) -> bool:
        return self._can_return

    @property
    def coords(self) -> tuple[int, int, int, bool]:
        assert self._coords is not None, "coords must be set before being accessed"
        return self._coords


class Exit:
    _valid_entrance_types: list[EntranceType] | None = None

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        assert (
            self._valid_entrance_types is not None
        ), "valid_entrance_types must be set before being accessed"
        return self._valid_entrance_types


class RegularExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [EntranceType.FLAT, EntranceType.WORLD_MAP]


class PipeExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [EntranceType.PIPE, EntranceType.SPRING, EntranceType.NO_RETURN_FALL]


class WhirlpoolExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [
            EntranceType.WHIRLPOOL,
            EntranceType.NO_RETURN_FALL,
            EntranceType.SPRING,
        ]


class FallExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [EntranceType.NO_RETURN_FALL, EntranceType.SPRING]
    
class SpringExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [EntranceType.PIPE, EntranceType.WHIRLPOOL, EntranceType.WORLD_MAP]
    
class StalkExit(Exit):

    @property
    def valid_entrance_types(self) -> list[EntranceType]:
        return [EntranceType.CLIMB]
    

# entrances and exits should be compatible both ways

