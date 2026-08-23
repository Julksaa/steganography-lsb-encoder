def encode_lsb(pixels: list[int], message_bits: list[int]) -> list[int]:
    return [(p & ~1) | b for p, b in zip(pixels, message_bits)] + pixels[len(message_bits):]
