# Anagram checker program(anagram words)

def find_anagram(word, anagram):
    if len(word) == len(anagram):
        count = 0
        for o in anagram:
            check = o in word
            if check:
                count = count + 1
            else:
                return False
                break
        if count == len(anagram):
            return True
        else:
            return False
    else:
        return False


a = input("enter the word: ")
b = input("enter the anagram: ")

print(find_anagram(a.strip().replace(" ", ""), b.strip().replace(" ", "")))
