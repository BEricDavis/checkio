from collections import defaultdict as dd
def verify_anagrams(first_word, second_word):
    f_counts = dd(int)
    s_counts = dd(int)
    f_counts = {f: }
    for f in first_word:
        if f.isalpha():
            f_counts[f.lower()] += 1
    for s in second_word:
        if s.isalpha():
            s_counts[s.lower()] += 1

    if f_counts == s_counts:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"