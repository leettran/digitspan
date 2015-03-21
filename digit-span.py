import random, time, sys
random.seed()

print 'how many digits do you want? ',
N = sys.stdin.readline()
N = int(N)
print '\r'

num = random.randint(0, 10**N-1)
num = "%0{0}u".format(N) % num
for c in num:
    print c,
    time.sleep(1)    
    print '\r               '

a = random.randint(0,9)
b = random.randint(0,9)
while True:
    print '\r', a, '-', b, '= ',
    line = sys.stdin.readline()
    if a - b == int(line):
        break

while True:
    print '\rnow, input the numbers in REVERSED order: ',
    line = sys.stdin.readline()
    if line == '':
        print 'r', num
        break
    line = line.strip()
    line = list(line.strip())
    line.reverse()
    line = ''.join(line)
    if line == num:
        print '\rDone!'
        break
