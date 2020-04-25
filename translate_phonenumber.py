# This is translate phonnumber
translate_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

number = input("Phone: ")
ch = ""
for n in number:
    ch += translate_number.get(n, "!") + " "
print(ch)

# My Method
# number = input("Phone: ")
# for n in number:
#     print(translate_number[n])