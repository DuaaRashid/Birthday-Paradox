import random
     
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def main():
    count = 0
    noOfTime = int(input("Enter a number : ") )   
    for i in range(1000):
        randomBirthday = getRandomBirthday(noOfTime) #getRandomBirthday=randomBirth(list)
        match = getMatch(randomBirthday)
        if match:
            count = count+1
    
    probability = round(count / 1000 * 100, 2)
    print("Total no of matches " + str(count))        
    print("Result : " + str(probability))        
         

def getRandomBirthday(index):
    randomBirth = []
    for i in range(0,index):
        rand=''
        random.shuffle(date)
        random.shuffle(month)
        rand += str(date[0]) + " " + month[0]
        randomBirth.append(rand)
    return randomBirth

    
def getMatch(bList):
    for i in range(len(bList)): #lenOFBlist = randomBirhday(list)'s length, randomBirthday=[6april,28sep,6april], i=6april
        for j in range (i+1,len(bList)): #j=28sep
            if bList[i] == bList[j]: #1.6april==28sep ? false 2.6april==6april ? true 3.returns true and breaks the loop.
                return True
    
    
    return False

main()