from randomizer.helpers.eventtables import Music, AreaObjects, RadialDirections
from randomizer.helpers.objectsequencetables import SequenceSpeeds, _0x10Flags
from math import floor


class SongNote:
    val = None
    name = ""
    sfx = None


class Fa(SongNote):
    val = 0
    name = "Fa"
    sfx = 36


class So(SongNote):
    val = 1
    name = "So"
    sfx = 37


class La(SongNote):
    val = 2
    name = "La"
    sfx = 38


class Ti(SongNote):
    val = 3
    name = "Ti"
    sfx = 39


class Do(SongNote):
    val = 4
    name = "Do"
    sfx = 40


class Re(SongNote):
    val = 5
    name = "Re"
    sfx = 41


class Mi(SongNote):
    val = 6
    name = "Mi"
    sfx = 42


class Note:
    note = None
    duration = 0

    def __init__(self, note, duration):
        self.note = note
        self.duration = duration


original_toadofsky_confirmations = [
    "EVENT_1074_pause_107",
    "EVENT_1074_pause_113",
    "EVENT_1074_pause_113",
    "EVENT_1074_pause_121",
    "EVENT_1074_pause_121",
    "EVENT_1074_pause_129",
    "EVENT_1074_pause_129",
    "EVENT_1074_pause_137",
    "EVENT_1074_pause_145",
]


