import sys
from tables import symbol_table  # key=symbol (str), value=register (int)
from myparser import Parser
from translator import Translator

asm_file = sys.argv[1]
out_file = sys.argv[2]
# asm_file = "./06/pong/Pong.asm"
# out_file = "./finalPong.hack"

parser1 = Parser(asm_file)

translator = Translator(out_file)


print("first pass start")

## First Pass
while parser1.instructions_left:
    instruction = parser1.next_instruction()
    ## ignores empty/comment lines and strips in-line comments
    if instruction == "":
        break
    print(parser1.line_num, instruction)
    if instruction.startswith("("):
        ## label
        symbol_table[instruction[1:-1]] = parser1.line_num + 1

print("first pass completed")
print("symbol table: ", symbol_table, "\n")
print("second pass start")

## Second Pass
parser2 = Parser(asm_file)
register = 16
while parser2.instructions_left:
    instruction = parser2.next_instruction()
    if instruction == "":
        break

    if instruction.startswith("("):
        ## label
        continue

    elif instruction.startswith("@"):
        ## A-instruction
        addr = None
        print(parser2.line_num, f"A-instruction:", instruction)

        if 48 <= ord(instruction[1]) <= 57:
            ## integer
            addr = parser2.parse_Ainstruction(instruction)
            translator.write_Ainstruction(int(addr))

        else:

            ## symbol
            symbol = parser2.parse_Ainstruction(instruction)
            if symbol in symbol_table:
                addr = symbol_table[symbol]  # int
            else:
                ## new variable symbol
                symbol_table[symbol] = register  # int
                addr = register
                register += 1

            translator.write_Ainstruction(addr)

    else:
        ## C-instruction
        print(parser2.line_num, f"C-instruction:", instruction)
        dest, comp, jump = parser2.parse_Cinstruction(instruction)
        print("\tdest", dest)
        print("\tcomp", comp)
        print("\tjump", jump)
        translator.write_Cinstruction(dest, comp, jump)

print("second pass end")
print("symbol table: ", symbol_table, "\n")

translator.close_file()


# ## First Pass: create list of clean instructions and add reference labels to SymbolTable
# instructions = []
# with open(asm_file, "r") as f:
#     content = f.readlines()
#     # print("Content:")
#     lineNum = 0
#     for line in content:
#         # print(lineNum, " ", line)

#         if line.strip().startswith("//") or line == "\n":  ## .strip() to remove indentation
#             ## comment line or empty line
#             lineNum -= 1
#         elif line.strip().startswith("("):
#             ## reference label
#             label = line.strip()[1:-1]
#             # print("LINE: ", line, "LABEL: ", label, "LINE NUMBER: ", lineNum)

#             symbol_table.add_symbol(label, str(lineNum))
#             lineNum -= 1
#         else:
#             ## instruction with line number
#             instructions.append(line.split("//")[0].strip().replace(" ", ""))
#             ## .strip() removes '\t' (tab) and '\n' (end of line)
#             ## .replace() remove spaces in-between            

#         lineNum += 1


# print("clean instructions with symbols (and length):")
# print(len(instructions))
# print(instructions)
# print("Symbol Table (start):")
# print(symbol_table.symbol_table)


# ## Second Pass: read symbols from SymbolTable as needed, and if not found, add to the table (variable symbols)
# final_instructions = []
# register = 16
# for instr in instructions:
#     if instr.startswith("@"):
#         ## A-instruction

#         if 48 <= ord(instr[1]) <= 57:
#             ## integer 0,...,9 ---> not a symbol
#             final_instructions.append(instr)
#         else:
#             ## symbol
#             symbol = instr[1:]

#             if symbol in symbol_table.symbol_table:
#                 ## read symbol value from table
#                 final_instructions.append("@" + symbolT.symbol_table[symbol])
#             else:
#                 ## new variable symbol ---> add to table with value = current register number
#                 symbolT.symbol_table[symbol] = str(register)
#                 final_instructions.append("@" + str(register))
#     else:
#         ## C-instruction
#         final_instructions.append(instr)

#     register += 1


## parse clean instructions list
# print("clean instructions with numbers (and length):")
# print(len(final_instructions))
# print(final_instructions)
# print("Symbol Table (end):")
# print(symbolT.symbol_table)
# parser2 = Parser()
# parser2.parse(final_instructions)  # populates self.binary with clean instructions in binary


# ## write to output file
# with open(f"{out_file}", "w") as f:
#     for line in parser2.binary:
#         f.write(line + "\n")
