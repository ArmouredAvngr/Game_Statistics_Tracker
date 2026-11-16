# Game Statistics Tracker

A lightweight, cross-platform Python command-line utility that calculates your Kill/Death (K/D) and Win/Loss (W/L) ratios across multiple games and logs every session to an Excel-ready `Stats.csv` file in your `Documents` folder.

## 🎮 Features
* **Automatic Ratio Calculation:** Computes and rounds your **K/D Ratio** and **W/L Ratio** to 2 decimal places while safely handling zero deaths or losses.
* **Persistent CSV Logging:** Appends each game's stats (`Game`, `Kills`, `Deaths`, `Wins`, `Losses`, `K/D Ratio`, `W/L Ratio`) into `Stats.csv` without overwriting previous sessions.
* **Cross-Platform Compatibility:** Uses `os.path.expanduser` and `os.path.join` to locate any user's `Documents` folder automatically across Windows, macOS, and Linux.
* **Zero External Dependencies:** Built using only Python's standard `os` and `csv` modules.

## 🚀 How to Use

### Option 1: Windows Executable (No Python Required)
1. Go to the **Releases** section on the right side of this page.
2. Download the **`.exe`** file under **Assets**.
3. Double-click the file, enter your game statistics, and open `Documents\Stats.csv` in Excel or any spreadsheet viewer to see your saved history. *(Note: If Windows SmartScreen appears, click **More info → Run anyway**).*

### Option 2: Run via Python (Windows / macOS / Linux)
1. Download the `.py` script from this repository.
2. Run the script in your terminal:
   ```bash
   python Game_Stats_Tracker.py
   ```
