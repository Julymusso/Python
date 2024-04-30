# \r\n - para quebra de linha -> CRLF
# \n -> LF (unix)

print ("argumento1", 3, 4, sep="-", end='\r\n')
print ("argumento", 5, 7, sep="-", end='\n')
print ("argumento", 5, 7, sep="-", end='LA\n')