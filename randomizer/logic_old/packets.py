
start = 0x1DB000
end = 0x1DB7FF

class Packets:
    def __init__(self):
        self.output = []

    def assemble_from_table(table):
        output = bytearray()
        for packet in table:
            if packet is None:
                output.extend([0xFF] * 5)
            else:
                sprite = packet["sprite"]
                script = packet["action_script"]
                unknown_bits = packet["unknown_bits"]
                unknown_bytes = packet["unknown_bytes"]
                shadow = packet["shadow"]

                output.append(((sprite - 0xC0) & 0x3F) + (unknown_bytes[0] << 6))
                output.append(unknown_bytes[1] + (unknown_bytes[2] << 3) + (unknown_bytes[3] << 5))
                output.append(unknown_bytes[4] + (unknown_bits[0] << 2) + (unknown_bits[1] << 3) + (unknown_bits[2] << 4) + (shadow << 5) + (unknown_bytes[5] << 6))
                output.append(script & 0xFF)
                output.append(((script >> 8) & 0x03) + (unknown_bytes[6] << 4))
        while len(output) < (end + 1) - start:
            output.append(0xFF)
        return output