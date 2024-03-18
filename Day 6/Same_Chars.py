# list = ["good","god", "adc", "cba"]
# count = 2

sorted_list_of_words = []
def user_inp():
    given_input = list(input("Enter the words : ").split(" "))
    for i in given_input:
        removed_dupes_set = set(i)
        removed_dupes_list = list(str(x) for x in removed_dupes_set)
        removed_dupes_list.sort()
        removed_dupes_str = "".join(str(x) for x in removed_dupes_list)
        sorted_list_of_words.append(removed_dupes_str)
    print(sorted_list_of_words)
    print("count of the same chars words in the given list = ",count(sorted_list_of_words))
    
def count(words_list):
    count = 0
    for i in range(len(words_list)):
        for j in words_list[i+1:]:
            print("i = ",words_list[i],"j = ",j)
            if words_list[i] == j:
                count+=1
    return count 
user_inp()