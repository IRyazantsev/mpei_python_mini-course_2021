# number = 4294967295

file = open('file_bin.bin', 'rb')
data = file.read(4)
var = int.from_bytes(data, byteorder='big')
print(var)
