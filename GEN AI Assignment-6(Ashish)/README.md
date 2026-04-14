# Python Exception Handling Lab - Tasks Overview

This repository contains a series of Python tasks focused on robust programming using **Exception Handling**. Each task demonstrates how to handle specific runtime errors and logical edge cases to ensure the program continues running or terminates gracefully.

## 🛠 Project Structure

The project is organized into five core tasks, covering various real-world scenarios:

### Task 1: Basic Arithmetic & Flow Control
- **Description**: A numerator/denominator calculator.
- **Concepts**: `try`, `except`, `else`, and `finally`.
- **Handling**: 
  - `ZeroDivisionError`: When the denominator is zero.
  - `ValueError`: When user input is not an integer.
  - `finally`: Ensures "Operation Complete" prints regardless of success or failure.

### Task 2: Bill Calculator with Data Validation
- **Description**: Iterates through a list of product prices containing "dirty" data (strings and negative values).
- **Handling**:
  - `TypeError`: Raised and caught when an item is not a number.
  - `ValueError`: Custom raised exception for negative prices.
  - **Behavior**: Skips invalid items but continues calculating the total for valid entries.

### Task 3: Custom Age Validator
- **Description**: A function-based approach to validate age inputs.
- **Handling**:
  - Logic checks to ensure age is between 1 and 120.
  - Raises a `ValueError` with a descriptive message if the input falls outside the range.

### Task 4: File I/O Management
- **Description**: Reads exactly the first three lines of a user-specified text file.
- **Handling**:
  - `FileNotFoundError`: If the file name provided does not exist.
  - `PermissionError`: If the file is locked or restricted.
  - **Logic**: Uses a loop to read one line at a time to remain memory-efficient.

### Task 5: Interactive Shopping Cart
- **Description**: A continuous loop that accepts item prices until the user enters 'q'.
- **Handling**:
  - `ValueError`: Handles non-numeric inputs and prevents negative values from being added to the cart.
  - **Summary**: Displays the total count of valid items and the final bill amount.

---

## 🚀 How to Run
1. Open the `Task1.ipynb` notebook in VS Code, Jupyter, or Google Colab.
2. Run each cell sequentially to see how different inputs trigger specific error handlers.

## 📚 Course Context
This lab is part of a course on **Generative AI**, focusing on data cleaning and robust Python scripting for data preprocessing.