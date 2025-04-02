
# Is Python valid
print("Program Initialized")

# Import System
import sys

# Import Tkinter
from tkinter import Tk, Button, PhotoImage, Label
print("Successfully imported TK")

# Import Html Stuff
import requests
import json
print("Successfully imported http")

# Import PathLib
from pathlib import Path
print("Successfully imported PathLib")

# Find Image Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\m4hdi\Desktop\Blackjack\.venv\assets")
print("Path Found")

# Calculate Spread
def spread_calculator():
    global Current_Bet
    if True_Count < 2:
        Current_Bet = 0
    elif True_Count < 3:
        Current_Bet = Spread[1]
    elif True_Count < 4:
        Current_Bet = Spread[2]
    elif True_Count < 5:
        Current_Bet = Spread[3]
    elif True_Count < 6:
        Current_Bet = Spread[4]
    else:
        Current_Bet = Spread[5]

# Find Relative Path for assets
def relative_to_assets(path: str) -> Path:
    # Return Relative Path
    return ASSETS_PATH / Path(path)

# Loading Bar For Console Updates
def loading_bar_logic():
    global i
    i += 1
    percent = round(float((i / bar_total) * 100), 2)
    bar = ('-' * int(20 * (i / bar_total))).ljust(20)
    sys.stdout.write(f'\r[{bar}] {percent}%')  # \r moves the cursor to the beginning
    sys.stdout.flush()
    if percent == 100:
        print(" Done!")
        i = 0

# Load Images
def image_gen():
    global ImgA, Img2, Img3, Img4, Img5, Img6, Img7, Img8, Img9, ImgT, ImgC, ImgS, bar_total
    bar_total = 12
    print("Generating Images...")
    ImgA = PhotoImage(
        file=relative_to_assets("button_1.png"))
    loading_bar_logic()
    Img2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    loading_bar_logic()
    Img3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    loading_bar_logic()
    Img4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    loading_bar_logic()
    Img5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    loading_bar_logic()
    Img6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    loading_bar_logic()
    Img7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    loading_bar_logic()
    Img8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    loading_bar_logic()
    Img9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    loading_bar_logic()
    ImgT = PhotoImage(
        file=relative_to_assets("button_10.png"))
    loading_bar_logic()
    ImgC = PhotoImage(
        file=relative_to_assets("clear.png"))
    loading_bar_logic()
    ImgS = PhotoImage(
        file=relative_to_assets("split.png"))
    loading_bar_logic()

# Number of decks
def number_of_decks():
    global Deck_Count, Total_Ace, Total_2, Total_3, Total_4, Total_5, Total_6, Total_7, Total_8, Total_9, Total_10, Total_All, bar_total
    bar_total = 11
    # Deck Number
    Deck_Count = int(input("How Many Decks : "))
    print(f"Deck Amount Updated to {Deck_Count}")
    print("Setting Up Totals...")
    # Individual Card Number
    Total_Ace = Deck_Count * 4
    loading_bar_logic()
    Total_2 = Deck_Count * 4
    loading_bar_logic()
    Total_3 = Deck_Count * 4
    loading_bar_logic()
    Total_4 = Deck_Count * 4
    loading_bar_logic()
    Total_5 = Deck_Count * 4
    loading_bar_logic()
    Total_6 = Deck_Count * 4
    loading_bar_logic()
    Total_7 = Deck_Count * 4
    loading_bar_logic()
    Total_8 = Deck_Count * 4
    loading_bar_logic()
    Total_9 = Deck_Count * 4
    loading_bar_logic()
    Total_10 = Deck_Count * 4 * 4
    loading_bar_logic()
    Total_All = Deck_Count * 52
    loading_bar_logic()

