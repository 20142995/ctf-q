import zlib
compress = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x00\xcbM-\xc9\xc8O\xf1K\xccMeba``(I-.\x01\x00\xf89"P\x13\x00\x00\x00\t\t\t\t\t\t\t\t\t'
result = zlib.decompress(compress, 16 + zlib.MAX_WBITS)
print(result)