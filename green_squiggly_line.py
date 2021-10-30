

def run(sentence):
    def is_letter(c):
        return c.isalpha()

    # Check uppper
    if not is_letter(sentence[0]) or sentence[0] != sentence[0].upper():
        return False

    if sentence[-1] != '.':
        return False



    for i in range(1, len(sentence) - 1):
        if sentence[i] == '.':
            return False
        if sentence[i] == ',':
            if sentence[i+1] != ' ':
                return False
            if not is_letter(sentence[i-1]):
                return False
            if i + 2 >= len(sentence) or not is_letter(sentence[i+2]):
                return True
        if sentence[i] == ' ' and sentence[i-1] == ' ':
            return False

    return True

sentence = input()

arr = []
i = 0
while sentence:
    i += 1
    x = run(sentence)
    if not x:
        arr.append(i)
    try:
        sentence = input()
    except:
        sentence = None

if len(arr) == 0:
    print("No Problems")
else:
    for y in arr:
        print(y, end=' ')