import random

from randomizer.data import dialogs, ship_passwords
from . import flags
from .utils import new_command
from randomizer.helpers.flag_helpers import MarrymoreGating
from randomizer.helpers.eventtables import _0x60Flags, AreaObjects
from randomizer.helpers.flag_helpers import (
    FireworksOptions,
    BanditsWayGating,
    ForestMazeGating,
    BoosterTowerGating,
    MarrymoreGating,
    SeaGating,
    YaridovichGating,
    MonstroTownGating,
    BarrelVolcanoGating,
    BowsersKeepGating,
    FactoryGating,
    EXPChallengeOptions,
    PlayableCharacters,
    ShopQualities,
    WinConditions,
    PipeVaultGating,
)


# There's a way to do perfect allocations with DYNAMIC PROGRAMMING,
# but I'm not doing that.
def allocate_string(string_length, free_list):
    for base in sorted(free_list, key=lambda x: free_list[x]):
        if free_list[base] >= string_length:
            size = free_list[base]
            del free_list[base]
            free_list[base + string_length] = size - string_length
            return base

    # If we get this far, we couldn't find space for the string.
    return None


def randomize_all(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    """
    # Check flag?
    if world.open_mode:
        randomize_wishes(world)
        if world.settings.is_flag_value(flags.QuizShuffle, True):
            randomize_quiz(world)
        if world.settings.is_flag_value(flags.RandomSunkenShipPassword, True):
            randomize_password(world)

        for id, wish in world.wishes.wishes:
            world.replace_dialog(id, wish)
        if world.settings.is_flag_value(flags.QuizShuffle, True):
            for id, question in world.quiz.questions:
                world.replace_dialog(id, question)

        # misc. dialogs
        if world.settings.is_flag_enabled(flags.EXPStarsAnywhere):
            world.replace_dialog(
                1222,
                """ I have an item to sell, but you\n don't have enough coins.[await]""",
            )
            world.replace_dialog(
                1223,
                """ You're looking for items?\n I'll sell one for 400 coins.\n Are you interested?[await]\n  [select] (Yes)\n  [select] (No)[await]""",
            )
            world.replace_dialog(
                1224,
                """ You want another item?[await]\n  [select] (Yes)\n  [select] (No)[await]""",
            )
            world.replace_dialog(
                1227,
                """ I found another item.\n I'll sell it for 800 coins.[await]\n  [select] (Buy it)\n  [select] (Pass)[await]""",
            )
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.hill):
            world.replace_dialog(
                2116,
                """ You want to know why we're\n standing around?[await]\n I'm waiting for something\n interesting to happen.[await][pause] But I think\n the usual troublemakers are busy\n on Booster Hill.""",
            )
        elif world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            world.replace_dialog(
                2116,
                """ You want to know why we're\n standing around?[await]\n I'm waiting for something\n interesting to happen.[await][pause] But I think\n the usual troublemakers are busy\n up atop Booster Tower.""",
            )
        elif world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.kggg):
            world.replace_dialog(
                2116,
                """ You want to know why we're\n standing around?[await]\n I'm waiting for something\n interesting to happen.[await][pause] But I think\n the usual troublemakers are busy\n clowning around.""",
            )
        value = world.settings.get_flag(flags.GrateGuyPrizeThreshold).value
        world.search_replace_dialog("`GRATE_GUY_PRIZE_CAP`", "%i" % value)
        # disable sj dog checks if SJ not learnable in seed
        if (
            flags.LearnableSpells.SuperJump
            in world.settings.get_flag(flags.AvailableSpells).disabled
        ):
            world.eventscripts[2063] = [
                new_command(
                    2063,
                    "run_dialog",
                    [
                        2049,
                        AreaObjects.MARIO,
                        [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE],
                    ],
                ),
                new_command(2063, "ret"),
            ]


RWRITER = "%RANDOM_WRITER%"
box_dialog_ids = [
    [1696, 1697, 1698, 1699, 1700],
    [1708, 1709, 1710, 1711, 1712],
    [1720, 1721, 1722, 1723, 1724],
    [1732, 1733, 1734, 1735, 1736],
    [1744, 1745, 1746, 1747, 1748],
    [1756, 1757, 1758, 1759, 1760],
]
recitation_ids = [
    [1701, 1702, 1703, 1704, 1705],
    [1713, 1714, 1715, 1716, 1717],
    [1725, 1726, 1727, 1728, 1729],
    [1737, 1738, 1739, 1740, 1741],
    [1749, 1750, 1751, 1752, 1753],
    [1761, 1762, 1763, 1764, 1765],
]


