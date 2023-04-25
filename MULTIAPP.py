import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip
import requests
import wikipedia
import tkinter.messagebox as messagebox
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
import io
import os
import calendar as cal
from googletrans import Translator
import datetime as dt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("MULTIAPP")
        self.master.geometry("300x400")
        
        self.label = tk.Label(self.master, text="Choose an option:")
        self.label.pack(pady=10)
        
        self.apps_button = tk.Button(self.master, text="Apps", command=self.show_apps, bg="#008CBA", fg="white", font=("Helvetica", 14, "bold"), padx=10, pady=5, bd=0, activebackground="#00688B", activeforeground="white")
        self.apps_button.pack(side=tk.TOP, pady=10)


        self.games_button = tk.Button(self.master, text="Games", command=self.show_games, bg="#0077B6", fg="white", font=("Arial", 16, "bold"), padx=30, pady=10, bd=0, activebackground="#023E8A", activeforeground="white", relief=tk.RIDGE, highlightthickness=0, highlightcolor="#0077B6", highlightbackground="#0077B6", borderwidth=0, border=0, overrelief=tk.RAISED)
        self.games_button.pack(pady=10)
        
        self.tools_button = tk.Button(self.master, text="Basic Tools", command=self.show_tools, bg="#FFE66D", fg="#333333", font=("Courier", 18, "bold"), padx=40, pady=12, bd=0, activebackground="#FFDD91", activeforeground="#333333")
        self.tools_button.pack(pady=10)
        
        self.simulators_button = tk.Button(self.master, text="Simulators", command=self.show_simulators, bg="#FFE38D", fg="#333443", font=("Courier", 18, "bold"), padx=40, pady=12, bd=0, activebackground="#FFDD91", activeforeground="#333333")
        self.simulators_button.pack(pady=10)    
    def show_games(self):
        # This function will be called when the "Games" button is clicked
        self.games_window = tk.Toplevel(self.master)
        self.games_window.title("Games")
        self.games_window.geometry("300x350")
        
        self.label = tk.Label(self.games_window, text="Choose a game:")
        self.label.pack(pady=10)
        self.tic_tac_toe_button = tk.Button(self.games_window, text="Tic Tac Toe", command=self.play_tic_tac_toe, font=("Arial", 14), bg="#FFD700", fg="black", padx=10, pady=5)
        self.tic_tac_toe_button.pack()

        self.start_pong_game_button = tk.Button(self.games_window, text="Ping Pong game", command=self.start_pong_game, font=("Arial", 14), bg="#7FFFD4", fg="black", padx=10, pady=5)
        self.start_pong_game_button.pack()

        self.number_guessing_game_button = tk.Button(self.games_window, text="Number guessing game", command=self.number_guessing_game, font=("Arial", 14), bg="#FFA07A", fg="black", padx=10, pady=5)
        self.number_guessing_game_button.pack()

        self.card_guessing_game_button = tk.Button(self.games_window, text="Card guessing game", command=self.card_guessing_game, font=("Arial", 14), bg="#ADD8E6", fg="black", padx=10, pady=5)
        self.card_guessing_game_button.pack()

        self.circle_game_button = tk.Button(self.games_window, text="Click the circle", command=self.circle, font=("Arial", 14), bg="#ADD8F5", fg="black", padx=10, pady=5)
        self.circle_game_button.pack()
   
