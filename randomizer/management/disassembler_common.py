
def dbyte(offset=0):
    def inner_dbyte(args):
        return '0x%04x' % (2*args[0] + offset), args[1:]
    return inner_dbyte


def shortify(arr, dex):
    return arr[dex] + (arr[dex + 1] << 8)


def bit(arr, dex, bit_num):
    return (arr[dex] & 1 << bit_num) >> bit_num


def byte(offset=0, prefix='', table=None):
    def inner_byte(args):
        if table and args[0] in table:
            return '%s%s' % (prefix and (prefix + '.'), table[args[0]]), args[1:]
        return '0x%02x' % (args[0] + offset), args[1:]
    return inner_byte


def byte_int(offset=0):
    def inner_byte(args):
        return '%i' % (args[0] + offset), args[1:]
    return inner_byte


def short_int(offset=0):
    def inner_short(args):
        return '%i' % (args[0] + (args[1] << 8) + offset), args[2:]
    return inner_short


def short(offset=0):
    def inner_short(args):
        return '0x%04x' % (args[0] + (args[1] << 8) + offset), args[2:]
    return inner_short


def con(constant):
    def inner_con(args):
        return '0x%02x' % (constant), args
    return inner_con


def named(name, *arg_parsers):
    def inner_named(args):
        acc = []
        for parse in arg_parsers:
            parsed_arg, args = parse(args)
            acc.append(parsed_arg)
        return name, acc
    return inner_named


def build_table(list):
    return {i.index: i.name for i in list}


def use_table_name(prefix, table, val):
    return '%s%s' % (prefix and (prefix + '.'), table[val])


def get_flag_string(args, prefix='', table=None, bits=None):
    val = 0x00
    if isinstance(args, bytearray):
        for i in range(len(args)):
            val |= args[i] << (8 * i)
    else:
        val = args
    if not bits:
        bits = [i for i in range(val.bit_length())]
    b = []
    for i in bits:
        if val & (1 << i) > 0:
            if (table and prefix):
                b.append('%s' % (use_table_name(prefix, table, i)))
            else:
                b.append('%i' % i)
    if len(b) > 0:
        return '[%s]' % (", ".join(b))
    else:
        return '[]'
