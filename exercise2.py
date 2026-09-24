dict = {
    "cat": "kissa",
    "dog": "koira",
    "house": "talo",
    "car": "auto",
    "tree": "puu"
}
print(dict)
word = input().lower()

def translate(word):
    if word in dict:
        print(dict[word])
    else:
        print("Word not found")