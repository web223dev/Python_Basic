def emoji(text):
    word = text.split(' ')
    emoji = {
        ":)": "🤗",
        ":(": "☹"
    }
    output = ""
    for w in word:
        output += emoji.get(w, w) + ' '
    return output

text = input(">")
print(emoji(text))