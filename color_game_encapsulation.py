import tkinter as tk
import random

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Randomizer Game")
        self.root.geometry("400x200")

        self.score = 0

        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
        self.color_names = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink']

        self.label_name = tk.Label(self.root, text="", font=("Helvetica", 18), bg="white")
        self.label_name.place(relx=0.5, rely=0.4, anchor="center")

        self.button_start = tk.Button(self.root, text="Start", command=self.update_game, bg="lightgrey", fg="black", relief="flat", padx=10, pady=5)
        self.button_start.place(relx=0.5, rely=0.6, anchor="center")

    def update_game(self):
        random_index_text = random.randint(0, len(self.colors) - 1)
        random_index_color = random.randint(0, len(self.colors) - 1)

        text_color = self.colors[random_index_text]
        font_color = self.colors[random_index_color]

        self.label_name.config(text=self.color_names[random_index_text], fg=font_color)
        self.score += 1
        print("Score:", self.score)

if __name__ == "__main__":
    root = tk.Tk()
    color_game = ColorGame(root)
    root.mainloop()
