import sys


# with open("newfile.txt", "w") as f1:
#     f1.write("new sentence2")

class Parser:
    def __init__(self, infile):
        self.content = open(infile, "r").readlines()  # list[str] of lines
        self.instructions_left = True
        self.n_lines = len(self.content)
        self.line_num = -1
        self.cur_line = 0

    def next_instruction(self) -> str:
        ## until there is a valid instruction or line_num = total_n_lines
        if self.cur_line >= self.n_lines:
            self.instructions_left = False
            return ""

        for i in range(self.cur_line, self.n_lines):

            line = self.content[i]
            if line.strip().startswith("//") or line == "\n":
                ## comment line or empty line
                continue

            else:
                ## valid instruction
                self.cur_line = i + 1
                if not line.startswith("("):
                    ## label doesn't have Assembly line number
                    self.line_num += 1
                return line.strip().split("//")[0].replace(" ", "")   ## remove indentation, in-line comments, and in-line spaces


    def parse_Ainstruction(self, instruction: str) -> str:
        return instruction[1:]


    def parse_Cinstruction(self, instruction: str) -> tuple[str, str, str]:
        ## dest = comp; jump
        dest, comp, jump, temp = None, None, None, None

        if "=" in instruction and ";" in instruction:
            ## there is destination and jump
            dest, temp = instruction.split("=")
            comp, jump = temp.split(";")

        elif "=" in instruction:
            ## there is only destination
            dest, comp = instruction.split("=")
            jump = "Null"

        elif ";" in instruction:
            ## there is only jump
            comp, jump = instruction.split(";")
            dest = "Null"

        return dest, comp, jump
    