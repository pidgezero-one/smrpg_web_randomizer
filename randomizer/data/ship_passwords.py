import random

hint_authors = [
    "         Memo left by Alanim:",
    "   Memo left by Amazing Ampharos:",
    "        Memo left by atbigelow:",
    "        Memo left by Cavin856:",
    "    Memo left by Dorkmaster Flek:",
    "        Memo left by FlareRDB:",
    "       Memo left by Gozengatta:",
    "     Memo left by inthenameofDT:",
    "     Memo left by LockeColeLive:",
    "         Memo left by patcdr:",
    "          Memo left by pidge:",
    "        Memo left by SeanCass:",
    "           Memo left by Smbai:",
    "     Memo left by SNESChalmers:"
    "         Memo left by swinch:",
    "     Memo left by Tinywetblanket:",
    "        Memo left by Yakibomb:",
]


class Password:
    word = ""
    trampoline_hint = ""
    troopa_hint = ""
    maze_hint = ""
    snake_hint = ""
    cannonball_hint = ""
    barrel_hint = ""
    drybones_hint = None
    entrance_hint = None
    saveroom_hint = None
    greaper_hint = None
    greaper_hint_2 = None


    
    submitter = "anonymous"
    submitter_credits = "ANONYMOUS"
    submitter_hint_prefix = "       Memo left by Anonymous:"

    def __init__(self, word, hint1, hint2, hint3, hint4, hint5, hint6, hint7=None, hint8=None, hint9=None, hint10=None, hint11=None, submitter="Anonymous", submitter_credits="ANONYMOUS", submitter_hint_prefix="       Memo left by Anonymous:"):
        self.word = word
        self.trampoline_hint = hint1
        self.troopa_hint = hint2
        self.maze_hint = hint3
        self.snake_hint = hint4
        self.cannonball_hint = hint5
        self.barrel_hint = hint6
        self.entrance_hint = hint7
        self.saveroom_hint = hint8
        self.greaper_hint = hint9
        self.greaper_hint_2 = hint10
        self.drybones_hint = hint11
        self.optional_hints = []
        self.submitter = submitter
        self.submitter_credits = submitter_credits
        self.submitter_hint_prefix = submitter_hint_prefix

