# pylint: disable=C0103

"""bank 0x3Axxxx export"""

from randomizer.types.battle_animation_scripts.classes import (
    AnimationScriptBankCollection,
)
from .battle_events import bank as battle_events
from .subroutines.export_0x3A711F import bank as subroutine_0x3A711F
from .subroutines.export_0x3A71DA import bank as subroutine_0x3A71DA
from .subroutines.export_0x3A72CE import bank as subroutine_0x3A72CE
from .subroutines.export_0x3A7333 import bank as subroutine_0x3A7333
from .subroutines.export_0x3A7531 import bank as subroutine_0x3A7531
from .subroutines.export_0x3A755E import bank as subroutine_0x3A755E
from .subroutines.export_0x3A7702 import bank as subroutine_0x3A7702
from .subroutines.export_0x3A7868 import bank as subroutine_0x3A7868
from .subroutines.export_0x3A78B8 import bank as subroutine_0x3A78B8
from .subroutines.export_0x3A7999 import bank as subroutine_0x3A7999
from .subroutines.export_0x3A7A03 import bank as subroutine_0x3A7A03
from .subroutines.export_0x3A7A93 import bank as subroutine_0x3A7A93
from .subroutines.export_0x3A7CCA import bank as subroutine_0x3A7CCA
from .subroutines.export_0x3A7D04 import bank as subroutine_0x3A7D04
from .subroutines.export_0x3A7DE5 import bank as subroutine_0x3A7DE5
from .subroutines.export_0x3A7E13 import bank as subroutine_0x3A7E13
from .subroutines.export_0x3A7E4B import bank as subroutine_0x3A7E4B
from .subroutines.export_0x3A7E96 import bank as subroutine_0x3A7E96
from .subroutines.export_0x3A7EE5 import bank as subroutine_0x3A7EE5
from .subroutines.export_0x3A7F43 import bank as subroutine_0x3A7F43
from .subroutines.export_0x3A7F92 import bank as subroutine_0x3A7F92
from .subroutines.export_0x3A7FE5 import bank as subroutine_0x3A7FE5
from .subroutines.export_0x3A803A import bank as subroutine_0x3A803A
from .subroutines.export_0x3A808F import bank as subroutine_0x3A808F
from .subroutines.export_0x3A80AC import bank as subroutine_0x3A80AC
from .subroutines.export_0x3A80F2 import bank as subroutine_0x3A80F2
from .subroutines.export_0x3A8106 import bank as subroutine_0x3A8106
from .subroutines.export_0x3A8142 import bank as subroutine_0x3A8142
from .subroutines.export_0x3A8160 import bank as subroutine_0x3A8160
from .subroutines.export_0x3A8174 import bank as subroutine_0x3A8174
from .subroutines.export_0x3A8192 import bank as subroutine_0x3A8192
from .subroutines.export_0x3A81C4 import bank as subroutine_0x3A81C4
from .subroutines.export_0x3A81F6 import bank as subroutine_0x3A81F6
from .subroutines.export_0x3A8232 import bank as subroutine_0x3A8232
from .subroutines.export_0x3A8264 import bank as subroutine_0x3A8264
from .subroutines.export_0x3A8282 import bank as subroutine_0x3A8282
from .subroutines.export_0x3A82AA import bank as subroutine_0x3A82AA
from .subroutines.export_0x3A82D2 import bank as subroutine_0x3A82D2
from .subroutines.export_0x3A82FA import bank as subroutine_0x3A82FA
from .subroutines.export_0x3A8322 import bank as subroutine_0x3A8322
from .subroutines.export_0x3A8336 import bank as subroutine_0x3A8336
from .subroutines.export_0x3A8354 import bank as subroutine_0x3A8354
from .subroutines.export_0x3A8458 import bank as subroutine_0x3A8458
from .subroutines.export_0x3A84E4 import bank as subroutine_0x3A84E4
from .subroutines.export_0x3A852A import bank as subroutine_0x3A852A
from .subroutines.export_0x3A855C import bank as subroutine_0x3A855C
from .subroutines.export_0x3A8584 import bank as subroutine_0x3A8584
from .subroutines.export_0x3A85B6 import bank as subroutine_0x3A85B6
from .subroutines.export_0x3A8674 import bank as subroutine_0x3A8674
from .subroutines.export_0x3A8698 import bank as subroutine_0x3A8698
from .subroutines.export_0x3A8852 import bank as subroutine_0x3A8852
from .subroutines.export_0x3A8894 import bank as subroutine_0x3A8894
from .subroutines.export_0x3A88FF import bank as subroutine_0x3A88FF
from .subroutines.export_0x3A8A7E import bank as subroutine_0x3A8A7E
from .subroutines.export_0x3A8AE8 import bank as subroutine_0x3A8AE8
from .subroutines.export_0x3A8BE4 import bank as subroutine_0x3A8BE4
from .subroutines.export_0x3A8CA0 import bank as subroutine_0x3A8CA0
from .subroutines.export_0x3A8E78 import bank as subroutine_0x3A8E78
from .subroutines.export_0x3A9532 import bank as subroutine_0x3A9532
from .subroutines.export_0x3A96BD import bank as subroutine_0x3A96BD
from .subroutines.export_0x3A9725 import bank as subroutine_0x3A9725
from .subroutines.export_0x3A97D2 import bank as subroutine_0x3A97D2
from .subroutines.export_0x3A986A import bank as subroutine_0x3A986A
from .subroutines.export_0x3A9D7B import bank as subroutine_0x3A9D7B
from .subroutines.export_0x3A9EC1 import bank as subroutine_0x3A9EC1
from .subroutines.export_0x3A9F93 import bank as subroutine_0x3A9F93
from .subroutines.export_0x3AA070 import bank as subroutine_0x3AA070
from .subroutines.export_0x3AA17B import bank as subroutine_0x3AA17B
from .subroutines.export_0x3AA288 import bank as subroutine_0x3AA288
from .subroutines.export_0x3AA5BE import bank as subroutine_0x3AA5BE
from .subroutines.export_0x3AA6A7 import bank as subroutine_0x3AA6A7
from .subroutines.export_0x3AA8F2 import bank as subroutine_0x3AA8F2
from .subroutines.export_0x3ABBC6 import bank as subroutine_0x3ABBC6
from .subroutines.export_0x3AC148 import bank as subroutine_0x3AC148
from .subroutines.export_0x3AC1F1 import bank as subroutine_0x3AC1F1
from .subroutines.export_0x3AC795 import bank as subroutine_0x3AC795
from .subroutines.export_0x3AC7CF import bank as subroutine_0x3AC7CF
from .subroutines.export_0x3ACCB1 import bank as subroutine_0x3ACCB1
from .subroutines.export_0x3ACF48 import bank as subroutine_0x3ACF48
from .subroutines.export_0x3AD703 import bank as subroutine_0x3AD703