# Decrement number of cards
def decrement_card_count(Card, MainButtonPressed):
    global Total_Ace, Total_2, Total_3, Total_4, Total_5, Total_6, Total_7, Total_8, Total_9, Total_10, Total_All, Card_Out
    if Card == "A" and Total_Ace > 0:
        Total_Ace -= 1
        Total_All -= 1
        Card_Out = "Ace"
        print("Ace Out")
    elif Card == "2" and Total_2 > 0:
        Total_2 -= 1
        Total_All -= 1
        Card_Out = "2"
        print("2 Out")
    elif Card == "3" and Total_3 > 0:
        Total_3 -= 1
        Total_All -= 1
        Card_Out = "3"
        print("3 Out")
    elif Card == "4" and Total_4 > 0:
        Total_4 -= 1
        Total_All -= 1
        Card_Out = "4"
        print("4 Out")
    elif Card == "5" and Total_5 > 0:
        Total_5 -= 1
        Total_All -= 1
        Card_Out = "5"
        print("5 Out")
    elif Card == "6" and Total_6 > 0:
        Total_6 -= 1
        Total_All -= 1
        Card_Out = "6"
        print("6 Out")
    elif Card == "7" and Total_7 > 0:
        Total_7 -= 1
        Total_All -= 1
        Card_Out = "7"
        print("7 Out")
    elif Card == "8" and Total_8 > 0:
        Total_8 -= 1
        Total_All -= 1
        Card_Out = "8"
        print("8 Out")
    elif Card == "9" and Total_9 > 0:
        Total_9 -= 1
        Total_All -= 1
        Card_Out = "9"
        print("9 Out")
    elif Card == "T" and Total_10 > 0:
        Total_10 -= 1
        Total_All -= 1
        Card_Out = "T"
        print("T Out")
    # Http request
    if len(PH) > 1 and len(DH) > 0 and MainButtonPressed == 1:
        get_blackjack_decision()
    # New True Count
    calculate_counts()
    # Update Labels
    update_deck_comp()
    update_deck_count()

# Calculate Running Count and True Count
def calculate_counts():
    global True_Count
    # Calculate total remaining cards
    Total_Cards = (Total_Ace + Total_2 + Total_3 + Total_4 + Total_5
                   + Total_6 + Total_7 + Total_8 + Total_9 + Total_10)
    # Calculate Running Count (based on Zen  values)
    Count = Total_Ace * -1 + Total_2 * 1 + Total_3 * 1 + Total_4 * 1 + Total_5 * 1 \
            + Total_6 * 1 + Total_7 * 0 + Total_8 * 0 + Total_9 * 0 + Total_10 * -1
    if Total_Cards == 0:
        True_Count = 0
    else:
        # Calculate True Count
        True_Count = -Count / (Total_Cards / 52)


# Update Deck Comp
def update_deck_comp():
    percentoftotal = (Total_All / (Deck_Count * 52)) * 100
    Deck_Comp.config(
        text=f"DECK COMP\nA : {Total_Ace}\n2 : {Total_2}\n3 : {Total_3}\n4 : {Total_4}\n5 : {Total_5}\n6 : {Total_6}"
             f"\n7 : {Total_7}\n8 : {Total_8}\n9 : {Total_9}\nT : {Total_10}\nAll : {Total_All} ({percentoftotal:.2f}%)"
    )

# Update Count
def update_deck_count():
    spread_calculator()
    CountTag.config(
            text=f"The count is : {True_Count:4f} ({Current_Bet}$)"
    )

# Update Spread
def update_spread():
    global Spread_Comp
    Spread_Comp.config(
        text=f"SPREAD\n1: {Spread[1]*Decision_Value:.2f}\n2: {Spread[2]*Decision_Value:.2f}\n3: {Spread[3]*Decision_Value:.2f}\n4: {Spread[4]*Decision_Value:.2f}\n5: {Spread[5]*Decision_Value:.2f}",
        bd=0,
        bg="#ffffff",
        fg="#000000",
        anchor='w',
        highlightthickness=0
    )