def randomize_password(world):
    password = random.choice(ship_passwords.pool)
    decoy_word = random.choice(
        [p for p in ship_passwords.pool if p.word != password.word]
    )
    correct_positions = []

    # modify the letter selection and recitation to be for this word
    for index, letter in enumerate(list(password.word)):
        letters = ship_passwords.suggest_letter_bank(
            password.word, index, decoy_word.word
        )
        correct_position = letters.index(password.word[index])
        correct_positions.append(correct_position)

        # generate the dialogs that display your letter selection when you stand under the boxes
        box_dialogs = []
        box_dialogs.append(
            """[page]\n Key letter%i  <%s> %s  %s  %s  %s[end]"""
            % (index + 1, letters[0], letters[1], letters[2], letters[3], letters[4])
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s <%s> %s  %s  %s[end]"""
            % (index + 1, letters[0], letters[1], letters[2], letters[3], letters[4])
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s <%s> %s  %s[end]"""
            % (index + 1, letters[0], letters[1], letters[2], letters[3], letters[4])
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s  %s <%s> %s[end]"""
            % (index + 1, letters[0], letters[1], letters[2], letters[3], letters[4])
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s  %s  %s <%s>[end]"""
            % (index + 1, letters[0], letters[1], letters[2], letters[3], letters[4])
        )
        box_dialog_pairs = zip(box_dialogs, box_dialog_ids[index])
        for dialog_content, dialog_id in box_dialog_pairs:
            world.replace_dialog(dialog_id, dialog_content)

        # populate the dialogs that are used in reciting your password
        recitation_pairs = zip(letters, recitation_ids[index])
        for letter, dialog_id in recitation_pairs:
            world.replace_dialog(dialog_id, """%s[end]""" % letter)

    # calibrate correctness checker
    world.eventscripts[3411] = [
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_31",
            "command": "jmp_if_var_not_equals_const",
            "args": [
                0x7024,
                correct_positions[0],
                "EVENT_3411_jmp_if_var_not_equals_const_33",
            ],
        },
        {"identifier": "EVENT_3411_inc_32", "command": "inc", "args": [0x70AC]},
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_33",
            "command": "jmp_if_var_not_equals_const",
            "args": [
                0x7026,
                correct_positions[1],
                "EVENT_3411_jmp_if_var_not_equals_const_35",
            ],
        },
        {"identifier": "EVENT_3411_inc_34", "command": "inc", "args": [0x70AC]},
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_35",
            "command": "jmp_if_var_not_equals_const",
            "args": [
                0x7028,
                correct_positions[2],
                "EVENT_3411_jmp_if_var_not_equals_const_37",
            ],
        },
        {"identifier": "EVENT_3411_inc_36", "command": "inc", "args": [0x70AC]},
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_37",
            "command": "jmp_if_var_not_equals_const",
            "args": [
                0x702A,
                correct_positions[3],
                "EVENT_3411_jmp_if_var_not_equals_const_39",
            ],
        },
        {"identifier": "EVENT_3411_inc_38", "command": "inc", "args": [0x70AC]},
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_39",
            "command": "jmp_if_var_not_equals_const",
            "args": [
                0x702C,
                correct_positions[4],
                "EVENT_3411_jmp_if_var_not_equals_const_41",
            ],
        },
        {"identifier": "EVENT_3411_inc_40", "command": "inc", "args": [0x70AC]},
        {
            "identifier": "EVENT_3411_jmp_if_var_not_equals_const_41",
            "command": "jmp_if_var_not_equals_const",
            "args": [0x702E, correct_positions[5], "EVENT_3411_ret"],
        },
        {"identifier": "EVENT_3411_inc_42", "command": "inc", "args": [0x70AC]},
        {"identifier": "EVENT_3411_ret", "command": "ret"},
    ]

    # populate hint dialogs
    random.shuffle(ship_passwords.hint_authors)
    # guarantee that the hint submitter will get their name on one of the hints
    writers = [password.submitter_hint_prefix] + ship_passwords.hint_authors
    number_of_writers = len(
        [
            h
            for h in [
                password.troopa_hint,
                password.trampoline_hint,
                password.maze_hint,
                password.snake_hint,
                password.cannonball_hint,
                password.barrel_hint,
                password.entrance_hint,
                password.saveroom_hint,
                password.greaper_hint_2,
                password.greaper_hint,
                password.drybones_hint,
            ]
            if h is not None and RWRITER in h
        ]
    )
    writers = writers[:number_of_writers]
    random.shuffle(writers)
    for s in writers:
        if RWRITER in password.troopa_hint:
            password.troopa_hint = password.troopa_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.trampoline_hint:
            password.trampoline_hint = password.trampoline_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.maze_hint:
            password.maze_hint = password.maze_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.snake_hint:
            password.snake_hint = password.snake_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.cannonball_hint:
            password.cannonball_hint = password.cannonball_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.barrel_hint:
            password.barrel_hint = password.barrel_hint.replace(RWRITER, s)
            continue
        if password.entrance_hint and RWRITER in password.entrance_hint:
            password.entrance_hint = password.entrance_hint.replace(RWRITER, s)
            continue
        if password.saveroom_hint and RWRITER in password.saveroom_hint:
            password.saveroom_hint = password.saveroom_hint.replace(RWRITER, s)
            continue
        if password.greaper_hint and RWRITER in password.greaper_hint:
            password.greaper_hint = password.greaper_hint.replace(RWRITER, s)
            continue
        if password.greaper_hint_2 and RWRITER in password.greaper_hint_2:
            password.greaper_hint_2 = password.greaper_hint_2.replace(RWRITER, s)
            continue
        if password.drybones_hint and RWRITER in password.drybones_hint:
            password.drybones_hint = password.drybones_hint.replace(RWRITER, s)
            continue
    world.replace_dialog(1664, password.troopa_hint)
    world.replace_dialog(1665, password.trampoline_hint)
    world.replace_dialog(1666, password.maze_hint)
    world.replace_dialog(1667, password.snake_hint)
    world.replace_dialog(1668, password.cannonball_hint)
    world.replace_dialog(1669, password.barrel_hint)
    if password.entrance_hint is not None:
        world.replace_dialog(1673, password.entrance_hint)
    if password.saveroom_hint is not None:
        world.replace_dialog(1674, password.saveroom_hint)
    if password.greaper_hint is not None:
        world.replace_dialog(1675, password.greaper_hint)
    if password.greaper_hint_2 is not None:
        world.replace_dialog(1676, password.greaper_hint_2)
    if password.drybones_hint is not None:
        world.replace_dialog(1656, password.drybones_hint)

    # credits
    world.password = password


