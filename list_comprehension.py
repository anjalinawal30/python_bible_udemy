even_number = [x for x in range(1,101) if x % 2 == 0]
print(even_number)
odd_number = [x for x in range(1,101) if x % 2 != 0]
print(odd_number)


words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
