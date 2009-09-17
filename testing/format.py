word = "aaaaaaaaaaaaaaaaaaaaaaaaaa"

def format_this(x,y):
    
    indent = y
    wcount = len(x)
    num = (indent - wcount)
    space = " "
    print word, space * num, "table"
    
format_this(word,50)

