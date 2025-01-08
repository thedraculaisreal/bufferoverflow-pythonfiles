excluded_bytes = {}
#!mona bytearray -b "\x00\x01\x02\x03\x04\x23\x24\x3c\x3d\x83\x84\xba\xbb"
#!mona bytearray -b "\x00\x23\x3c\x83\xba"
for x in range(1, 256):
    if x not in excluded_bytes:
        print("\\x" + "{:02x}".format(x), end='')
print()
