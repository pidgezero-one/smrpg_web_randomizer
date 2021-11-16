from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline
from randomizer.data.palettes import Sprite, ImagePack, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
import string, random, math, functools, copy

UNCOMPRESSED_GFX_START = 0x280000
UNCOMPRESSED_GFX_END = 0x330000

SPRITE_PTRS_START = 0x250000
SPRITE_PTRS_END = 0x251000

IMAGE_PTRS_START = 0x251800
IMAGE_PTRS_END = 0x252000

ANIMATION_PTRS_START = 0x252000
ANIMATION_PTRS_END = 0x252C00

ANIMATION_DATA_BANK_1_START = 0x259000
ANIMATION_DATA_BANK_1_END = 0x280000

ANIMATION_DATA_BANK_2_START = 0x360000
ANIMATION_DATA_BANK_2_END = 0x370000

PALETTE_OFFSET = 0x253000

DEBUG_INDEX = 3

alphabet = string.ascii_lowercase + string.digits

def random_tile_id():
    return ''.join(random.choices(alphabet, k=8))

def sortByUsedSprites(tup1, tup2):
    l1 = tup1[1]
    l2 = tup2[1]
    if len(l1) < len(l2):
        l1 += [0] * (len(l2) - len(l1))
    elif len(l1) > len(l2):
        l2 += [0] * (len(l1) - len(l2))
    used = zip(l1, l2)
    for x in used:
        if x[0] < x[1]:
            return -1
        elif x[0] > x[1]:
            return 1
    return 0

def is_significant_tile(tiledata):
    return len([a for a in tiledata if a > 0]) > 4

def tileset_similarity(tileset1, tileset2):
    sanitized_t1 = [t for t in tileset1 if is_significant_tile(t)]
    sanitized_t2 = [t for t in tileset2 if is_significant_tile(t)]
    t1 = set(sanitized_t1)
    t2 = set(sanitized_t2)
    similarity = len(set(t1).intersection(set(t2)))
    return similarity

def is_same_animation(animation1, animation2):
    if animation1.unknown != animation2.unknown:
        return False
    if animation1.properties.vram_size != animation2.properties.vram_size:
        return False
    if len(animation1.properties.molds) != len(animation2.properties.molds):
        return False
    if len(animation1.properties.sequences) != len(animation2.properties.sequences):
        return False
    molds = zip(animation1.properties.molds, animation2.properties.molds)
    for m in molds:
        if m[0].gridplane != m[1].gridplane:
            return False
        if len(m[0].tiles) != len(m[1].tiles):
            return False
        for i in range(len(m[0].tiles)):
            ts1 = m[0].tiles[i]
            ts2 = m[1].tiles[i]
            if ts1.is_clone != ts2.is_clone:
                return False
            if ts1.mirror != ts2.mirror:
                return False
            if ts1.invert != ts2.invert:
                return False
            if ts1.x != ts2.x:
                return False
            if ts1.y != ts2.y:
                return False
            if ts1.y_plus != ts2.y_plus:
                return False
            if ts1.y_minus != ts2.y_minus:
                return False
            if not ts1.is_clone and not ts2.is_clone and ts1.subtile_bytes != ts2.subtile_bytes:
                return False
            if ts1.is_clone and ts2.is_clone:
                if len(ts1.tiles) != len(ts2.tiles):
                    return False
                clonecheck = zip(ts1.tiles, ts2.tiles)
                for ccheck in clonecheck:
                    if ccheck[0].mirror != ccheck[1].mirror:
                        return False
                    if ccheck[0].invert != ccheck[1].invert:
                        return False
                    if ccheck[0].x != ccheck[1].x:
                        return False
                    if ccheck[0].y != ccheck[1].y:
                        return False
                    if ccheck[0].y_plus != ccheck[1].y_plus:
                        return False
                    if ccheck[0].y_minus != ccheck[1].y_minus:
                        return False
                    if ccheck[0].subtile_bytes != ccheck[1].subtile_bytes:
                        return False
    sequences = zip(animation1.properties.sequences, animation2.properties.sequences)
    for s in sequences:
        s1 = s[0]
        s2 = s[1]
        if len(s1.frames) != len(s2.frames):
            return False
        for i in range(len(s1.frames)):
            as1 = s1.frames[i]
            as2 = s2.frames[i]
            if as1.duration != as2.duration:
                return False
            if as1.mold_id != as2.mold_id:
                return False
    return True


def is_clone_start(tile, compare_tile):
    if compare_tile.is_clone:
        return False, 0, 0
    if tile.subtile_bytes != compare_tile.subtile_bytes:
        return False, 0, 0
    # Clones might require an x/y offset of at least 1.
    # Unsure
    # Maybe clones can only be within a certain index?
    # Try some of these things if it wont build
    # Definitely cannot be a source tile if x/y is too large - indicates it is also a clone
    if compare_tile.x > 255 or compare_tile.y > 255:
        return False, 0, 0
    if tile.x - compare_tile.x < 0 or tile.y - compare_tile.y < 0:
        return False, 0, 0
    if tile.mirror != compare_tile.mirror or tile.invert != compare_tile.invert:
        return False, 0, 0
    return True, tile.x - compare_tile.x, tile.y - compare_tile.y

