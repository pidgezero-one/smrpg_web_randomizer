# Logic module for matching overworld sprites to area bosses.
import math
from randomizer.data.npcmodeltables import VramStore
from randomizer.data.objectsequencetables import _0x08Flags
from randomizer.data.roomobjecttables import RadialDirection


locations_with_replaceable_sprites = ["HammerBros", "Croco1", "Mack", "Belome1", "Bowyer", "Croco2", "Punchinello", "KingCalamari", "Booster", "Bundt", "Johnny", "Yaridovich",
                                      "Belome2", "Jagger", "Jinx3", "MegaSmilax", "Dodo", "Valentina", "Magikoopa", "Boomer", "CzarDragon", "AxemRangers", "Countdown", "Clerk", "Manager", "Director", "Gunyolk"]
locations_using_huge_sprites = ["Belome1", "Belome2", "Dodo"]
locations_to_sub_crystal_in_for_culex = ["Booster", "Mack", "Croco1", "HammerBros", "Manager", "Dodo", "Belome1", "Belome2", "Valentina", "Magikoopa"]
boss_ids = [23, 27, 33, 50, 51, 52, 76, 87, 114, 134, 137, 192, 194, 195, 196, 197, 199, 200, 204, 205, 208, 216, 218, 220, 221, 224, 226, 230, 233, 234, 240, 241, 245, 246, 248, 249, 251, 255]
crystal_ids = [149, 150, 151, 152]
statue_rooms = [341, 109, 115, 122, 120, 110, 113, 119, 408, 499, 501, 440, 497, 447]
bosses_that_need_alternate_flip_condition = ["KnifeGuy", "Croco1", "Croco2", "Clerk", "Manager", "Director"]
shovel_knight_bosses = ["Clerk", "Manager", "Director"]

def invert_direction(direction):
    if direction == RadialDirection.NORTHEAST:
        return RadialDirection.SOUTHEAST
    elif direction == RadialDirection.NORTHWEST:
        return RadialDirection.SOUTHWEST
    elif direction == RadialDirection.SOUTHEAST:
        return RadialDirection.NORTHWEST
    elif direction == RadialDirection.SOUTHWEST:
        return RadialDirection.NORTHEAST
    else:
        raise Exception("What direction did you pass here?")


def approximate_dimension(num):
    base = max(num - 0x20, 0)
    return 0x20 + math.ceil(base / 8) * 8

def get_sprite_property(model, prop):
    if prop in model.keys():
        return model[prop]
    elif "extra_props" in model.keys() and prop in model["extra_props"].keys():
        return model["extra_props"][prop]
    elif prop == "extra_props" and "extra_props" not in model.keys():
        return {}
    else:
        return None

def get_queue_target_byte(npc_id):
    return npc_id + 0x14
    

