import sys

args = sys.argv[1:] 

if args:
    argumento = args[0]
    print(f"O argumento passado é: {argumento}")
else:
    print("Nenhum argumento passado.")