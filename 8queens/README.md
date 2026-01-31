Set N = 8
Create an array BOARD of size N
Fill BOARD with -1
Set ROW = 0

WHILE ROW is not less than 0
    Move queen in current row to next column

    WHILE column is inside the board
        Assume position is safe

        FOR each previous row
            IF same column OR same diagonal
                Mark position as unsafe
                Stop checking
            END IF
        END FOR

        IF position is safe
            Stop checking columns
        ELSE
            Move queen to next column
        END IF
    END WHILE

    IF a safe column is found
        IF this is the last row
            Display the board
            Stop
        ELSE
            Go to next row
            Reset next row column
        END IF
    ELSE
        Reset current row
        Go back to previous row
    END IF
END WHILE
