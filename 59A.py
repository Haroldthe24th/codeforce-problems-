word = input("")

w_len = len(word)

lc_c = 0
uc_c = 0

def foo():
    global lc_c
    global uc_c
    global word
    global w_len
    if(word.isupper()):
        print(word)
        return
    if(word.islower()):
        print(word)
        return
    
    for c in range(0, w_len):
        if(word[c].isupper()):
            uc_c += 1
        else:
            lc_c += 1
    if(uc_c > lc_c):
        print(word.upper())
    else:
        print(word.lower())
    
foo()