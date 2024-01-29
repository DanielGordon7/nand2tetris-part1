
## create Symbol Table with pre-defined symbols
symbol_table = {}
for i in range(16):
    symbol_table[f"R{i}"] = i

symbol_table["SCREEN"] = 16384
symbol_table["KBD"] = 24576
symbol_table["SP"] = 0
symbol_table["LCL"] = 1
symbol_table["ARG"] = 2
symbol_table["THIS"] = 3
symbol_table["THAT"] = 4


## create Control table
comp_table = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100", "A": "110000", "!D": "001101",
                "!A": "110001", "-D": "001111", "-A": "110011", "D+1": "011111", "A+1": "110111", "D-1": "001110",
                "A-1": "110010", "D+A": "000010", "D-A": "010011", "A-D": "000111", "D&A": "000000", "D|A": "010101"}


## create Destination table - have to accept either MD/DM and either AMD/ADM due to bug (mentioned in project06 instruction)
dest_table = {"Null": "000", "M": "001", "D": "010", "MD": "011", "DM": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111", "ADM": "111"}


## create Jump table
jump_table = {"Null": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}


# def print_tables():
#     for k,v in comp_table.items():
#         print(k, " ", v)
#     for k,v in dest_table.items():
#         print(k, " ", v)
#     for k,v in jump_table.items():
#         print(k, " ", v)
