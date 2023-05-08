import math
"""
def euclidH(state):
        count = 0
        rows = [[state[0],state[1],state[2]],[state[3],state[4],state[5]],[state[6],state[7],state[8]]]

        for i in range(0, len(state)):
            if(state[i] != 0):
                if(state[i] != i+1):
                    x = 0
                    y = 0
                    for j in range(0,len(rows)):
                        for k in range (0, len(rows[j])):
                            if(rows[j][k] == i+1):
                                x = k
                                y = j
                    #find distance to correct position
                    if(i<3):
                        count += math.sqrt((x-i)**2 + (y-0)**2)
                    elif(i<6):
                        count += math.sqrt((x-(i-3))**2 + (y-1)**2)
                    else:
                        count += math.sqrt((x-(i-6))**2 + (y-2)**2)
        return count

blah = [4,2,3,7,5,6,1,8,0]

print(euclidH(blah))
"""

class Problem:
    def __init__(self) -> None:
        pass
        

tester = Problem()



if(tester):
    print("tester is True")