pool = (
    Password(
        "twoson",
        "%RANDOM_WRITER%\n\n         It is from Earthbound.[await]",
        "%RANDOM_WRITER%\n\n      It has an “s” in the word.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n             It wasn't first.[await]",
        "%RANDOM_WRITER%\n               At least...\n  two consonants are side by side.[await]",
        "%RANDOM_WRITER%\n\n   The “w” comes before the “o”s.[await]",
        "           Memo left by Ness:\n\n      It's where I met Everdred.[await]",
        "           Memo left by Paula:\n\n           It is my home town.[await]",
        "           Memo left by Jeff:\n\nApple Kid is at least as good as me.[await]",
        "           Memo left by Poo:\n             A quaint town,\n   Paula has told me much about it.[await]",
    ),
    Password(
        "↑←→↑←→",
        "%RANDOM_WRITER%\n\n        It is Epona's favourite.[await]",
        "%RANDOM_WRITER%\n\n            Malon teaches it.[await]",
        "%RANDOM_WRITER%\n\n             It's all arrows.[await]",
        "%RANDOM_WRITER%\n\n      You can hear it on a ranch.[await]",
        "%RANDOM_WRITER%\n\n It has two of each character in it.[await]",
        "%RANDOM_WRITER%\n         It can also be played in\n               Melody Bay.[await]",
        " It was the weirdest thing, he pulled\n out his ocarina and the song just\n carried on the wind.[await][page]\n A horse came running up seconds\n later, but there's no way it could\n have been there.[await][pause]\n     -Kakariko village guards report[await]",
        " I'm gonna call you “grasshopper”!\n\n                                  -Romani[await]",
        "                  Neigh.\n\n                                    -Epona[await]",
        " Is that Epona? How did you tame\n that wild horse right under my\n nose?![await][pause] I was going to present that\n horse to the great Ganondorf...\n                                      -Ingo[await]",
    ),
    Password(
        "fzerox",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n      There is an “X” and a “Z”.[await]",
        "%RANDOM_WRITER%\n\n     There is an “F” in the word.[await]",
        "%RANDOM_WRITER%\n\n    The “X” comes after the “R”.[await]",
        "%RANDOM_WRITER%\n\n    The “E” comes before the “O”.[await]",
        "%RANDOM_WRITER%\n\n         You Got Boost Power![await]",
        "%RANDOM_WRITER%\n\n                  Go Fast.[await]",
        "%RANDOM_WRITER%\n\n  Doing a side attack re-gains grip.[await]",
        "%RANDOM_WRITER%\n\n         Nobody likes Big Hand.[await]",
        "%RANDOM_WRITER%\n\n            Beware Fire Field.[await]",
        "\nDRY BONES: No, I don't drive\n Sonic Phantom.[await]",
    ),
    Password(
        "bowser",
        "%RANDOM_WRITER%\n\n           He has 8 children.[await]",
        "%RANDOM_WRITER%\n\n    The “R” comes after the “O”.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n     There is an “S” in the word.[await]",
        "%RANDOM_WRITER%\n\n       The “O” is beside the “B”.[await]",
        "%RANDOM_WRITER%\n               At least...\n  two consonants are side by side.[await]",
        "%RANDOM_WRITER%\n\n           Beware of the fire.[await]",
        "%RANDOM_WRITER%\n\n          The spikes can hurt.[await]",
        "\n              STAFF NOTICE[await][page]\n The password has been changed to\n the GIVEN NAME of our king and\n admiral.[await]\n                           ~ Management[await]",
        "%RANDOM_WRITER%\n\n    He is gonna work me to death.[await]",
        "DRY BONES: I was a Koopa, just\n like my boss... once.[await]",
        "Naegleria & Cynas",
        "NAEGLERIA",
        "   Memo left by Naegleria & Cynas:"
    ),
    Password(
        "mallow",
        "%RANDOM_WRITER%\n\n     There is an “M” in the word.[await]",
        "%RANDOM_WRITER%\n\n    There is a “W” in the word.[await]",
        "%RANDOM_WRITER%\n\n          It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n        It has four consonants.[await]",
        "%RANDOM_WRITER%\n\n      An “L” follows another “L”.[await]",
        "%RANDOM_WRITER%\n\n    The “A” comes before the “O”.[await]",
        "%RANDOM_WRITER%\n\n              He cries a lot.[await]",
        "%RANDOM_WRITER%\n\n             Pink pompadour.[await]",
        "%RANDOM_WRITER%\n\n           Looks like popcorn.[await]",
        "%RANDOM_WRITER%\n\n    Doesn't look like a frog to me.[await]",
        "\nDRY BONES: The password is a\n name.[await]",
        "Naegleria",
        "NAEGLERIA",
        "        Memo left by Naegleria:"
    ),
    Password(
        "smithy",
        "%RANDOM_WRITER%\n\n          It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n    The “M” comes before the “T”.[await]",
        "%RANDOM_WRITER%\n\n      A “Y” is used as a vowel.[await]",
        "%RANDOM_WRITER%\n\nThe “S” is between two consonants.[await]",
        "%RANDOM_WRITER%\n\n There are two pairs of consonants.[await]",
        "%RANDOM_WRITER%\n\n    The “H” comes before the “Y”.[await]",
        "%RANDOM_WRITER%\n\n              A strong boss.[await]",
        "%RANDOM_WRITER%\n\n      His lair's theme is in 13/8.[await]",
        "%RANDOM_WRITER%\n\n            Great moustache.[await]",
        "%RANDOM_WRITER%\n    I bet someone will point out the\n             time signature.[await]",
        "\nDRY BONES: The password is a\n name.[await]",
        "Naegleria",
        "NAEGLERIA",
        "        Memo left by Naegleria:"
    ),
    Password(
        "flower",
        "%RANDOM_WRITER%\n\n          A pretty little thing.[await]",
        "%RANDOM_WRITER%\n\n      Contains the word “OWE”.[await]",
        "%RANDOM_WRITER%\n\n             Give me an “F”![await]",
        "%RANDOM_WRITER%\n\n      Contains the word “LOW”.[await]",
        "%RANDOM_WRITER%\n\n            Wiggler wears it.[await]",
        "%RANDOM_WRITER%\n\n You've likely collected some so far.[await]",
        "%RANDOM_WRITER%\n I've seen dozens of Fire types, but\n          Ice ones also exist.[await]",
        "%RANDOM_WRITER%\n\n        You reap what you sow.[await]",
        "%RANDOM_WRITER%\n\n    Arrangements... will be made.[await]",
        "%RANDOM_WRITER%\n\n            What's that smell?[await]",
        "\n      DRY BONES: Leaf me alone.[await]",
        "HeroicReplicas",
        "HEROICREPLICAS",
        "     Memo left by HeroicReplicas:"
    ),
    Password(
        "crafts",
        "%RANDOM_WRITER%\n\nBICOASTAL: Shipwreck + Letter #1.[await]",
        "%RANDOM_WRITER%\n\n  ORLOPS: Shipwreck + Letter #2.[await]",
        "%RANDOM_WRITER%\n\n  RAREFY: Shipwreck + Letter #3.[await]",
        "%RANDOM_WRITER%\n\n      NO-FACE: Shipwreck + #4.[await]",
        "%RANDOM_WRITER%\n\n      CHATTY: Shipwreck + #5.[await]",
        "%RANDOM_WRITER%\n\n        GUST: Shipwreck + #6.[await]",
        "        Here is an example hint.\n\nNONLEGAL: a wrecked GALLEON + N.[await]",
        "        Here is an example hint.\n\n  BADGER: a wrecked BARGE + D.[await]",
        "        Here is an example hint.\n\n    AFTER: a wrecked RAFT + E.[await]",
        "        Here is an example hint.\n             MAGNA CARTA:\n     a wrecked CATAMARAN + G.[await]",
        "DRY BONES: The password's letters\n are hidden among six wrecked kinds\n of ship.[await]",
        "Projectyl",
        "PROJECTYL",
        "        Memo left by Projectyl:"
    ),
    Password(
        "ocelot",
        "%RANDOM_WRITER%\n\n  You might *spot* it in the jungle.[await]",
        "%RANDOM_WRITER%\n\n     All 6 characters are letters.[await]",
        "%RANDOM_WRITER%\n      It has as many consonants\n               as vowels.[await]",
        "%RANDOM_WRITER%\n\n   Small, but more than *a little*.[await]",
        "%RANDOM_WRITER%\n\n           Starts with an “O”.[await]",
        "%RANDOM_WRITER%\n\n         It's a pretty good cat.[await]",
        None,None,None,None,None,
        "TriumphantBass",
        "TRIUMPHANTBASS",
        "    Memo left by TriumphantBass:"
    ),
    Password(
        "wallet",
        "%RANDOM_WRITER%\n\n      It often has pictures in it.[await]",
        "%RANDOM_WRITER%\n\n      There is a “T” in the word.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n        It has four consonants.[await]",
        "%RANDOM_WRITER%\n\n  A consonant repeats in the word.[await]",
        "%RANDOM_WRITER%\n\n    The “W” comes before the “T”.[await]",
        "\n             I may be folded.[await]",
        "\n            I may be stuffed.[await]",
        "\n           I may be on a chain.[await]"
        "\n           I might have a bill.[await]"
        "\n     DRY BONES: I may be sat on.[await]",
        "Aweglib",
        "AWEGLIB",
        "         Memo left by Aweglib:"
    ),
    Password(
        "stamos",
        "%RANDOM_WRITER%\n     It is the name of an actor on\n              “Full House”.[await]",
        "%RANDOM_WRITER%\n\n    There are two “S” in the word.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n        It has four consonants.[await]",
        "%RANDOM_WRITER%\n\n   It is also an emote from a king.[await]",
        "%RANDOM_WRITER%\n\n    The “M” comes before the “O”.[await]",
        None,
        " BarbarousKing passed through\n here. He was so lost, he started\n guessing at the password.[await][page]\n But all he could think of was the\n actor that played Jesse on\n “Full House”.[await]"
        " It's a make-shift crossword\n puzzle. The letters contain\n “S”, “M”, “A”, “O”, and “T”.[await]",
        "%RANDOM_WRITER%\n\n  You could just Google the answer.[await]",
        "DRY BONES: Have you been reading\n the notes posted around these\n rooms?[await]",
        "FedoraFriday",
        "FEDORAFRIDAY",
        "      Memo left by FedoraFriday:"
    ),
    Password(
        "boxboy",
        "%RANDOM_WRITER%\n\n   It is found in a treasure chest.[await]",
        "%RANDOM_WRITER%\n\n      It's best buds with Fautso.[await]",
        "%RANDOM_WRITER%\n\n       Two letters appear twice.[await]",
        "%RANDOM_WRITER%\n\n      There is a “Y” in the word.[await]",
        "%RANDOM_WRITER%\n\n     It usually lives underground.[await]",
        "%RANDOM_WRITER%\n\n     It counters Special attacks.[await]",
        None,None,None,None,None,
        "Cynas",
        "CYNAS",
        "          Memo left by Cynas:"
    ),
    Password(
        "catnip",
        "%RANDOM_WRITER%\n\n     It's a bite that doesn't hurt.[await]",
        "%RANDOM_WRITER%\n\n          It's a purrfect treat.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n      Its consumer is consumed.[await]",
        "%RANDOM_WRITER%\n\n      It's named for its lovers.[await]",
        "%RANDOM_WRITER%\n\n      It has no repeated letters.[await]"
    ),
    Password(
        "chess2",
        "%RANDOM_WRITER%\n\n          An infamous sequel.[await]",
        "%RANDOM_WRITER%\n\n  It's played on a checkered board.[await]",
        "%RANDOM_WRITER%\n\n              David Sirlin?[await]",
        "%RANDOM_WRITER%\n\n          It contains two “S”.[await]",
        "%RANDOM_WRITER%\n\n          It contains a number.[await]",
        "%RANDOM_WRITER%\n\n        It has four consonants.[await]",
    ),
    Password(
        "comedy",
        "%RANDOM_WRITER%\n\n             A theatre genre.[await]",
        "%RANDOM_WRITER%\n\n     It's a synonym for “humour”.[await]",
        "%RANDOM_WRITER%\n\n    The “C” comes before the “O”.[await]",
        "%RANDOM_WRITER%\n\n      There is a “Y” in the word.[await]",
        "%RANDOM_WRITER%\n             As You Like It,\n       Much Ado About Nothing.[await]",
        "%RANDOM_WRITER%\n\n            It contains “me”.[await]",
        "%RANDOM_WRITER%\n           The sum of tragedy,\n   and something you cannot stop.[await]",
        "%RANDOM_WRITER%\n\n      The obverse of misfortune.[await]",
        "%RANDOM_WRITER%\n\n       Cooperate with Me or Dye.[await]",
        " With adjective Divine, Featuring\n Dante from the “Devil May Cry”\n series.[await]",
    ),
    Password(
        "hamlet",
        "%RANDOM_WRITER%\n\n           A little bit of pig.[await]",
        "%RANDOM_WRITER%\n\n      Another word for “village”.[await]",
        "%RANDOM_WRITER%\n\n       “Amleth” by another name.[await]",
        "%RANDOM_WRITER%\n\n           It has two vowels.[await]",
        "%RANDOM_WRITER%\n\n    The “M” comes before the “L”.[await]",
        "%RANDOM_WRITER%\n\n          A prince and a play.[await]",
    ),
    Password(
        "aeneid",
        "%RANDOM_WRITER%\n\n     Fuel for “Homer” fanfiction.[await]",
        "%RANDOM_WRITER%\n\n       An embarrassing classic.[await]",
        "%RANDOM_WRITER%\n\n   Concerning a man and his arms.[await]",
        "%RANDOM_WRITER%\n\n     One letter is repeated twice.[await]",
        "%RANDOM_WRITER%\n\n        The word is its subject.[await]",
        "%RANDOM_WRITER%\n      And life with a groan fled\n  indignant into the shadows below.[await]",
    ),
    Password(
        "wrppps",
        "          Memo left by Jolene:\n   They're modes of fast transport\n              for Gonzalez.[await]",
        "          Memo left by Jolene:\n       Ignoring vowels is so you,\n                Gonzalez.[await]",
        "          Memo left by Dazzle:\n Even I think 3 identical letters in a\n            row is too much![await]",
        "          Memo left by Dazzle:\n\n Any star pieces hidden back there?[await]",
        "  Memo left by Traveling Sisters 3:\n\n   We love charades! .. 2 words![await]",
        "  Memo left by Traveling Sisters 3:\n   We're too terrified of the biting\n         plants to use that![await]",
        " You ever notice how sometimes you\n can just skip letters and still\n know what a word is?",
        " Lk, cn y rd ths vn thgh thr rn't ny\n vwls?[await]"
        " Classic modes of moving from one\n place to another are the best.[await][pause] Well,\n other than running.[delay] Gross.[await]",
        " You ever wonder how plumbers move\n around so quickly?[await][pause] One second\n they're in a sewer, and the next\n they're in the sky.[await]\n It's kinda weird.[await]"
        "\n   DRY BONES: Naps are the best.[await]",
        "Calereliya",
        "CALERELIYA",
        "        Memo left by Calereliya:"
    ),
    Password(
        "beetle",
        "          Memo left by Petuni:\n    Uh, I'm a PUNI. How DARE you\n        compare us to that bug?[await]",
        "          Memo left by Petuni:\n    I'm not even that small, Mario!\n     Even I could keep it as a pet![await]",
        "       Memo left by Rawk Hawk:\n Yeah, I RAAAWK! But when I smash\n          you, you'll REEEK![await]",
        "       Memo left by Rawk Hawk:\n Get back in the rookie room, scrub!\n You and those creepy flying things![await]",
        "            Memo left by Pat:\n       Look, I gave you RSTLNE.\n        That's 3 of the letters![await]",
        "          Memo left by Vanna:\n\n  (Pssst, the other letter is a B.)[await]",
        None,None,None,None,None,
        "Calereliya",
        "CALERELIYA",
        "        Memo left by Calereliya:"
    ),
    Password(
        "♪♪♪♪♪♪",
        "        Memo left by Toadofsky:\n\n               BRILLIANT![await]",
        "      Memo left by Cranky Kong:\n   I can get down with it too, you\n       young whippersnappers![await]",
        "          Memo left by Banjo:\n\n    Hey Kazooie! I love this tune![await]",
        "         Memo left by Kazooie:\n    I am so sick of gathering these\n       things. You have no idea.[await]",
        "        Memo left by Gruntilda:\n     Locked is the door; you must\n         search all the floors![await]",
        "        Memo left by Bruntilda:\n  She played in Grunty and the Flute\nFellows. Her guitar is... not good.[await]",
        None,None,None,None,None,
        "Calereliya",
        "CALERELIYA",
        "        Memo left by Calereliya:"
    ),
    Password(
        "shells",
        "%RANDOM_WRITER%\n\n It is found on the bed of the ocean.[await]",
        "%RANDOM_WRITER%\n\n     There is an “H” in the word.[await]",
        "%RANDOM_WRITER%\n\n           It has one vowel.[await]",
        "%RANDOM_WRITER%\n\n    One letter appears as a pair.[await]",
        "%RANDOM_WRITER%\n        A letter appears twice,\n           but not as a pair.[await]",
        "%RANDOM_WRITER%\n\n           The word is plural.[await]",
        "%RANDOM_WRITER%\n\n            Find more pearls.",
        "%RANDOM_WRITER%\n\n      Scour the sea bed for them.",
        "%RANDOM_WRITER%\n\n          They were all empty.",
        "%RANDOM_WRITER%\n Is there a difference between those\n found in the sea and on the beach?[await]"
        "\n    DRY BONES: She sells them...[await]",
        "Naegleria",
        "NAEGLERIA",
        "        Memo left by Naegleria:"
    ),
    Password(
        "donkey",
        "       Memo left by Roland Yeep:\n\n      He rolls through the jungle.[await]",
        "        Memo left by Miya Moto:\n  What he IS, and what he's NAMED,\n        are not remotely similar.[await]",
        "     Memo left by Teetee Veechat:\n\n    There is a “D” in the word.[await]",
        "         Memo left by W. Inky:\n           It has two vowels,\n         and four consonants.[await]",
        "%RANDOM_WRITER%\n     Both vowels have consonants\n         on either side of them.[await]",
        "         Memo left by the Krew:\n\n    The “N” comes before the “K”.[await]",
        " The password is about the hero of\n another far-off island...[await]",
        " His greatest foe got his start on\n a ship similar to this one...[await]",
        " This hero is “crazy” about a\n specific type of food![await]",
        " He makes a cameo here in the\n Mushroom Kingdom![await][pause] Though, he\n doesn't appreciate his wardrobe\n very much...[await]"
        "DRY BONES: He's the leader of the\n bunch, you know him well![await]",
        "LimeFiasco",
        "LIMEFIASCO",
        "       Memo left by LimeFiasco:"
    ),
    Password(
        "weston",
        "           Memo left by Luigi:\n    It is the name of a ghost I've\n                 caught.[await]",
        "%RANDOM_WRITER%\n\n   It includes a cardinal direction.[await]",
        "%RANDOM_WRITER%\n       This ghost loves freezing\n              temperatures.[await]",
        "           Memo left by Luigi:\n      Is is the only ghost I found\n        in the mansion basement.[await]",
        "%RANDOM_WRITER%\n\n    The “O” comes before the “N”.[await]",
        "           Memo left by Luigi:\n     It is currently trapped safely\n            inside a portrait.[await]",
        "\n    North, East, South, and West.[await]",
        " We met an adventurer who enjoyed\n freezing temperatures. He locked\n himself inside of cold storage. [await]",
        "\n   “Sir ••••••••••, The Chilly Climber”[await][page]\n Weird... the name has been\n scribbled out.[await]",
        "\n    He has no idea he is a ghost...[await]",
        None,
        "Mr Dean",
        "MR DEAN",
        "         Memo left by Mr Dean:"
    ),
)