def is_clone_continuation(tile, compare_tile, x_offset, y_offset):
    if tile.is_clone or compare_tile.is_clone:
        return False
    if tile.subtile_bytes != compare_tile.subtile_bytes:
        return False
    if (tile.x - compare_tile.x) != x_offset or (tile.y - compare_tile.y) != y_offset:
        return False
    if tile.mirror != compare_tile.mirror:
        return False
    if tile.invert != compare_tile.invert:
        return False
    return True

# find all possible clones of the tile within the given mold tileset
def get_clone_ranges(mold_id, tiles, tile_index, compare_tiles, index=0, index2=0):
    tile = tiles[tile_index]
    clone_candidates = []
    # don't compare to self
    if mold_id == index2:
        tile_compare_index = tile_index - 1
    else:
        tile_compare_index = len(compare_tiles) - 1

    is_candidate = False
    x_offset = 0
    y_offset = 0
    mirror = False
    invert = False
    start = tile_compare_index
    end = tile_compare_index
    check = tile_index

    # final eligibility check of potential clone, adds if passes
    def finish_candidate(end_index, start_index, x_offset, y_offset):
        cloned = compare_tiles[start_index:end_index+1]
        if len(cloned) == 0:
            return False
        elif x_offset < 0 or y_offset < 0:
            return False
        elif len(cloned) == 1:
            if tile.x > 255 or tile.y > 255:
                pass
            elif max(tile.subtile_bytes) > 255:
                pass
            elif len([sb for sb in tile.subtile_bytes if sb != 0]) > 2:
                pass
            else:
                return False
        clone_candidates.append((mold_id, start_index, end_index+1, x_offset, y_offset))
        return True

    while tile_compare_index >= 0:
        #print(index, mold_id, index2, tile_index, tile_compare_index)
        compare_tile = compare_tiles[tile_compare_index]
        #if mold_id == 23 and index2 == 23:
        #    print(tile, compare_tile)
        is_ending = False
        # if no active clone check, starts one if it matches
        #if index == 146 and index2 == 4:
        #    print("sprite", index, "mold:", index2, "tile:", tile_index, tile, "comp mold:", mold_id, "comp tile:", tile_compare_index, compare_tile, "start:", start)
        if not is_candidate:
            is_candidate, x_offset, y_offset = is_clone_start(tile, compare_tile)
            if is_candidate:
                end = tile_compare_index
                # if index == 8:
                #     print("mold:", index, "tile:", index2, "comp tile:", tile_compare_index, "end:", end)
        # if active clone check, ends it if it comes across an unmatched tile
        elif is_candidate:
            is_ending = (end - tile_compare_index == 15) or (mold_id == index2 and check == end) or not is_clone_continuation(tiles[check], compare_tile, x_offset, y_offset)
        #if index == 16 and index2 == 18:
        #    print("sprite:", index, "mold:", index2, "tile:", tile_index, "check:", check, "matched mold:", mold_id, "matched tile:", tile_compare_index, start, end, x_offset, y_offset, mirror, invert, is_ending)
        if is_candidate:
            if is_ending or tile_compare_index == 0 or check == 0:
                start = tile_compare_index
                if is_ending:
                    start += 1
                added = finish_candidate(end, start, x_offset, y_offset)
                #if added and index == 0 and index2 == 23:
                #    print("sprite:", index, "mold:", index2, "matched mold:", mold_id, start, end, x_offset, y_offset, mirror, invert)
                is_candidate = False
                x_offset = 0
                y_offset = 0
                mirror = False
                invert = False
                check = tile_index
            else:
                check = max(0, check - 1)
        tile_compare_index -= 1

    # need some way to detect internal clones within the same mold
    # most likely want to do this after looking for clones elsewhere

    return clone_candidates


