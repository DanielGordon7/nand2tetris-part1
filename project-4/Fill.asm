// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.



(LISTEN)

    @SCREEN
    D = A
    @scraddr
    M = D

    @KBD
    D = M
    @key
    M = D

    @i
    M = 1

    // if key==0 goto (WHITE)
    @key
    D = M
    @WHITE
    D;JEQ

    (BLACK)
        // if i>8155 goto (STOP)
        @i
        D = M
        @8155
        D = D - A
        @STOP
        D;JGT

        // RAM[scraddr] = -1
        @scraddr
        A = M
        M = -1
        
        // scraddr++
        @scraddr
        M = M + 1

        // i++
        @i
        M = M + 1

        @BLACK
        0;JMP

    (WHITE)
        // if i>8155 goto (STOP)
        @i
        D = M
        @8155
        D = D - A
        @STOP
        D;JGT

        // RAM[scraddr] = 0
        @scraddr
        A = M
        M = 0
        
        // scraddr ++
        @scraddr
        M = M + 1

        // i++
        @i
        M = M + 1

        @WHITE
        0;JMP

(STOP)
@LISTEN
0;JMP