def randomize_wishes(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    """
    world.wishes.wishes.clear()

    selected_wishes = random.sample(dialogs.wish_strings, len(dialogs.wish_dialogs))

    for index, dialog_id in enumerate(dialogs.wish_dialogs):
        world.wishes.wishes.append((dialog_id, selected_wishes[index]))


def randomize_quiz(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    """
    world.quiz.questions.clear()
    questions = dialogs.get_quiz_questions()
    if len(questions) > len(dialogs.quiz_dialogs):
        random_questions = random.sample(questions, len(dialogs.quiz_dialogs))
    else:
        random_questions = questions
    random_questions += random.sample(
        dialogs.backfill_questions, len(dialogs.quiz_dialogs) - len(random_questions)
    )
    random.shuffle(random_questions)

    for dialog_id, question in zip(dialogs.quiz_dialogs, random_questions):
        # Randomize order of incorrect answers for some extra variety.
        random.shuffle(question.wrong_answers)

        # Double check these
        if 1842 <= dialog_id < 1858:
            correct = 0
        elif 1858 <= dialog_id < 1874:
            correct = 1
        else:
            correct = 2
        string = question.get_string(correct)
        world.quiz.questions.append((dialog_id, string))


def assemble_from_table(pointer_table, data_table):
    if len(pointer_table) != 4096:
        raise Exception("dialog pointer table must have exactly 4096 entries")

    if len(data_table) != 3:
        raise Exception(
            "data table must consist of exactly 3 arrays, 1 per dialog data bank"
        )

    new_pointer_table = [None] * 4096

    # Will need to substitute vars into any strings here where appropriate. i.e. Peach's name into #735
    # `PEACH_NAME`
    # `PEACH_ARTICLE`
    # done - `TOWER_BOSS_1`
    # partially done - needs handler for when recruit is empty - `MARRYMORE_CHARACTER`
    # done - `RANDOM_BOSS_NAME_1` should exclude `TOWER_BOSS_1`
    # done - `RANDOM_BOSS_NAME_2` should exclude `TOWER_BOSS_1`
    # done - `RANDOM_BOSS_NAME_3` should exclude `TOWER_BOSS_1`
    # doen - `RANDOM_CHARACTER_NAME` should exclude `MARRYMORE_CHARACTER`
    # done - `SUPER_JUMP_PRIZE_1_CAP`
    # done - `SUPER_JUMP_PRIZE_2_CAP`
    # done - `GRATE_GUY_PRIZE_CAP`
    # done - 3847 needs generated bellhop menu
    # done - Set 2116 to either:
    #    You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy on Booster Hill.
    #    You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy up atop Booster Tower.
    # Set strong Mushroom Kingdom NPC hint to 2235
    # Set strong Rose Town NPC hint to pointers 803, 875
    # Set strong Marrymore hint to pointer 1006 (bellhop says something like "I can't let you leave yet. If you really need to go visit <place with a star piece>, you can wait until you're finished working.")
    # Set strong Johnny Note hint to pointer 1787. Figure out how to write it in-character for whoever replaced Johnny
    # Set strong Booster Tower note hint to pointer 2822
    # done - Dialogs 1222, 1223, 1224, 1227 will need to change dpeending on if star shuffle is on or not.
    # password hints: 1664, 1665, 1667, 1668, 1669, 1673, 1674, 1675, 1676, 1690
    # tadpole pond hints: 2664, 2665, 2668 (tadpole); 2718 (scroll);
    # Character palette names: overwrite 1179-1183

    # convert dialogs to byte vals
    compressed_dialog = [
        [dialogs.compress(d) for d in data_table[0]],  # 0x22
        [dialogs.compress(d) for d in data_table[1]],  # 0x23
        [dialogs.compress(d) for d in data_table[2]],  # 0x24
    ]

    assembled_dialog_data = []

    assembled_pointers = bytearray([])

    for b in range(len(compressed_dialog)):
        bank = 0x22 + b
        pointer_position = 0

        assembled_dialog_for_this_bank = bytearray([])
        # convert pointer data to offsets
        for dialog_id in range(len(compressed_dialog[b])):
            d = compressed_dialog[b][dialog_id]
            # print ('0x%02x' % (8 + pointer_position))
            for i in range(len(d)):
                indices = [
                    j
                    for j, x in enumerate(pointer_table)
                    if x["bank"] == bank and x["index"] == dialog_id and x["pos"] == i
                ]
                # if len(indices) > 0:
                #    print (hex(bank), dialog_id, i, indices, d, len(d))
                #    print ([hex(ord(c)) for c in d])
                for matched_pointer in indices:
                    new_pointer_table[matched_pointer] = pointer_position
                pointer_position += 1
            assembled_dialog_for_this_bank += d
            # print (dialog_id)
            # print (str(d))
            # print (len(d), pointer_position)
            # print ([hex(c) for c in d])
            # print ('')
            # print ('')

        # convert to pointers relative to section pointer
        if b == 0:
            offsets = [
                0,
                new_pointer_table[0x200],
                new_pointer_table[0x400],
                new_pointer_table[0x600],
            ]
            offsets = [o + 8 for o in offsets]
            for i in range(0x3FF, 0x1FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x200]
            for i in range(0x5FF, 0x3FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x400]
            for i in range(0x7FF, 0x5FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x600]
        elif b == 1:
            offsets = [0, new_pointer_table[0xA00]]
            offsets = [o + 4 for o in offsets]
            for i in range(0xBFF, 0x9FF, -1):
                new_pointer_table[i] -= new_pointer_table[0xA00]
        else:
            offsets = [0, new_pointer_table[0xE00]]
            offsets = [o + 4 for o in offsets]
            for i in range(0xFFF, 0xDFF, -1):
                new_pointer_table[i] -= new_pointer_table[0xE00]

        # final output for data bank: section pointers plus dialog data
        assembled_bank_dialog_data = bytearray([])
        for val in offsets:
            assembled_bank_dialog_data.append(val & 0xFF)
            assembled_bank_dialog_data.append(val >> 8)
        assembled_bank_dialog_data += assembled_dialog_for_this_bank

        # make sure it's not overflowing, fill up with empty data if space left
        if b == 0:
            max_length = 0x22FD18 - 0x220000
            empty_space = max_length - len(assembled_bank_dialog_data)
        elif b == 1:
            max_length = 0x23F2D5 - 0x230000
            empty_space = max_length - len(assembled_bank_dialog_data)
        else:
            max_length = 0x249000 - 0x240000
            empty_space = max_length - len(assembled_bank_dialog_data)
        if empty_space < 0:
            raise Exception(
                "Bank 0x%02x dialog data too long: %i bytes (expected up to %i)"
                % (0x22 + b, len(assembled_bank_dialog_data), max_length)
            )
        elif empty_space > 0:
            assembled_bank_dialog_data += bytearray([0x00 for x in range(empty_space)])

        assembled_dialog_data.append(assembled_bank_dialog_data)

    # pointer bytes
    for i in range(len(new_pointer_table)):
        val = new_pointer_table[i]
        # print(i, hex(val))
        assembled_pointers.append(val & 0xFF)
        assembled_pointers.append(val >> 8)

    return assembled_pointers, assembled_dialog_data
