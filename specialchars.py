from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    a = ""
    b = ""
    c = ""

    for char in my_string:
        if char in  ascii_letters:
            a = a + char
        elif char in punctuation:
            b = b + char
        else:
            c = c + char

    print(a)
    print(b)
    print(c)

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")


 
