# to find the most frequency occuring numbers in a given list 
# eg : [1,2,3,4,2,3,4,2,2,1,3]
# in this list the number 2 and 3 occured more no of times than the other numbers 

# my approach 
# -> find the numbers in the list 
# -> find the average by dividing the total length of the list by numbers in the list
# -> find the occurences of each number and if they are above the average then add it to emptylist
# -> print the empty list as most freq occured numbers in the list

listOfNumbers = list(input("Enter the numbers: "))

emptyList = []

totalNumbers = len(set(listOfNumbers))

lenOfList = len(listOfNumbers)

avg = lenOfList / totalNumbers


def countFunc(number,occured):
    for i in listOfNumbers:
        if number == i:
            occured += 1
        else:
            continue
    return occured

for i in listOfNumbers:
    count = 0
    count = countFunc(i,count)
    if count > avg:
        if i not in emptyList:
            emptyList.append(i)
    else:
        continue
    
print(emptyList, "Most freq occured numbers in the given list is = ",len(emptyList))
