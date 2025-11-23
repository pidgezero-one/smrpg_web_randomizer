import random

from randomizer.logic import utils, flags
from randomizer.logic.dialogs import allocate_string
from randomizer.logic.patch import Patch


"""
IMPORTANT NOTES ABOUT MODIFYING:
* The fontset is only UPPER CASE A-Z, space and period. Everything else looks like a space.
* The font/color is dependant on the Y position. Dunno why.
* We're basically out of credits space. Can't add more cards, but could add more titles to those cards.
** Changing this might be hard.
** Dunno if the length is hard coded in the code, or if moving the string table would solve the space problem.
* Watch the whole credits! There's a chance it can freeze at the end or corrupt the firework screen if you do it wrong.

"""

EMPTY_STRING = "                                       "

END_CREDITS_DELAY_1 = 34
END_CREDITS_DELAY_2 = 40
BEGIN_TITLES_DELAY = 50
END_TITLES_DELAY = 40

FINAL_DELAY = 0xFF


def to_str(string):
    return (
        "".join([chr(i + ord("A") - 1) for i in string])
        .replace("\\", " ")
        .replace("[", ".")
    )


def inv_str(string):
    string = string.replace(" ", "\\").replace(".", "[").replace("_", "]")
    return chr(len(string)) + "".join([chr(ord(i) - ord("A") + 1) for i in string])


