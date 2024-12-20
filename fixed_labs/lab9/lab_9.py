#Требуется разработать компьютерную игру «крестики-нолики».
#Минимальные требования:
#1.Графичекский интерфейс (использовать внутреннюю библиотеку питона  tkinter).
#2.Игра с приложением (приложение не должно проигрывать)

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.init_main_window()

    def init_main_window(self):
        self.window = tk.Tk()
        self.window.title("выберите сторону - крестики или оолики")
        self.window.geometry("300x150")
        self.window.eval('tk::PlaceWindow . center')
        tk.Label(self.window, text="выберите, за кого играть:").pack(pady=10)
        tk.Button(self.window, text="крестики", command=lambda: self.start_game("X")).pack(pady=5)
        tk.Button(self.window, text="колики", command=lambda: self.start_game("O")).pack(pady=5)
        self.window.mainloop()

    def start_game(self, player_choice):
        self.player = player_choice
        self.bot = "O" if player_choice == "X" else "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.window.destroy()
        self.create_game_window()

    def create_game_window(self):
        self.game_window = tk.Tk()
        self.game_window.title("крестики нолики")
        self.game_window.geometry("300x300")
        self.game_window.eval('tk::PlaceWindow . center')

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.game_window, text="", font='normal 20 bold', height=2, width=5,
                                               command=lambda i=i, j=j: self.player_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        if self.bot == "X":
            self.bot_move()

        self.game_window.mainloop()

    def player_move(self, i, j):
        if self.buttons[i][j]['text'] == "":
            self.buttons[i][j]['text'] = self.player
            self.board[i][j] = self.player
            if self.check_winner():
                messagebox.showinfo("игра окончена", f"победили {self.player}!")
                self.end_game()
            elif self.is_draw():
                messagebox.showinfo("игра окончена", "ничья!")
                self.end_game()
            else:
                self.bot_move()

    def bot_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.bot
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            i, j = best_move
            self.buttons[i][j]['text'] = self.bot
            self.board[i][j] = self.bot

            if self.check_winner():
                messagebox.showinfo("игра окончена", "выиграл бот!")
                self.end_game()
            elif self.is_draw():
                messagebox.showinfo("игра окончена", "ничья!")
                self.end_game()

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(simulate=True)
        if winner:
            return 1 if winner == self.bot else -1
        if self.is_draw(simulate=True):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = self.bot
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = self.player
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, simulate=False):
        for line in self.board:
            if line[0] == line[1] == line[2] and line[0] != "":
                return line[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != "":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
            return self.board[0][2]

        return None

    def is_draw(self, simulate=False):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def end_game(self):
        self.game_window.destroy()
        self.init_main_window()

# Запуск игры
TicTacToe()