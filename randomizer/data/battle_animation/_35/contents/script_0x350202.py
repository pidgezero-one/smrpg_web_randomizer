# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *
script = AnimationScriptBlock(expected_size=512, expected_beginning=0x350202, script=[
	DefineObjectQueue([
        "monster_sprite_behaviour_0_no_movement_for_escape", # terrapin
		"monster_sprite_behaviour_0_no_movement_for_escape", # spikey
		"monster_sprite_behaviour_5_sprite_shadow", # skytroopa
		"monster_sprite_behaviour_0_no_movement_for_escape", # madmallet static
		"monster_sprite_behaviour_0_no_movement_for_escape", # shaman
		"monster_sprite_behaviour_0_no_movement_for_escape", # crook
		"monster_sprite_behaviour_0_no_movement_for_escape", # goomba
		"monster_sprite_behaviour_0_no_movement_for_escape", # piranha plant
		"monster_sprite_behaviour_0_no_movement_for_escape", # amanita
		"monster_sprite_behaviour_5_sprite_shadow", # goby
		"monster_sprite_behaviour_6_floating_sprite_shadow", # bloober
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana red
		"monster_sprite_behaviour_5_sprite_shadow", # lakitu
		"monster_sprite_behaviour_5_sprite_shadow", # birdy
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pinwheel
		"monster_sprite_behaviour_0_no_movement_for_escape", # rat funk
		"monster_sprite_behaviour_0_no_movement_for_escape", # k9
		"monster_sprite_behaviour_0_no_movement_for_escape", # magmite
		"monster_sprite_behaviour_5_sprite_shadow", # big boo
		"monster_sprite_behaviour_0_no_movement_for_escape", # drybones
		"monster_sprite_behaviour_5_sprite_shadow", # greaper
		"monster_sprite_behaviour_6_floating_sprite_shadow", # sparky
		"monster_sprite_behaviour_0_no_movement_for_escape", # chomp
		"monster_sprite_behaviour_0_no_movement_for_escape", # pandorite
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy ranger
		"monster_sprite_behaviour_0_no_movement_for_escape", # bobomb static
		"monster_sprite_behaviour_0_no_movement_for_escape", # spookum
		"monster_sprite_behaviour_11_fade_out_death", # hammer bro
		"monster_sprite_behaviour_5_sprite_shadow", # buzzer
		"monster_sprite_behaviour_0_no_movement_for_escape", # ameboid
		"monster_sprite_behaviour_0_no_movement_for_escape", # gecko
		"monster_sprite_behaviour_0_no_movement_for_escape", # wiggler
		"monster_sprite_behaviour_0_no_movement_for_escape", # crusty
		"monster_sprite_behaviour_11_fade_out_death", # kamek
		"monster_sprite_behaviour_6_floating_sprite_shadow", # leuko
		"monster_sprite_behaviour_0_no_movement_for_escape", # jawful
		"monster_sprite_behaviour_5_sprite_shadow", # enigma
		"monster_sprite_behaviour_0_no_movement_for_escape", # blaster
		"monster_sprite_behaviour_0_no_movement_for_escape", # guerrilla
		"monster_sprite_behaviour_5_sprite_shadow", # birdy henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # hobgoblin
		"monster_sprite_behaviour_0_no_movement_for_escape", # reacher
		"monster_sprite_behaviour_0_no_movement_for_escape", # shogun
		"monster_sprite_behaviour_0_no_movement_for_escape", # orb user
		"monster_sprite_behaviour_5_sprite_shadow", # heavy troopa
		"monster_sprite_behaviour_6_floating_sprite_shadow", # shadow
		"monster_sprite_behaviour_6_floating_sprite_shadow", # cluster
		"monster_sprite_behaviour_0_no_movement_for_escape", # bahamutt (kamek)
		"monster_sprite_behaviour_6_floating_sprite_shadow", # octolot
		"monster_sprite_behaviour_0_no_movement_for_escape", # frogog
		"monster_sprite_behaviour_0_no_movement_for_escape", # clerk
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # gunyolk
		"monster_sprite_behaviour_0_no_movement_for_escape", # boomer
		"monster_sprite_behaviour_0_no_movement_for_escape", # remo con
		"monster_sprite_behaviour_0_no_movement_for_escape", # snapdragon
		"monster_sprite_behaviour_0_no_movement_for_escape", # stumpet
		"monster_sprite_behaviour_0_no_movement_for_escape", # dodo 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # jester
		"monster_sprite_behaviour_0_no_movement_for_escape", # artichoker
		"monster_sprite_behaviour_0_no_movement_for_escape", # arachne
		"monster_sprite_behaviour_6_floating_sprite_shadow", # carroboscis
		"monster_sprite_behaviour_0_no_movement_for_escape", # hippopo
		"monster_sprite_behaviour_0_no_movement_for_escape", # mastadoom
		"monster_sprite_behaviour_0_no_movement_for_escape", # corkpedite
		"monster_sprite_behaviour_0_no_movement_for_escape", # terra cotta
		"monster_sprite_behaviour_0_no_movement_for_escape", # spikester
		"monster_sprite_behaviour_5_sprite_shadow", # malakoopa
		"monster_sprite_behaviour_0_no_movement_for_escape", # pounder static
		"monster_sprite_behaviour_0_no_movement_for_escape", # poundette static
		"monster_sprite_behaviour_0_no_movement_for_escape", # sackit
		"monster_sprite_behaviour_0_no_movement_for_escape", # gu goomba
		"monster_sprite_behaviour_0_no_movement_for_escape", # chewy
		"monster_sprite_behaviour_6_floating_sprite_shadow", # fireball
		"monster_sprite_behaviour_5_sprite_shadow", # mr kipper
		"monster_sprite_behaviour_5_sprite_shadow", # factory chief
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana blue
		"monster_sprite_behaviour_5_sprite_shadow", # manager
		"monster_sprite_behaviour_5_sprite_shadow", # bluebird
		"monster_sprite_behaviour_1_slide_backward_when_hit", # geno clone S
		"monster_sprite_behaviour_0_no_movement_for_escape", # alley rat
		"monster_sprite_behaviour_0_no_movement_for_escape", # chow
		"monster_sprite_behaviour_0_no_movement_for_escape", # magmus
		"monster_sprite_behaviour_5_sprite_shadow", # lil boo
		"monster_sprite_behaviour_0_no_movement_for_escape", # vomer
		"monster_sprite_behaviour_5_sprite_shadow", # glum reaper
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pyrosphere
		"monster_sprite_behaviour_0_no_movement_for_escape", # chomp chomp
		"monster_sprite_behaviour_0_no_movement_for_escape", # hidon
		"monster_sprite_behaviour_5_sprite_shadow", # sling shy
		"monster_sprite_behaviour_0_no_movement_for_escape", # rob-omb
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy guy
		"monster_sprite_behaviour_0_no_movement_for_escape", # ninja
		"monster_sprite_behaviour_5_sprite_shadow", # stinger
		"monster_sprite_behaviour_0_no_movement_for_escape", # goombette
		"monster_sprite_behaviour_0_no_movement_for_escape", # geckit
		"monster_sprite_behaviour_0_no_movement_for_escape", # jabit
		"monster_sprite_behaviour_0_no_movement_for_escape", # star cruster
		"monster_sprite_behaviour_0_no_movement_for_escape", # team gauge
		"monster_sprite_behaviour_6_floating_sprite_shadow", # muckle
		"monster_sprite_behaviour_0_no_movement_for_escape", # forkies
		"monster_sprite_behaviour_5_sprite_shadow", # gorgon
		"monster_sprite_behaviour_0_no_movement_for_escape", # big bertha
		"monster_sprite_behaviour_0_no_movement_for_escape", # chained kong
		"monster_sprite_behaviour_10_fade_out_death_floating", # fautso
		"monster_sprite_behaviour_0_no_movement_for_escape", # straw head
		"monster_sprite_behaviour_5_sprite_shadow", # bluebird henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # armored ant
		"monster_sprite_behaviour_0_no_movement_for_escape", # orbison
		"monster_sprite_behaviour_6_floating_sprite_shadow", # tub o troopa
		"monster_sprite_behaviour_6_floating_sprite_shadow", # doppel
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pulsar
		"monster_sprite_behaviour_0_no_movement_for_escape", # bobomb henchman
		"monster_sprite_behaviour_6_floating_sprite_shadow", # octovader
		"monster_sprite_behaviour_0_no_movement_for_escape", # ribbite
		"monster_sprite_behaviour_0_no_movement_for_escape", # director
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # pounder henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # puppox
		"monster_sprite_behaviour_0_no_movement_for_escape", # fink flower
		"monster_sprite_behaviour_0_no_movement_for_escape", # crook henchman
		"monster_sprite_behaviour_5_sprite_shadow", # springer
		"monster_sprite_behaviour_0_no_movement_for_escape", # apprentice henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # kriffid
		"monster_sprite_behaviour_0_no_movement_for_escape", # spinthra
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana red henchman
		"monster_sprite_behaviour_2_bowser_clone_sprite", # bowser clone S
		"monster_sprite_behaviour_6_floating_sprite_shadow", # BLOOBER HENCHMAN
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy guy henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # apprentice
		"monster_sprite_behaviour_1_slide_backward_when_hit", # toadstool 3
		"monster_sprite_behaviour_0_no_movement_for_escape", # piranha plant henchman
		"monster_sprite_behaviour_3_mario_clone_sprite", # mario clone S
		"monster_sprite_behaviour_0_no_movement_for_escape", # poundette henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # mad mallet henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # box boy
		"monster_sprite_behaviour_4_no_reaction_when_hit", # shelly
		"monster_sprite_behaviour_12_fade_out_death_2", # punchinello 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # dodo 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # oerlikon
		"monster_sprite_behaviour_0_no_movement_for_escape", # chester
		"monster_sprite_behaviour_0_no_movement_for_escape", # body
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # torte
		"monster_sprite_behaviour_5_sprite_shadow", # shy away
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx clone
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made bodyguard
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made drill bit
		"monster_sprite_behaviour_8_floating_slide_backward_when_hit", # formless
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # mokura
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # fire crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # water crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # earth crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # wind crystal
		"monster_sprite_behaviour_3_mario_clone_sprite", # mario clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # toadstool 2
		"monster_sprite_behaviour_2_bowser_clone_sprite", # bowser clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # geno clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # mallow clone
		"monster_sprite_behaviour_0_no_movement_for_escape", # shyster
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 3
		"monster_sprite_behaviour_0_no_movement_for_escape", # hangin shy
		"monster_sprite_behaviour_0_no_movement_for_escape", # smelter
		"monster_sprite_behaviour_11_fade_out_death", # machine made mack
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # machine made bowyer
		"monster_sprite_behaviour_11_fade_out_death", # machine made yaridovich
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem pink
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem black
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem red
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem yellow
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem green
		"monster_sprite_behaviour_0_no_movement_for_escape", # bahamutt (chester)
		"monster_sprite_behaviour_1_slide_backward_when_hit", # mallow clone s
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 4
		"monster_sprite_behaviour_0_no_movement_for_escape", # culex 3D
		"monster_sprite_behaviour_11_fade_out_death", # johnny 2
		"monster_sprite_behaviour_5_sprite_shadow", # starslap
		"monster_sprite_behaviour_0_no_movement_for_escape", # mukumuku
		"monster_sprite_behaviour_5_sprite_shadow", # zeostar
		"monster_sprite_behaviour_0_no_movement_for_escape", # jagger
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 4
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy tank
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy safe
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # fire crystal 3d
		"monster_sprite_behaviour_0_no_movement_for_escape", # microbomb
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # water crystal 3d
		"monster_sprite_behaviour_6_floating_sprite_shadow", # grit
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # neosquid
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # yaridovich mirage
		"monster_sprite_behaviour_8_floating_slide_backward_when_hit", # helio
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # right eye
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # left eye
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # knife guy
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # grate guy
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bundt
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 2
		"monster_sprite_behaviour_17_no_reaction_when_hit_2", # count down
		"monster_sprite_behaviour_16_normal", # ding a ling
		"monster_sprite_behaviour_11_fade_out_death", # belome 1
		"monster_sprite_behaviour_11_fade_out_death", # belome 2
		"monster_sprite_behaviour_11_fade_out_death", # belome 3
		"monster_sprite_behaviour_7_floating", # smilax
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # earth crystal 3d
		"monster_sprite_behaviour_7_floating", # megasmilax
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # birdetta
		"monster_sprite_behaviour_0_no_movement_for_escape", # eggbert
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem yellow
		"monster_sprite_behaviour_12_fade_out_death_2", # punchinello
		"monster_sprite_behaviour_0_no_movement_for_escape", # tentacles
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem red
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem green
		"monster_sprite_behaviour_0_no_movement_for_escape", # king bomb
		"monster_sprite_behaviour_0_no_movement_for_escape", # mezzo bomb
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bundt 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # raspberry
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # king calamari
		"monster_sprite_behaviour_0_no_movement_for_escape", # tentacles
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 3
		"monster_sprite_behaviour_10_fade_out_death_floating", # zombone
		"monster_sprite_behaviour_10_fade_out_death_floating", # czar dragon
		"monster_sprite_behaviour_5_sprite_shadow", # cloaker
		"monster_sprite_behaviour_5_sprite_shadow", # domino
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # mad adder
		"monster_sprite_behaviour_11_fade_out_death", # mack
		"monster_sprite_behaviour_0_no_movement_for_escape", # bodyguard
		"monster_sprite_behaviour_11_fade_out_death", # yaridovich
		"monster_sprite_behaviour_0_no_movement_for_escape", # drill bit
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem pink
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem black
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bowyer
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # raspberry 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # torte 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # exor
		"monster_sprite_behaviour_13_fade_out_death_smithy_spell_cast", # smithy 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # shyper
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy body
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy mage
		"monster_sprite_behaviour_14_fade_out_death_no_escape_movement", # smithy chest
		"monster_sprite_behaviour_0_no_movement_for_escape", # croco 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # croco 2
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # wind crystal 3d
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # earthlink
		"monster_sprite_behaviour_0_no_movement_for_escape", # aero
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # axem rangers
		"monster_sprite_behaviour_0_no_movement_for_escape", # booster 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # booster 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit static
		"monster_sprite_behaviour_11_fade_out_death", # johnny 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit 2
		"monster_sprite_behaviour_5_sprite_shadow", # valentina
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # cloaker
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # domino
		"monster_sprite_behaviour_0_no_movement_for_escape", # candle
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2" # culex
    ], identifier="monster_sprite_behaviour_pointers")
])
