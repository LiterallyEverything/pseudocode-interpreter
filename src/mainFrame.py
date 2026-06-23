import pci
inter = pci.interpreter()

with open("prog.pseudo", "r") as program:
    code = program.read()
    if code:
        inter.initRun(code)
    else:
        while True:
            line = input("pseudo>>>")
            inter.initRun(line)

