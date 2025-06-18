def is_palindrome(word):
    return word == word[::-1]

def find_palindrome_pairs(words):
    result = []
    n = len(words)

    for i in range(n):
        for j in range(n):
            if i != j:
                combined = words[i] + words[j]
                if is_palindrome(combined):
                    result.append((words[i], words[j]))
    return result

# Example usage
words = ["tan", "nat", "fan", "naf", "ten", "net"]
pairs = find_palindrome_pairs(words)
print(pairs)
