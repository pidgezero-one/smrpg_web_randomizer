import random

from randomizer.logic import utils, flags
from randomizer.logic.dialogs import allocate_string
from randomizer.logic.patch import Patch


'''
IMPORTANT NOTES ABOUT MODIFYING:
* The fontset is only UPPER CASE A-Z, space and period. Everything else looks like a space.
* The font/color is dependant on the Y position. Dunno why.
* We're basically out of credits space. Can't add more cards, but could add more titles to those cards.
** Changing this might be hard.
** Dunno if the length is hard coded in the code, or if moving the string table would solve the space problem.
* Watch the whole credits! There's a chance it can freeze at the end or corrupt the firework screen if you do it wrong.

'''

EMPTY_STRING = '                                       '

def to_str(string):
    return ''.join([chr(i + ord('A') - 1) for i in string]).replace('\\', ' ').replace('[', '.')

def inv_str(string):
    string = string.replace(' ', '\\').replace('.', '[').replace('_', ']')
    return chr(len(string)) + ''.join([chr(ord(i) - ord('A') + 1) for i in string])

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
        self.acc += [0xE3, 0x00, 0x0F, 0x02, 0x0B, 0x16, 0x00, 0x01, 0x03, 0x04, 0x10, delay, 0x01]

    def end_thing_2(self, delay):
        self.acc += [0xE3, 0x00, 0x0F, 0x02, 0x16, 0x0B, 0x00, 0x01, 0x03, 0x04, 0x10, delay, 0x00]

    def end_thing_3(self, delay):
        self.acc += [0xE3, 0x00, 0x0F, 0x02, 0x16, 0x0B, 0x00, 0x09, 0x0B, 0x04, 0x10, delay, 0x00]

    def end_thing_4(self, delay):
        self.acc += [0xE3, 0x00, 0x0F, 0x02, 0x0B, 0x16, 0x00, 0x09, 0x0B, 0x04, 0x10, delay, 0x00]

    def clear(self, words):
        for (x, y, font) in words:
            self.add(x, y, font, EMPTY_STRING)
        del words[:]

    # Yeah, got into a OpenGL vibe here.
    def begin_credits(self):
        pass

    def add_credit(self, x, y, font, string, scroll=0):
        self.current_credits.append((x, y, font))
        self.add(x, y, font, string, scroll) #7

    def end_credits(self, delay_1, delay_2): # 26
        self.end_thing(delay_1)
        self.end_thing_2(delay_2)
        self.clear(self.current_credits)

    def begin_titles(self, delay):
        self.end_thing_3(delay) # 13
        self.clear(self.current_titles) #7

    def add_title(self, x, y, font, string, scroll=0):
        self.current_titles.append((x, y, font))
        self.add(x, y, font, string, scroll) #7

    def end_titles(self, delay):
        self.end_thing_4(delay) #13

    def empty_title(self):
        self.acc += [0xE3, 0, 0, 0, 0, 0, 0]

    def finalize(self):
        # Return a patch next time...
        credit_start = 0x3FDBB0
        credit_len = 3380
        #print(len(self.acc))

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
        #print("initial:", len(self.acc))
        if credit_len - len(self.acc) >= 101:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xc0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xc2, " ")
            self.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)
            #print("first:", len(self.acc))
        while credit_len - len(self.acc) >= 108:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xc0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xc2, " ")
            self.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)
            #print("ptr:", len(self.acc))

        #print("final:", credit_len - len(self.acc), "out of", credit_len)
        assert len(self.acc) <= credit_len

        string_table_start = 0x3FE8E4
        string_table_size = len(self.strings) * 2

        # Fill the unused section of credits script with 0.
        # This is very important.
        self.acc += (credit_len - len(self.acc)) * [0]

        free_list = {
            0x3f9c40: 952,
            credit_start + len(self.acc): credit_len - len(self.acc),
            string_table_start + string_table_size: 2080 - string_table_size
        }

        patch = Patch()
        patch.add_data(credit_start, bytearray(self.acc))
        for i in range(len(self.strings)):
            string = inv_str(self.strings[i])
            base = allocate_string(len(string), free_list)
            patch.add_data(base, string)
            patch.add_data(string_table_start + i*2, utils.ByteField(base & 0xFFFF, num_bytes=2).as_bytes())

        # Underscore
        patch.add_data(0x3FFDDA, '\x3F\xC0\x7F\x80')
        return patch

END_CREDITS_DELAY_1 = 34
END_CREDITS_DELAY_2 = 40
BEGIN_TITLES_DELAY = 50
END_TITLES_DELAY = 40