#game functions
    def play_tic_tac_toe(self):
        # Initialize variables
        player = "X"
        moves = 0
        winner = False
        board = [["", "", ""], ["", "", ""], ["", "", ""]]

        # Define functions to check for winner and end game
        def check_winner(board):
            # Check for rows
            for row in board:
                if row[0] == row[1] == row[2] != "":
                    return True
            # Check for columns
            for col in range(3):
                if board[0][col] == board[1][col] == board[2][col] != "":
                    return True
            # Check for diagonals
            if board[0][0] == board[1][1] == board[2][2] != "":
                return True
            if board[0][2] == board[1][1] == board[2][0] != "":
                return True
            return False

        def end_game(message):
            nonlocal winner
            winner = True
            label.config(text=message)
            for button in buttons:
                button.config(state=tk.DISABLED)

        # Define function to handle button clicks
        def button_click(row, col):
            nonlocal player, moves, board
            if board[row][col] == "":
                board[row][col] = player
                buttons[row][col].config(text=player, state=tk.DISABLED)
                moves += 1
                if check_winner(board):
                    end_game(f"Player {player} wins!")
                elif moves == 9:
                    end_game("It's a tie!")
                else:
                    player = "O" if player == "X" else "X"
                    label.config(text=f"Player {player}'s turn.")

        # Create tkinter window and widgets
        window = tk.Tk()
        window.title("Tic Tac Toe")
        label = tk.Label(window, text=f"Player {player}'s turn.", font=("Helvetica", 16), pady=10)
        label.grid(row=0, column=0, columnspan=3)
        buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(window, text="", font=("Helvetica", 16), height=2, width=4,
                                    command=lambda row=row, col=col: button_click(row, col))
                button.grid(row=row+1, column=col, padx=5, pady=5)
                button_row.append(button)
            buttons.append(button_row)

        # Start tkinter event loop
        window.mainloop()
   
        winner_label = tk.Label(window, font=("Helvetica", 16))
        winner_label.pack()
       
        # Start tkinter event loop
        window.mainloop()
    def number_guessing_game(self):
        # Initialize game variables
        # Initialize game variables
        number_to_guess = random.randint(1, 100)
        guesses_left = 5

        # Create window and widgets
        

        # Define event handlers
        def submit_guess():
            nonlocal guesses_left
            guess = int(input_entry.get())
            guesses_left -= 1
            if guess == number_to_guess:
                result_label.config(text="Congratulations, you guessed the number!")
                submit_button.config(state=tk.DISABLED)
            elif guess < number_to_guess:
                result_label.config(text=f"Too low! You have {guesses_left} guesses left.")
            else:
                result_label.config(text=f"Too high! You have {guesses_left} guesses left.")
            if guesses_left == 0:
                result_label.config(text=f"Sorry, you ran out of guesses. The number was {number_to_guess}.")
                submit_button.config(state=tk.DISABLED)

        def new_game():
            nonlocal number_to_guess, guesses_left
            number_to_guess = random.randint(1, 100)
            guesses_left = 5
            submit_button.config(state=tk.NORMAL)
            result_label.config(text="")
            input_entry.delete(0, tk.END)

        root = tk.Tk()
        root.title("Number Guessing Game")

        title_label = tk.Label(root, text="Guess a number between 1 and 100:")
        title_label.pack()

        input_frame = tk.Frame(root)
        input_frame.pack()

        input_entry = tk.Entry(input_frame, width=5)
        input_entry.pack()

        submit_button = tk.Button(input_frame, text="Guess", command=submit_guess)
        submit_button.pack()

        result_label = tk.Label(root, text="")
        result_label.pack()

        reset_button = tk.Button(root, text="New Game", command=new_game)
        reset_button.pack()
        root.mainloop()
    def card_guessing_game(self):

    # Initialize game variables
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        deck = [(suit, value) for suit in suits for value in values]
        random.shuffle(deck)
        current_card = deck.pop(0)

        # Create window and widgets
        

        # Define event handlers
        def submit_guess():
            nonlocal current_card
            guess = input_entry.get().split()
            if len(guess) != 2 or guess[0] not in values or guess[1] not in suits:
                result_label.config(text="Invalid guess, please enter a value and a suit.\n EXAPLES FOR VALID INPUT - 4 Hearts, Ace 3")
            elif guess[0] == current_card[1] and guess[1] == current_card[0]:
                result_label.config(text="Congratulations, you guessed the next card!")
                submit_button.config(state=tk.DISABLED)
            else:
                result_label.config(text=f"Sorry, the next card is {deck[0][1]} of {deck[0][0]}.")
            input_entry.delete(0, tk.END)

        def new_game():
            nonlocal deck, current_card
            suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
            values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
            deck = [(suit, value) for suit in suits for value in values]
            random.shuffle(deck)
            current_card = deck.pop(0)
            submit_button.config(state=tk.NORMAL)
            current_card_label.config(text=f"{current_card[1]} of {current_card[0]}")
            result_label.config(text="")
            input_entry.delete(0, tk.END)

        root = tk.Tk()
        root.title("Card Guessing Game")

        title_label = tk.Label(root, text="Guess the next card in the deck:")
        title_label.pack()

        current_card_label = tk.Label(root, text=f"{current_card[1]} of {current_card[0]}")
        current_card_label.pack()

        input_frame = tk.Frame(root)
        input_frame.pack()

        input_entry = tk.Entry(input_frame, width=50)
        input_entry.pack(side=tk.LEFT)

        submit_button = tk.Button(input_frame, text="Guess", command=submit_guess)
        submit_button.pack(side=tk.LEFT)

        result_label = tk.Label(root, text="")
        result_label.pack()

        reset_button = tk.Button(root, text="New Game", command=new_game)
        reset_button.pack()
        root.mainloop()   
    def start_pong_game(self):
        WIDTH = 600
        HEIGHT = 400
        PADDLE_WIDTH = 10
        PADDLE_HEIGHT = 100
        BALL_RADIUS = 10
        PADDLE_SPEED = 5
        BALL_SPEED = 2.5
        # Initialize game window
        root = tk.Tk()
        root.title("Pong Game")
        canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        canvas.pack()

        # Initialize game objects
        ball = canvas.create_oval(WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS,
                                                WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS,
                                                fill='white')
        left_paddle = canvas.create_rectangle(0, HEIGHT/2-PADDLE_HEIGHT/2,
                                                            PADDLE_WIDTH, HEIGHT/2+PADDLE_HEIGHT/2,
                                                            fill='white')
        right_paddle = canvas.create_rectangle(WIDTH-PADDLE_WIDTH, HEIGHT/2-PADDLE_HEIGHT/2,
                                                            WIDTH, HEIGHT/2+PADDLE_HEIGHT/2,
                                                            fill='white')

        # Initialize game state
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED
        left_paddle_dy = 0
        right_paddle_dy = 0
        left_player_score = 0
        right_player_score = 0

        # Create score display
        left_score_display = canvas.create_text(WIDTH/4, HEIGHT/10, text=str(left_player_score), font=("Arial", 40), fill='white')
        right_score_display = canvas.create_text(3*WIDTH/4, HEIGHT/10, text=str(right_player_score), font=("Arial", 40), fill='white')

        # Bind keyboard events
        canvas.bind_all('<KeyPress-w>', lambda event: move_left_paddle_up())
        canvas.bind_all('<KeyPress-s>', lambda event: move_left_paddle_down())
        canvas.bind_all('<KeyRelease-w>', lambda event: stop_left_paddle())
        canvas.bind_all('<KeyRelease-s>', lambda event: stop_left_paddle())
        canvas.bind_all('<KeyPress-Up>', lambda event: move_right_paddle_up())
        canvas.bind_all('<KeyPress-Down>', lambda event: move_right_paddle_down())
        canvas.bind_all('<KeyRelease-Up>', lambda event: stop_right_paddle())
        canvas.bind_all('<KeyRelease-Down>', lambda event: stop_right_paddle())

        def move_left_paddle_up():
            nonlocal left_paddle_dy
            left_paddle_dy = -PADDLE_SPEED

        def move_left_paddle_down():
            nonlocal left_paddle_dy
            left_paddle_dy = PADDLE_SPEED

        def stop_left_paddle():
            nonlocal left_paddle_dy
            left_paddle_dy = 0

        def move_right_paddle_up():
            nonlocal right_paddle_dy
            right_paddle_dy = -PADDLE_SPEED

        def move_right_paddle_down():
            nonlocal right_paddle_dy
            right_paddle_dy = PADDLE_SPEED

        def stop_right_paddle():
            nonlocal right_paddle_dy
            right_paddle_dy = 0

        def update():
            nonlocal ball_dx, ball_dy, left_paddle_dy, right_paddle_dy, left_player_score, right_player_score

            # Move ball
            canvas.move(ball, ball_dx, ball_dy)

            # Move paddles
            canvas.move(left_paddle, 0, left_paddle_dy)
            canvas.move(right_paddle, 0, right_paddle_dy)

            # Check for ball collision with top or bottom wall
            ball_y = canvas.coords(ball)[1]
            if ball_y <= 0 or ball_y+2*BALL_RADIUS >= HEIGHT:
                ball_dy *= -1

            # Check for ball collision with left or right paddle
            ball_x = canvas.coords(ball)[0]
            if ball_x <= PADDLE_WIDTH and canvas.coords(left_paddle)[1] < ball_y+BALL_RADIUS < canvas.coords(left_paddle)[3]:
                ball_dx *= -1
            elif ball_x+2*BALL_RADIUS >= WIDTH-PADDLE_WIDTH and canvas.coords(right_paddle)[1] < ball_y+BALL_RADIUS < canvas.coords(right_paddle)[3]:
                ball_dx *= -1

            # Check for ball going out of bounds
            if ball_x < 0:
                right_player_score += 1
                canvas.itemconfig(right_score_display, text=str(right_player_score))
                canvas.coords(ball, WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS)
                ball_dx *= -1
            elif ball_x+2*BALL_RADIUS > WIDTH:
                left_player_score += 1
                canvas.itemconfig(left_score_display, text=str(left_player_score))
                canvas.coords(ball, WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS)
                ball_dx *= -1

            # Schedule next update
            canvas.after(10, update)

    # Start game loop
        update()
        root.mainloop()
    def circle(self):
        # Global variables
        WIDTH = 500
        HEIGHT = 500
        COLORS = ["red", "blue", "green", "yellow", "orange"]
        score = 0

        def create_circle():
            """
            Create a circle with a random color and position.
            """
            # Generate random coordinates for the circle
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            
            # Choose a random color for the circle
            color = random.choice(COLORS)
            
            # Create the circle and add it to the canvas
            circle = canvas.create_oval(x-10, y-10, x+10, y+10, fill=color, tags=("circle",))
            
            # Schedule the next circle to be created
            canvas.after(1000, lambda: remove_circle(circle))
            canvas.after(600, create_circle)
            

        def remove_circle(circle):
            """
            Remove a circle from the canvas.
            """
            canvas.delete(circle)
            

        def click_circle(event):
            """
            Handle clicks on circles.
            """
            nonlocal score 
            
            # Find all the objects that intersect with the click position
            items = canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
            
            # Check if any of the items are circles
            for item in items:
                if "circle" in canvas.gettags(item):
                    # Delete the object and increase the score
                    canvas.delete(item)
                    score += 10
            
            # Update the score label
            score_label.config(text="Score: {}".format(score))
            

        # Create the main window
        root = tk.Tk()
        root.title("Click the Circles!")

        # Create the canvas
        canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        canvas.pack()

        # Create the score label
        score_label = tk.Label(root, text="Score: {}".format(score))
        score_label.pack()

        # Bind the canvas to the click event
        canvas.bind("<Button-1>", click_circle)

        # Schedule the first circle to be created
        canvas.after(1000, create_circle)

        # Start the main loop
        root.mainloop()

    ##############################################################      
    def show_tools(self):
        self.tools_window = tk.Toplevel(self.master)
        self.tools_window.title("Basic Tools")
        self.tools_window.geometry("300x350")
        
        self.label = tk.Label(self.tools_window, text="Choose a tool:")
        self.label.pack(pady=10)
        # This function will be called when the "Basic Tools" button is clicked
        self.size_converter_button = tk.Button(self.tools_window, text="Size Converter", command=self.show_size_converter, font=("Arial", 12), bg="lightblue", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
        self.size_converter_button.pack(pady=5)

        self.location_teller_button = tk.Button(self.tools_window, text="Location Teller", command=self.show_location_teller, font=("Arial", 12), bg="lightgreen", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
        self.location_teller_button.pack(pady=5)

        self.password_generator_button = tk.Button(self.tools_window, text="Password Generator", command=self.show_password_generator, font=("Arial", 12), bg="lightyellow", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
        self.password_generator_button.pack(pady=5)

        self.interest_calculator_button = tk.Button(self.tools_window, text="Compound Interest calculator", command=self.show_interest_calculator, font=("Arial", 12), bg="orange", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
        self.interest_calculator_button.pack(pady=5)

        self.calculator_button = tk.Button(self.tools_window, text="Calculator", command=self.cal, font=("Arial", 12), bg="pink", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
        self.calculator_button.pack(pady=5)

#tools functions
    def show_size_converter(self):
        
            def convert():
                try:
                    input_val = float(input_entry.get())
                    input_unit = input_var.get()
                    output_unit = output_var.get()
                    if input_unit == 'cm':
                        if output_unit == 'm':
                            output_val = input_val / 100
                        elif output_unit == 'km':
                            output_val = input_val / 100000
                        elif output_unit == 'in':
                            output_val = input_val / 2.54
                        else:
                            output_val = input_val
                    elif input_unit == 'm':
                        if output_unit == 'cm':
                            output_val = input_val * 100
                        elif output_unit == 'km':
                            output_val = input_val / 1000
                        elif output_unit == 'in':
                            output_val = input_val * 39.37
                        else:
                            output_val = input_val
                    elif input_unit == 'km':
                        if output_unit == 'cm':
                            output_val = input_val * 100000
                        elif output_unit == 'm':
                            output_val = input_val * 1000
                        elif output_unit == 'in':
                            output_val = input_val * 39370.1
                        else:
                            output_val = input_val
                    else:
                        if output_unit == 'cm':
                            output_val = input_val * 2.54
                        elif output_unit == 'm':
                            output_val = input_val / 39.37
                        elif output_unit == 'km':
                            output_val = input_val / 39370.1
                        else:
                            output_val = input_val
                    output_entry.delete(0, tk.END)
                    output_entry.insert(0, f"{output_val:.4f}")
                except ValueError:
                    pass

            size_window = tk.Toplevel(root)
            size_window.title("Size Converter")
            size_window.geometry("400x200")

            input_label = tk.Label(size_window, text="Input:")
            input_label.grid(row=0, column=0, padx=5, pady=5)
            input_var = tk.StringVar(value='cm')
            input_menu = tk.OptionMenu(size_window, input_var, 'cm', 'm', 'km', 'in')
            input_menu.grid(row=0, column=1, padx=5, pady=5)
            input_entry = tk.Entry(size_window)
            input_entry.grid(row=0, column=2, padx=5, pady=5)

            output_label = tk.Label(size_window, text="Output:")
            output_label.grid(row=1, column=0, padx=5, pady=5)
            output_var = tk.StringVar(value='m')
            output_menu = tk.OptionMenu(size_window, output_var, 'cm', 'm', 'km', 'in')
            output_menu.grid(row=1, column=1, padx=5, pady=5)
            output_entry = tk.Entry(size_window)
            output_entry.grid(row=1, column=2, padx=5, pady=5)

            convert_button = tk.Button(size_window, text="Convert", command=convert)
            convert_button.grid(row=2, column=1, padx=5, pady=5)

            size_window.mainloop()
    def show_location_teller(self):
        
        def get_location():
            api_key = '258fb5d81a9d00d71be648fa0a0fbbdf'
            url = f"http://api.ipstack.com/check?access_key={api_key}"
            response = requests.get(url)
            data = response.json()

            country = data["country_name"]
            region = data["region_name"]
            city = data["city"]

            result = f"Country: {country}\nRegion: {region}\nCity: {city}"

            result_window = tk.Toplevel(root)
            result_window.title("Location")
            result_window.geometry("300x100")

            label = tk.Label(result_window, text=result)
            label.pack(pady=20)

        root = tk.Tk()
        root.title("Location Teller")
        root.geometry("300x300")

        label = tk.Label(root, text="Click button to get your current location")
        label.pack(pady=10)

        button = tk.Button(root, text="Show Location", command=get_location)
        button.pack(pady=10)

        root.mainloop()
    def show_password_generator(self):
        def generate_password():
            length = int(length_entry.get())

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            result_label.config(text=f"Your password is:\n{password}")
            copy_button.config(state=tk.NORMAL)

        def copy_password():
            password = result_label.cget("text").split("\n")[1]
            pyperclip.copy(password)

        root = tk.Tk()
        root.title("Password Generator")
        root.geometry("400x350")

        length_label = tk.Label(root, text="Enter password length:")
        length_label.pack(pady=10)

        length_entry = tk.Entry(root)
        length_entry.pack()

        generate_button = tk.Button(root, text="Generate Password", command=generate_password)
        generate_button.pack(pady=20)

        result_label = tk.Label(root, text="")
        result_label.pack()

        copy_button = tk.Button(root, text="Copy Password to Clipboard", state=tk.DISABLED, command=copy_password)
        copy_button.pack(pady=10)

        root.mainloop()  
    def show_interest_calculator(self):
        def calculate_interest():
            principal = float(principal_entry.get())
            rate = float(rate_entry.get())
            time = float(time_entry.get())

            if interest_type.get() == "Compound":
                interest =  principal * ((1 + rate / 100) ** time - 1)
            else:
                interest = principal * ((1 + rate / 100) ** time - 1)

            result_label.config(text=f"Interest: {interest:.2f}")


        root = tk.Tk()
        root.title("Interest Calculator")
        root.geometry("400x400")

        principal_label = tk.Label(root, text="Principal Amount:")
        principal_label.pack(pady=10)

        principal_entry = tk.Entry(root)
        principal_entry.pack()

        rate_label = tk.Label(root, text="Rate of Interest (%):")
        rate_label.pack(pady=10)

        rate_entry = tk.Entry(root)
        rate_entry.pack()

        time_label = tk.Label(root, text="Time (in years):")
        time_label.pack(pady=10)

        time_entry = tk.Entry(root)
        time_entry.pack()

        interest_type_label = tk.Label(root, text="Select Interest Type:")
        interest_type_label.pack(pady=10)

        interest_type = tk.StringVar(value="Compound")
        # simple_interest_radio = tk.Radiobutton(root, text="Simple", variable=interest_type, value="Simple")
        # simple_interest_radio.pack()

        compound_interest_radio = tk.Radiobutton(root, text="Compound", variable=interest_type, value="Compound")
        compound_interest_radio.pack()

        calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
        calculate_button.pack(pady=20)

        result_label = tk.Label(root, text="")
        result_label.pack()

        root.mainloop()  
    def cal(self):
        class ScientificCalculator:
            def __init__(self, master):
                self.master = master
                master.title("Scientific Calculator")
                master.resizable(False, False)
                master.config(bg='black')

                # Create entry box to display numbers
                self.entry = tk.Entry(master, width=32, font=('Arial', 16), justify='right', bd=0, bg='white')
                self.entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')
                self.entry.focus_set()

                # Create buttons for numbers and operators
                buttons = ['(', ')', 'AC', 'sin', 'cos', 'tan',
                        '7', '8', '9', 'sqrt', 'log', 'ln',
                        '4', '5', '6', 'x^2', 'x^y', 'e^x',
                        '1', '2', '3', '1/x', 'pi', 'x!',
                        '0', '.', '+/-', '/', '*', '-',
                        '=','⌫', 'Exit']

                row = 1
                col = 0
                for button in buttons:
                    if button == '=':
                        command = lambda x=button: self.calculate()
                    elif button == 'Exit':
                        command = lambda x=button: master.quit()
                    elif button == 'AC':
                        command = lambda x=button: self.clear()
                    elif button == '⌫':
                        command = lambda x=button: self.backspace()    
                    else:
                        command = lambda x=button: self.button_click(x)
                    tk.Button(master, text=button, width=6, height=2, font=('Arial', 16), command=command, bd=0, bg='#D9D9D9', fg='#333333').grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
                    col += 1
                    if col > 5:
                        col = 0
                        row += 1

            def button_click(self, text):
                if text == 'sqrt':
                    # Calculate the square root of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.sqrt(current)) # type: ignore
                elif text == 'sin':
                    # Calculate the sine of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.sin(current)) # type: ignore
                elif text == 'cos':
                    # Calculate the cosine of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.cos(current)) # type: ignore
                elif text == 'tan':
                    # Calculate the tangent of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.tan(current))# type: ignore
                elif text == 'log':
                    # Calculate the base-10 logarithm of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.log10(current))# type: ignore
                elif text == 'ln':
                    # Calculate the natural logarithm of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.log(current))# type: ignore
                elif text == 'x^2':
                    # Calculate the square of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, current**2)# type: ignore
                elif text == 'x^y':
                    # Calculate the power of a number
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, current)# type: ignore
                    self.power = current
                    self.operator = '^'
                elif text == 'e^x':
                    # Calculate e to the power of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.exp(current))# type: ignore
                elif text == '1/x':
                    # Calculate the reciprocal of the number in the entry box
                    current = float(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, 1/current)# type: ignore
                elif text == 'pi':
                    # Insert the value of pi into the entry box
                    self.entry.insert(tk.END, math.pi)# type: ignore
                elif text == 'x!':
                    # Calculate the factorial of the number in the entry box
                    current = int(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, math.factorial(current))# type: ignore
                else:
                    self.entry.insert(tk.END, text)
            def clear(self):
                # Clear the entry box
                self.entry.delete(0, tk.END)

            def calculate(self):
                # Evaluate the expression in the entry box
                try:
                    self.expression = self.entry.get()
                    self.result = eval(self.expression)
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, self.result)
                except:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
            def backspace(self):
                current_text = self.entry.get()
                new_text = current_text[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(0, new_text)
                
        root = tk.Tk()
        app = ScientificCalculator(root)
        root.mainloop()
##########################################################################################
    def show_simulators(self):
         # This function will be called when the "Simulators" button is clicked
        self.simulators_window = tk.Toplevel(self.master)
        self.simulators_window.title("Simulators")
        self.simulators_window.geometry("300x350")
        
        self.label = tk.Label(self.simulators_window, text="Choose a simulator:")
        self.label.pack(pady=10)

        # Define a custom style for the buttons
        style = ttk.Style()
        style.configure("Simulators.TButton", font=("Helvetica", 14), foreground="#333", background="#eee", padding=10, width=20)

        self.dice_roll_button = ttk.Button(self.simulators_window, text="Dice Roll", command=self.roll_dice, style="Simulators.TButton")
        self.dice_roll_button.pack(pady=5)

        self.coin_toss_button = ttk.Button(self.simulators_window, text="Coin Toss", command=self.toss_coin, style="Simulators.TButton")
        self.coin_toss_button.pack(pady=5)

        self.random_number_button = ttk.Button(self.simulators_window, text="Generate Random Number", command=self.generate_random_number, style="Simulators.TButton")
        self.random_number_button.pack(pady=5)

        self.joke_button = ttk.Button(self.simulators_window, text="Tell Me a Joke", command=self.tell_joke, style="Simulators.TButton")
        self.joke_button.pack(pady=5)

        self.math_button = ttk.Button(self.simulators_window, text="Maths challenge", command=self.maths_challenge, style="Simulators.TButton")
        self.math_button.pack(pady=5)

# Simulator functions
    def roll_dice(self):
        result = random.randint(1, 6)
        self.show_result(f"The result is: {result}")
    def toss_coin(self):
        result = random.choice(["Heads", "Tails"])
        self.show_result(f"The result is: {result}")
    def generate_random_number(self):
        result = random.randint(1, 100)
        self.show_result(f"The result is: {result}")
    def tell_joke(self):
        url = "https://icanhazdadjoke.com"
        response = requests.get(url, headers={"Accept": "text/plain"})
        joke = response.text
        self.show_result(joke)
    def show_result(self, result):
    # Calculate the number of lines in the result
        num_lines = len(result.split('\n'))

        # Set the height of the window based on the number of lines
        height = num_lines * 20 + 100

        self.result_window = tk.Toplevel(self.master)
        self.result_window.title("Result")
        self.result_window.geometry(f"500x{height}")

        self.label = tk.Label(self.result_window, text=result)
        self.label.pack(pady=20)
    def maths_challenge(self):
        global num1, num2
        
        def generate_problem():
            # Generate a new math problem
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            problem_text.config(text="What is " + str(num1) + " * " + str(num2) + "?")
            answer_entry.delete(0, tk.END)
            answer_entry.focus_set()

            return num1, num2

        def check_answer():
            global num1, num2
            # Get the user's answer
            answer = answer_entry.get()

            # Check if the answer is correct
            try:
                if int(answer) == num1 * num2:
                    response_text.config(text="Correct!")
                    score.set(score.get() + 1)
                else:
                    response_text.config(text="Incorrect. The answer is " + str(num1 * num2) + ".")
            except ValueError:
                response_text.config(text="Please enter a valid number.")

            # Generate a new problem
            num1, num2 = generate_problem()

        def countdown(remaining):
            if remaining <= 0:
                timer_text.config(text="Time's up!")
                answer_entry.config(state=tk.DISABLED)
                submit_button.config(state=tk.DISABLED)
                response_text.config(text="Final score: " + str(score.get()))
            else:
                timer_text.config(text="Time remaining: " + str(remaining) + " seconds")
                root.after(1000, countdown, remaining - 1)

        # Create the main window
        root = tk.Tk()
        root.title("Maths Challenge")

        # Set up the math problem frame
        problem_frame = tk.Frame(root)
        problem_frame.pack()
        problem_text = tk.Label(problem_frame, text="")
        problem_text.pack(side=tk.LEFT)
        answer_entry = tk.Entry(problem_frame)
        answer_entry.pack(side=tk.LEFT)

        # Set up the submit button
        submit_button = tk.Button(root, text="Submit", command=check_answer)
        submit_button.pack()

        # Set up the response frame
        response_frame = tk.Frame(root)
        response_frame.pack()
        response_text = tk.Label(response_frame, text="")
        response_text.pack()

        # Set up the timer frame
        timer_frame = tk.Frame(root)
        timer_frame.pack()
        score = tk.IntVar()
        score.set(0)
        timer_text = tk.Label(timer_frame, text="Time remaining: 10 seconds")
        timer_text.pack()

        # Start the game
        num1, num2 = generate_problem()
        countdown(10)

        # Run the application
        root.mainloop()
###########################################
    def show_apps(self):
        self.apps_window = tk.Toplevel(self.master)
        self.apps_window.title("Apps")
        self.apps_window.geometry("300x250")
        
        self.label = tk.Label(self.apps_window, text="Choose an App:")
        self.label.pack(pady=10)
        
        self.paint_button = tk.Button(self.apps_window, text="Paint", command=self.paint_app)
        self.paint_button.pack(pady=5)

        self.todo_button = tk.Button(self.apps_window, text="To do List", command=self.todo)
        self.todo_button.pack(pady=5)

        self.cal_button = tk.Button(self.apps_window, text="Calendar", command=self.create_calendar)
        self.cal_button.pack(pady=5)

        self.em_button = tk.Button(self.apps_window, text="Tranlator", command=self.translator_app)
        self.em_button.pack(pady=5)

        self.ex_button = tk.Button(self.apps_window, text="Expense tracker", command=self.exp)
        self.ex_button.pack(pady=5)

# Apps function
    def paint_app(self):
        # Create root window
        root = tk.Tk()
        root.title("Paint App")
        root.geometry("500x500")
        # Create canvas
        canvas = tk.Canvas(root, bg="white", width=400, height=400)
        canvas.pack(side=tk.TOP, padx=10, pady=10)

        # Bind mouse events
        canvas.bind("<B1-Motion>", lambda event: draw(event, canvas))

        # Create color picker button
        color_btn = tk.Button(root, text="Pick Color", command=lambda: choose_color(canvas))
        color_btn.pack(side=tk.LEFT, padx=10)

        # Create clear button
        clear_btn = tk.Button(root, text="Clear", command=lambda: clear_canvas(canvas))
        clear_btn.pack(side=tk.LEFT, padx=10)

        # Create eraser button
        eraser_btn = tk.Button(root, text="Eraser", command=lambda: set_color(canvas, "white"))
        eraser_btn.pack(side=tk.LEFT, padx=10)

        # Create thickness slider
        thickness_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Pen/Eraser Thickness",
                                    length=200, command=lambda val: set_thickness(canvas, val))
        thickness_slider.pack(side=tk.LEFT, padx=10)

        # Set default color and thickness
        color = "black"
        thickness = 1

        def draw(event, canvas):
            # Draw on canvas
            x, y = event.x, event.y
            canvas.create_oval(x-thickness, y-thickness, x+thickness, y+thickness, fill=color, outline=color)

        def choose_color(canvas):
            # Open color picker and set selected color
            nonlocal color
            color = askcolor()[1]

        def clear_canvas(canvas):
            # Clear canvas
            canvas.delete("all")

        def set_color(canvas, new_color):
            # Set current color
            nonlocal color
            color = new_color

        def set_thickness(canvas, new_thickness):
            # Set current thickness
            nonlocal thickness
            thickness = int(new_thickness)

        # Start main loop
        root.mainloop()
    def todo(self):
        def add_item():
            item = entry.get()
            if item:
                listbox.insert(tk.END, item)
                entry.delete(0, tk.END)

        def delete_item():
            index = listbox.curselection()
            if index:
                listbox.delete(index)

        def clear_list():
            listbox.delete(0, tk.END)

        def save_list():
            with open("todo_list.txt", "w") as f:
                for i in range(listbox.size()):
                    f.write(listbox.get(i) + "\n")

        def load_list():
            try:
                with open("todo_list.txt", "r") as f:
                    items = f.read().splitlines()
                    for item in items:
                        listbox.insert(tk.END, item)
            except FileNotFoundError:
                pass

        root = tk.Tk()
        root.title("To-Do List")

        frame1 = tk.Frame(root)
        frame1.pack()

        label = tk.Label(frame1, text="Add Item:")
        label.pack(side=tk.LEFT)

        entry = tk.Entry(frame1)
        entry.pack(side=tk.LEFT)

        button_add = tk.Button(frame1, text="Add", command=add_item)
        button_add.pack(side=tk.LEFT)

        button_delete = tk.Button(root, text="Delete Item", command=delete_item)
        button_delete.pack()

        button_clear = tk.Button(root, text="Clear List", command=clear_list)
        button_clear.pack()

        button_save = tk.Button(root, text="Save List", command=save_list)
        button_save.pack()

        button_load = tk.Button(root, text="Load List", command=load_list)
        button_load.pack()

        listbox = tk.Listbox(root)
        listbox.pack()

        load_list()

        root.mainloop()
    def create_calendar(self):
        def show_calendar(year):
            cal_year = cal.calendar(year)
            calendar_text.config(state=tk.NORMAL)
            calendar_text.delete("1.0", tk.END)
            calendar_text.insert(tk.END, cal_year)

            # Highlight today's date
            today = dt.date.today()
            year_str = str(year)
            month_str = str(today.month).rjust(2, "0")
            day_str = str(today.day).rjust(2, "0")
            today_str = f" {day_str} {cal.month_abbr[today.month]} {year_str}"
            calendar_text.tag_config("today", background="yellow")
            calendar_text.tag_remove("today", "1.0", tk.END)
            pos = calendar_text.search(today_str, "1.0", tk.END)
            while pos:
                end_pos = f"{pos}+10c"
                calendar_text.tag_add("today", pos, end_pos)
                pos = calendar_text.search(today_str, end_pos, tk.END)
            calendar_text.config(state=tk.DISABLED)



        def prev_year():
            nonlocal current_year
            current_year -= 1
            year_label.config(text=current_year)
            show_calendar(current_year)

        def next_year():
            nonlocal current_year
            current_year += 1
            year_label.config(text=current_year)
            show_calendar(current_year)

        root = tk.Tk()
        root.title("Calendar")
        root.geometry("400x400")

        current_year = dt.datetime.now().year

        year_frame = tk.Frame(root)
        year_frame.pack(pady=10)

        prev_button = tk.Button(year_frame, text="<< Prev Year", command=prev_year)
        prev_button.pack(side=tk.LEFT)

        year_label = tk.Label(year_frame, text=current_year)
        year_label.pack(side=tk.LEFT, padx=10)

        next_button = tk.Button(year_frame, text="Next Year >>", command=next_year)
        next_button.pack(side=tk.LEFT)

        calendar_text = tk.Text(root)
        calendar_text.pack()

        show_calendar(current_year)

        root.mainloop()
    def translator_app(self):
        root = tk.Tk()
        root.title("Translator App")

        def translate_text():
            # Get source and target languages and text
            source_lang = source_var.get()
            target_lang = target_var.get()
            source_text = source_textbox.get("1.0", "end").strip()

            # Translate text using Google Translate
            translator = Translator()
            translated = translator.translate(source_text, src=source_lang.lower(), dest=target_lang.lower())

            # Display translated text in target text box
            target_textbox.config(state="normal")
            target_textbox.delete("1.0", "end")
            target_textbox.insert("1.0", translated.text) # type: ignore
            target_textbox.config(state="disabled")

        # Create widgets
        source_label = tk.Label(root, text="Source Language:")
        source_var = tk.StringVar(value="English")
        source_option = tk.OptionMenu(root, source_var, "English", "Hindi", "Spanish", "French", "German", "Chinese", "Japanese")

        target_label = tk.Label(root, text="Target Language:")
        target_var = tk.StringVar(value="Hindi")
        target_option = tk.OptionMenu(root, target_var, "English", "Hindi", "Spanish", "French", "German", "Chinese", "Japanese")

        source_textbox = tk.Text(root, height=5, width=50)
        target_textbox = tk.Text(root, height=5, width=50, state="disabled")

        translate_button = tk.Button(root, text="Translate", command=translate_text)

        # Add widgets to grid
        source_label.grid(row=0, column=0, padx=10, pady=10)
        source_option.grid(row=0, column=1, padx=10, pady=10)

        target_label.grid(row=1, column=0, padx=10, pady=10)
        target_option.grid(row=1, column=1, padx=10, pady=10)

        source_textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        target_textbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        translate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        def update_source_language(*args):
            source_label.config(text="Source Language: " + source_var.get())

        def update_target_language(*args):
            target_label.config(text="Target Language: " + target_var.get())

        source_var.trace("w", update_source_language)
        target_var.trace("w", update_target_language)

        root.mainloop()
    def exp(self):
        class ExpenseTracker:
            def __init__(self, master):
                self.master = master
                master.title("Expense Tracker")
                master.geometry("500x400")

                # Create labels and entries for the expense description and amount
                self.description_label = tk.Label(master, text="Description:")
                self.description_label.grid(row=0, column=0)
                self.description_entry = tk.Entry(master)
                self.description_entry.grid(row=0, column=1)

                self.amount_label = tk.Label(master, text="Amount:")
                self.amount_label.grid(row=1, column=0)
                self.amount_entry = tk.Entry(master)
                self.amount_entry.grid(row=1, column=1)

                self.date_label = tk.Label(master, text="Date:")
                self.date_label.grid(row=2, column=0)
                self.date_entry = tk.Entry(master)
                self.date_entry.insert(0, dt.datetime.today().strftime('%Y-%m-%d'))
                self.date_entry.grid(row=2, column=1)
                # Create a button to add the expense to the tracker
                self.add_button = tk.Button(master, text="Add", command=self.add_expense)
                self.add_button.grid(row=2, column=3)

                # Create a label to display the total expenses
                self.total_expenses_label = tk.Label(master, text="Total expenses:")
                self.total_expenses_label.grid(row=3, column=0)
                self.total_expenses_value = tk.Label(master, text="0")
                self.total_expenses_value.grid(row=3, column=1)

                self.print_button = tk.Button(master, text="Print Expenses", command=self.print_expenses)
                self.print_button.grid(row=7, column=1)

                # Create a frame to display the list of expenses
                self.expenses_frame = tk.Frame(master)
                self.expenses_frame.grid(row=4, column=0, columnspan=2)
                
                # Create a button to calculate the total expenses
                self.total_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
                self.total_button.grid(row=6, column=1)

            

                # Initialize the expenses list and total expenses to zero
                self.expenses = []
                self.total_expenses = 0

            def add_expense(self):
                # Add the expense description, amount, and date to the expenses list and update the total expenses
                description = self.description_entry.get()
                amount = float(self.amount_entry.get())
                date = self.date_entry.get()
                self.expenses.append((description, amount, date))
                self.total_expenses += amount

                # Update the total expenses label
                self.total_expenses_value.configure(text=str(self.total_expenses))

                # Clear the description, amount, and date entries
                self.description_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
                self.date_entry.insert(0, dt.datetime.today().strftime('%Y-%m-%d'))

                # Update the expenses frame to display the new expense
                expense_frame = tk.Frame(self.expenses_frame)
                expense_frame.pack(side=tk.TOP, fill=tk.X)
                description_label = tk.Label(expense_frame, text=description)
                description_label.pack(side=tk.LEFT)
                amount_label = tk.Label(expense_frame, text=str(amount))
                amount_label.pack(side=tk.LEFT)
                date_label = tk.Label(expense_frame, text=date)
                date_label.pack(side=tk.LEFT)
                delete_button = tk.Button(expense_frame, text="Delete", command=lambda: self.delete_expense(expense_frame, amount))
                delete_button.pack(side=tk.RIGHT)


            def delete_expense(self, expense_frame, amount):
                # Remove the expense from the expenses list and update the total expenses
                self.expenses.remove((expense_frame.winfo_children()[0].cget("text"), amount))
                self.total_expenses -= amount

                # Update the total expenses label
                self.total_expenses_value.configure(text=str(self.total_expenses))

                # Destroy the expense frame
                expense_frame.destroy()
            def calculate_total(self):
                # Calculate the total expenses and display it
                self.total_expenses = sum([expense[1] for expense in self.expenses])
                self.total_expenses_value.config(text=str(self.total_expenses))

            
            def print_expenses(self):
                if self.expenses:
                    # Ask the user for the filename to save the PDF
                    c = canvas.Canvas("expenses.pdf")
                    
                    # Create a new PDF document with the given filename
                    
                    
                    # Define the styles for the report
                    title_style = ("Helvetica-Bold", 20)
                    heading_style = ("Helvetica-Bold", 12)
                    normal_style = ("Helvetica", 10)
                    
                    # Add the title to the report
                    c.setFont(*title_style)
                    c.drawString(50, 750, "Expense Tracker Report")
                    
                    # Add a heading for the expense data
                    c.setFont(*heading_style)
                    c.drawString(50, 700, "Expenses")
                    
                    # Add the expense data to the report
                    y = 650
                    for expense in self.expenses:
                        if len(expense) >= 3:
                            description, amount, date = expense
                            c.setFont(*normal_style)
                            c.drawString(50, y, f"Description: {description}, Amount: {amount}, Date: {date}")
                            y -= 20
                        else:
                            print("Invalid expense format")
                    
                    # Save the report and close the PDF document
                    c.save()
                else:
                    print("No expenses recorded")


        root = tk.Tk()
        expense_tracker = ExpenseTracker(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
