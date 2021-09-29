number = 4294967295

file = open('file_bin.bin', 'wb')
var = int(number).to_bytes(4, byteorder='big')
file.write(var)
file.close()
