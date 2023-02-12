from randomizer.logic import utils
from randomizer.types.bosses.classes import MimicBoss
from randomizer.entities.bosses.locations import (
    AxemRangers,
    Belome1,
    Belome2,
    Birdetta,
    Boomer,
    Booster,
    Bowyer,
    BoxBoy,
    Bundt,
    Chester,
    Clerk,
    CloakerDomino,
    ClownBros,
    Countdown,
    Croco1,
    Croco2,
    Culex,
    CzarDragon,
    Director,
    Dodo,
    Exor,
    Gunyolk,
    HammerBros,
    Hidon,
    Jagger,
    Jinx1,
    Jinx2,
    Jinx3,
    Johnny,
    KingCalamari,
    Mack,
    Magikoopa,
    MegaSmilax,
    Mokura,
    Pandorite,
    Punchinello,
    Smithy,
    Valentina,
    Yaridovich,
    Manager,
)
from randomizer.entities.bosses.bosses import (
    AxemRangersBoss,
    Belome1Boss,
    Belome2Boss,
    BirdettaBoss,
    BoomerBoss,
    BoosterBoss,
    BowyerBoss,
    BoxBoyBoss,
    BundtBoss,
    ChesterBoss,
    ClerkBoss,
    CloakerDominoBoss,
    CountdownBoss,
    Croco1Boss,
    Croco2Boss,
    CulexBoss,
    CzarBoss,
    DirectorBoss,
    DodoBoss,
    ExorBoss,
    GrateGuyBoss,
    GunyolkBoss,
    HammerBroBoss,
    HidonBoss,
    JaggerBoss,
    Jinx1Boss,
    Jinx2Boss,
    Jinx3Boss,
    JohnnyBoss,
    KingCalamariBoss,
    MackBoss,
    MagikoopaBoss,
    ManagerBoss,
    MegaSmilaxBoss,
    MokuraBoss,
    PandoriteBoss,
    PunchinelloBoss,
    SmithyBoss,
    ValentinaBoss,
    YaridovichBoss,
    ManagerBoss,
)
from randomizer.helpers.objectsequencetables import _0x08Flags


