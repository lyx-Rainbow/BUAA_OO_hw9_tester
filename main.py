import json
import os

def compare(file1: str, file2: str) -> bool:
    f1 = open(file1, "r")
    a = f1.readlines()
    f2 = open(file2, "r")
    b = f2.readlines()

    same = True
    if (len(a) != len(b)):
        same = False
        print("Number of Lines different!")
    else:
        for i in range(len(a)):
            if (a[i] != b[i]):
                same = False
                print("difference in output1.txt/line " +  str(i + 1))
    return same

if __name__ == '__main__':
    parameters = json.load(open("parameter.json"))
    testNum = parameters["testNum"]
    jar1 = parameters["jar1"]
    jar2 = parameters["jar2"]
    count = 0
    for i in range(testNum):
        count += 1
        os.system("python dataGenerator.py > input.txt")
        os.system("java -jar " + jar1 + " < input.txt > output1.txt")
        os.system("java -jar " + jar2 + " < input.txt > output2.txt")
        if not compare('output1.txt', 'output2.txt'):
            break;
        else:
            print("Test" + str(i) + " Same");
    if count == testNum:
        print("All Same!")