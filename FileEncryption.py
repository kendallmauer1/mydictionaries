codes ={
'A':'%', 'a':'9', 'B':'@', 'b':'#'
}

infile = "info_security-1.txt"
outfile = "encrypted.txt"

with open(infile, 'r') as file:
    paragraph = file.read()

encryption = ""
for character in paragraph:

    if character in codes:
        encryption += codes[character]
    else:
        encryption += character

with open(outfile, 'w') as file:
    file.write(encryption)