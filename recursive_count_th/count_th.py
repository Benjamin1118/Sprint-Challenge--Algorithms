'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    string = "th"
    count = 0

    index = word.find(string)
    if index >= 0:
        count += 1
        word = word[index + len(string):]

        #recursivly call count_th to count other th's
        count += count_th(word)


    return count



    
    
