from collections import defaultdict
import math

def solution(S):
    
    lines = S.split("\n")
    res = 0
    longestNumber = ""
    phones = defaultdict(int)
    phonesCost = defaultdict(int)
    for line in lines:
        details = line.split(",")
        time, number = details[0], details[1]
        timeLst = time.split(":")
        seconds = int(timeLst[0])*360+int(timeLst[1])*60+int(timeLst[2])
        if longestNumber != "" and phones[longestNumber] < phones[number]+seconds:
            longestNumber = number
        elif longestNumber != "" and phones[longestNumber] == phones[number]+seconds:
            tempNum1 = number.replace("-","")
            tempNum2 = longestNumber.replace("-","")
            if int(tempNum1) < int(tempNum2):
                longestNumber = number
        elif longestNumber == "":
            longestNumber = number

        if seconds < 300:
            res += seconds * 3
            phonesCost[number] += seconds * 3
        else:
            res += int(math.ceil(seconds / 60))*150
            phonesCost[number] += int(math.ceil(seconds / 60))*150
        
        phones[number] += seconds


    res -= phonesCost[longestNumber]

    return res

print(solution('00:01:07,400-234-090\n00:06:07,701-080-080\n00:05:00,400-234-090'))