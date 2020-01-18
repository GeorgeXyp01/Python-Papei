f = open("file.txt", "r")
words = f.read().split()
vowels=["a", "e", "u", "o", "i", "y"]

def func(n):
    return len(n)

for i in range(len(words)):
    str = words[i]
    list(str)
    for x in str:
        if x in vowels:
            str = str.replace(x, "")
    words[i]="".join(str)
    
words.sort(reverse=True, key=func)

for i in range(5):
    print(words[i][::-1])


f.close()
