import os
arquivo1 = open ("exercicio_olamundo.txt", 'w', encoding='utf-8')
print(os.path.abspath(arquivo1.name))
arquivo1.write("olá mundo!!!")

print(os.path.relpath(arquivo1.name))
print(arquivo1)