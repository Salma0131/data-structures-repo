def count_vowels_consonants(str):
    set_vowels = set("a","i","u","e","o")
    count_vowels = 0 
    for char in str:
        if char in set_vowels:
            count_vowels+=1
    count_consonants = len(str) - count_vowels
    return count_vowels, count_consonants


def median_char(str):
    sorted_str = sorted(str)
    if len(str) % 2 == 0:
        return sorted_str[(len(str) // 2) - 1]
    return sorted_str[len(str) // 2]


def word_score(str):
    max_score = 0
    best_word = ""
    words = str.split()

    for word in words:
        score = 0
        for char in word:
            score += ord(char) - ord('a') + 1
        if score > max_score:
            max_score = score
            best_word = word
    return best_word

def largest_of_three(x,y,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z
        
def find_match(arr,lst):
    result = []
    for i in arr:
        if i in set(lst):
            result.append(i)
    return result


def find_match3(arr,lst,lst2):
    result = []
    for i in arr:
        if i in find_match(lst,lst2):
            result.append(i)
    return result