from tables import comp_table, dest_table, jump_table


class Translator:
    def __init__(self, outfile):
        self.outfile = open(outfile, "w")


    def write_Ainstruction(self, address: int) -> str:

        binary = []
        powers = [2**x for x in range(15, -1, -1)]
        for pow in powers:
            if address >= pow:
                address = address % pow
                binary.append(1)
            else:
                binary.append(0)
        self.outfile.write("".join(str(x) for x in binary) + "\n")


    def write_Cinstruction(self, dest: str, comp: str, jump: str) -> str:
        """
        dest: 3 bits
        comp: 7 bits
        jump: 3 bits
        """
        ## comp tables has keys in terms of A only. Therefore, it comp has M instead, convert it to A
        a = "0"
        if "M" in comp:
            comp = comp.replace("M", "A")
            a = "1"

        # print("a", a)
        # print("comp", comp)
        # print("dest", dest)
        # print("jump", jump)

        self.outfile.write("111" + a + comp_table[comp] + dest_table[dest] + jump_table[jump] + "\n")

    def close_file(self):
        self.outfile.close()
    
