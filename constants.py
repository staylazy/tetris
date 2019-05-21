from colors import *

L = [ [('X', RED),'0'], #LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
	  [('X', RED),'0'],
	  [('X', RED),('X', RED)] ]

L1 = [ [('X', RED),('X', RED),('X', RED)],
	   [('X', RED),'0','0'] ]

L2 = [ [('X', RED),('X', RED)],
	   ['0',('X', RED)],
       ['0',('X', RED)] ]

L3 = [ ['0','0',('X', RED)],
       [('X', RED),('X', RED),('X', RED)] ]

LD = [ [('A', RED),'0'],
	   [('A', RED),'0'],
	   [('A', RED),('A', RED)] ]

LD1 = [ [('A', RED),('A', RED),('A', RED)],
	    [('A', RED),'0','0'] ]

LD2 = [ [('A', RED),('A', RED)],
	    ['0',('A', RED)],
        ['0',('A', RED)] ]

LD3 = [ ['0','0',('A', RED)],
        [('A', RED),('A', RED),('A', RED)] ]

I = [ [('X', ORANGE)],#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
	  [('X', ORANGE)],
	  [('X', ORANGE)],
	  [('X', ORANGE)] ]

I1 = [ [('X', ORANGE),('X', ORANGE),('X', ORANGE),('X', ORANGE)] ]

ID = [ [('A', ORANGE)],
	   [('A', ORANGE)],
	   [('A', ORANGE)],
	   [('A', ORANGE)] ]

ID1 = [ [('A', ORANGE),('A', ORANGE),('A', ORANGE),('A', ORANGE)] ]

J = [ ['0',('X', YELLOW)],#JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
	  ['0',('X', YELLOW)], 
	  [('X', YELLOW),('X', YELLOW)] ]

J1 = [ [('X', YELLOW),'0','0'],
	   [('X', YELLOW),('X', YELLOW),('X', YELLOW)] ]

J2 = [ [('X', YELLOW),('X', YELLOW)],
	   [('X', YELLOW),'0'], 
	   [('X', YELLOW),'0'] ]

J3 = [ [('X', YELLOW),('X', YELLOW),('X', YELLOW)],
	   ['0','0',('X', YELLOW)] ]

JD = [ ['0',('A', YELLOW)],
	   ['0',('A', YELLOW)],
	   [('A', YELLOW),('A', YELLOW)] ]

JD1 = [ [('A', YELLOW),'0','0'],
	    [('A', YELLOW),('A', YELLOW),('A', YELLOW)] ]

JD2 = [ [('A', YELLOW),('A', YELLOW)],
	    [('A', YELLOW),'0'], 
	    [('A', YELLOW),'0'] ]

JD3 = [ [('A', YELLOW),('A', YELLOW),('A', YELLOW)],
	    ['0','0',('A', YELLOW)] ]

O = [ [('X', GREEN),('X', GREEN)], #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
	  [('X', GREEN),('X', GREEN)] ]

OD = [ [('A', GREEN),('A', GREEN)],
	   [('A', GREEN),('A', GREEN)] ]

T = [ ['0',('X', TEAL),'0'],      #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
	  [('X', TEAL),('X', TEAL),('X', TEAL)] ]

T1 = [ [('X', TEAL),'0'],     
	   [('X', TEAL),('X', TEAL)],
	   [('X', TEAL),'0'] ]

T2 = [ [('X', TEAL),('X', TEAL),('X', TEAL)],
	   ['0',('X', TEAL),'0'] ]

T3 = [ ['0',('X', TEAL)],     
	   [('X', TEAL),('X', TEAL)],
	   ['0',('X', TEAL)] ]

TD =  [ ['0',('A', TEAL),'0'],     
	    [('A', TEAL),('A', TEAL),('A', TEAL)] ]

TD1 = [ [('A', TEAL),'0'],     
	    [('A', TEAL),('A', TEAL)],
	    [('A', TEAL),'0'] ]

TD2 = [ [('A', TEAL),('A', TEAL),('A', TEAL)],
	    ['0',('A', TEAL),'0'] ]

TD3 = [ ['0',('A', TEAL)],     
	    [('A', TEAL),('A', TEAL)],
	    ['0',('A', TEAL)] ]

S = [['0',('X', BLUE),('X', BLUE)], #SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
	 [('X', BLUE),('X', BLUE),'0']     ]

S1 = [[('X', BLUE),'0'],
	  [('X', BLUE),('X', BLUE)],
	  ['0',('X', BLUE)]]

SD1 = [[('A', BLUE),'0'],
	   [('A', BLUE),('A', BLUE)],
	   ['0',('A', BLUE)]]

SD = [['0',('A', BLUE),('A', BLUE)],
	  [('A', BLUE),('A', BLUE),'0']     ]	 

Z = [ [('X', PURPLE),('X', PURPLE),'0'], #ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
	  ['0',('X', PURPLE),('X', PURPLE)] ]

Z1 = [ ['0',('X', PURPLE)],
	   [('X', PURPLE),('X', PURPLE)],
	   [('X', PURPLE),'0'] ]

ZD = [ [('A', PURPLE),('A', PURPLE),'0'],
	   ['0',('A', PURPLE),('A', PURPLE)] ]

ZD1 = [ ['0',('A', PURPLE)],
	    [('A', PURPLE),('A', PURPLE)],
	   	[('A', PURPLE),'0'] ]
#          1   2   3   4    5   6   7   8     9   10  11   12 13 14  15     16 17    18 19
SHAPES = [[L, L1, L2, L3], [J, J1, J2, J3], [O], [I, I1], [T, T1, T2, T3], [S, S1], [Z, Z1]]

SHAPES_DROPED = [[LD, LD1, LD2, LD3], [JD, JD1, JD2, JD3], [OD], [ID, ID1], [TD, TD1, TD2, TD3], [SD, SD1], [ZD, ZD1]]

GAME_FIELD = [ 	['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0']	]