def is_vanilla(boss, location):
    return (
        (
            utils.isclass_or_instance(location, HammerBros)
            and utils.isclass_or_instance(boss, HammerBroBoss)
        )
        or (
            utils.isclass_or_instance(location, Croco1)
            and utils.isclass_or_instance(boss, Croco1Boss)
        )
        or (
            utils.isclass_or_instance(location, Mack)
            and utils.isclass_or_instance(boss, MackBoss)
        )
        or (
            utils.isclass_or_instance(location, Pandorite)
            and utils.isclass_or_instance(boss, PandoriteBoss)
        )
        or (
            (
                utils.isclass_or_instance(location, Belome1)
                or utils.isclass_or_instance(location, Belome2)
            )
            and (
                utils.isclass_or_instance(boss, Belome1Boss)
                or utils.isclass_or_instance(boss, Belome2Boss)
            )
        )
        or (
            utils.isclass_or_instance(location, Bowyer)
            and utils.isclass_or_instance(boss, BowyerBoss)
        )
        or (
            utils.isclass_or_instance(location, Croco2)
            and utils.isclass_or_instance(boss, Croco2Boss)
        )
        or (
            utils.isclass_or_instance(location, Punchinello)
            and utils.isclass_or_instance(boss, PunchinelloBoss)
        )
        or (
            utils.isclass_or_instance(location, Booster)
            and utils.isclass_or_instance(boss, BoosterBoss)
        )
        or (
            utils.isclass_or_instance(location, ClownBros)
            and utils.isclass_or_instance(boss, GrateGuyBoss)
        )
        or (
            utils.isclass_or_instance(location, Bundt)
            and utils.isclass_or_instance(boss, BundtBoss)
        )
        or (
            utils.isclass_or_instance(location, KingCalamari)
            and utils.isclass_or_instance(boss, KingCalamariBoss)
        )
        or (
            utils.isclass_or_instance(location, Hidon)
            and utils.isclass_or_instance(boss, HidonBoss)
        )
        or (
            utils.isclass_or_instance(location, Johnny)
            and utils.isclass_or_instance(boss, JohnnyBoss)
        )
        or (
            utils.isclass_or_instance(location, Yaridovich)
            and utils.isclass_or_instance(boss, YaridovichBoss)
        )
        or (
            utils.isclass_or_instance(location, Mokura)
            and utils.isclass_or_instance(boss, MokuraBoss)
        )
        or (
            utils.isclass_or_instance(location, Jagger)
            and utils.isclass_or_instance(boss, JaggerBoss)
        )
        or (
            (
                utils.isclass_or_instance(location, Jinx1)
                or utils.isclass_or_instance(location, Jinx2)
                or utils.isclass_or_instance(location, Jinx3)
            )
            and (
                utils.isclass_or_instance(boss, Jinx1Boss)
                or utils.isclass_or_instance(boss, Jinx2Boss)
                or utils.isclass_or_instance(boss, Jinx3Boss)
            )
        )
        or (
            utils.isclass_or_instance(location, Culex)
            and utils.isclass_or_instance(boss, CulexBoss)
        )
        or (
            utils.isclass_or_instance(location, BoxBoy)
            and utils.isclass_or_instance(boss, BoxBoyBoss)
        )
        or (
            utils.isclass_or_instance(location, MegaSmilax)
            and utils.isclass_or_instance(boss, MegaSmilaxBoss)
        )
        or (
            utils.isclass_or_instance(location, Dodo)
            and utils.isclass_or_instance(boss, DodoBoss)
        )
        or (
            utils.isclass_or_instance(location, Birdetta)
            and utils.isclass_or_instance(boss, BirdettaBoss)
        )
        or (
            utils.isclass_or_instance(location, Valentina)
            and utils.isclass_or_instance(boss, ValentinaBoss)
        )
        or (
            utils.isclass_or_instance(location, CzarDragon)
            and utils.isclass_or_instance(boss, CzarBoss)
        )
        or (
            utils.isclass_or_instance(location, AxemRangers)
            and utils.isclass_or_instance(boss, AxemRangersBoss)
        )
        or (
            utils.isclass_or_instance(location, Chester)
            and utils.isclass_or_instance(boss, ChesterBoss)
        )
        or (
            utils.isclass_or_instance(location, Magikoopa)
            and utils.isclass_or_instance(boss, MagikoopaBoss)
        )
        or (
            utils.isclass_or_instance(location, Boomer)
            and utils.isclass_or_instance(boss, BoomerBoss)
        )
        or (
            utils.isclass_or_instance(location, Exor)
            and utils.isclass_or_instance(boss, ExorBoss)
        )
        or (
            utils.isclass_or_instance(location, Countdown)
            and utils.isclass_or_instance(boss, CountdownBoss)
        )
        or (
            utils.isclass_or_instance(location, CloakerDomino)
            and utils.isclass_or_instance(boss, CloakerDominoBoss)
        )
        or (
            utils.isclass_or_instance(location, Clerk)
            and utils.isclass_or_instance(boss, ClerkBoss)
        )
        or (
            utils.isclass_or_instance(location, Manager)
            and utils.isclass_or_instance(boss, ManagerBoss)
        )
        or (
            utils.isclass_or_instance(location, Director)
            and utils.isclass_or_instance(boss, DirectorBoss)
        )
        or (
            utils.isclass_or_instance(location, Gunyolk)
            and utils.isclass_or_instance(boss, GunyolkBoss)
        )
        or (
            utils.isclass_or_instance(location, Smithy)
            and utils.isclass_or_instance(boss, SmithyBoss)
        )
    )


def has_vanilla_henchmen(boss, location):
    return (
        len(location.repeatable_henchmen + location.unique_henchmen) == 0
        or len(boss.repeatable_henchmen + boss.unique_henchmen) == 0
    )