def find_clones(tiles, molds, index=0, index2=0):
    output = []
    tmp_output = []

    tile_index = len(tiles) - 1
    # iterate backwards thru tiles in the mold we're currently forming
    while tile_index >= 0:
        clone_candidates = []
        tile = tiles[tile_index]
        if tile.is_clone:
            tmp_output.insert(0, tile)
            tile_index -= 1
            continue
        # iterate backwards thru molds to start looking for clones
        mold_index = len(molds) - 1
        while mold_index >= 0:
            mold = molds[mold_index]
            if not mold.gridplane:
                # look for any possible point in previous molds that looks like it could be a clone range ending with this tile
                clone_candidates += get_clone_ranges(mold_index, tiles, tile_index, mold.tiles, index, index2)
            mold_index -= 1
        # if index == 8 and index2 == 14:
        #     print(tile_index, clone_candidates)

        # print(clone_candidates)

        # if eligible ranges found, create clone container for all tiles in range
        if len(clone_candidates) > 0:
            eligible_candidates = [c for c in clone_candidates if c[3] <= 255 and c[4] <= 255]
            ineligible_candidates = [c for c in clone_candidates if c not in eligible_candidates]
            # clone detection just doesnt work out sometimes, ie 3 sets of the same tiles that overall are >255 apart
            # in those cases, un-clone them and just treat as normal tiles
            if len(eligible_candidates) == 0:
                candidate = max(ineligible_candidates,key=lambda item:item[2]-item[1])
                decoupled_tiles = copy.deepcopy(molds[candidate[0]].tiles[candidate[1]:candidate[2]])
                decoupled_tiles.reverse()
                for c_tile in decoupled_tiles:
                    tmp_output.insert(0, c_tile)
            else:
                candidate = max(eligible_candidates,key=lambda item:item[2]-item[1])
                tmp_output.insert(0, Clone(
                    mirror=False,
                    invert=False,
                    x=candidate[3],
                    y=candidate[4],
                    tiles=molds[candidate[0]].tiles[candidate[1]:candidate[2]]
                ))
            tile_index -= (candidate[2]-candidate[1])
        # otherwise just append the tile and move onto the next one
        else:
            tmp_output.insert(0, tile)
            tile_index -= 1

    # after scanning previous molds, check for internal clones as well
    tile_index = len(tmp_output) - 1
    ineligible_to_be_clones = []
    while tile_index >= 0:
        tile = tmp_output[tile_index]
        if tile_index in ineligible_to_be_clones or tile.is_clone:
            output.insert(0, tile)
            tile_index -= 1
            continue
        #print(tile_index, tile)

        clone_candidates = get_clone_ranges(len(molds), tmp_output, tile_index, tmp_output, index, index2)
        if len(clone_candidates) > 0:
            candidate = max(clone_candidates,key=lambda item:item[2]-item[1])
            output.insert(0, Clone(
                mirror=False,
                invert=False,
                x=candidate[3],
                y=candidate[4],
                tiles=tmp_output[candidate[1]:candidate[2]]
            ))
            tile_index -= (candidate[2]-candidate[1])
            ineligible_to_be_clones.extend(list(range(candidate[1], candidate[2])))
        else:
            output.insert(0, tile)
            tile_index -= 1

    # if index == 146:
    #     print("")
    #     print(index, index2)
    #     for i, x in enumerate(output):
    #         print(i, x)
    return output

before_expansion_targets = [0, 1]
half_expansion_targets = [6]
small_expansion_targets = [132]

