# sudoku
def check_row(new_num, row):
    cond = False
    while cond == False:
        for item in sudoku[row]:
            if new_num==int(item):
                new_num+=1
                break
        else:
            cond = True
    print new_num

def check_col(new_num, col):
    cond = False
    while cond == False:
        for item in range(0,9):
            #print str(new_num) + "compared with" + sudoku[item][col]
            if new_num==int(sudoku[item][col]):
                new_num+=1
                break
        else:
            cond = True
    print new_num

def check_block(arg):
    pass

def print_sudoku(arg):
    pass

sudoku = [["4","0","0",'5','1','2','3','0','0'],["0","0","0",'0','0','0','0','0','0'],\
["3","0","0",'0','0','0','0','0','0'],["0","0","0",'0','0','0','0','0','0'],\
["0","0","0",'0','0','0','0','0','0'],["0","0","0",'0','0','0','0','0','0'],\
["2","0","0",'0','0','0','0','0','0'],["0","0","0",'0','0','0','0','0','0'],\
["1","0","0",'0','0','0','0','0','0']]
for item in sudoku
    print " ".join(item)

check_row(2,0)
check_col(0,0)

