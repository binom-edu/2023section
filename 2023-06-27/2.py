fin = open('/home/ak/prog/2023-06-27/hello.txt', 'r')
s = fin.read().splitlines()
print(s)

fin.close()