class Song:
    notes = []
    name = ""
    submitter = ""
    submitter_credits = "ANONYMOUS"
    apprentice_hint_1 = ""
    apprentice_hint_2 = ""
    mole_hint = ""
    scroll_text = ""

    def __init__(
        self,
        notes,
        name,
        submitter="Anonymous",
        submitter_credits="ANONYMOUS",
        hint_1="",
        hint_2="",
        hint_3="",
        scroll="",
    ):
        self.notes = [Note(n, d) for (n, d) in notes]
        self.name = name
        self.submitter = submitter
        self.submitter_credits = submitter_credits
        self.apprentice_hint_1 = hint_1
        self.apprentice_hint_2 = hint_2
        self.mole_hint = hint_3
        self.scroll_text = scroll

    def generate_starfish_hint(self, subscript):
        note_index = 0
        output = []
        for index, cmd in enumerate(subscript):
            # replace or remove the sound effect
            if cmd["command"] == "play_sound" and note_index < len(self.notes):
                output.append(
                    {
                        "identifier": "EVENT_2061_action_queue_async_2_SUBSCRIPT_play_sound_%i"
                        % index,
                        "command": "play_sound",
                        "args": [self.notes[note_index].note.sfx],
                    }
                )
                note_index += 1
            elif cmd["command"] != "play_sound":
                output.append(cmd)
        return output

    def generate_tadpole_hint(self):
        num_notes_to_hint = floor(len(self.notes) * 5 / 8)
        notes_to_hint = self.notes[:num_notes_to_hint]
        delays = [45 for n in notes_to_hint]
        delays[0] = 30
        if len(delays) > 1:
            delays[len(delays) - 2] = 75
        delays[len(delays) - 1] = 100

        notes_to_write = zip(notes_to_hint, delays)

        output = []

        for index, pair in enumerate(notes_to_write):
            output.extend(
                [
                    {
                        "identifier": "EVENT_1088_play_sound_%i" % index,
                        "command": "play_sound",
                        "args": [pair[0].note.sfx, 6],
                    },
                    {
                        "identifier": "EVENT_1088_pause_%i" % index,
                        "command": "pause",
                        "args": [pair[1]],
                    },
                ]
            )
        output.append({"identifier": "EVENT_1088_ret", "command": "ret"})

        return output

    def generate_input_script(self, song_order):
        def prefix_command_name(cmd_name):
            return "EVENT_%i_%s" % (song_order + 1082, cmd_name)

        note_variable_pairs = zip(
            self.notes, [0x7024, 0x7026, 0x7028, 0x702A, 0x702C, 0x702E, 0x7030, 0x7032]
        )

        output = []

        for index, pair in enumerate(note_variable_pairs):
            address = pair[1]

            note_input = [
                {
                    "identifier": "set_7000_to_tapped_button_%i" % index,
                    "command": "set_7000_to_tapped_button",
                },
                {"identifier": "pause_%i" % index, "command": "pause", "args": [1]},
                {
                    "identifier": "mem_7000_and_const_%i" % index,
                    "command": "mem_7000_and_const",
                    "args": [0x0080],
                },
                {
                    "identifier": "jmp_if_7000_equals_short_%i" % index,
                    "command": "jmp_if_var_equals_const",
                    "args": [
                        0x7000,
                        128,
                        prefix_command_name("jmp_if_bit_clear_%i" % index),
                    ],
                },
                {
                    "identifier": "jmp_%i" % index,
                    "command": "jmp",
                    "args": [
                        prefix_command_name("set_7000_to_tapped_button_%i" % index)
                    ],
                },
                {
                    "identifier": "jmp_if_bit_clear_%i" % index,
                    "command": "jmp_if_bit_clear",
                    "args": [
                        0x7044,
                        3,
                        prefix_command_name("set_7000_to_tapped_button_%i" % index),
                    ],
                },
                {
                    "identifier": "set_action_script_sync_%i" % index,
                    "command": "set_action_script",
                    "args": [0x14 + index, True, 571],
                },
                {
                    "identifier": "set_7000_to_7000_short_mem_%i" % index,
                    "command": "copy_var_to_var",
                    "args": [0x7012, 0x7000],
                },
                {
                    "identifier": "jmp_to_subroutine_%i" % index,
                    "command": "jmp_to_subroutine",
                    "args": ["EVENT_1074_jmp_if_7000_equals_short_369"],
                },
                {
                    "identifier": "EVENT_1082_dec_short_mem_%i" % index,
                    "command": "dec_var_from_7000",
                    "args": [0x7010],
                },
                {
                    "identifier": "jmp_to_subroutine__%i" % index,
                    "command": "run_event_as_subroutine",
                    "args": [1085],
                },
            ]
            if index < len(self.notes) - 1:
                note_input.extend(
                    [
                        {
                            "identifier": "copy_var_to_var_%i" % index,
                            "command": "copy_var_to_var",
                            "args": [0x7012, address],
                        },
                        {
                            "identifier": "copy_var_to_var__%i" % index,
                            "command": "copy_var_to_var",
                            "args": [0x7012, 0x7010],
                        },
                        {
                            "identifier": "action_queue_sync_13_%i" % index,
                            "command": "action_queue",
                            "args": [AreaObjects.SCREEN_FOCUS, True],
                            "subscript": [
                                {
                                    "identifier": "EVENT_1082_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0",
                                    "command": "set_animation_speed",
                                    "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]],
                                },
                                {
                                    "identifier": "EVENT_1082_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_1",
                                    "command": "shift_northeast_steps",
                                    "args": [2],
                                },
                                {
                                    "identifier": "EVENT_1082_action_queue_sync_13_SUBSCRIPT_ret_2",
                                    "command": "ret",
                                },
                            ],
                        },
                        {
                            "identifier": "action_queue_async_%i" % index,
                            "command": "action_queue",
                            "args": [0x14 + index + 1, False],
                            "subscript": [
                                {
                                    "identifier": "EVENT_1082_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_0",
                                    "command": "transfer_to_xyzf",
                                    "args": [
                                        7 + index,
                                        41 - (index * 2),
                                        0,
                                        RadialDirections.EAST,
                                    ],
                                },
                                {
                                    "identifier": "EVENT_1082_action_queue_async_14_SUBSCRIPT_shift_southeast_pixels_1",
                                    "command": "shift_southeast_pixels",
                                    "args": [5],
                                },
                                {
                                    "identifier": "EVENT_1082_action_queue_async_14_SUBSCRIPT_shift_southwest_pixels_2",
                                    "command": "shift_southwest_pixels",
                                    "args": [4],
                                },
                                {
                                    "identifier": "EVENT_1082_action_queue_async_14_SUBSCRIPT_ret_3",
                                    "command": "ret",
                                },
                            ],
                        },
                        {
                            "identifier": "set_action_script_sync___%i" % index,
                            "command": "set_action_script",
                            "args": [0x14 + index + 1, True, 570],
                        },
                        {
                            "identifier": "set_%i" % index,
                            "command": "set_var_to_const",
                            "args": [0x70A9, 0x14 + index + 1],
                        },
                        {
                            "identifier": "set_action_script_sync_____%i" % index,
                            "command": "set_action_script",
                            "args": [AreaObjects.MARIO, True, 515],
                        },
                    ]
                )
            else:
                note_input.extend(
                    [
                        {
                            "identifier": "pause_action_script_%i" % index,
                            "command": "pause_action_script",
                            "args": [AreaObjects.MARIO],
                        },
                        {
                            "identifier": "copy_var_to_var____%i" % index,
                            "command": "copy_var_to_var",
                            "args": [0x7012, address],
                        },
                        {
                            "identifier": "copy_var_to_var______%i" % index,
                            "command": "copy_var_to_var",
                            "args": [0x7012, 0x7010],
                        },
                        {
                            "identifier": "pause__%i" % index,
                            "command": "pause",
                            "args": [10],
                        },
                        {
                            "identifier": "copy_var_to_var_-_%i" % index,
                            "command": "set_var_to_const",
                            "args": [0x7012, 3],
                        },
                        {
                            "identifier": "set_7000_to_7000_short_mem___%i" % index,
                            "command": "copy_var_to_var",
                            "args": [0x7012, 0x7000],
                        },
                        {
                            "identifier": "dec_short_mem___%i" % index,
                            "command": "dec_var_from_7000",
                            "args": [0x7010],
                        },
                    ]
                )
                if len(self.notes) == 8:
                    note_input.append(
                        {
                            "identifier": "jmp_to_subroutine_end",
                            "command": "run_event_as_subroutine",
                            "args": [1085],
                        }
                    )
                elif len(self.notes) == 7:
                    note_input.append(
                        {
                            "identifier": "jmp_to_subroutine_end",
                            "command": "run_event_as_subroutine",
                            "args": [1087],
                        }
                    )
                else:
                    note_input.append(
                        {
                            "identifier": "jmp_to_subroutine_end",
                            "command": "run_event_as_subroutine",
                            "args": [1086],
                        }
                    )
                note_input.extend(
                    [
                        {
                            "identifier": "jmp__%i" % index,
                            "command": "jmp",
                            "args": ["EVENT_1074_set_bit_0"],
                        },
                        {"identifier": "EVENT_1082_ret_%i" % index, "command": "ret"},
                    ]
                )
            for item in range(len(note_input)):
                note_input[item]["identifier"] = prefix_command_name(
                    note_input[item]["identifier"]
                )
            output.extend(note_input)

        return output

    def generate_playback_script(self, song_order):
        def prefix_command_name(cmd_name):
            return "EVENT_%i_%s" % (song_order + 1079, cmd_name)

        note_variable_pairs = zip(
            self.notes, [0x7024, 0x7026, 0x7028, 0x702A, 0x702C, 0x702E, 0x7030, 0x7032]
        )

        # for songs with less than 8 notes, figure out how toadofsky should react to %s of correctness
        toadofsky_confirmations = [original_toadofsky_confirmations[0]]
        for i in range(0, len(self.notes)):
            ratio = (
                round(len(original_toadofsky_confirmations) * (i + 1) / len(self.notes))
                - 1
            )
            toadofsky_confirmations.append(original_toadofsky_confirmations[ratio])

        # build scripts

        script_note_checks = []
        script_correctness_checks = []
        script_toadofsky_reactions = [
            {
                "identifier": prefix_command_name("jmp_if_7000_equals_reaction_%i" % 0),
                "command": "jmp_if_var_equals_const",
                "args": [0x7000, 0, toadofsky_confirmations[0]],
            }
        ]
        for index, pair in enumerate(note_variable_pairs):
            address = pair[1]
            note = pair[0].note.val
            duration = pair[0].duration
            if duration == 0:
                duration = 35

            script_toadofsky_reactions.append(
                {
                    "identifier": prefix_command_name(
                        "jmp_if_7000_equals_reaction_%i" % (index + 1)
                    ),
                    "command": "jmp_if_var_equals_const",
                    "args": [0x7000, index + 1, toadofsky_confirmations[index + 1]],
                }
            )

            note_check = [
                {
                    "identifier": "set_7000_to_7000_short_mem_notecheck_%i" % index,
                    "command": "copy_var_to_var",
                    "args": [address, 0x7000],
                },
                {
                    "identifier": "jmp_to_subroutine_notecheck_%i" % index,
                    "command": "jmp_to_subroutine",
                    "args": ["EVENT_1074_jmp_if_7000_equals_short_369"],
                },
                {
                    "identifier": "jmp_if_var_not_equals_notecheck_%i" % index,
                    "command": "jmp_if_var_not_equals_const",
                    "args": [
                        address,
                        note,
                        prefix_command_name(
                            "set_action_script_sync_notecheck__%i" % index
                        ),
                    ],
                },
                {
                    "identifier": "set_action_script_sync_notecheck_%i" % index,
                    "command": "set_action_script",
                    "args": [0x14 + index, True, 571],
                },
                {
                    "identifier": "set_bit_notecheck_%i" % index,
                    "command": "set_bit",
                    "args": [0x7043, index],
                },
                {
                    "identifier": "jmp_notecheck_%i" % index,
                    "command": "jmp",
                    "args": [prefix_command_name("pause_notecheck_%i" % index)],
                },
                {
                    "identifier": "set_action_script_sync_notecheck__%i" % index,
                    "command": "set_action_script",
                    "args": [0x14 + index, True, 572],
                },
                {
                    "identifier": "clear_bit_notecheck_%i" % index,
                    "command": "clear_bit",
                    "args": [0x7043, index],
                },
                {
                    "identifier": "pause_notecheck_%i" % index,
                    "command": "pause",
                    "args": [duration],
                },
            ]
            for item in range(len(note_check)):
                note_check[item]["identifier"] = prefix_command_name(
                    note_check[item]["identifier"]
                )
            script_note_checks.extend(note_check)

            correctness_check = [
                {
                    "identifier": "jmp_if_var_not_equals_const_correctcheck_%i" % index,
                    "command": "jmp_if_var_not_equals_const",
                    "args": [
                        address,
                        note,
                        prefix_command_name(
                            "jmp_if_var_not_equals_const_correctcheck_%i" % (index + 1)
                        )
                        if index < len(self.notes) - 1
                        else script_toadofsky_reactions[0]["identifier"],
                    ],
                },
                {
                    "identifier": "inc_correctcheck_%i" % index,
                    "command": "inc",
                    "args": [0x7000],
                },
            ]
            for item in range(len(correctness_check)):
                correctness_check[item]["identifier"] = prefix_command_name(
                    correctness_check[item]["identifier"]
                )
            script_correctness_checks.extend(correctness_check)

        final_script = []
        final_script.extend(script_note_checks)
        final_script.extend(
            [
                {
                    "identifier": prefix_command_name("pause_mandatory"),
                    "command": "pause",
                    "args": [45],
                },
                {
                    "identifier": prefix_command_name(
                        "play_music_current_volume_mandatory"
                    ),
                    "command": "play_music_current_volume",
                    "args": [Music._17_TADPOLE_POND],
                },
                {
                    "identifier": prefix_command_name("set_mandatory"),
                    "command": "set_var_to_const",
                    "args": [0x7000, 0],
                },
            ]
        )
        final_script.extend(script_correctness_checks)
        final_script.extend(script_toadofsky_reactions)

        return final_script


