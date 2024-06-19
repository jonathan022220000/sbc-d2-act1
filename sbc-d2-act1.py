word = "summer bootcamp"
#      01234567891011121314
#     -141314121110987654321

#
print(word.title())
#Lower Case
print(word.capitalize().replace("p","P"))
print(word[7:11].replace("b","L"))
print(word[11:15].replace("p","E"))
print(word[12].upper() + word[5].upper())
print(word.replace(" ","jonathan").isalpha())
