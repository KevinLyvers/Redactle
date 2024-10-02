import random 

G1size = 100
G2size = 200

G1 = []
G2 = []

for i in range(G1size):
    G1.append(["1"])
    
for i in range(G2size):
    G2.append(["2"])

random.shuffle(G1)
random.shuffle(G2)

for i in range(100):
    G1[i].append("t")

random.shuffle(G1)
random.shuffle(G2)
    
for i in range(0):
    G2[i].append("t")

random.shuffle(G1)
random.shuffle(G2)

for i in range(20):
    G1[i].append("e")
    
random.shuffle(G1)
random.shuffle(G2)

all = G1 + G2

#random.shuffle(all)

print(len(all))
print(all)

sum1 = 0
sum2 = 0
for i in range(1000000):
    take = all[random.randint(0, 299)]
    #print(take)
    #input()
    if "t" in take:
        if "1" in take:
            sum1 += 1
        if "2" in take:
            sum2 += 1
            
print(sum1 / 1000000)
print(sum2 / 1000000)


# given a random article guessing e will distuinsh G1 6.66% of the time and G2 0% of the time
# given a random article guessing t will distuinsh G1 26.6874% 