inputFile="/home/andres/Documents/ParallelComputing/libras"
f = open(inputFile)
result = open(inputFile+"-result","w+")
import re
for line in f.readlines():
    try:
        versionIndx = re.search('\d+', line).start()
        print(line[0:versionIndx-1]+"\t"+line[versionIndx:-5])
        result.write(line[0:versionIndx-1]+ "\n")
    except Exception:
        print("some crapparoni")
f.close()
result.close()