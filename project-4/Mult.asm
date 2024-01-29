// R2 = R0 * R1
// will add R0 to itself R1 times
// let n = R1, prod = R0 + R0 + ... + R0 ---> (n times)
// for (i=0:n) {
//    prod += R0
// }

@prod
M = 0

@R1
D = M
@n
M = D

@i
M = 1

(LOOP)
    // if i > n goto (STOP)
    @i
    D = M
    @n
    D = D - M
    @STOP
    D;JGT

    // prod = prod + R0
    @R0
    D = M
    @prod
    M = M + D

    // i++
    @i
    M = M + 1

    @LOOP
    0;JMP

(STOP)
@prod
D = M
@R2
M = D

(END)
@END
0;JMP
