import numpy as np
import time


# Make GameBoard
def make_board():
    while True:
        try:
            x = int(input("What Size Board Would You Like?: "))
            if x > 1:
                return x
            else:
                print('Invalid Board')
                continue
        except IndexError:
            pass
        except ValueError:
            x = 0
            pass
        if x > 1:
            break
        else:
            print('Invalid Board')



# Makes Winning Gameboard To Compare Against User's Gameboard 
def correct_board(x):
    num_count = x*x-1
    nums = np.arange(1, num_count + 1)
    
    correct_array = np.full((x,x), 0)

    index = 0
    row = 0
    column = 0
    
    while True:
        if len(nums) == 0:
            break
        correct_array[row][column] = nums[0]
        nums = nums[1:]
        if column == x-1:
            row += 1
            column = 0
        else:
            column += 1
        continue
    return correct_array




# Filling Gameboard With Numbers
def fill_board(x, correct_array):
    num_count = x*x-1
    nums = np.arange(1, num_count + 1)
    np.random.shuffle(nums)

    array = np.full((x,x), 0)

    index = 0
    row = 0
    column = 0
    while True:
        if len(nums) == 0:
            break
        array[row][column] = nums[0]
        nums = nums[1:]
        if column == x-1:
            row += 1
            column = 0
        else:
            column += 1
        continue
    
    return array

# Returns True or False if Board Is Valid
def board_check(x, array, correct_array):
    
    # Checking if board given is already solved board
    same_board = np.array_equal(array, correct_array)
    
    if same_board == True:
        valid = False
        return valid

    else:
        # If board is solvable algorithm
        flat_board = array.flatten()
        list_board = list(flat_board)

        for i in list_board:
            if i == 0:
                index_0 = list_board.index(i)
                
        del list_board[index_0]

        n = len(list_board)

        inversion_count = 0
        for i in range(n):
            for j in range(i+1,n):
                if list_board[i] > list_board[j]:
                    inversion_count += 1
        
        # Zero always starts on bottom row
        row_from_bottom = 1

        if x % 2 != 0:
            if inversion_count % 2 == 0:
                valid = True
                return valid
            else:
                valid = False
                return valid

        else:
            if x % 2 != 0:
                if row_from_bottom % 2 == 0:
                    valid = True
                    return valid
                else:
                    valid = False
                    return valid

            else:
                if inversion_count % 2 == 0:
                    valid = True
                    return valid
                else:
                    valid = False
                    return valid



# Keeps making new boards if board_check returned False
def new_board(x, array, correct_array):
    while True:
        array = fill_board(x, correct_array)
        valid = board_check(x, array, correct_array)
        if valid == False:
            print(array)
            print('Invalid Board: Making New Board')
            time.sleep(3)
            continue
        else:
            return array
  


# Moving Zero
def play_game(array, correct_array):
    play = True
    while play:
        # Find zero    
        find_0 = np.where(array == 0)
        row_0 = find_0[0][0] # Row number of zero
        column_0 = find_0[1][0] # Column number of zero

        num_up = -1
        num_right = -1
        num_down = -1
        num_left = -1
       

        try:
            num_up = array[row_0 - 1][column_0]
        except IndexError:
            pass

        try:
            num_down = array[row_0 + 1][column_0]
        except IndexError:
            pass

        try:
            num_right = array[row_0][column_0 + 1]
        except IndexError:
            pass

        try:
            num_left = array[row_0][column_0 - 1]
        except IndexError:
            pass

        try:
            loc_up = np.where(array == num_up)
            loc_up_row = loc_up[0][0]
            loc_up_column = loc_up[1][0]
        except IndexError:
            pass

        try:
            loc_down = np.where(array == num_down)
            loc_down_row = loc_down[0][0]
            loc_down_column = loc_down[1][0]
        except IndexError:
            pass


        try: 
            loc_right = np.where(array == num_right)
            loc_right_row = loc_right[0][0]
            loc_right_column = loc_right[1][0]
        except IndexError:
            pass

        try:
            loc_left = np.where(array == num_left)
            loc_left_row = loc_left[0][0]
            loc_left_column = loc_left[1][0]
        except IndexError:
            pass


        while True:
            try:
                print('')
                ask_swap = int(input(f"Swap what number?: "))
                print('')
            except ValueError:
                print('')
                print(array)
                print('Invalid Move')
                continue

            if ask_swap == num_up and num_up != -1:
                array[loc_up_row][loc_up_column] = 0
                array[row_0][column_0] = ask_swap
                game_complete = np.array_equal(array, correct_array)
                if game_complete == True:
                    print(array)
                    print('WINNER WINNER CHICKEN DINNER!')
                    play = False
                    break
                else:
                    print(array)
                    break
            
            if ask_swap == num_down and num_down != -1:
                array[loc_down_row][loc_down_column] = 0
                array[row_0][column_0] = ask_swap
                game_complete = np.array_equal(array, correct_array)
                if game_complete == True:
                    print(array)
                    print('WINNER WINNER CHICKEN DINNER!')
                    play = False
                    break
                else:
                    print(array)
                    break
            if ask_swap == num_right and num_right != -1:
                array[loc_right_row][loc_right_column] = 0
                array[row_0][column_0] = ask_swap
                game_complete = np.array_equal(array, correct_array)
                if game_complete == True:
                    print(array)
                    print('WINNER WINNER CHICKEN DINNER!')
                    play = False
                    break
                else:
                    print(array)
                    break
            if ask_swap == num_left and num_left != -1:
                array[loc_left_row][loc_left_column] = 0
                array[row_0][column_0] = ask_swap
                game_complete = np.array_equal(array, correct_array)
                if game_complete == True:
                    print(array)
                    print('WINNER WINNER CHICKEN DINNER!')
                    play = False
                    break
                else:
                    print(array)
                    break
            else:
                print('')
                print(array)
                print('Invalid Move')
                continue






# Main Loop
def main_loop():
    x = make_board() # x = size chosen board
    correct_array = correct_board(x)
    array = fill_board(x, correct_array)
    valid = board_check(x, array, correct_array) # Returns True or False
    if valid == False:
        new_array = new_board(x, array, correct_array)
        print(new_array)
        play_game(new_array, correct_array)
        
    else:
        print(array)
        play_game(array, correct_array)



main_loop()
