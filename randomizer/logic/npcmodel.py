class NPCModels:
    def __init__(self):
        self.output = []

    def assemble_from_table(table):
        output = bytearray()
        for model in table:
            output.append(model["sprite"] & 0xFF)
            output.append((model["vram_size"] << 5) | (model["vram_store"] << 2) | (model["sprite"] >> 8))
            output.append((model["priority_2"] << 7) | (model["priority_1"] << 6) | (model["priority_0"] << 5) | (model["byte2_bit4"] << 4) | (model["byte2_bit3"] << 3) | (model["byte2_bit2"] << 2) | (model["byte2_bit1"] << 1) | model["byte2_bit0"])
            if model["y_pixel_shift"] < 0:
                byte4 = (1 << 4) | (model["y_pixel_shift"] + 16)
            else:
                byte4 = model["y_pixel_shift"]
            byte4 |= (model["shadow"] << 5)
            byte4 |= (model["cannot_clone"] << 7)
            output.append(byte4)
            output.append((model["obtuse_axis"] << 4) | model["acute_axis"])
            output.append((model["byte5_bit7"] << 7) | (model["byte5_bit6"] << 6) | (model["show_shadow"] << 5) | model["height"])
            output.append(model["byte6_bit2"] << 2)
        return output