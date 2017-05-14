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
    return new_num

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
    return new_num

def check_block_sub(new_num, range_row_min, range_row_max, range_col_min, range_col_max):
    cond = False
    while cond == False:
        cond = True
        for a in range(range_row_min,range_row_max):
            for b in range(range_col_min,range_col_max):
                if new_num==int(sudoku[a][b]):
                    new_num += 1
                    cond = False
                    break
    return new_num

def check_block(new_num, row, col):
        if row < 3:
            if col <3:
                check_block_sub(new_num, 0,3,0,3)
            if 3 <= col < 6:
                check_block_sub(new_num, 0,3,3,6)
            if 6 <= col:
                check_block_sub(new_num, 0,3,6,9)
        if 3 <= row < 6:
            if col <3:
                check_block_sub(new_num, 3,6,0,3)
            if 3 <= col < 6:
                check_block_sub(new_num, 3,6,3,6)
            if 6 <= col:
                check_block_sub(new_num, 3,6,6,9)
        if 6 <= row :
            if col <3:
                check_block_sub(new_num, 6,9,0,3)
            if 3 <= col < 6:
                check_block_sub(new_num, 6,9,3,6)
            if 6 <= col:
                check_block_sub(new_num, 6,9,6,9)

def sudoku_solver(sudoku):
    solve_order = []
    cond = False
    while cond == False:
        cond = True
        for row in range(0,9):
            for col in range(0,9):
                if int(sudoku[row][col])==0:
                    if max(check_row(1,row), check_col(1,col), check_block(1,row,col)) <= 9:
                        sudoku[row][col]=str(max(check_row(1,row), check_col(1,col), check_block(1,row,col)))
                        cond = False
                        solve_order.append([row, col])
                    else:
                        sudoku[solve_order[-1][0]][solve_order[-1][1]]="0"
                        del solve_order[-1]
                        sudoku[solve_order[-1][0]][solve_order[-1][1]]=str(int(sudoku[solve_order[-1][0]][solve_order[-1][1]])+1)
                        cond = False
                    print_sudoku(sudoku)

def print_sudoku(sudoku):
    print "---------------------------"
    for item in sudoku:
        print " ".join(item)

sudoku = [\
["5","9","3",'8','7','4','1','2','6'],\
["4","6","8",'3','2','1','0','7','9'],\
["7","1","2",'6','5','9','8','3','4'],\
["2","4","9",'7','1','6','3','5','8'],\
["8","7","6",'0','3','5','2','4','1'],\
["1","3","5",'2','4','8','6','9','7'],\
["6","5","4",'1','9','2','7','8','3'],\
["9","8","7",'5','6','3','4','1','2'],\
["3","2","1",'4','8','7','9','6','5']]

print_sudoku(sudoku)
sudoku_solver(sudoku)
