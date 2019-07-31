with open('mimasv2_fw.bin', 'rb') as f:
    fw = f.read()
with open('mimasv2_par.bin', 'rb') as f:
    bs = f.read()

OFFSET = 0x100000

if len(bs) > OFFSET:
    raise ValueError(len(bs))

bs = bs + bytes(OFFSET - len(bs))
assert len(bs) == OFFSET
with open('mimasv2_final.bin', 'wb') as f:
    f.write(bs + fw)
