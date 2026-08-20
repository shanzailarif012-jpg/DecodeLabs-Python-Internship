# Project 2: Expense Tracker

## 📌 Overview
A console-based Python application that tracks user expenses in real-time using the Accumulator Pattern. Users can continuously enter expense amounts, and the program maintains a running total until the user chooses to exit.

## 🎯 Objective
- Understand data accumulation and state management in Python
- Master type casting (`int()`) for safe numerical operations
- Implement defensive coding using `try/except` error handling
- Build a stable, continuously running program using `while True` loops

## ⚙️ Features
- Continuous expense entry via a `while True` loop
- Accumulator pattern (`total = total + expense`) to maintain a running total
- Sentinel value (`quit`) to gracefully exit the program (case-insensitive)
- Error handling for invalid inputs (e.g., letters instead of numbers) using `try/except ValueError`
- Displays the final total once the session ends

## 🧠 Key Concepts Used
- **Accumulator Pattern** — building state incrementally (`total += expense`)
- **Type Casting** — converting string input to integer using `int()`
- **Sentinel Values** — using a special input (`quit`) to break a loop
- **Exception Handling** — catching `ValueError` to prevent crashes on invalid input
- **State Management** — initializing `total` outside the loop to preserve its value across iterations

## 🖥️ How to Run
```bash
python Expense_Tracker_main.py
```

## 📝 Sample Run