class Sprites:
    def __init__(self):
        self.output = []

        # Sprite - high level container consisting of 1 image and 1 animation
        # Image - contains a palette pointer and a graphics offset
        # Animation - image about how to arrange the graphics at the offset in the Image
    
    def assemble_from_tables(sprites, insert_whitespace=False):

        tile_groups = {}
        wip_sprites = []
        
        def get_most_similar_tileset(ts, index=0):
            best = None
            best_similarity = 0
            for k in tile_groups:
                similarity = tileset_similarity(ts, tile_groups[k]["tiles"])
                #if index== 400:
                #    print(index, k, tile_groups[k]["used_by"], similarity)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best = k
            #if index == 400:
            #    print(best, max(best_similarity/len(ts), best_similarity/len(tile_groups[best]["tiles"])))
            if best is not None:
                return best, max(best_similarity/len(ts), best_similarity/len(tile_groups[best]["tiles"]))
            else:
                return None, 0

        def get_comparative_similarity(key1, key2):
            similarity = tileset_similarity(wip_sprites[key1]["tiles"], wip_sprites[key2]["tiles"]) / len([y for y in wip_sprites[key1]["tiles"] if is_significant_tile(y)])
            if similarity == 1:
                return int(similarity)
            return math.trunc(round(similarity * 10.0)) / 10

        def rearrange_tiles(group):
            tile_use = []
            relevant_sprites = group["used_by"]
            all_tiles = group["tiles"]
            # print(len(all_tiles))

            for tile in all_tiles:
                sprites_using_this_tile = []
                for sprite_id in relevant_sprites:
                    if tile in wip_sprites[sprite_id]["tiles"]:
                        sprites_using_this_tile.append(sprite_id)
                tile_use.append((tile, sprites_using_this_tile))

            tile_use.sort(key=functools.cmp_to_key(sortByUsedSprites))

            # if 0 in relevant_sprites:
            #     for tu in tile_use:
            #         print(tu[1], tu[0])
            #     print([t[0] for t in tile_use])

            # print(len(set([t[0] for t in tile_use])))
            return {
                "used_by": group["used_by"],
                "tiles": [t[0] for t in tile_use]
            }

        
        unique_tiles_length = 0

        # collect unique subtiles and group sprites by graphic similarity
        for index, sprite in enumerate(sprites):
            wip_sprite = {
                "sprite_data": sprite
            }

            unique_subtiles = []
            for mold in sprite.animation.properties.molds:
                for tile in mold.tiles:
                    for subtile in tile.subtile_bytes:
                        if subtile is not None:
                            hashable = tuple(subtile)
                            if hashable not in unique_subtiles:
                                unique_subtiles.append(hashable)
            key, sim = get_most_similar_tileset(unique_subtiles, index)

            if key is None or sim < 0.075: # 0.075 seems to be the sweet spot
                tile_id = random_tile_id()
                while tile_id in tile_groups:
                    tile_id = random_tile_id()
                tile_groups[tile_id] = {"used_by": [index], "tiles": set(unique_subtiles)}
                key = tile_id
            else:
                tile_groups[key]["used_by"].append(index)
                tile_groups[key]["tiles"] = set(list(tile_groups[key]["tiles"]) + unique_subtiles)
            wip_sprite["tiles"] = unique_subtiles
            wip_sprite["tile_group"] = key
            # print(index, len(wip_sprite["tiles"]))
            wip_sprites.append(wip_sprite)
            #if index == 0:
            #    id_to_check = key
            #if key == id_to_check:
                #print("tiles in sprite %i: " % index, len(unique_subtiles))
                #print(wip_sprite)
                #print(index)
                #print("all tiles in %s: " % key, len(tile_groups[id_to_check]["tiles"]))
                #print("")
                #print("")

        # within each tile group, determine which sprites actually use which tiles
        for k in tile_groups:
            # group tiles together by proximity
            has_variance = False
            if len(tile_groups[k]["used_by"]) > 1:
                # if 191 in tile_groups[k]["used_by"] or 474 in tile_groups[k]["used_by"]:
                #     print (k, len(tile_groups[k]["tiles"]), tile_groups[k]["used_by"])
                # if len(tile_groups[k]["tiles"]) > 512:
                #     print("This one may be too long")
                variance = []
                for t in tile_groups[k]["used_by"]:
                    if 191 in tile_groups[k]["used_by"] or 474 in tile_groups[k]["used_by"]:
                        print([get_comparative_similarity(t, x) for x in tile_groups[k]["used_by"]])
                    variance.append([get_comparative_similarity(t, x) for x in tile_groups[k]["used_by"]])
                for x in range(len(variance)):
                    for y in range(x+1, len(variance)):
                        if variance[x][y] != 1 and variance[y][x] != 1:
                            has_variance = True
                #print(has_variance)
                #print("")
            if has_variance:
                tile_groups[k] = rearrange_tiles(tile_groups[k])
            else:
                tile_groups[k]["tiles"] = list(tile_groups[k]["tiles"])
            tile_groups[k]["variance"] = has_variance
            unique_tiles_length += len(tile_groups[k]["tiles"])

        # calculate free space
        free_tiles = (UNCOMPRESSED_GFX_END - UNCOMPRESSED_GFX_START - (unique_tiles_length * 0x20)) // 0x20
        #print("free space", free_tiles)
        # reserve 64 tiles for minecart and 8bit
        free_tiles -= 64
        if free_tiles < 0:
            free_tiles = 0

        placed_tile_keys = []

        output_tiles = bytearray([])

        complete_sprites = []
        complete_images = []
        complete_animations = []

        # print(len(wip_sprites))
        

        # start building stuff
        for sprite_index, sprite in enumerate(wip_sprites):
            tile_key = sprite["tile_group"]
            available_tiles = tile_groups[tile_key]["tiles"]
            # print(sprite_index, tile_key)
            # for a in available_tiles:
            #     print(a)
            # print(wip_sprite["tiles"])
            # print(sprite_index, len(wip_sprite["tiles"]))
            # if sprite_index == 0:
            #     print(sprite)
            #     print(available_tiles)
            #if tile_key == id_to_check:
                #print(wip_sprite)
                #print(sprite_index)
                #print("tiles in sprite %i: " % sprite_index, len(sprite["tiles"]))
                #print("all tiles in %s: " % tile_key, len(tile_groups[id_to_check]["tiles"]))
                #print("")
                #print("")

            lowest_subtile_index = len(available_tiles)
            highest_subtile_index = 0
            for t in sprite["tiles"]:
                tilegroup_index_of_this_tile = available_tiles.index(t)
                if tilegroup_index_of_this_tile < lowest_subtile_index:
                    lowest_subtile_index = tilegroup_index_of_this_tile
                if tilegroup_index_of_this_tile > highest_subtile_index:
                    highest_subtile_index = tilegroup_index_of_this_tile

            inserting_whitespace_before = False
            whitespace_amount = 0
            # check if this tile group has already been placed
            if tile_key not in placed_tile_keys:
                offset = UNCOMPRESSED_GFX_START + len(output_tiles)
                if insert_whitespace and free_tiles > 0 and sprite_index == 0:
                    whitespace_amount = min(free_tiles, 510 - (highest_subtile_index - lowest_subtile_index))
                    tile_groups[tile_key]["offset"] = offset + (0x20 * whitespace_amount)
                    #print(sprite_index, highest_subtile_index, lowest_subtile_index, whitespace_amount, len([0]* (0x20 * whitespace_amount)))
                    output_tiles += bytearray([0] * (0x20 * whitespace_amount))
                    inserting_whitespace_before = True
                    free_tiles -= whitespace_amount
                else:
                    tile_groups[tile_key]["offset"] = offset
                placed_tile_keys.append(tile_key)
                for t in available_tiles:
                    output_tiles += bytearray(t)
            else:
                offset = tile_groups[tile_key]["offset"]
                if insert_whitespace and sprite_index == 1:
                    #print(hex(tile_groups[tile_key]["offset"]))
                    offset += ((lowest_subtile_index) * 0x20)
                    whitespace_amount = 510 - (highest_subtile_index - lowest_subtile_index)
                    if (offset - (whitespace_amount * 0x20)) < 0x280000:
                        whitespace_amount = (offset - 0x280000) // 0x20
                    #print(hex(offset))
                    #print(sprite_index, highest_subtile_index, lowest_subtile_index, whitespace_amount, len([0]* (0x20 * whitespace_amount)))
                    inserting_whitespace_before = True
                    offset -= (whitespace_amount * 0x20)
            # print(sprite_index, hex(offset))
            if sprite_index == 6 or sprite_index == 3:
                whitespace_amount = min(free_tiles, 510 - (highest_subtile_index - lowest_subtile_index))
                #print(sprite_index, highest_subtile_index, lowest_subtile_index, whitespace_amount, len([0]* (0x20 * whitespace_amount)))
                free_tiles -= whitespace_amount
                output_tiles += bytearray([0] * (0x20 * whitespace_amount))
            elif sprite_index == 132 or sprite_index == 234:
                whitespace_amount = 32
                #print(sprite_index, highest_subtile_index, lowest_subtile_index, whitespace_amount, len([0]* (0x20 * whitespace_amount)))
                free_tiles -= whitespace_amount
                output_tiles += bytearray([0] * (0x20 * whitespace_amount))

            # get image pack #, or create new
            if not inserting_whitespace_before:
                offset += ((lowest_subtile_index) * 0x20)
            # need to change this to accommodate diff offsets in same tile group
            palette_ptr = PALETTE_OFFSET + sprite["sprite_data"].palette_id * 30
            image_index_to_use = len(complete_images)
            for image_index, image in enumerate(complete_images):
                if image.graphics_pointer == offset and image.palette_pointer == palette_ptr:
                    image_index_to_use = image_index
            #print(sprite_index, image_index_to_use, hex(offset))
            if image_index_to_use == len(complete_images):
                complete_images.append(ImagePack(image_index_to_use, offset, palette_ptr))


            # get animation #, or create new
            animation_num_to_use = len(complete_animations)
            for prev_sprite_index, prev_sprite in enumerate(wip_sprites[0:sprite_index]):
                if is_same_animation(sprite["sprite_data"].animation, prev_sprite["sprite_data"].animation):
                    animation_num_to_use = complete_sprites[prev_sprite_index].animation_num
            # if not found, create new
            # print(sprite_index, animation_num_to_use)
            if animation_num_to_use == len(complete_animations):
                molds = []
                for mold_index, m in enumerate(sprite["sprite_data"].animation.properties.molds):
                    # build numerical subtile bytes
                    these_tiles = []
                    for tile in m.tiles:
                        subtile_bytes = []
                        for subtile in tile.subtile_bytes:
                            if subtile is None:
                                subtile_index = 0
                            else:
                                subtile_index = available_tiles.index(tuple(subtile)) + 1 - lowest_subtile_index
                                if inserting_whitespace_before:
                                    subtile_index += whitespace_amount
                            subtile_bytes.append(subtile_index)
                        this_tile = copy.deepcopy(tile)
                        this_tile.subtile_bytes = subtile_bytes
                        these_tiles.append(this_tile)
                    this_mold = copy.deepcopy(m)

                    # create clones and use in mold
                    if not this_mold.gridplane:
                        clones = find_clones(these_tiles, molds, sprite_index, mold_index)
                        #if sprite_index == 2:
                        #    print(sprite_index, mold_index, len(clones), [x.is_clone for x in clones])
                        these_tiles = clones
                    this_mold.tiles = these_tiles
                    molds.append(this_mold)
                    # if sprite_index == 0:
                    #     print(this_mold)
                
                this_props = copy.deepcopy(sprite["sprite_data"].animation.properties)
                this_props.molds = molds
                complete_animations.append(AnimationPack(animation_num_to_use, length=sprite["sprite_data"].animation.length, unknown=sprite["sprite_data"].animation.unknown, properties=this_props))

            # create sprite pack
            complete_sprites.append(Sprite(len(complete_sprites), image_index_to_use, animation_num_to_use, sprite["sprite_data"].palette_offset, sprite["sprite_data"].unknown_num))
        
        
        if len(complete_images) < 512:
            ind = len(complete_images)
            while ind < 512:
                complete_images.append(ImagePack(ind, UNCOMPRESSED_GFX_START + len(output_tiles), 0x250000))
                ind += 1
        if len(complete_animations) < 444:
            ind = len(complete_animations)
            while ind < 444:
                complete_animations.append(AnimationPack(ind, unknown=0x0002, properties=AnimationPackProperties(
                    vram_size=2048,
                    molds=[Mold(0, gridplane=False, tiles=[])],
                    sequences=[AnimationSequence(frames=[])]
                )))
                ind += 1
        output_tiles += bytearray([0] * (UNCOMPRESSED_GFX_END - UNCOMPRESSED_GFX_START - len(output_tiles)))
        print("sprites", len(complete_sprites))
        print("images", len(complete_images))
        print("animations", len(complete_animations))

        return assemble_from_tables_(complete_sprites, complete_images, complete_animations, output_tiles)

        # problem: clones can't reference a relative offset > 7FFF
            

            

            


