number = 4294967295
file = open('file_bin.txt', 'w')
s = str(number) + '\n'
file.write(s)
file.close()

file = open('file_bin.bin', 'wb')
var = int(number).to_bytes(4, byteorder ='big')
file.write(var)
file.close()

file = open('file_bin.bin', 'rb')
data = file.read(4)
var = int.from_bytes(data, "big")
print(var)
