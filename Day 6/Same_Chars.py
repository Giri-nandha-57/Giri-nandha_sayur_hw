sorted_list_of_words = []
def user_inp():
    index = 0
    given_input = list(input("Enter the words : ").split(" "))
    for i in range(len(given_input)):
        index+=1
        index_j = index
        for j in given_input[i+1:]:
            if given_input[i] == j:
                given_input.pop(index_j)
            else:
                index_j+=1
    for i in given_input:
        removed_dupes_set = set(i)
        removed_dupes_list = list(str(x) for x in removed_dupes_set)
        removed_dupes_list.sort()
        removed_dupes_str = "".join(str(x) for x in removed_dupes_list)
        sorted_list_of_words.append(removed_dupes_str)
    print("count of the same chars words in the given list = ",count(sorted_list_of_words))
    
def count(words_list):
    count = 0
    index = 0
    for i in range(len(words_list)):
        index+=1
        index_j = index
        for j in words_list[i+1:]:
            if words_list[i] == j:
                words_list.pop(index_j)
                count+=1
            else:
                index_j+=1
    return count
user_inp()