from tkinter import *
from tkinter import messagebox

Player1 = 'X'
stop_game = False


def clicked(r, c):
    global Player1

    if Player1 == 'X' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="X")
        states[r][c] = 'X'
        Player1 = 'O'

    if Player1 == 'O' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="O")
        states[r][c] = 'O'
        Player1 = 'X'

    check_if_win()


def check_if_win():
    global stop_game

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True

            messagebox.showinfo("Winner", str(states[i][0]) + " Won")
            dialog_box()
            return

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True

            messagebox.showinfo("Winner", str(states[0][i]) + " Won")
            dialog_box()
            return

        elif states[0][0] == states[1][1] == states[2][2] != 0:
            stop_game = True

            messagebox.showinfo("Winner", str(states[1][1]) + " Won")
            dialog_box()
            return

        elif states[0][2] == states[1][1] == states[2][0] != 0:
            stop_game = True

            messagebox.showinfo("Winner", str(states[0][2]) + " Won")
            dialog_box()
            return

        if all(states[i][j] != 0 for i in range(3) for j in range(3)):
            stop_game = True

            messagebox.showinfo("Tie", "Tie")
            dialog_box()
            return


def dialog_box():

    # Custom Dialog Box
    dialog = Toplevel(root)
    dialog.title("Continue?")
    dialog.geometry("300x150")
    dialog.resizable(False, False)

    dialog.geometry("+10000+10000")   # Put dialog box off-screen initially

    msg_label = Label(
        dialog, text='Do you wish to continue playing?', font=("Comic Sans MS", 14))
    msg_label.pack(pady=20)

    yes_btn = Button(dialog, text='Yes', font=(
        "Comic Sans MS", 14), command=lambda: reset_game(dialog))
    yes_btn.pack(side=LEFT, padx=20)

    no_btn = Button(dialog, text='No', font=(
        "Comic Sans MS", 14), command=lambda: root.destroy())
    no_btn.pack(side=RIGHT, padx=20)

    # Center the dialog box on the screen
    dialog.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    dialog_width = dialog.winfo_width()
    dialog_height = dialog.winfo_height()
    x_position = (screen_width - dialog_width) // 2
    y_position = (screen_height - dialog_height) // 2
    dialog.geometry(f"+{x_position}+{y_position}")

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)


def reset_game(dialog):
    global Player1, stop_game
    Player1 = 'X'
    stop_game = False

    if not stop_game:
        Player1 = 'X'
        for i in range(3):
            for j in range(3):
                b[i][j].configure(text='')
                states[i][j] = 0
    dialog.destroy()


# Creating the canvas
root = Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Button
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# states of cells
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            height=4, width=8,
            font=("Comic Sans MS", "26"),
            command=lambda r=i, c=j: clicked(r, c))

        b[i][j].grid(row=i, column=j)

mainloop()