# Define Global Counter Function
def counter_logic():
    global ButA, But2, But3, But4, But5, But6, But7, But8, But9, ButT, bar_total
    bar_total = 10
    print("Generating Main Buttons...")
    # Cards Out
    ButA = Button(
        image=ImgA,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("A", 1),
        relief="flat"
    )
    ButA.place(
        x=10.0,
        y=10.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But2 = Button(
        image=Img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("2", 1),
        relief="flat"
    )
    But2.place(
        x=45.0,
        y=10.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But3 = Button(
        image=Img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("3", 1),
        relief="flat"
    )
    But3.place(
        x=80.0,
        y=10.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But4 = Button(
        image=Img4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("4", 1),
        relief="flat"
    )
    But4.place(
        x=115.0,
        y=10.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But5 = Button(
        image=Img5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("5", 1),
        relief="flat"
    )
    But5.place(
        x=150.0,
        y=10.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But6 = Button(
        image=Img6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("6", 1),
        relief="flat"
    )
    But6.place(
        x=10.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But7 = Button(
        image=Img7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("7", 1),
        relief="flat"
    )
    But7.place(
        x=45.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But8 = Button(
        image=Img8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("8", 1),
        relief="flat"
    )
    But8.place(
        x=80.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    But9 = Button(
        image=Img9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("9", 1),
        relief="flat"
    )
    But9.place(
        x=115.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButT = Button(
        image=ImgT,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decrement_card_count("T", 1),
        relief="flat"
    )
    ButT.place(
        x=150.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

# Comp and Count Elements
def count_comp():
    global Deck_Comp, CountTag, Spread_Comp
    # Show True Count
    CountTag = Label(
        text=f"The count is : 0.000000 (0$)",
        bd=0,
        bg="#ffffff",
        fg="#000716",
        anchor='w',
        highlightthickness=0
    )
    CountTag.place(
        x=10.0,
        y=90.0,
        width=200.0,
        height=30.0
    )
    print("CountTag generated")

    # Deck Composition
    Deck_Comp = Label(
        text=f"DECK COMP\nA : {Total_Ace}\n2 : {Total_2}\n3 : {Total_3}\n4 : {Total_4}\n5 : {Total_5}"
             f"\n6 : {Total_6}\n7 : {Total_7}\n8 : {Total_8}\n9 : {Total_9}\nT : {Total_10}\nAll : {Total_All} (100.00%)",
        bd=0,
        bg="#ffffff",
        fg="#000000",
        anchor='w',
        highlightthickness=0
    )
    Deck_Comp.place(
        x=10.0,
        y=120.0,
        width=110.0,
        height=180.0
    )
    print("Deck_Comp generated")

    # Spread Composition
    Spread_Comp = Label(
        text=f"SPREAD\n1: {Spread[1]:.2f}\n2: {Spread[2]:.2f}\n3: {Spread[3]:.2f}\n4: {Spread[4]:.2f}\n5: {Spread[5]:.2f}",
        bd=0,
        bg="#ffffff",
        fg="#000000",
        anchor='w',
        highlightthickness=0
    )
    Spread_Comp.place(
        x=130.0,
        y=120.0,
        width=90.0,
        height=100.0
    )
    print("Spread_Comp generated")

# Dealer Main
def dealer_cards():
    global  bar_total
    dealer_comp()
    bar_total = 10
    print("Generating Dealer Buttons...")
    # Dealer Cards
    ButDHA = Button(
        image=ImgA,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("A"),
        relief="flat"
    )
    ButDHA.place(
        x=220.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH2 = Button(
        image=Img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("2"),
        relief="flat"
    )
    ButDH2.place(
        x=255.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH3 = Button(
        image=Img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("3"),
        relief="flat"
    )
    ButDH3.place(
        x=290.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH4 = Button(
        image=Img4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("4"),
        relief="flat"
    )
    ButDH4.place(
        x=325.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH5 = Button(
        image=Img5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("5"),
        relief="flat"
    )
    ButDH5.place(
        x=360.0,
        y=45.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH6 = Button(
        image=Img6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("6"),
        relief="flat"
    )
    ButDH6.place(
        x=220.0,
        y=80.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH7 = Button(
        image=Img7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("7"),
        relief="flat"
    )
    ButDH7.place(
        x=255.0,
        y=80.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH8 = Button(
        image=Img8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("8"),
        relief="flat"
    )
    ButDH8.place(
        x=290.0,
        y=80.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDH9 = Button(
        image=Img9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("9"),
        relief="flat"
    )
    ButDH9.place(
        x=325.0,
        y=80.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButDHT = Button(
        image=ImgT,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dealer_hand("T"),
        relief="flat"
    )
    ButDHT.place(
        x=360.0,
        y=80.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

# Dealer Sub
def dealer_hand(selected_card_DH):
    global DH
    DH = selected_card_DH
    decrement_card_count(selected_card_DH, 0)
    if len(PH) > 1 and len (DH) > 0:
        get_blackjack_decision()
    update_dealer()

# Dealer Comp
def dealer_comp():
    global Dealer
    # Show Dealer Hand
    Dealer = Label(
        text=f"Dealer Has : {DH}",
        bd=0,
        bg="#ffffff",
        fg="#000716",
        highlightthickness=0
    )
    Dealer.place(
        x=220.0,
        y=10.0,
        width=170.0,
        height=28.0
    )
    print(f"Dealer Label generated")

# Update Dealer
def update_dealer():
    Dealer.config(
            text=f"Dealer Has : {DH}"
    )

# Player Main
def player_cards():
    global bar_total
    player_comp()
    bar_total = 10
    print("Generating Player Buttons...")
    # Player Cards
    ButPHA = Button(
        image=ImgA,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("A"),
        relief="flat"
    )
    ButPHA.place(
        x=220.0,
        y=150.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH2 = Button(
        image=Img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("2"),
        relief="flat"
    )
    ButPH2.place(
        x=255.0,
        y=150.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH3 = Button(
        image=Img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("3"),
        relief="flat"
    )
    ButPH3.place(
        x=290.0,
        y=150.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH4 = Button(
        image=Img4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("4"),
        relief="flat"
    )
    ButPH4.place(
        x=325.0,
        y=150.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH5 = Button(
        image=Img5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("5"),
        relief="flat"
    )
    ButPH5.place(
        x=360.0,
        y=150.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH6 = Button(
        image=Img6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("6"),
        relief="flat"
    )
    ButPH6.place(
        x=220.0,
        y=185.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH7 = Button(
        image=Img7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("7"),
        relief="flat"
    )
    ButPH7.place(
        x=255.0,
        y=185.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH8 = Button(
        image=Img8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("8"),
        relief="flat"
    )
    ButPH8.place(
        x=290.0,
        y=185.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPH9 = Button(
        image=Img9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("9"),
        relief="flat"
    )
    ButPH9.place(
        x=325.0,
        y=185.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButPHT = Button(
        image=ImgT,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: player_hand("T"),
        relief="flat"
    )
    ButPHT.place(
        x=360.0,
        y=185.0,
        width=30.0,
        height=30.0
    )
    loading_bar_logic()

    ButClear = Button(
        image=ImgC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clear_hand(),
        relief="flat"
    )
    ButClear.place(
        x=310.0,
        y=220.0,
        width=80.0,
        height=30.0
    )
    print("Clear Button generated")

    ButSplit = Button(
        image=ImgS,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: split_mode(),
        relief="flat"
    )
    ButSplit.place(
        x=310.0,
        y=255.0,
        width=80.0,
        height=30.0
    )
    print("Split Button generated")

# Player Sub
def player_hand(selected_card_PH):
    global PH
    PH = PH + selected_card_PH
    decrement_card_count(selected_card_PH, 0)
    if len(PH) > 1 and len (DH) > 0:
        get_blackjack_decision()
    update_player()

# Player Comp
def player_comp():
    global Player, Action, SplitMode
    # Show Player Hand
    Player = Label(
        text=f"Player Has : {PH}",
        bd=0,
        bg="#ffffff",
        fg="#000716",
        highlightthickness=0
    )
    Player.place(
        x=220.0,
        y=115.0,
        width=170.0,
        height=30.0
    )
    print(f"Player Label generated")

    Action = Label(
        text=f"{Decision} : {Decision_Value}x Insurance : {Insurance}",
        bd=0,
        bg="#ffffff",
        fg="#000716",
        anchor='e',
        highlightthickness=0
    )
    Action.place(
        x=120.0,
        y=220.0,
        width=180.0,
        height=30.0
    )
    print(f"Action Label generated")

    SplitMode = Label(
        text=f"Splitted : False",
        bd=0,
        bg="#ffffff",
        fg="#000716",
        anchor='e',
        highlightthickness=0
    )
    SplitMode.place(
        x=120.0,
        y=255.0,
        width=180.0,
        height=30.0
    )
    print(f"Split Label generated")

# Clear Player Hand
def clear_hand():
    global PH, DH, Decision, Insurance, Decision_Value, Split_Mode
    PH = ""
    DH = ""
    Decision = "Nan"
    Insurance = "NaN"
    Decision_Value = 1
    Split_Mode = 1
    update_split_mode()
    update_action_text()
    update_dealer()
    update_player()
    update_spread()
    print("Labels Cleared")

# Update PLayer
def update_player():
    Player.config(
            text=f"Player Has : {PH}"
    )

# Split Card
def split_mode():
    global Decision, Decision_Value, Insurance
    Decision, Decision_Value, Insurance = "NaN", 0, "NaN"
    update_action_text()
    global Split_Mode, PH
    if Split_Mode == 1 and len(PH) == 2 and len(DH) > 0 and PH[0] == PH[1]:
        Split_Mode = 2
        if len(PH) > 1:
            PH = PH[0]
            update_player()
        print("Splitting (Hand 1)")
    elif Split_Mode == 2 and len(PH) > 1:
        Split_Mode = 0
        if len(PH) > 1:
            PH = PH[0]
            update_player()
        print("Splitting (Hand 2)")
    elif Split_Mode == 0 and len(PH) > 1:
        Split_Mode = 1
        clear_hand()
        print("Splitting is now allowed")
    update_split_mode()
    if len(PH) > 1 and len(DH) > 0:
        get_blackjack_decision()

# Update Split Status
def update_split_mode():
    if Split_Mode == 1:
        Splitted = False
        Hand = ""
    elif Split_Mode == 2:
        Splitted = True
        Hand = " (Hand 1)"
    else:
        Splitted = True
        Hand = " (Hand 2)"
    SplitMode.config(
            text=f"Splitted{Hand} : {Splitted}"
    )

# Function to request and process blackjack decisions
def get_blackjack_decision():
    global Decision, Insurance, Decision_Value, Split_Mode
    ResetSplitModeHtml = 0
    if Split_Mode == 2:
        Split_Mode = 0
        ResetSplitModeHtml = 1
    url = "https://wizardofodds.com/calculators-js/blackjack/calculate/"
    params = {
        "a": Total_2,  # Number of 2s remaining
        "b": Total_3,  # Number of 3s remaining
        "c": Total_4,  # Number of 4s remaining
        "d": Total_5,  # Number of 5s remaining
        "e": Total_6,  # Number of 6s remaining
        "f": Total_7,  # Number of 7s remaining
        "g": Total_8,  # Number of 8s remaining
        "h": Total_9,  # Number of 9s remaining
        "i": Total_10,  # Number of 10s remaining
        "j": Total_Ace,  # Number of Aces remaining
        "k": 1,  # Before or After Hand is dealt
        "l": 1.5,  # Blackjack payout ratio
        "m": 0,  # Peak for BJ
        "n": 0,  # Hits on Soft 17
        "o": 0,  # Double
        "p": Split_Mode,  # Split
        "q": Split_Mode,  # Split Aces
        "r": 0,  # Draw to Split Aces
        "s": 0,  # Double After Split
        "t": 0,  # Surrender
        "u": DH,  # Dealer card
        "v": PH,  # Player cards
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("Error", False):
            Decision, Insurance = "", ""
        elif Split_Mode == 0:
            stand_value = data.get("Stand", 0.0)
            hit_value = data.get("Hit", 0.0)
            Decisions = [("Stand", stand_value), ("Hit", hit_value)]
            Decision, Decision_Value = max(((name, value) for name, value in Decisions if value != 0),
                                              key=lambda x: x[1], default=("None", 0))
            Decision_Value += 1
            Insurance = "No"
        else:
            insurance_value = data.get("Insurance", 0.0)
            stand_value = data.get("Stand", 0.0)
            hit_value = data.get("Hit", 0.0)
            double_value = data.get("Double", 0.0)
            split_value = data.get("Split", 0.0)
            Decisions = [("Stand", stand_value), ("Hit", hit_value), ("Double", double_value), ("Split", split_value)]
            Decision, Decision_Value = max(((name, value) for name, value in Decisions if value != 0),
                                              key=lambda x: x[1], default=("None", 0))
            Decision_Value += 1
            if insurance_value > 0:
                Insurance = "Yes"
            else:
                Insurance = "No"
    if ResetSplitModeHtml == 1:
        Split_Mode = 2
    update_action_text()
    update_spread()

# Update Action and Insurance
def update_action_text():
    Action.config(
            text=f"{Decision} : {Decision_Value:.2f}x Insurance : {Insurance}"
    )

# Avoid Crashes
def avoid_boot_crash():
    global DH, PH, Decision, Decision_Value, Insurance, Split_Mode, shoe_counter, Spread, i, Card_Out
    DH = ""
    PH = ""
    Decision = "NaN"
    Decision_Value = 0
    Insurance = "NaN"
    Split_Mode = 1
    shoe_counter = 0
    Card_Out = "No"
    print("Boot Vars Assigned")
    Spread = {
        1: 100,
        2: 200,
        3: 300,
        4: 400,
        5: 500
    }
    i = 0

# Shoe Per Hour
def update_window_title():
    global shoe_counter
    if shoe_counter == 0:
        print("Window Title Updater Loaded")
    shoe_counter += 0.01
    # Calculate elapsed time in hours
    shoe_counter_in_hours = shoe_counter / 3600
    # Calculate total cards dealt
    total_cards_dealt = (Deck_Count * 52) - (
                Total_Ace + Total_2 + Total_3 + Total_4 + Total_5 + Total_6 + Total_7 + Total_8 + Total_9 + Total_10)
    # Calculate estimated shoes per hour (how many complete shoes have been played)
    shoes_per_hour = total_cards_dealt / (Deck_Count * 52) / shoe_counter_in_hours
    # Update the window title
    window.title(f"BLACKJACK Shoes/Hour: {shoes_per_hour:.2f} ({Card_Out} Out)")
    # Call the function again after 1 second
    window.after(10, update_window_title)

# Window Structure Calls
def window_open(always_on_top):
    global window
    # Avoid Boot Crash
    avoid_boot_crash()

    # Generate Shoe
    number_of_decks()

    # initialize window
    window = Tk()

    # Make Always on top
    if always_on_top == True:
        window.attributes('-topmost', True)

    # Set Size
    window.geometry("400x320")

    # Set Window Name
    window.title("BLACKJACK")

    # Make it non-resizable
    window.resizable(False, False)

    # Set Background
    window.configure(bg="#ffffff")

    # Generate Images
    image_gen()

    # Count and Comp
    count_comp()

    # Place Count Buttons and Labels
    counter_logic()

    # Place Dealer Buttons and Labels
    dealer_cards()

    # Place Player Buttons and Labels
    player_cards()

    # Update Title
    update_window_title()

    # Run It!!!
    window.mainloop()
