import random

from randomizer.data import dialogs, ship_passwords
from . import flags

# There's a way to do perfect allocations with DYNAMIC PROGRAMMING,
# but I'm not doing that.


def allocate_string(string_length, free_list):
    for base in sorted(free_list, key=lambda x: free_list[x]):
        if free_list[base] >= string_length:
            size = free_list[base]
            del free_list[base]
            free_list[base+string_length] = size - string_length
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


RWRITER = "%RANDOM_WRITER%"
box_dialog_ids = [[1696, 1697, 1698, 1699, 1700], [1708, 1709, 1710, 1711, 1712], [1720, 1721, 1722, 1723, 1724], [
    1732, 1733, 1734, 1735, 1736], [1744, 1745, 1746, 1747, 1748], [1759, 1757, 1758, 1759, 1760]]
recitation_ids = [[1701, 1702, 1703, 1704, 1705], [1713, 1714, 1715, 1716, 1717], [1725, 1726, 1727, 1728, 1729], [
    1737, 1738, 1739, 1740, 1741], [1749, 1750, 1751, 1752, 1753], [1761, 1762, 1763, 1764, 1765]]


def randomize_password(world):
    password = random.choice(ship_passwords.pool)
    decoy_word = random.choice(
        [p for p in ship_passwords.pool if p.word != password.word])
    correct_positions = []

    # modify the letter selection and recitation to be for this word
    for index, letter in enumerate(list(password.word)):
        letters = ship_passwords.suggest_letter_bank(password.word, index, decoy_word)
        correct_position = letters.index(password.word[index])
        correct_positions.append(correct_position)

        # generate the dialogs that display your letter selection when you stand under the boxes
        box_dialogs = []
        box_dialogs.append('''[page]\n Key letter%i  <%s> %s  %s  %s  %s[end]''' % (
            index, letters[0], letters[1], letters[2], letters[3], letters[4]))
        box_dialogs.append('''[page]\n Key letter%i   %s <%s> %s  %s  %s[end]''' % (
            index, letters[0], letters[1], letters[2], letters[3], letters[4]))
        box_dialogs.append('''[page]\n Key letter%i   %s  %s <%s> %s  %s[end]''' % (
            index, letters[0], letters[1], letters[2], letters[3], letters[4]))
        box_dialogs.append('''[page]\n Key letter%i   %s  %s  %s <%s> %s[end]''' % (
            index, letters[0], letters[1], letters[2], letters[3], letters[4]))
        box_dialogs.append('''[page]\n Key letter%i   %s  %s  %s  %s <%s>[end]''' % (
            index, letters[0], letters[1], letters[2], letters[3], letters[4]))
        box_dialog_pairs = zip(box_dialogs, box_dialog_ids[index])
        for dialog_content, dialog_id in box_dialog_pairs:
            world.replace_dialog(dialog_id, dialog_content)

        # populate the dialogs that are used in reciting your password
        recitation_pairs = zip(letters, recitation_ids[index])
        for letter, dialog_id in recitation_pairs:
            world.replace_dialog(dialog_id, '''%s[end]''' % letter)

    # calibrate correctness checker
    world.eventscripts[3411] = [
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_31',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x7024, correct_positions[0], 'EVENT_3411_jmp_if_var_not_equals_short_33']
        },
        {
            "identifier": 'EVENT_3411_inc_32',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_33',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x7026, correct_positions[1], 'EVENT_3411_jmp_if_var_not_equals_short_35']
        },
        {
            "identifier": 'EVENT_3411_inc_34',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_35',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x7028, correct_positions[2], 'EVENT_3411_jmp_if_var_not_equals_short_37']
        },
        {
            "identifier": 'EVENT_3411_inc_36',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_37',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x702a, correct_positions[3], 'EVENT_3411_jmp_if_var_not_equals_short_39']
        },
        {
            "identifier": 'EVENT_3411_inc_38',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_39',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x702c, correct_positions[4], 'EVENT_3411_jmp_if_var_not_equals_short_41']
        },
        {
            "identifier": 'EVENT_3411_inc_40',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_jmp_if_var_not_equals_short_41',
            "command": 'jmp_if_var_not_equals_short',
            "args": [0x702e, correct_positions[5], 'EVENT_3411_ret']
        },
        {
            "identifier": 'EVENT_3411_inc_42',
            "command": 'inc',
            "args": [0x70ac]
        },
        {
            "identifier": 'EVENT_3411_ret',
            "command": "ret"
        }
    ]

    # populate hint dialogs
    writers = [password.submitter_hint_prefix] + \
        random.shuffle(ship_passwords.hint_authors)
    for s in writers:
        # randomize the order of these
        if RWRITER in password.troopa_hint:
            password.troopa_hint = password.troopa_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.trampoline_hint:
            password.trampoline_hint = password.trampoline_hint.replace(
                RWRITER, s)
            continue
        if RWRITER in password.maze_hint:
            password.maze_hint = password.maze_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.snake_hint:
            password.snake_hint = password.snake_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.cannonball_hint:
            password.cannonball_hint = password.cannonball_hint.replace(
                RWRITER, s)
            continue
        if RWRITER in password.barrel_hint:
            password.barrel_hint = password.barrel_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.entrance_hint:
            password.entrance_hint = password.entrance_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.saveroom_hint:
            password.saveroom_hint = password.saveroom_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.greaper_hint:
            password.greaper_hint = password.greaper_hint_2.replace(RWRITER, s)
            continue
        if RWRITER in password.greaper_hint:
            password.greaper_hint_2 = password.greaper_hint_2.replace(
                RWRITER, s)
            continue
        if RWRITER in password.drybones_hint:
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
    world.password_submitter = password.submitter_credits


def randomize_wishes(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    """
    world.wishes.wishes.clear()
    available_wishes = dialogs.wish_strings.copy()

    for dialog_id in dialogs.wish_dialogs:
        wish = random.choice(dialogs.wish_strings)
        available_wishes.remove(wish)
        world.wishes.wishes.append((dialog_id, wish))


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
    random_questions += random.sample(dialogs.backfill_questions,
                                      len(dialogs.quiz_dialogs) - len(random_questions))
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
