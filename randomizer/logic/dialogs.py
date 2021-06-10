import random

from randomizer.data import dialogs
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


def randomize_wishes(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    """
    world.wishes.wishes.clear()
    available_wishes = dialogs.wish_strings.copy()

    for dialog_id in dialogs.wish_dialogs:
        wish = random.choice(possible_wishes)
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
    random_questions += random.sample(dialogs.backfill_questions, len(dialogs.quiz_dialogs) - len(random_questions))
    random.shuffle(random_questions)

    free_list = {
        0x22e082: 3953,  # Existing Questions
    }
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
        # Questions should be short enough that this doesn't happen, but give us a traceback if it does.
        if not base:
            raise ValueError("Unable to allocate space for question: {!r}".format(string))
        world.quiz.questions.append((dialog_id, string))