all_songs = [
    Song(
        [(Re, 15), (Mi, 100), (Re, 7), (Do, 7), (Ti, 65), (La, 65), (So, 0)],
        "Chrono Cross - Time's Scar",
        hint_1=" When was the start of all this?\n ♪“Re Mi Re Do Ti La So”. When did\n the cogs of fate begin to turn?[await]",
        hint_2=" From deep within the flow of\n time... ♪“Re Mi Re Do Ti La So”.[await]",
        hint_3=" Whilst our laughter echoed,\n “Re Mi Re Do Ti La So”,\n under cerulean skies...[await]",
        scroll="\n          Re Mi Re Do Ti La So[await]",
    ),
    Song(
        [(Fa, 20), (Ti, 20), (Re, 40), (Fa, 20), (Ti, 20), (Re, 0)],
        "Song of Soaring",
        submitter="TriumphantBass",
        submitter_credits="TRIUMPHANTBASS",
        hint_1=" My favorite song?[await][page]\n It's the Song of Soaring!\n ♪“Fa Ti Re, Fa Ti Re”.\n It gives me a flutter![await]",
        hint_2=" The Moleville miners were singing,\n ♪“Fa Ti Re, Fa Ti Re”.\n Light and breezy![await]",
        hint_3="\n            Repeat after me![await][page]\n We'll go “FA”r~[delay]\n            Build equi“TY”~[delay]\n                         Get a “RA”ise~[await][page]\n\n                Once more![await]",
        scroll="\n           Fa Ti Re Fa Ti Re[await]",
    ),
    Song(
        [(Do, 12), (La, 23), (Do, 12), (Ti, 23), (Do, 12), (Ti, 23), (So, 0)],
        "Green Hill Zone",
        hint_1=" Gotta go fast!\n ♪“Do La Do Ti Do Ti So”.[await]",
        hint_2=" ♪“Do La Do Ti Do Ti So”.\n A song that goes great with\n chili dogs.[await]",
        hint_3=" Do La Do Ti Do Ti So.\n You're too slow![await]",
        scroll="\n          Do La Do Ti Do Ti So[await]",
    ),
    Song(
        [(So, 25), (La, 25), (Ti, 50), (Ti, 25), (Re, 25), (La, 50), (La, 25), (Ti, 0)],
        "Earthbound - Smiles and Tears",
        hint_1=" ♪“So La Ti Ti Re La La Ti”.\n I miss you...[await]",
        hint_2=" ♪“So La Ti Ti Re La La Ti”.\n Now say, “fuzzy pickles!”[await]",
        hint_3=" Earthbound?\n           “SO” “LA”st year.\n                            “TI”ck tock![await][page]\n No “TI”me to spa“RE”,\n     p“LA”y the “LA”test “TI”tle,\n                                Mother 3![await]",
        scroll="\n         So La Ti Ti Re La La Ti[await]",
    ),
    Song(
        [(So, 40), (Fa, 40), (Mi, 80), (Re, 20), (Mi, 40), (Re, 10), (Ti, 10), (Do, 0)],
        "I See The Light",
        submitter="TriumphantBass",
        submitter_credits="TRIUMPHANTBASS",
        hint_1=" My favorite song?[await][page]\n It's “I See The Light!”\n ♪“So Fa Mi Re Mi Re Ti Do”.\n It's warm and bright![await]",
        hint_2=" The moles adapted it up from\n somewhere,\n ♪“So Fa Mi Re Mi Re Ti Do”.[await]\n Theirs is somewhat shifted.[await]",
        hint_3=" Our song?[await]\n “SO” “FA”r “ME”, I've been\n “RE”-“MI”, “RE”-“MI”-niscing.[await][page]\n Think I'll “RE”-“TI”-re soon, once\n I've made the “DO”ugh![await]",
        scroll="\n        So Fa Mi Re Mi Re Ti Do[await]",
    ),
    Song(
        [(La, 18), (La, 35), (Re, 35), (Do, 35), (La, 70), (So, 18), (La, 35), (Do, 0)],
        "TNT",
        submitter="Alex.the.Riddler",
        submitter_credits="ALEX.THE.RIDDLER",
        hint_1=" 'Cause I'm TNT, Dynamite.\n ♪“La La Re Do La So La Do”.[await]",
        hint_2=" I swam all the way to Australia\n and discovered this cool band.\n ♪“La La Re Do La So La Do”.[await]",
        hint_3=" This is the song we sing when we\n blow up the TNT![delay]\n      “So Fa Mi Re Mi Re Ti Do”[await]",
        scroll="\n       So Fa Mi Re Mi Re Ti Do[await]",
    ),
    Song(
        [(Fa, 15), (So, 15), (Mi, 42), (Re, 8), (Do, 8), (Ti, 0)],
        "SMB3 Flute",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the SMB3 Flute music,\n ♪“Fa So Mi Re Do Ti”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the SMB3 Flute song.\n ♪“Fa So Mi Re Do Ti”.[await]\n It makes you feel like you're being\n whisked away...[await]",
        hint_3=" Some of us are learnin' how to play\n the flute. We only know how to play\n the tune from SMB3, though.[await]",
        scroll="\n            Fa So Mi Re Do Ti[await]",
    ),
    Song(
        [(La, 80), (Ti, 40), (La, 40), (Fa, 20), (La, 20), (Re, 40), (Ti, 0)],
        "Elegy of Emptiness",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Elegy of Emptiness,\n ♪“La Ti La Fa La Re Ti”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Elegy of Emptiness.\n ♪“La Ti La Fa La Re Ti”.[await]\n It's got...[delay] soul?[await][pause] Wait,[delay] that's\n not right...[await]",
        hint_3=" We've been singin' a new song,\n “Elegy of Emptiness”.[await][pause] Pa' Mole\n heard it from somewhere.[await]\n It's kinda creepy, but it grows\n on ya![await]",
        scroll="\n          La Ti La Fa La Re Ti[await]",
    ),
    Song(
        [(Mi, 15), (Ti, 45), (Mi, 15), (Ti, 15), (Re, 15), (Mi, 0)],
        "Prelude of Light",
        submitter="NYRambler",
        submitter_credits="NYRAMBLER",
        hint_1=" I've heard it played on an\n Ocarina before![await]",
        hint_2=" Perhaps it's a PRELUDE to\n something that's... LIGHT?[await]",
        hint_3=" “MI”gh“TI” fine weather for some\n “MI”gh“TI” “RE”laxing “MI”ning![await]",
        scroll="\n            Mi Ti Mi Ti Re Mi[await]",
    ),
    Song(
        [(Ti, 20), (Re, 20), (Do, 40), (La, 20), (Ti, 20), (La, 40), (So, 0)],
        "Free Bird",
        submitter="NYRambler",
        submitter_credits="NYRAMBLER",
        hint_1=" I've heard someone request it\n at a concert many times![await]",
        hint_2=" If I leave here tomorrow, will you\n still remember me?[await]",
        hint_3=" “TI”me to “Re”member how to “Do”\n this... “La”st “Ti”me, “La”st\n “So”und![await]",
        scroll="\n          Ti Re Do La Ti La So[await]",
    ),
    Song(
        [
            (Mi, 20),
            (Re, 10),
            (Do, 20),
            (Do, 110),
            (Mi, 20),
            (Re, 10),
            (Do, 20),
            (Re, 0),
        ],
        "Under the Sea",
        submitter="Alex.the.Riddler",
        submitter_credits="ALEX.THE.RIDDLER",
        hint_1=" Darling, it's better down where it's\n wetter. Take it from me![await]",
        hint_2=" Sometimes I like to think of myself\n as half a mermaid!\n ♪“Mi Re Do Do Mi Re Do Re”.[await]",
        hint_3=" Have you ever seen a mermaid on\n your travels, Mario?[await]",
        scroll="\n       Mi Re Do Do Mi Re Do Re[await]",
    ),
    Song(
        [(Ti, 35), (Do, 35), (La, 18), (Do, 18), (Re, 18), (So, 18), (Ti, 18), (Do, 0)],
        "I'm Blue",
        submitter="Alex.the.Riddler",
        submitter_credits="ALEX.THE.RIDDLER",
        hint_1="\n    I'm blue, da ba dee da ba daa.[await]",
        hint_2=" What if the whole world was blue\n like the ocean?[await]",
        hint_3=" Yo listen up, here's the story,\n about a little guy that lives in a\n blue world! Ti Do La Do Re So Ti Do[await]",
        scroll="\n        Ti Do La Do Re So Ti Do[await]",
    ),
    Song(
        [
            (So, 60),
            (La, 100),
            (La, 60),
            (Ti, 60),
            (Re, 10),
            (Do, 10),
            (Ti, 10),
            (So, 0),
        ],
        "Never Gonna Give You Up",
        submitter="Alex.the.Riddler",
        submitter_credits="ALEX.THE.RIDDLER",
        hint_1=" Bet you aren't expecting to get\n Rickrolled![await]",
        hint_2=" Never gonna give you up!\n Never gonna let you down![await]",
        hint_3=" Never gonna run around, and\n desert you!\n So La La Ti Re Do Ti So~[await]",
        scroll="\n        So La La Ti Re Do Ti So[await]",
    ),
    Song(
        [(Fa, 40), (So, 20), (Fa, 20), (Ti, 40), (La, 40), (Fa, 0)],
        "Requiem of Spirit",
        submitter="Mr. Thee",
        submitter_credits="MR. THEE",
        hint_1=" I got Silver Gauntlets!\n I can finally play that darn song!!\n ♪“Fa So Fa Ti La Fa”.[await]",
        hint_2=" My favorite song?[await][page]\n It's the song that saves me from\n having to enter Wasteland to get\n into the Spirit Temple.[await]\n ♪“Fa So Fa Ti La Fa”.[await]",
        hint_3=" Have you ever heard a song that\n can warp you to the desert?[await]\n I don't think it works in our world.[delay]\n You have to go through the sewers\n to warp to our desert.[await]",
        scroll="\n            Fa So Fa Ti La Fa[await]",
    ),
    Song(
        [(La, 35), (Re, 70), (La, 35), (Re, 35), (Ti, 70), (La, 35), (So, 35), (La, 0)],
        "Apache (Jump on it)",
        submitter="Alex.the.Riddler",
        submitter_credits="ALEX.THE.RIDDLER",
        hint_1=" Mario! Jump on it! That's like\n what you do, right?[await]",
        hint_2=" Think of this song when you're\n doing super jumps!\n ♪“La Re La Re Ti La So La”.[await]",
        hint_3=" “LA”y me to “RE”st. “LA”y me to\n “RE”st.[await][pause] “TI”s “LA”ter than you\n think.[await][pause] “SO” much “LA”ter than\n you think.~[await]",
        scroll="\n        La Re La Re Ti La So La[await]",
    ),
    Song(
        [(So, 35), (Do, 35), (Re, 35), (Mi, 35), (So, 35), (Do, 35), (Ti, 35), (Do, 0)],
        "Mother 3 Love Theme",
        submitter="CousinCatnip",
        submitter_credits="COUSINCATNIP",
        hint_1=" My favorite song?[await][page]\n I think it's called the\n “Theme of Hearts”.[await]\n No,[delay] wait,[delay] that's not right.[await]\n Maybe it was “Glove Team”?[await]\n No, no,[delay] I got it![await][page]\n It's “Love Theme”.\n ♪“So Do Re Mi So Do Ti Do”.[await]\n Toadofsky may like it,\n but let's make him LOVE it![await]",
        hint_2=" My favorite song?[await][page]\n I think it's called the\n “Theme of Hearts”.[await]\n No,[delay] wait,[delay] that's not right.[await]\n Maybe it was “Glove Team”?[await]\n No, no,[delay] I got it![await][page]\n It's “Love Theme”.\n ♪“So Do Re Mi So Do Ti Do”.[await]\n Toadofsky may like it,\n but let's make him LOVE it![await]",
        hint_3=" “Love Theme” is all the rage. Check\n it out:[await][page]\n\n       We feel it in our “SO”ul~[await][page]\n\n       With everything we “DO”~[await][page]\n\n[1]     My heart is still a w“RE”ck~[await][page]\n\n   So it's “MI”ghty time to change~[await][page]\n\n      I'm diggin' up to re“SO”il~[await][page]\n\n       “DO” you know it's me?~[await][page]\n\n         Feelin' kinda “TI”red~[await][page]\n\n    But I “DO”n't want it to end!~[await]",
        scroll="\n       So Do Re Mi So Do Ti Do[await]",
    ),
    Song(
        [(Mi, 35), (Re, 18), (Mi, 42), (Re, 18), (Mi, 35), (So, 18), (La, 0)],
        "SMB3 Overworld bar 1",
        submitter="SeanCass",
        submitter_credits="SEANCASS",
        hint_1=" My favorite song?[await][page]\n It's “SMB3 Overworld Bar 1”.\n ♪“Mi Re Mi Re Mi So La”.\n Toadofsky's fond of it, too![await]",
        hint_2=" The time signature for the song is\n 1-1.[await][pause] At least, according to\n “Super Mario Bros. 3.”[await]",
        hint_3=" It's the Moleville “MI”nes!\n “RE”ad all about it![await][page]\n I wish I had a Bambino Bomb for\n these “MI”nes, “RE”ally I wish!\n Don't “MI”nd if I do![await][page]\n “SO” you gotta find that bomb,\n I hope it's not your “LA”st\n key item![await]",
        scroll="\n         Mi Re Mi Re Mi So La[await]",
    ),
    Song(
        [(Mi, 35), (Re, 18), (Mi, 24), (Mi, 24), (Do, 18), (Re, 0)],
        "SMB3 Overworld bar 2",
        submitter="SeanCass",
        submitter_credits="SEANCASS",
        hint_1=" My favorite song?[await][page]\n It's “SMB3 Overworld Bar 2”.\n ♪“Mi Re Mi Mi Do Re”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song? It's...[await][page]\n [delay]Wait,[delay] I thought this song was from\n Mario 3, but it's the second part?[await][page]\n OH![await][pause] It's the 2nd bar of 1-1![await][pause]\n I get it now.[await]",
        hint_3=" Moles “MI”ne! We “RE”ally dig![await]\n Moles “MI”ne for “MI”nerals![await]\n Wait, “DO” we “RE”ally?[await]",
        scroll="\n           Mi Re Mi Mi Do Re[await]",
    ),
    Song(
        [(Mi, 35), (Re, 18), (Mi, 24), (So, 24), (La, 24), (Do, 0)],
        "SMB3 Overworld bar 4",
        submitter="SeanCass",
        submitter_credits="SEANCASS",
        hint_1=" My favorite song?[await][page]\n It's “SMB3 Overworld Bar 4”.\n ♪“Mi Re Mi So La Do”.\n Toadofsky's fond of it, too![await]",
        hint_2=" What a nice closing bar to Grass\n Land, a 1 to 1 representation if I\n do say so myself.[await]\n I don't mean the Juice Bar, though![await]",
        hint_3=" We live in the “MI”nes, “RE”ad between the lines![await][pause] These “MI”nes\n are ours![await][pause] “SO” make like a “LA”ke\n and “DO”n't quake![await]",
        scroll="\n           Mi Re Mi So La Do[await]",
    ),
    Song(
        [(Mi, 35), (Mi, 35), (Re, 35), (Do, 35), (Ti, 35), (La, 35), (So, 35), (Fa, 0)],
        "I'm falling down all these stairs",
        submitter="GoodMorningCrono",
        submitter_credits="GOODMORNINGCRONO",
        hint_1=" I warned you about stairs bro!\n I told you dog![await]",
        hint_2=" I told you man!\n I TOLD you about stairs![await]",
        hint_3=" I love to “ME” “ME”, yes I\n “RE”ally “DO”![await][pause] Oh no, it's “TI”me\n for work, I'm “LA”te, “SO” please\n “FA”hgive me dude![await]",
        scroll="\n       Mi Mi Re Do Ti La So Fa[await]",
    ),
    Song(
        [(La, 15), (Ti, 15), (Do, 15), (Re, 15), (Ti, 30), (So, 15), (La, 15)],
        "The Lick",
        submitter="frozenspade",
        submitter_credits="FROZENSPADE",
        hint_1=" My favorite song?[await][page]\n It's “The Lick”.\n ♪“La Ti Do Re Ti So La”.\n Toadofsky's a fan of Jazz.[await]",
        hint_2=" My favorite song?[await][page]\n It's “The Lick”.\n ♪“La Ti Do Re Ti So La”.\n Ya like Jazz?[await]",
        hint_3=" La Ti Do Re Ti So La~[delay]\n Hmm,[delay] where have I heard this\n before?[await]",
        scroll="\n          La Ti Do Re Ti So La[await]",
    ),
    Song(
        [(La, 15), (Fa, 15), (La, 15), (Ti, 15), (So, 15), (La, 15), (Ti, 15), (Re, 0)],
        "Pekora BGM",
        submitter="SushiKishi",
        submitter_credits="SUSHIKISHI",
        hint_1=" For some reason, I have a craving\n for almonds.[await][pause] And...[delay] explosions?[await]\n ♪“La Fa La Ti So La Ti Re”.[await]\n Say,[delay] did you just hear laughing?[await]",
        hint_2=" I was watching this rabbit on TV\n earlier today, and now I can't get\n the song out of my head.[await][page]\n ♪ U-sa-da Pe![delay] Ko![delay] Ra![delay]\n    U-sa-da Pe![delay] Ko![delay] Ra![delay]\n    U-sa-da PEKO-PEKO-CHAN![delay]\n    PEKO-PEKO-CHAN![await]",
        hint_3=" D-DIG, D-DIG DIG DIG! What's the\n cutest song in the entire game?[await]\n D-DIG, D-DIG DIG DIG!\n It's Pekora's BGM![await][page]\n D-DIG, D-DIG DIG DIG!\n And how does that song go?[await]\n D-DIG, D-DIG DIG DIG! It goes\n “LA FA LA TI SO LA TI RE”![await]",
        scroll="\n        La Fa La Ti So La Ti Re[await]",
    ),
    Song(
        [(So, 30), (La, 15), (Fa, 30), (So, 75), (Ti, 30), (La, 15), (Fa, 30), (So, 0)],
        "John Cena Trumpets",
        submitter="SushiKishi",
        submitter_credits="SUSHIKISHI",
        hint_1=" I have a date today, but I lost my\n watch. Do you have the time?[await]\n ♪“So La Fa So Ti La Fa So”.[await]\n What time was my date again...?\n OH NO! THE TIME IS NOW![await]",
        hint_2=" Someone gave me some sheet\n music to pass on to Toadofsky.[await]\n Unfortunately, I dropped the scroll\nin the water, the ink washed off,\n and I can't read the notes.[await]\n Even with the five-second rule, my\n time was up. Your time is now! Go\n find those notes for me, please![await]",
        hint_3=" All our kids're gettin' to that age\n where they're really into pro\n wrestling.[await][pause] They can't stop singin'\n John Cena's entrance music![await]\n I promise you kids, I can see ya!\n And I can DEFINITELY hear ya![await]\n (So La Fa So Ti La Fa So~...)[await]",
        scroll="\n        So La Fa So Ti La Fa So[await]",
    ),
    Song(
        [(Ti, 70), (Re, 35), (La, 88), (Ti, 70), (Re, 35), (La, 0)],
        "Zelda's Lullaby",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's Zelda's Lullaby,\n ♪“Ti Re La Ti Re La”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's Zelda's Lullaby.\n ♪“Ti Re La Ti Re La”.[await]\n It's comforting, isn't it?[await]",
        hint_3=" I swear, if these fellas don't stop\n singin' lullabies, we're all gonna\n fall asleep on the job![await]",
        scroll="\n            Ti Re La Ti Re La[await]",
    ),
    Song(
        [(Re, 18), (Ti, 18), (La, 70), (Re, 18), (Ti, 18), (La, 0)],
        "Epona's Song",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's Epona's Song,\n ♪“Re Ti La Re Ti La”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's Epona's Song.\n It fills me with joy![await]",
        hint_3=" What's that? You wanna hear\n Epona's Song? Well, alright then![await][page]\n\n    Standing here, I “RE”member~[await][page]\n\n            That “TI”me when~[await][page]\n\n      My mother wrote for you~[await][page]\n\n             This bal“LA”d~[await][page]\n [delay].[delay].[delay].[delay]Whoa, I gotta get back to work![await]\n But the song repeats that part.[await]",
        scroll="\n            Re Ti La Re Ti La[await]",
    ),
    Song(
        [(Re, 60), (Mi, 60), (Re, 60), (Mi, 60), (Re, 60), (Mi, 60), (Ti, 0)],
        "The Brink of Time",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's The Brink of Time,\n ♪“Re Mi Re Mi Re Mi Ti”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's The Brink of Time.\n ♪“Re Mi Re Mi Re Mi Ti”.[await]\n It's quite melancholic.[await]",
        hint_3=" Feels like I'm gonna be workin'\n here 'til the end of time![await]",
        scroll="\n         Re Mi Re Mi Re Mi Ti[await]",
    ),
    Song(
        [(Fa, 18), (La, 18), (Ti, 35), (Fa, 18), (La, 18), (Ti, 0)],
        "Saria's Song",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's Saria's Song,\n ♪“Fa La Ti Fa La Ti”.\n It's got a hot beat![await]",
        hint_2=" My favorite song?[await][page]\n It's Saria's Song.[await]\n A song like that is sure to cheer\n you up when you're feeling down![await]",
        hint_3=" ♪(Fa La Ti, Fa La Ti...)[await]\n I visited the forest,[delay] an' now I\n can't get this tune outta my head![await]",
        scroll="\n            Fa La Ti Fa La Ti[await]",
    ),
    Song(
        [(Ti, 12), (So, 12), (Mi, 60), (Ti, 12), (So, 12), (Mi, 0)],
        "Sun's Song",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Sun's Song,\n ♪“Ti So Mi To So Mi”.\n Toadofsky's fond of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Sun's Song.\n ♪“Ti So Mi To So Mi”.\n I wonder what it means?[await]",
        hint_3=" I tell ya, I can't wait for the work\n day to be over.[await][pause] I wish there was a\n way to make the day pass quicker![await]",
        scroll="\n           Ti So Mi To So Mi[await]",
    ),
    Song(
        [(Ti, 35), (Fa, 70), (So, 35), (Ti, 35), (Fa, 70), (So, 0)],
        "Song of Time",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Song of Time,\n ♪“Ti Fa So Ti Fa So”.\n It makes me reflect...[await]",
        hint_2=" My favorite song?[await][page]\n It's the Song of Time.\n ♪“Ti Fa So Ti Fa So”.\n It's mysterious, isn't it?[await]",
        hint_3=" Have ya ever wished you could\n just give the day a do-over,\n Mario?[await]",
        scroll="\n            Ti Fa So Ti Fa So[await]",
    ),
    Song(
        [(Fa, 12), (So, 12), (Re, 55), (Fa, 12), (So, 12), (Re, 0)],
        "Song of Storms",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Song of Storms,\n ♪“Fa So Re Fa So Re”.\n It's wily![await]",
        hint_2=" My favorite song?[await][page]\n It's the Song of Storms.[await][pause] But I'm\n worried if I recite it here, it'll\n cause a flood.[await]",
        hint_3=" ♪(Fa So Re, Fa So Re...)[await]\n This tune makes my head spin, but\n I can't get it outta my head![await]",
        scroll="\n           Fa So Re Fa So Re[await]",
    ),
    Song(
        [(Fa, 18), (Re, 18), (Ti, 80), (La, 18), (Ti, 18), (La, 0)],
        "Minuet of Forest",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Minuet of Forest,\n ♪“Fa Re Ti La Ti La”.\n Isn't it cute?[await]",
        hint_2=" My favorite song?[await][page]\n It's the Minuet of Forest.[await][pause] Such a\n cute and sprightly song![await]",
        hint_3="\n      “FA”r away in a fo“RE”st~[await][page]\n\n     “TI”me seems to stand still~[await][page]\n\n Wood“LA”nd creatures so “TI”mid~[await][page]\n\n   Live among “LA”vish green hills~[await][page]\n Oops![delay] I reckon that's about all I\n can remember from that song...[await]",
        scroll="\n            Fa Re Ti La Ti La[await]",
    ),
    Song(
        [(So, 15), (Fa, 15), (So, 15), (Fa, 15), (Ti, 15), (La, 15), (Ti, 15), (La, 0)],
        "Bolero of Fire",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Bolero of Fire,\n ♪“So Fa So Fa Ti La Ti La”.\n What a great rhythm![await]",
        hint_2=" My favorite song?[await][page]\n It's the Bolero of Fire.[await]\n It makes me want to just start\n dancing, and I don't have legs![await]",
        hint_3=" ♪(So Fa So Fa Ti La Ti La...)[await]\n I swear, this tune's a hot beat![await]\n Does it feel a little warm in here?[await]",
        scroll="\n        So Fa So Fa Ti La Ti La[await]",
    ),
    Song(
        [(Fa, 40), (So, 40), (La, 40), (La, 40), (Ti, 40)],
        "Serenade of Water",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Serenade of Water,\n ♪“Fa So La La Ti”.\n It's so breezy![await]",
        hint_2=" My favorite song?[await][page]\n It's the Serenade of Water.\n ♪“Fa So La La Ti”.\n It gives me the chills![await]",
        hint_3=" Boy howdy, I sure wish I was\n somewhere a little colder\n right now!",
        scroll="\n              Fa So La La Ti[await]",
    ),
    Song(
        [(Ti, 35), (La, 35), (La, 18), (Fa, 18), (Ti, 18), (La, 18), (So, 18)],
        "Nocturne of Shadow",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Nocturne of Shadow,\n ♪“Ti La La Fa Ti La So”.\n It's unsettling![await]",
        hint_2=" My favorite song?[await][page]\n It's the Nocturne of Shadow.[await]\n Something about it just draws me\n right in.[await]",
        hint_3=" ♪(Ti La La Fa Ti La So...)[await]\n Y'know, workin' in these mines can\n be mighty creepy sometimes...[await]",
        scroll="\n          Ti La La Fa Ti La So[await]",
    ),
    Song(
        [(Re, 18), (Ti, 18), (Re, 18), (Ti, 35), (Fa, 35), (La, 70), (Fa, 0)],
        "Sonata of Awakening",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Sonata of Awakening,\n ♪“Re Ti Re Ti Fa La Fa”.\n Toadofsky's font of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Sonata of Awakening.[await]\n I'm afraid that if I hum it,\n something weird will happen.[await]",
        hint_3=" ♪(Re Ti Re Ti Fa La Fa...)[await]\n Y'know, it's weird, but I've been\n havin' some trouble sleeping.[await]",
        scroll="\n          Re Ti Re Ti Fa La Fa[await]",
    ),
    Song(
        [(Ti, 35), (La, 35), (Fa, 35), (Ti, 35), (La, 35), (Fa, 0)],
        "Song of Healing",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Song of Healing,\n ♪“Ti La Fa Ti La Fa”.\n Toadofsky's font of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Song of Healing.[await]\n I feel so clean and refreshed\n every time I hear it.[await]",
        hint_3="\n        When the “TI”me comes~[await][page]\n\n        To “LA”y down to rest~[await][page]\n\n          I will “FA”ll asleep~[await][page]\n\n      And my soul will refresh~![await][page]\n If you sing that song twice in\n a row...[delay] well, you'll be feelin'\n much better![await]",
        scroll="\n            Ti La Fa Ti Ta Fa[await]",
    ),
    Song(
        [(Fa, 35), (La, 35), (Ti, 35), (Fa, 35), (La, 35), (Ti, 35), (La, 35), (Fa, 0)],
        "Goron Lullaby",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Goron Lullaby,\n ♪“Fa La Ti Fa La Ti La Fa”.\n Toadofsky's font of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Goron Lullaby.\n ♪“Fa La Ti Fa La Ti La Fa”.\n Don't fall asleep![await]",
        hint_3=" I swear, if these fellas don't stop\n singin' lullabies, we're all gonna\n fall asleep on the job![await]",
        scroll="\n         Fa La Ti Fa La Ti La Fa[await]",
    ),
    Song(
        [(Ti, 60), (Re, 12), (Do, 12), (La, 60), (Fa, 12), (Ti, 12), (La, 0)],
        "New Wave Bossa Nova",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the New Wave Bossa Nova,\n ♪“Ti Re Do La Fa Ti La”.\n Toadofsky's font of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the New Wave Bossa Nova.[await]\n It'd be cool if a giant turtle\n appeared in our pond, too.[await]",
        hint_3=" ♪(Ti Re Do La Fa Ti La...)[await]\n I'm tellin ya, I could use a\n vacation![await]",
        scroll="\n          Ti Re Do La Fa Ti La[await]",
    ),
    Song(
        [(Ti, 80), (La, 40), (Fa, 40), (La, 40), (Ti, 40), (Re, 60)],
        "Oath to Order",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n It's the Oath to Order,\n ♪“Ti La Fa La Ti Re”.\n Toadofsky's font of it, too![await]",
        hint_2=" My favorite song?[await][page]\n It's the Oath to Order.[await]\n I heard that song carries great\n power in a far-off land.[await]",
        hint_3=" Wassat? You wanna hear our\n song?[await][pause] Well, here goes![await][page]\n\n   Through the passage of “TI”me~[await][page]\n\n    And in “LA”nds “FA”r apart~[await][page]\n\n     We shall always be friends~[await][page]\n\n     I dec“LA”re this with heart~[await][page]\n\n     I will s“TI”ll heed your call~[await][page]\n\n      If you need me, my friend~[await][page]\n\n       I will always be the“RE”~[await][page]\n\n          Until the very end~![await]",
        scroll="\n            Ti La Fa La Ti Re[await]",
    ),
    Song(
        [(Fa, 12), (So, 12), (Ti, 12), (Re, 12), (Ti, 12), (Do, 12)],
        "For the Animals of the Forest",
        submitter="pidgezero_one",
        submitter_credits="PIDGEZERO_ONE",
        hint_1=" My favorite song?[await][page]\n ♪“Fa So Ti Re Ti Do”.\n I heard it in a forest once. I\n suspected the flutist was a ghost.[await]",
        hint_2=" My favorite song?[await][page]\n ♪“Fa So Ti Re Ti Do”.\n Most animals love that song.\n Especially birds.[await]",
        hint_3=" Don't ya wish sometimes that you\n could just fly anywhere ya wanted?[await]",
        scroll="\n            Fa So Ti Re Ti Do[await]",
    ),
]
