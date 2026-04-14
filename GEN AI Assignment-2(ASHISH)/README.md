# Assignment 2 — Conditionals, Loops & Loop Control

## Overview

All tasks in Assignment 2 have been successfully completed. This assignment covered conditionals (`if/elif/else`), loops (`for`, `while`), and loop control statements (`break`, `continue`).

---

## Tasks Completed

### Task 1 — Discount Rules (if / elif / else)
- Read `order_amount` from user using `input()`
- Handled non-numeric input using `.isdigit()` before converting to `int`
- Applied discount rules:
  - `>= 2000` → 15% discount
  - `1500 <= amount < 2000` → 10% discount
  - `1000 <= amount < 1500` → 7% discount
  - otherwise → 0% discount
- **Extra:** Added 5% tax after discount and printed subtotal, tax, and final total

### Task 2 — Process Multiple Orders (for loop)
- Given `orders = [1200, 2500, 800, 1750, 3000]`
- Used a `for` loop to apply discount rules from Task 1 to each order
- Printed a summary table: `order_amount → discount% → final_amount`
- Computed and printed total revenue after discounts
- **Extra:** Counted and printed number of orders that received a discount

### Task 3 — User Menu (while loop + break / continue)
- Implemented a while-loop driven interactive menu
- Menu options:
  - `1` — Add order amount to a running list
  - `2` — Show all orders and totals after applying discounts
  - `q` — Quit
- Used `continue` to re-show menu after invalid input
- Used `break` to exit on `q`
- Validated order amount input using `.isdigit()`

### Task 4 — Loop Control with Conditions (break & continue)
- Given `daily = [200, 150, 0, 400, 50, -1, 300]`
- Used a `for` loop with:
  - `break` when `-1` is found (corrupted data — stop processing)
  - `continue` when `0` is found (no sales day — skip adding)
  - Added valid positive sales to `total_sales` and printed running total
- Printed final total after loop completes or stops early

---

# Concepts Covered

| Concept | Used in |
| `if / elif / else` | Task 1, Task 2, Task 3, Task 4 |
| `for` loop | Task 2, Task 4 |
| `while` loop | Task 3 |
| `break` | Task 3, Task 4 |
| `continue` | Task 3, Task 4 |
| Running totals | Task 2, Task 3, Task 4 |
| f-strings | Task 1, Task 2, Task 3, Task 4 |
# Notes

- No external libraries used — only built-in Python
- Discount logic is consistent across all tasks
- Input validation handled before type conversion to avoid crashes
- `break` and `continue` used as required by each task

-------------------------------------- 
# Assignment 2 completed Successfully
--------------------------------------