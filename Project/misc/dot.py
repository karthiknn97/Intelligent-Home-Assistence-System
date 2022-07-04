def get_next_character(f):
    """Reads one character from the given textfile"""
    c = f.read(1)
    while c: 
        yield c
        c = f.read(1)
 
# Usage: 
with open("AY.txt", encoding="utf-8") as f:
        fi.write("{")
        for c in get_next_character(f):
            print(c, sep="", end="")
            fi.write(c)
            if c != "\n" :
                fi.write(",")
            else :
                fi.write("},{")