all_symbols = list('''♥♪•~©:;#×+%↑→←*&()-/?!.,\'''')
vowels = list('aeiouy')
uncommon_consonants = list('bcdfghjklmnpqrstvwxz')

symbols = list('''0123456789♪•~©↑→←*&,\'''')
common_consonants = list('bcdfghklmnprstw')

def get_similar_letters(letter):

    if letter in all_symbols:
        return [c for c in symbols if c != letter]
    elif letter in vowels:
        return [c for c in vowels if c != letter]
    elif letter in uncommon_consonants:
        return [c for c in common_consonants if c != letter]
    else:
        raise Exception('unusable password letter %s' % letter)


def suggest_letter_bank(word, position, decoy_word):
    # add correct letter
    letters = [word[position]]
    # pick one other letter from this word
    letters.append(random.choice([c for c in list(word) if c != word[position]]))
    # pick letter at this index from decoy word (another random word in the pool)
    if decoy_word[position] not in letters:
        letters.append(decoy_word[position])
    # get random letters similar to this one
    letter_bank = [c for c in get_similar_letters(word[position]) if c not in letters]
    # if not enough fillable letters from that, add a random consonant
    if len(letter_bank) < 5 - len(letters):
        letters.extend(random.sample(letter_bank, min(5-len(letters), len(letter_bank))))
    if len(letters) < 5:
        letters.extend(random.sample([c for c in common_consonants if c not in letters], 5-letters))
    random.shuffle(letters)
    return letters