def patch_overworld_bosses(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        ???

    """

    preloaders = [[None]*len(world.rooms)]*len(world.eventscripts)


    for location in [l for l in world.boss_locations if l.name in locations_with_replaceable_sprites]:
        shuffled_boss = None
        for enemy in location.pack.common_enemies:
            if enemy.index in boss_ids:
                shuffled_boss = enemy
                #culex crystal replacement
                if enemy.index == 255 and location.name in locations_to_sub_crystal_in_for_culex:
                    stats = [shuffled_boss.attack, shuffled_boss.defense, shuffled_boss.magic_attack,
                             shuffled_boss.magic_defense]
                    crystal_colour = stats.index(max(stats))
                    crystal = crystal_ids[crystal_colour]
                    for e in location.pack.common_enemies:
                        if e.index == crystal:
                            shuffled_boss = e

        if shuffled_boss is not None:
            
            #don't do any shuffling if the boss is vanilla
            if shuffled_boss.index != location.original_boss:

                # determine sprite to use
                battle_sprite_fits_height = approximate_dimension(
                    shuffled_boss.sprite_height) <= approximate_dimension(location.sprite_height)
                battle_sprite_fits_width = approximate_dimension(shuffled_boss.sprite_width) <= approximate_dimension(
                    location.sprite_width)
                battle_sprite_fits_overworld = battle_sprite_fits_height and battle_sprite_fits_width
                battle_sprite_fits_large_room = shuffled_boss.sprite_height < 80 and shuffled_boss.sprite_width < 48

                use_battle_sprite = location.name is not "Gunyolk" and (battle_sprite_fits_overworld or (
                    battle_sprite_fits_large_room and location.name in locations_using_huge_sprites))

                # get model data by merging original model with relevant data from the boss replacing it
                if location.model is not None:
                    model = {
                        **location.model,
                        **enemy.get_model(use_battle_sprite)
                    }
                else:
                    raise '%s location has no base model data' % location.name

                # replace Dodo sprite if bandit's way, that location doesn't work nicely
                if location.name in ["Croco1"] and shuffled_boss.index == 137:
                    ep = get_sprite_property(model, "extra_props")
                    model = {
                        **model,
                        "sprite": 389,
                        "extra_props": {
                            **ep, 
                            "sequence": 0,
                            "freeze": False
                        }
                    }
                
                #generate model data
                for target_room in location.target_npcs:
                    room_data = world.rooms[target_room["room"]]
                    target_npcs = target_room.npcs
                    for npc in target_npcs:
                        #non-clone
                        index, target_npc = next((i for i, n in enumerate(room_data["objects"]) if n["id"] == npc.index), None)
                        if target_npc is not None:
                            target_model_id = target_npc.model
                            world.models[target_model_id] = {
                                **world.models[target_model_id],
                                **model
                            }
                        else:
                            raise Exception("NPC #%i not found in room %i", (npc.index, target_room["room"]))
                        #clone
                        #figure out this later, i don't know if it'll even matter

                #handle sidekicks


                for target_room in location.target_npcs:

                    preloader_scripts_for_this_room = []

                    room_id = target_room["room"]
                    script_id = world.rooms[room_id]["entrance_event"]
                    subscript = []
                    # consider converting to deque
                    sequence = get_sprite_property(model, "sequence")
                    mold = get_sprite_property(model, "mold")
                    sprite_plus = get_sprite_property(model, "sprite_plus")
                    freeze = get_sprite_property(model, "freeze")
                    statue_mold = get_sprite_property(model, "statue_mold")
                    statue_east_shift = get_sprite_property(model, "statue_east_shift")
                    statue_west_shift = get_sprite_property(model, "statue_west_shift")
                    statue_south_shift = get_sprite_property(model, "statue_south_shift")
                    opposite_statue_west_shift = get_sprite_property(model, "opposite_statue_west_shift")
                    opposite_statue_south_shift = get_sprite_property(model, "opposite_statue_south_shift")
                    if sprite_plus is None:
                        sprite_plus = 0
                    if freeze is None:
                        freeze = False
                    if room_id in statue_rooms:
                        freeze = True

                    
                    invert_directions = get_sprite_property(model, "invert_se_sw")

                    for npc_id in target_room.npcs:

                        #insert preloader into room event
                        identifier = 'EVENT_%i_room_%i_npc_%i_%s_preloader' % (script_id, room_id, npc_id, shuffled_boss.name)
                        identifier_prefix = '%s_' % identifier
                        if sequence is not None:
                            flags = [_0x08Flags.READ_AS_SEQUENCE]
                            if freeze:
                                flags.append(_0x08Flags.LOOPING_OFF)
                            subscript.append({
                                "identifier": '%s_sequence' % identifier_prefix,
                                "command": "set_sprite_sequence",
                                "args": [sequence, sprite_plus, flags]
                            })
                        elif mold is not None:
                            flags = [_0x08Flags.READ_AS_MOLD]
                            if freeze:
                                flags.append(_0x08Flags.LOOPING_OFF)
                            subscript.append({
                                "identifier": '%s_mold' % identifier_prefix,
                                "command": "set_sprite_sequence",
                                "args": [mold, sprite_plus, flags]
                            })
                        elif freeze is not None:
                            subscript.append({
                                "identifier": '%s_freeze' % identifier_prefix,
                                "command": "sequence_looping_off"
                            })
                        if room_id in statue_rooms:
                            uniform_direction_statues = model["vram_store"] == VramStore._02_SWSE

                            # calculate pixel shift
                            if statue_east_shift is not None or statue_west_shift is not None or statue_south_shift is not None:
                                if statue_east_shift is None:
                                    statue_east_shift = 0
                                if statue_west_shift is None:
                                    statue_west_shift = 0
                                if statue_south_shift is None:
                                    statue_south_shift = 0
                                statue_west_shift *= -1
                                if room_id == 110 and (shuffled_boss.index == 51 or shuffled_boss.index in bosses_that_need_alternate_flip_condition):
                                    statue_east_shift *= -1
                                statue_x_shift = statue_east_shift + statue_west_shift
                                statue_y_shift = statue_south_shift

                            if opposite_statue_west_shift is not None or opposite_statue_south_shift is not None:
                                if opposite_statue_west_shift is None:
                                    opposite_statue_west_shift = 0
                                if opposite_statue_south_shift is None:
                                    opposite_statue_south_shift = 0
                                opposite_statue_west_shift *= -1
                                opposite_statue_x_shift = statue_east_shift + statue_west_shift
                                opposite_statue_y_shift = statue_south_shift


                            # set correct static sprite
                            if statue_mold is not None:
                                subscript.append({
                                    "identifier": '%s_statue_mold' % identifier_prefix,
                                    "command": "set_sprite_sequence",
                                    "args": [statue_mold, sprite_plus, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_MOLD]]
                                })

                            if room_id is not 110:
                                if not uniform_direction_statues: # statues facing north vs south need different pixel shifts
                                    if room_id == 499:
                                        north_facing_statues = [2, 3]
                                        south_facing_statues = [1, 4]
                                    elif room_id == 497:
                                        north_facing_statues = world.rooms[room_id]["objects"]
                                        south_facing_statues = []
                                    else:
                                        divider = len(world.rooms[room_id]["objects"]) - math.ceil(len(world.rooms[room_id]["objects"]) / 2)
                                        south_facing_statues = world.rooms[room_id]["objects"][:divider]
                                        north_facing_statues = world.rooms[room_id]["objects"][divider:]
                                else: # if sprite doesn't support north, have them all face southwest
                                    south_facing_statues = world.rooms[room_id]["objects"]
                                    north_facing_statues = []

                                # apply pixel shift
                                if npc_id in south_facing_statues:
                                    if statue_x_shift != 0 and statue_y_shift != 0:
                                        subscript.append({
                                            "identifier": '%s_statue_pixel_shift' % identifier_prefix,
                                            "command": "shift_xy_pixels",
                                            "args": [statue_x_shift, statue_y_shift]
                                        })
                                elif npc_id in north_facing_statues:
                                    if opposite_statue_x_shift != 0 and opposite_statue_y_shift != 0:
                                        subscript.append({
                                            "identifier": '%s_statue_pixel_shift' % identifier_prefix,
                                            "command": "shift_xy_pixels",
                                            "args": [opposite_statue_x_shift, opposite_statue_y_shift]
                                        })
                            else: # special case for dodo room: facing northwest
                                if not uniform_direction_statues:
                                    if shuffled_boss.index == 51: #Gunyolk special case
                                        statue_x_shift -= 5
                                if uniform_direction_statues: # use normal pixel shift if sprites don't support north
                                    if statue_x_shift != 0 and statue_y_shift != 0:
                                        subscript.append({
                                            "identifier": '%s_statue_pixel_shift' % identifier_prefix,
                                            "command": "shift_xy_pixels",
                                            "args": [statue_x_shift, statue_y_shift]
                                        })
                                else: # use normal X pixel shift but inverted Y pixel shift otherwise
                                    if statue_x_shift != 0 and opposite_statue_y_shift != 0:
                                        subscript.append({
                                            "identifier": '%s_statue_pixel_shift' % identifier_prefix,
                                            "command": "shift_xy_pixels",
                                            "args": [statue_x_shift, opposite_statue_y_shift]
                                        })

                        preloader_for_this_npc = {
                            "identifier": identifier,
                            "command": 'action_queue_async',
                            "args": [0x14 + npc_id],
                            "subscript": subscript
                        }

                        preloader_scripts_for_this_room.append(preloader_for_this_npc)



                        #index, level_object = next((i for i, n in enumerate(world.rooms[room_id]["objects"]) if n["id"] == npc_id), None)
                        #    if index is not None:


                        # replace existing commands in scripts where appropriate
                        # may need a traversal

                        # invert F on relevant room object if this NPC has invert_se_sw set to true
                        for index in range(len(world.rooms[room_id]["objects"])):
                            level_object = world.rooms[room_id]["objects"][index]
                            if invert_directions:
                                if level_object.id == npc_id:
                                    original_model = {**level_object}
                                    original_model.direction == invert_direction(original_model.direction)
                                    world.rooms[room_id]["objects"][index] = {**original_model}
                                else:
                                    for cindex in range(len(world.rooms[room_id]["objects"][index]["clones"])):
                                        clone_object = world.rooms[room_id]["objects"][index]["clones"][cindex]
                                        if clone_object.id == npc_id:
                                            original_model = {**clone_object}
                                            original_model.direction == invert_direction(original_model.direction)
                                            world.rooms[room_id]["objects"][index]["clones"][cindex] = {**original_model}


                        # how to resolve partitions?

                        # consider changing event commands from dicts to classes

                        # special cases
                        if location.name == "HammerBros":
                            continue #placeholder

                    

                    # compile all preloaders for this room, finish with a jump to the "real" event body at the end
                    if len(preloader_scripts_for_this_room) > 0:
                        existing_script = world.eventscripts[script_id]
                        if len(existing_script) == 0:
                            raise Exception("Preloader event %i for room %i is length 0", (script_id, room_id))
                        first_event = existing_script[0]["identifier"]
                        if preloaders[script_id][room_id] is None:
                            preloaders[script_id][room_id] = preloader_scripts_for_this_room
                        else:
                            preloaders[script_id][room_id].extend(preloader_scripts_for_this_room)
                        preloaders[script_id][room_id].append({
                            "identifier": 'event_%i_room_%i_preloader_end_jump' % (script_id, room_id),
                            "command": 'jmp',
                            "args": [first_event]
                        })


                # add preloaders to world scripts
                for script_id in range(len(preloaders)):
                    preloader_script = []

                    for room_id in range(len(preloaders[script_id])):
                        preloader = preloaders[script_id][room_id]
                        if preloader is not None:
                            jump_target = preloader[0]["identifier"]
                            preloader_script.append({
                                "identifier": 'event_%i_room_%i_preloader_jump' % (script_id, room_id),
                                "command": 'jmp_if_7000_equals_short',
                                "args": [room_id, jump_target]
                            })
                    if len(preloader_script) > 0:
                        truthy_scripts = [s for s in preloaders[script_id] if s is not None]
                        final_script = [
                            {
                                "identifier": "event_%i_preloader_set_var" % script_id,
                                "command": "set_7000_to_current_level"
                            },
                            *preloader_script,
                            *[item for sublist in truthy_scripts for item in sublist], # will this unpack?
                            *world.eventscripts[script_id]
                        ]
                        world.eventscripts[script_id] = final_script

                    

        else:
            raise "What boss is this?"