# LINE 1, LINE 2, LINE 3. put EMPTY_STRING if you don't have anything.
DEV_MESSAGES = [
    ('DONT TRY IT...ALANIM.', 'I ALREADY DID IT.', '   PAST ALANIM'),
    ('NOW TRY IT', 'BLINDFOLDED', '     PATCDR'),
    ('OH MAN I REALLY', 'HOPE THAT CODE WORKED', '       PIDGEZERO_ONE'),
    ('OHH I GOTTA THINK', 'OF SOMETHING FUNNY', '       YAKI'),
    ('WHY ARE YOU', 'USING ZSNES', '    DORKMASTER FLEK'),
    ('GARY WAS HERE', 'ASH IS A LOSER', EMPTY_STRING),
]

# Takes world because everything does.
# If we every implement stats, we'll need it, probably.
def update_credits(world):
    credits = Credits()

    # Don't need this for the first title.
    # credits.begin_title(BEGIN_TITLES_DELAY)
    #2
    credits.add_title(0x80, 0x00, 0x08, 'SUPER MARIO RPG ORIGINAL CREDITS')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'C. FUJIOKA   K. MATSUHARA')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. MAEKAWA   Y. MATSUMURA')
    credits.add_credit(0x80, 0x00, 0xc2, 'T. KUDO         Y. HASEBE')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #3
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'R. MUTO         F. FUKAYA')
    credits.add_credit(0x80, 0x40, 0x81, 'M. YOSHIOKA       A. OHTA')
    credits.add_credit(0x80, 0x00, 0xc2, 'AOY             H. MINABA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #5
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'K. KURASHIMA      K. KATO')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. HATAE     K. KURASHIMA')
    credits.add_credit(0x80, 0x00, 0xc2, 'J. MIFUNE        K. NISHI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #7
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'T. KURIHARA       A. UEDA')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. MIYAMOTO      Y. ABIRU')
    credits.add_credit(0x80, 0x00, 0xc2, 'M. TSUTSUI        T. MOGI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #8
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'Y. SASAKI    T. SAKAGUCHI')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. AZUMA     Y. SHIMOMURA')
    credits.add_credit(0x80, 0x00, 0xc2, 'T. SUGAWARA     H. SUZUKI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #10
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'M. WATANABE   C. MINEKAWA')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. HIRATA       Y. HIROTA')
    credits.add_credit(0x80, 0x00, 0xc2, 'K. MAEDA     K. TAKAHASHI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #12
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'R. MARUYA         N. WADA')
    credits.add_credit(0x80, 0x40, 0x81, 'A. ITO         T. WOOLSEY')
    credits.add_credit(0x80, 0x00, 0xc2, 'H. HAMADA        Y. CHIBA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #13
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'K. KAWASAKI     N. HANADA')
    credits.add_credit(0x80, 0x40, 0x81, 'R. KOUDA        R.KOMATSU')
    credits.add_credit(0x80, 0x00, 0xc2, 'K. KANEKO       H. MASUDA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #13
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'Y. SHIBANO   S. HASHIMOTO')
    credits.add_credit(0x80, 0x40, 0x81, 'K. HASHIMOTO    H. OHMORI')
    credits.add_credit(0x80, 0x00, 0xc2, 'M. SAKAKIBARA   T. KAYANO')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #14
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'A. YAMAGUCHI      H. ITOU')
    credits.add_credit(0x80, 0x40, 0x81, 'Y. KOTABE      N. UEMATSU')
    credits.add_credit(0x80, 0x00, 0xc2, 'K. TANABE       T. NOMURA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #15
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'A. TEJIMA    H. SAKAGUCHI')
    credits.add_credit(0x80, 0x40, 0x81, 'K. KONDO     S. TAKAHASHI')
    credits.add_credit(0x80, 0x00, 0xc2, 'H. YAMADA  T. KURIBAYASHI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #20
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'J. WORNELL    H. YAMAUCHI')
    credits.add_credit(0x80, 0x40, 0x81, 'K. MCDONALD     T. MIZUNO')
    credits.add_credit(0x80, 0x00, 0xc2, 'S. MIYAMOTO')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    #24
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'RANDOMIZER ORIGINAL CONCEPT')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xc0, 0xc0, 'ABYSSONYM')
    credits.add_credit(0x80, 0x80, 0x81, 'LACKATTACK')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #25
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'DEVELOPMENT')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'ALANIM    DORKMASTER FLEK')
    credits.add_credit(0x80, 0x40, 0x81, 'YAKIBOMB           SWINCH')
    credits.add_credit(0x80, 0x00, 0xc2, 'PATCDR      PIDGEZERO_ONE')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'ATBIGELOW        FORALIAS')
    credits.add_credit(0x80, 0x40, 0x81, 'AMAZING AMPHAROS')
    credits.add_credit(0x80, 0x00, 0xc2, 'SNESCHALMERS')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, '  SPRITING    FONTS AND ICONS')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, '  XIRR           SMBAI   ')
    credits.add_credit(0x80, 0x40, 0x81, 'DARKDATA       SEANCASS  ')
    credits.add_credit(0x80, 0x00, 0xc2, '                ALANIM   ')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'PALETTES')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'DEVILING            SMBAI')
    credits.add_credit(0x80, 0x40, 0x81, 'EGGTALK         HERRSHAUN')
    credits.add_credit(0x80, 0x00, 0xc2, 'MYOHMYKE       AARONDOBBE')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0xc0, 0xc0, 'MINAMIYO    PIDGEZERO_ONE')
    credits.add_credit(0x80, 0x80, 0x81, 'XIRR             DARKDATA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'DIALOGS')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'CYNAS       PIDGEZERO_ONE')
    credits.add_credit(0x80, 0x40, 0x81, 'BROATMEAL        DARKDATA')
    credits.add_credit(0x80, 0x00, 0xc2, 'SUPREME DIRT')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #27
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'QUALITY ASSURANCE AND RESEARCH')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'SEANCASS    INTHENAMEOFDT')
    credits.add_credit(0x80, 0x40, 0x81, 'LOCKECOLELIVE  GOZENGATTA')
    credits.add_credit(0x80, 0x00, 0xc2, 'CAVIN               SMBAI')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'TINYWETBLANKET    AIRNICK')
    credits.add_credit(0x80, 0x40, 0x81, 'WEFFJEBSTER     BROATMEAL')
    credits.add_credit(0x80, 0x00, 0xc2, 'CYNAS               FLARE')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'GUNTHERRIDEL     XELECIUM')
    credits.add_credit(0x80, 0x40, 0x81, 'MINAMIYO       CALERELIYA')
    credits.add_credit(0x80, 0x00, 0xc2, 'SPACE COW      SAXXON FOX')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'ATEATREE         INVARIEL')
    credits.add_credit(0x80, 0x40, 0x81, 'GOODMORNINGCRONO  LYLOVIR')
    credits.add_credit(0x80, 0x00, 0xc2, 'ANTHONY MULBERRY')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)
    
    #29
    if world.settings.is_flag_enabled(flags.RandomTadpolePondSong):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, 'MELODY BAY TUNES IN THIS SEED')
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        tadpole_submitters = list(set([world.tadpole_songs[0].submitter_credits, world.tadpole_songs[1].submitter_credits, world.tadpole_songs[2].submitter_credits]))
        if len(tadpole_submitters) == 1:
            credits.add_credit(0x80, 0x80, 0xc0, EMPTY_STRING)
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[0])
            credits.add_credit(0x80, 0x00, 0xc2, EMPTY_STRING)
        elif len(tadpole_submitters) == 2:
            credits.add_credit(0x80, 0x80, 0xc0, EMPTY_STRING)
            credits.add_credit(0x80, 0xc0, 0xc0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x80, 0x81, tadpole_submitters[1])
        else:
            credits.add_credit(0x80, 0x80, 0xc0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[1])
            credits.add_credit(0x80, 0x00, 0xc2, tadpole_submitters[2])
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)
    
    #30
    if world.settings.is_flag_enabled(flags.RandomSunkenShipPassword):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, 'SHIP PASSWORD IN THIS SEED')
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        credits.add_credit(0x80, 0x40, 0x81, world.password.submitter_credits)
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #31
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'SPECIAL THANKS')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xc0, 0xc0, 'DARKKEFKA       DOOMSDAY')
    credits.add_credit(0x80, 0x80, 0x81, 'GIANGURGOLO        OMEGA')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #32
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'INSPIRATION')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'ALTTP RANDOMIZER')
    credits.add_credit(0x80, 0x40, 0x81, 'OOT RANDOMIZER')
    credits.add_credit(0x80, 0x00, 0xc2, 'FFIV FREE ENTERPRISE')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #new
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'IF YOU WANT YOUR NAME HERE...')
    credits.end_titles(END_TITLES_DELAY)


    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, "VISIT")
    credits.add_credit(0x80, 0x40, 0x81, "RANDOMIZER.SMRPGSPEEDRUNS.COM")
    credits.add_credit(0x80, 0x00, 0xc2, "TO CONTRIBUTE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'SPECIAL DEV MESSAGE')
    credits.end_titles(END_TITLES_DELAY)


    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, dev_line1)
    credits.add_credit(0x80, 0x40, 0x81, dev_line2)
    credits.add_credit(0x80, 0x00, 0xc2, dev_line3)
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    #33
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'THANK YOU SMRPG COMMUNITY.')
    credits.add_credit(0x80, 0x40, 0x81, 'WITHOUT YOU...')
    credits.add_credit(0x80, 0x00, 0xc2, 'NONE OF THIS WOULD BE POSSIBLE.')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    #38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, 'DEDICATED IN MEMORY OF')
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xc0, 'TINYWETBLANKET')
    credits.add_credit(0x80, 0x40, 0x81, 'THANK YOU MIKAYLA')
    credits.add_credit(0x80, 0x00, 0xc2, 'WE MISS YOU')
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    credits.end_thing(END_CREDITS_DELAY_1) # Yeah, my abstraction breaks at the end.

    return credits.finalize()