def assemble_from_tables_(sprites, images, animations, output_tiles=[]):

    sprite_data = []
    image_data = []
    animation_pointers = []
    animation_data_bank_1 = []
    animation_data_bank_2 = []
    animation_banks = [[], [], [], []]
    animation_bank_bounds = [(0x259000, 0x260000), (0x260000, 0x270000), (0x270000, 0x280000), (0x360000, 0x370000)]
    bank_in_use = 0

    used_animations = []

    for sprite in sprites:
        assert sprite.image_num <= 0x1FF
        assert sprite.palette_offset <= 7
        sprite_data.append(sprite.image_num & 0xFF)
        sprite_data.append(((sprite.image_num >> 8) & 0x01) + (sprite.palette_offset << 1) + (sprite.unknown << 4))
        assert sprite.animation_num <= 0xFFFF
        sprite_data.append(sprite.animation_num & 0xFF)
        sprite_data.append((sprite.animation_num >> 8) & 0xFF)
        if sprite.animation_num not in used_animations:
            used_animations.append(sprite.animation_num)

    for image in images:
        bank = ((image.graphics_pointer - UNCOMPRESSED_GFX_START) >> 16) & 0x0F
        gfx_short = image.graphics_pointer & 0xFFF0
        assert gfx_short <= 0xFFFF
        image_data.append((gfx_short & 0xF0) + bank)
        image_data.append(gfx_short >> 8)
        palette_ptr = image.palette_pointer - PALETTE_OFFSET + 0x3000
        assert palette_ptr <= 0xFFFF
        image_data.append(palette_ptr & 0xFF)
        image_data.append(palette_ptr >> 8)

    anim_bank = ANIMATION_DATA_BANK_1_START

    for anim_id, animation in enumerate(animations):

        if anim_id not in used_animations:
            animation = AnimationPack(anim_id, unknown=0x0002, properties=AnimationPackProperties(vram_size=2048,
                molds=[
                    Mold(0, gridplane=False,
                        tiles=[]
                    ),
                ],
                sequences=[
                    AnimationSequence(
                        frames=[]
                    ),
                ]
            ))

        length_bytes = bytearray([])
        sequence_offset = bytearray([0x0C, 0x00])
        mold_offset = bytearray([])
        num_sequences = len(animation.properties.sequences)
        num_molds = len(animation.properties.molds)
        assert num_molds <= 32
        assert num_sequences <= 32
        count_bytes = bytearray([num_sequences, num_molds])
        vram = animation.properties.vram_size >> 8
        misc_bytes = bytearray([vram & 0xFF, (vram >> 8) & 0xFF, 0x02, 0x00])
        sequence_ptrs = bytearray([])
        sequence_bytes = bytearray([])
        mold_ptrs = bytearray([])
        mold_bytes = bytearray([])

        for sequence in animation.properties.sequences:
            this_sequence_offset = 0x0C + (len(animation.properties.sequences) + 1) * 2 + len(sequence_bytes)
            assert this_sequence_offset <= 0xFFFF
            if len(sequence.frames) == 0:
                sequence_ptrs.extend([0xFF, 0xFF])
            else:
                sequence_ptrs.append(this_sequence_offset & 0xFF)
                sequence_ptrs.append(this_sequence_offset >> 8)
                for frame in sequence.frames:
                    sequence_bytes.append(frame.duration)
                    sequence_bytes.append(frame.mold_id)
                sequence_bytes.append(0)
        sequence_ptrs.extend([0, 0])

        mold_offset_short = 0x0C + len(sequence_ptrs) + len(sequence_bytes)
        mold_offset.append(mold_offset_short & 0xFF)
        mold_offset.append((mold_offset_short >> 8) & 0xFF)
        for mold_index, mold in enumerate(animation.properties.molds):
            this_mold_offset = 0x0C + len(sequence_ptrs) + len(sequence_bytes) + (len(animation.properties.molds) + 1) * 2 + len(mold_bytes)
            assert this_mold_offset <= 0x7FFF
            #print(anim_id, mold_index, hex(anim_bank + this_mold_offset))
            animation.properties.molds[mold_index].offset = this_mold_offset
            if mold.gridplane:
                this_mold_offset += (0x80 << 8)
            if len(mold.tiles) > 0:
                mold_ptrs.append(this_mold_offset & 0xFF)
                mold_ptrs.append((this_mold_offset >> 8) & 0xFF)
                this_mold_bytes = bytearray([])
                if mold.gridplane:
                    for tile_index, tile in enumerate(mold.tiles):
                        # if anim_id <= 1:
                        #     print(anim_id, mold_index, tile.subtile_bytes)
                        for i, subtile_byte in enumerate(tile.subtile_bytes):
                            if subtile_byte >= 0x100:
                                tile.is_16bit = True
                        tile_bytes = bytearray([])
                        animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                        byte_1 = (tile.format & 0x03) + (tile.is_16bit << 3) + (tile.y_plus << 4) + (tile.y_minus << 5) + (tile.mirror << 6) + (tile.invert << 7)
                        tile_bytes.append(byte_1)
                        if tile.is_16bit:
                            subtile_short = 0
                            for i, subtile_byte in enumerate(tile.subtile_bytes):
                                if subtile_byte >= 0x100:
                                    subtile_short += (1 << i)
                            tile_bytes.append(subtile_short & 0xFF)
                            tile_bytes.append((subtile_short >> 8) & 0xFF)
                        for subtile_byte in tile.subtile_bytes:
                            tile_bytes.append(subtile_byte & 0xFF)
                        this_mold_bytes += tile_bytes
                else:
                    #if anim_id == 0:
                        #print(mold)
                    for tile_index, tile in enumerate(mold.tiles):
                        tile_bytes = bytearray([])
                        animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                        found_clone = False
                        #if anim_id == 242:
                        #    print(mold_index, tile_index, tile)
                        if tile.is_clone:
                            byte_1 = (0x02) + (tile.mirror << 2) + (tile.invert << 3)
                            ct = tile.tiles[0]
                            found_offset = 0
                            tmp = mold_index
                            while tmp >= 0:
                                m = animation.properties.molds[tmp]
                                if not found_clone:
                                    for ct_index, compare_tile in enumerate(m.tiles):
                                        if not found_clone and not compare_tile.is_clone:
                                            if compare_tile.mirror == ct.mirror and compare_tile.invert == ct.invert and compare_tile.subtile_bytes == ct.subtile_bytes:
                                                confirm_tile = True
                                                conf_i = 0
                                                while conf_i < len(tile.tiles) and confirm_tile:
                                                    tmp_tile_1 = tile.tiles[conf_i]
                                                    if ct_index + conf_i >= len(m.tiles):
                                                        confirm_tile = False
                                                        continue
                                                    tmp_tile_2 = m.tiles[ct_index + conf_i]
                                                    if tmp_tile_2.is_clone:
                                                        confirm_tile = False
                                                        continue
                                                    elif tmp_tile_1.x != tmp_tile_2.x or tmp_tile_1.y != tmp_tile_2.y or tmp_tile_1.mirror != tmp_tile_2.mirror or tmp_tile_1.invert != tmp_tile_2.invert or tmp_tile_1.subtile_bytes != tmp_tile_2.subtile_bytes:
                                                        confirm_tile = False
                                                        continue
                                                    conf_i += 1
                                                if confirm_tile:
                                                    found_clone = True
                                                    found_offset = compare_tile.offset
                                tmp -= 1
                            if found_clone:
                                #print(tile)
                                byte_1 += (len(tile.tiles) << 4)
                                tile_bytes.append(byte_1)
                                tile_bytes.append(tile.y)
                                tile_bytes.append(tile.x)
                                tile_bytes.append(found_offset & 0xFF)
                                tile_bytes.append((found_offset >> 8) & 0x7F)
                                this_mold_bytes += tile_bytes
                                #if anim_id == 242:
                                #    print("clone ", [hex(a) for a in tile_bytes])
                            else:
                                raise Exception("no clones found for anim %i mold %i" % (anim_id, mold_index))
                        else:
                            print(anim_id, mold_index, tile_index, tile.y, tile.x, tile.subtile_bytes)
                            tile_bytes.append(tile.y ^ 0x80)
                            tile_bytes.append(tile.x ^ 0x80)
                            byte_upper_1 = 0
                            for i, subtile_byte in enumerate(tile.subtile_bytes):
                                if subtile_byte > 0:
                                    byte_upper_1 += (1 << (3-i))
                                    if subtile_byte > 255:
                                        animations[anim_id].properties.molds[mold_index].tiles[tile_index].format = 1
                                        tile.format = 1
                            for i, subtile_byte in enumerate(tile.subtile_bytes):
                                if subtile_byte > 0:
                                    tile_bytes.append(subtile_byte & 0xFF)
                                    if tile.format == 1:
                                        tile_bytes.append((subtile_byte >> 8) & 0x01)
                            byte_lower_1 = (tile.format & 0x03) + (tile.mirror << 2) + (tile.invert << 3)
                            tile_bytes.insert(0, byte_lower_1 + (byte_upper_1 << 4))
                            this_mold_bytes += tile_bytes
                            #if anim_id == 242:
                            #    print("standalone ", [hex(a) for a in tile_bytes])
                    this_mold_bytes.append(0)
                mold_bytes += this_mold_bytes
            else:
                mold_ptrs.extend([0xFF, 0xFF])
                # this_mold_bytes = bytearray([0x00])
                # mold_bytes += this_mold_bytes
        mold_ptrs.extend([0, 0])

        length_bytes_short = 2 + len(sequence_offset) + len(mold_offset) + len(count_bytes) + len(misc_bytes) + len(sequence_ptrs) + len(sequence_bytes) + len(mold_ptrs) + len(mold_bytes)
        length_bytes = bytearray([length_bytes_short & 0xFF, (length_bytes_short >> 8) & 0xFF])
        finished_bytes = length_bytes + sequence_offset + mold_offset + count_bytes + misc_bytes + sequence_ptrs + sequence_bytes + mold_ptrs + mold_bytes

        # print(anim_id, len(finished_bytes))
        if animation_bank_bounds[bank_in_use][0] + len(animation_banks[bank_in_use]) + len(finished_bytes) >= animation_bank_bounds[bank_in_use][1]:
        #if anim_bank == ANIMATION_DATA_BANK_1_START and anim_bank + len(animation_data_bank_1) + len(finished_bytes) >= ANIMATION_DATA_BANK_1_END:
            animation_banks[bank_in_use] += bytearray([0] * (animation_bank_bounds[bank_in_use][1] - animation_bank_bounds[bank_in_use][0] - len(animation_banks[bank_in_use])))
            bank_in_use += 1
        if bank_in_use > len(animation_banks):
            raise Exception('too many animation bytes')

        anim_ptr = 0xC00000 + animation_bank_bounds[bank_in_use][0] + len(animation_banks[bank_in_use])
        animation_banks[bank_in_use].extend(finished_bytes)

        # if anim_bank == ANIMATION_DATA_BANK_1_START:
        #     #print(anim_id, len(animation_data_bank_1) + anim_bank)
        #     anim_ptr = 0xC00000 + len(animation_data_bank_1) + anim_bank
        #     animation_data_bank_1.extend(finished_bytes)
        # else: 
        #     #print(anim_id, len(animation_data_bank_2) + anim_bank)
        #     anim_ptr = 0xC00000 + len(animation_data_bank_2) + anim_bank
        #     animation_data_bank_2.extend(finished_bytes)
        animation_pointers.extend([anim_ptr & 0xFF, (anim_ptr >> 8) & 0xFF, (anim_ptr >> 16) & 0xFF])

    animation_data_bank_1 = animation_banks[0] + animation_banks[1] + animation_banks[2]
    animation_data_bank_2 = animation_banks[3]

    sprite_data += bytearray([0] * (SPRITE_PTRS_END - SPRITE_PTRS_START - len(sprite_data)))
    image_data += bytearray([0] * (IMAGE_PTRS_END - IMAGE_PTRS_START - len(image_data)))
    animation_pointers += bytearray([0] * (ANIMATION_PTRS_END - ANIMATION_PTRS_START - len(animation_pointers)))
    animation_data_bank_1 += bytearray([0] * (ANIMATION_DATA_BANK_1_END - ANIMATION_DATA_BANK_1_START - len(animation_data_bank_1)))
    animation_data_bank_2 += bytearray([0] * (ANIMATION_DATA_BANK_2_END - ANIMATION_DATA_BANK_2_START - len(animation_data_bank_2)))
    
    return bytearray(sprite_data), bytearray(image_data), bytearray(animation_pointers), bytearray(animation_data_bank_1), bytearray(animation_data_bank_2), output_tiles