class Credits(object):
    def __init__(self, table_offset=0):
        self.strings = {}
        self.inv_strings = {}
        self.acc = []
        self.table_offset = table_offset
        self.current_credits = []
        self.current_titles = []

    def add(self, x, y, font, string, scroll=0):
        assert len(string) <= len(EMPTY_STRING)
        if string in self.inv_strings:
            dex = self.inv_strings[string]
        else:
            dex = len(self.strings) + self.table_offset
            self.strings[dex] = string
            self.inv_strings[string] = dex
        self.acc += [0xE3, 0x12, dex, x, y, font, scroll]

    def end_thing(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x0B,
            0x16,
            0x00,
            0x01,
            0x03,
            0x04,
            0x10,
            delay,
            0x01,
        ]

    def end_thing_2(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x16,
            0x0B,
            0x00,
            0x01,
            0x03,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def end_thing_3(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x16,
            0x0B,
            0x00,
            0x09,
            0x0B,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def end_thing_4(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x0B,
            0x16,
            0x00,
            0x09,
            0x0B,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def clear(self, words):
        for x, y, font in words:
            self.add(x, y, font, EMPTY_STRING)
        del words[:]

    # Yeah, got into a OpenGL vibe here.
    def begin_credits(self):
        pass

    def add_credit(self, x, y, font, string, scroll=0):
        self.current_credits.append((x, y, font))
        self.add(x, y, font, string, scroll)  # 7

    def end_credits(self, delay_1, delay_2):  # 26
        self.end_thing(delay_1)
        self.end_thing_2(delay_2)
        self.clear(self.current_credits)

    def begin_titles(self, delay):
        self.end_thing_3(delay)  # 13
        self.clear(self.current_titles)  # 7

    def add_title(self, x, y, font, string, scroll=0):
        self.current_titles.append((x, y, font))
        self.add(x, y, font, string, scroll)  # 7

    def end_titles(self, delay):
        self.end_thing_4(delay)  # 13

    def empty_title(self):
        self.acc += [0xE3, 0, 0, 0, 0, 0, 0]

    def finalize(self):
        # Return a patch next time...
        credit_start = 0x3FDBB0
        credit_len = 3380
        # print(len(self.acc))

        # empty_string = ' ' * (remaining_space // 3)
        # space_filler = []

        # while remaining_space >= 73:
        #     remaining_space -= 73
        #     space_filler.append((self.begin_titles, [BEGIN_TITLES_DELAY]))
        #     space_filler.append((self.add_title, [0x80, 0x00, 0x08, EMPTY_STRING]))
        #     space_filler.append((self.end_titles, [END_TITLES_DELAY]))
        #     space_filler.append((self.begin_credits, []))
        #     space_filler.append((self.add_credit, [0x80, 0x80, 0xc0, EMPTY_STRING]))
        #     space_filler.append((self.add_credit, [0x80, 0x40, 0x81, EMPTY_STRING]))
        #     space_filler.append((self.add_credit, [0x80, 0x00, 0xc2, EMPTY_STRING]))
        #     space_filler.append((self.end_credits, [END_CREDITS_DELAY_1, END_CREDITS_DELAY_2]))

        # for i, (cmd, args) in enumerate(space_filler):
        #     if i == len(space_filler) - 1 and cmd == self.add_credit:
        #         args[3] == empty_string
        #     cmd(*args)

        # fill remaining space with pointers to empty text
        # print("initial:", len(self.acc))
        if credit_len - len(self.acc) >= 101:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xC0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xC2, " ")
            self.end_credits(FINAL_DELAY, END_CREDITS_DELAY_2)
            # print("first:", len(self.acc))
        while credit_len - len(self.acc) >= 108:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xC0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xC2, " ")
            self.end_credits(FINAL_DELAY, END_CREDITS_DELAY_2)
            # print("ptr:", len(self.acc))

        # print("final:", credit_len - len(self.acc), "out of", credit_len)
        assert len(self.acc) <= credit_len

        string_table_start = 0x3FE8E4
        string_table_size = len(self.strings) * 2

        # Fill the unused section of credits script with 0.
        # This is very important.
        self.acc += (credit_len - len(self.acc)) * [0]

        free_list = {
            0x3F9C40: 952,
            credit_start + len(self.acc): credit_len - len(self.acc),
            string_table_start + string_table_size: 2080 - string_table_size,
        }

        patch = Patch()
        patch.add_data(credit_start, bytearray(self.acc))
        for i in range(len(self.strings)):
            string = inv_str(self.strings[i])
            base = allocate_string(len(string), free_list)
            patch.add_data(base, string)
            patch.add_data(
                string_table_start + i * 2,
                utils.ByteField(base & 0xFFFF, num_bytes=2).as_bytes(),
            )

        # Underscore
        patch.add_data(0x3FFDDA, "\x3f\xc0\x7f\x80")
        return patch


# LINE 1, LINE 2, LINE 3. put EMPTY_STRING if you don't have anything.
DEV_MESSAGES = [
    ("DONT TRY IT...ALANIM.", "I ALREADY DID IT.", "   PAST ALANIM"),
    ("NOW TRY IT", "BLINDFOLDED", "     PATCDR"),
    ("IF YOU CAN READ THIS", "IT MEANS I FIXED IT", "       PIDGEZERO_ONE"),
    ("OHH I GOTTA THINK", "OF SOMETHING FUNNY", "       YAKI"),
    ("WHY ARE YOU", "USING ZSNES", "    DORKMASTER FLEK"),
    ("GARY WAS HERE", "ASH IS A LOSER", EMPTY_STRING),
]


# Takes world because everything does.
# If we every implement stats, we'll need it, probably.
def update_credits(world):
    credits = Credits()

    # Don't need this for the first title.
    # credits.begin_title(BEGIN_TITLES_DELAY)

    # This is what the remake does. We can do it too to make room for randomizer credits.
    credits.add_title(0x80, 0x00, 0x08, "SINCE MCMXCVI")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "BASED ON THE WORK OF")
    credits.add_credit(0x80, 0x40, 0x81, "THE ORIGINAL")
    credits.add_credit(0x80, 0x00, 0xC2, "DEVELOPMENT STAFF")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Randomizer credits strt here.
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "RANDOMIZER CONCEPT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "ABYSSONYM")
    credits.add_credit(0x80, 0x80, 0x81, "LACKATTACK")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 25
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "DEVELOPMENT LEADS")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "ALANIM    DORKMASTER FLEK")
    credits.add_credit(0x80, 0x80, 0xC2, "PATCDR      PIDGEZERO_ONE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0x81, "YAKIBOMB     ANAXEMRANGER")
    credits.add_credit(0x80, 0x40, 0xC0, "CLEARTONIC       FORALIAS")
    credits.add_credit(0x80, 0x00, 0x81, "AMAZING AMPHAROS   SWINCH")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARCHIPELAGO DEVELOPMENT LEAD")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x40, 0x81, "ROSALIE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARCHIPELAGO DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "SOLIDUS SNAKE")
    credits.add_credit(0x80, 0x80, 0x81, "BIGMALLETMAN")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "TEST WRITING")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "SERAPHIN EVELES")
    credits.add_credit(0x80, 0x80, 0x81, "WONDERJ")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARTWORK")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "XIRR")
    credits.add_credit(0x80, 0x40, 0x81, "DARKDATA")
    credits.add_credit(0x80, 0x00, 0xC2, "MR DEAN")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "SMBAI")
    credits.add_credit(0x80, 0x40, 0x81, "SEANCASS")
    credits.add_credit(0x80, 0x00, 0xC2, "ALANIM")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "DEVILING         MINAMIYO")
    credits.add_credit(0x80, 0x40, 0x81, "EGGTALK         HERRSHAUN")
    credits.add_credit(0x80, 0x00, 0xC2, "MYOHMYKE       AARONDOBBE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "WRITING")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "CYNAS       PIDGEZERO_ONE")
    credits.add_credit(0x80, 0x80, 0x81, "BROATMEAL        DARKDATA")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 27
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "QA AND RESEARCH")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "SEANCASS    INTHENAMEOFDT")
    credits.add_credit(0x80, 0x40, 0x81, "LOCKECOLELIVE  GOZENGATTA")
    credits.add_credit(0x80, 0x00, 0xC2, "CAVIN               FLARE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "TINYWETBLANKET      SMBAI")
    credits.add_credit(0x80, 0x40, 0x81, "WEFFJEBSTER     BROATMEAL")
    credits.add_credit(0x80, 0x00, 0xC2, "CYNAS        SNESCHALMERS")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "GUNTHERRIDEL     XELECIUM")
    credits.add_credit(0x80, 0x40, 0x81, "MINAMIYO       CALERELIYA")
    credits.add_credit(0x80, 0x00, 0xC2, "SPACE COW      SAXXON FOX")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ATEATREE         INVARIEL")
    credits.add_credit(0x80, 0x40, 0x81, "GOODMORNINGCRONO  LYLOVIR")
    credits.add_credit(0x80, 0x00, 0xC2, "ANTHONY MULBERRY")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 29
    if world.settings.is_flag_enabled(flags.RandomTadpolePondSong):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, "SELECTED MELODY BAY TUNES")
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        tadpole_submitters = list(
            set(
                [
                    world.tadpole_songs[0].submitter_credits,
                    world.tadpole_songs[1].submitter_credits,
                    world.tadpole_songs[2].submitter_credits,
                ]
            )
        )
        if len(tadpole_submitters) == 1:
            credits.add_credit(0x80, 0x80, 0xC0, EMPTY_STRING)
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[0])
            credits.add_credit(0x80, 0x00, 0xC2, EMPTY_STRING)
        elif len(tadpole_submitters) == 2:
            credits.add_credit(0x80, 0x80, 0xC0, EMPTY_STRING)
            credits.add_credit(0x80, 0xC0, 0xC0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x80, 0x81, tadpole_submitters[1])
        else:
            credits.add_credit(0x80, 0x80, 0xC0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[1])
            credits.add_credit(0x80, 0x00, 0xC2, tadpole_submitters[2])
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 30
    if world.settings.is_flag_enabled(flags.RandomSunkenShipPassword):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, "SELECTED SHIP PASSWORD")
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        credits.add_credit(0x80, 0x40, 0x81, world.password.submitter_credits)
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 31
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "SPECIAL THANKS")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "DARKKEFKA       DOOMSDAY")
    credits.add_credit(0x80, 0x80, 0x81, "GIANGURGOLO        OMEGA")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 32
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "INSPIRATION")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ALTTP RANDOMIZER")
    credits.add_credit(0x80, 0x40, 0x81, "OOT RANDOMIZER")
    credits.add_credit(0x80, 0x00, 0xC2, "FFIV FREE ENTERPRISE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # new
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "IF YOU WANT YOUR NAME HERE...")
    credits.end_titles(END_TITLES_DELAY)

    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "VISIT")
    credits.add_credit(0x80, 0x40, 0x81, "RANDOMIZER.SMRPGSPEEDRUNS.COM")
    credits.add_credit(0x80, 0x00, 0xC2, "TO CONTRIBUTE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "SPECIAL DEV MESSAGE")
    credits.end_titles(END_TITLES_DELAY)

    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, dev_line1)
    credits.add_credit(0x80, 0x40, 0x81, dev_line2)
    credits.add_credit(0x80, 0x00, 0xC2, dev_line3)
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    # 33
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "THANK YOU SMRPG COMMUNITY.")
    credits.add_credit(0x80, 0x40, 0x81, "WITHOUT YOU...")
    credits.add_credit(0x80, 0x00, 0xC2, "NONE OF THIS WOULD BE POSSIBLE.")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "DEDICATED TO")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "TINYWETBLANKET")
    credits.add_credit(0x80, 0x40, 0x81, "THANK YOU MIKAYLA")
    credits.add_credit(0x80, 0x00, 0xC2, "WE MISS YOU")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    credits.end_thing(END_CREDITS_DELAY_1)  # Yeah, my abstraction breaks at the end.

    return credits.finalize()
