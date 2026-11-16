import csv
import os

home = os.path.expanduser("~")
file_path = os.path.join(home, "Documents", "Stats.csv")

if not os.path.exists(file_path):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Kills", "Deaths", "Wins", "Losses", "K/D Ratio", "W/L Ratio"])

while True:
    game = input("Game name: ")
    kills = int(input("Kills: "))
    deaths = int(input("Deaths: "))
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))

    kdr = round(kills / max(deaths, 1), 2)
    wlr = round(wins / max(losses, 1), 2)

    print("Kill/Death ratio has been calculated")
    print("Win/Loss ratio has been calculated")

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([game, kills, deaths, wins, losses, kdr, wlr])

    again = input("Would you like to input a new game's statistics? (y/n): ")

    if again != "y":
        print("\nExiting...")
        print("All data saved to:", file_path)
        break