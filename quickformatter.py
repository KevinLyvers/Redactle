# just for video output

# read in results.txt

with open('resultsInv.txt', 'r') as file:
    data = file.read()
    
# split by Top 25 words
test = data.split("Top 25 words")

for entry in test:
    lines = entry.split("\n")
    for line in lines:
        datas = line.split(" ")
        if len(datas) > 2:
            if float(datas[-1]) >= 1:
                print("Category " + datas[-2][:-1])
            else:
                
                printdata = ""
                printdata += datas[-2] + ": "
                printdata += str(round(float(datas[-1]) * 100, 2)) + "%"
                print(printdata)
    print("\n")
        
       # print(datas)