def sanitize_animation_script(boss, boss_location, script, model):
    """Helper function that helps ensure that illegal sequences cannot be performed for substituted sprites in specific slots, but also substitutes specifically chosen sequences where appropriate."""
    # leave script alone if character is vanilla
    if not is_vanilla(boss, boss_location):
        new_script = []
        for _, subscript_command in enumerate(script):
            # Pretty much all of these animations are based around sequence setting
            # if a specific mold or sequence doesn't have an equivalent, just don't include it in the sanitized script
            if subscript_command["command"] == "set_sprite_sequence":
                # molds
                if _0x08Flags.READ_AS_MOLD in subscript_command["args"][2]:
                    # if setting mold to 0, that's ok, just reset to the right default mold for scarecrow or culex
                    if subscript_command["args"][0] == 0:
                        new_script.append(subscript_command)
                    # otherwise, it's subject to animation-specific rules
                    else:
                        if utils.isclass_or_instance(boss_location, Booster):
                            if subscript_command["args"][0] == 12:
                                new_script.append(
                                    {"identifier": "dummy", "command": "face_northeast"}
                                )

                # sequences
                else:
                    # bandit's way distraction
                    if (
                        utils.isclass_or_instance(boss_location, Croco1)
                        and model.animations is not None
                        and model.animations.bandits_way_distracted is not None
                    ):
                        if subscript_command["args"][0] == 5:
                            subscript_command["args"][
                                0
                            ] = model.animations.bandits_way_distracted.sequence_id
                            # no support for sprite offsets, but not necessary with the sprites we're using
                            new_script.append(subscript_command)
                    # ending credits race
                    elif (
                        utils.isclass_or_instance(boss_location, Croco1)
                        and model.animations is not None
                        and model.animations.recoil is not None
                    ):
                        if subscript_command["args"][0] == 2:
                            subscript_command["args"][
                                0
                            ] = model.animations.recoil.sequence_id
                            # no support for sprite offsets, but not necessary with the sprites we're using
                            new_script.append(subscript_command)
                    # moleville mines punch
                    elif utils.isclass_or_instance(boss_location, Punchinello):
                        if (
                            model.animations is not None
                            and model.animations.mines_punch is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.mines_punch.sequence_id
                                new_script.append(subscript_command)
                    # chapel laughing
                    elif utils.isclass_or_instance(boss_location, Booster):
                        if (
                            model.animations is not None
                            and model.animations.chapel_laugh is not None
                        ):
                            if subscript_command["args"][0] == 2:
                                subscript_command["args"][
                                    0
                                ] = model.animations.chapel_laugh.sequence_id
                                new_script.append(subscript_command)
                    # marrymore kitchen
                    elif utils.isclass_or_instance(boss_location, Bundt):
                        if (
                            model.animations is not None
                            and model.animations.kitchen_prep is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.kitchen_prep.sequence_id
                                if (
                                    model.animations.kitchen_prep.total_duration
                                    is not None
                                ):
                                    subscript_command["args"][2].append(
                                        _0x08Flags.LOOPING_OFF
                                    )
                                new_script.append(subscript_command)
                    # ship beckon
                    elif utils.isclass_or_instance(boss_location, KingCalamari):
                        if (
                            model.animations is not None
                            and model.animations.ship_beckon is not None
                        ):
                            if subscript_command["args"][0] == 1:
                                subscript_command["args"][
                                    0
                                ] = model.animations.ship_beckon.sequence_id
                                subscript_command["args"][2].append(
                                    _0x08Flags.LOOPING_OFF
                                )
                                new_script.append(subscript_command)
                    # ship chair
                    elif utils.isclass_or_instance(boss_location, Johnny):
                        if (
                            model.animations is not None
                            and model.animations.ship_chair is not None
                        ):
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][
                                    0
                                ] = model.animations.ship_chair.sequence_id
                                new_script.append(subscript_command)
                    # jagger
                    elif utils.isclass_or_instance(boss_location, Jagger):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 4
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.dojo_challenge is not None
                        ):
                            if subscript_command["args"][0] == 4:
                                subscript_command["args"][
                                    0
                                ] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # jinx
                    elif (
                        utils.isclass_or_instance(boss_location, Jinx1)
                        or utils.isclass_or_instance(boss_location, Jinx2)
                        or utils.isclass_or_instance(boss_location, Jinx3)
                    ):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 3
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.dojo_challenge is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # magikoopa - challenge only. sequence #10 also used in battle doors, which will be handled separately
                    elif utils.isclass_or_instance(boss_location, Magikoopa):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 10
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.keep_challenge is not None
                        ):
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][
                                    0
                                ] = model.animations.keep_challenge.sequence_id
                                new_script.append(subscript_command)
                    # similar to mold, restore default sequence if appropriate
                    else:
                        if subscript_command["args"][0] == 0:
                            new_script.append(subscript_command)
            else:
                new_script.append(subscript_command)
        return new_script
    else:
        return script