collection = AnimationScriptBankCollection(
    [
        battle_events,
        subroutine_0x3A711F,
        subroutine_0x3A71DA,
        subroutine_0x3A72CE,
        subroutine_0x3A7333,
        subroutine_0x3A7531,
        subroutine_0x3A755E,
        subroutine_0x3A7702,
        subroutine_0x3A7868,
        subroutine_0x3A78B8,
        subroutine_0x3A7999,
        subroutine_0x3A7A03,
        subroutine_0x3A7A93,
        subroutine_0x3A7CCA,
        subroutine_0x3A7D04,
        subroutine_0x3A7DE5,
        subroutine_0x3A7E13,
        subroutine_0x3A7E4B,
        subroutine_0x3A7E96,
        subroutine_0x3A7EE5,
        subroutine_0x3A7F43,
        subroutine_0x3A7F92,
        subroutine_0x3A7FE5,
        subroutine_0x3A803A,
        subroutine_0x3A808F,
        subroutine_0x3A80AC,
        subroutine_0x3A80F2,
        subroutine_0x3A8106,
        subroutine_0x3A8142,
        subroutine_0x3A8160,
        subroutine_0x3A8174,
        subroutine_0x3A8192,
        subroutine_0x3A81C4,
        subroutine_0x3A81F6,
        subroutine_0x3A8232,
        subroutine_0x3A8264,
        subroutine_0x3A8282,
        subroutine_0x3A82AA,
        subroutine_0x3A82D2,
        subroutine_0x3A82FA,
        subroutine_0x3A8322,
        subroutine_0x3A8336,
        subroutine_0x3A8354,
        subroutine_0x3A8458,
        subroutine_0x3A84E4,
        subroutine_0x3A852A,
        subroutine_0x3A855C,
        subroutine_0x3A8584,
        subroutine_0x3A85B6,
        subroutine_0x3A8674,
        subroutine_0x3A8698,
        subroutine_0x3A8852,
        subroutine_0x3A8894,
        subroutine_0x3A88FF,
        subroutine_0x3A8A7E,
        subroutine_0x3A8AE8,
        subroutine_0x3A8BE4,
        subroutine_0x3A8CA0,
        subroutine_0x3A8E78,
        subroutine_0x3A9532,
        subroutine_0x3A96BD,
        subroutine_0x3A9725,
        subroutine_0x3A97D2,
        subroutine_0x3A986A,
        subroutine_0x3A9D7B,
        subroutine_0x3A9EC1,
        subroutine_0x3A9F93,
        subroutine_0x3AA070,
        subroutine_0x3AA17B,
        subroutine_0x3AA288,
        subroutine_0x3AA5BE,
        subroutine_0x3AA6A7,
        subroutine_0x3AA8F2,
        subroutine_0x3ABBC6,
        subroutine_0x3AC148,
        subroutine_0x3AC1F1,
        subroutine_0x3AC795,
        subroutine_0x3AC7CF,
        subroutine_0x3ACCB1,
        subroutine_0x3ACF48,
        subroutine_0x3AD703,
    ]
)
