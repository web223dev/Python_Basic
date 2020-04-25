text = input(">")
word = text.split(' ')
emoji = {
    ":)": "🤗",
    ":(": "☹"
}
output = ""
for w in word:
    output += emoji.get(w, w) + ' '
print(output)