

import sys


inputFileName = sys.argv[1]
if "." in inputFileName:
    asm = ".asm"
    if asm in inputFileName:
        inputFileName = inputFileName.replace(".asm", "")
    else:
        raise ValueError("Please input the correct .asm file type.")


symbols={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
         'R0':0,'R1':1,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
         'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}


def parser():
    command_list = []

    asmFile = open(inputFileName + ".asm", "r")
    tempFile = open(inputFileName + ".tmp", "w")

    for line in asmFile:
        cleanedLine = cleanup(line)
        if cleanedLine != "":
            tempFile.write(cleanedLine + "\n")
    
    asmFile.close()
    tempFile.close()


def cleanup(fileLine):
    firstCharacter = fileLine[0]
    if firstCharacter == "\n" or firstCharacter == "/":
        return ""
    elif firstCharacter == " ":
        return cleanup(fileLine[1:])
    else:
        return firstCharacter + cleanup(fileLine[1:])


def firstPass():
    tempFile = open(inputFileName + ".tmp", "r")
    hackFile = open(inputFileName + ".hack", "w")
    linenumber = 0
    for line in tempFile:
        if line[0] == "(":
            label = line[1:-1]
            symbols[label] = linenumber
        else:
            linenumber += 1
            hackFile.write(line)
    tempFile.close()
    hackFile.close()

parser()
firstPass()