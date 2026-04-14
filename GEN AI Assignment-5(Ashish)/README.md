# Assignment 5 — Modules & Packages in Python

## Overview

All tasks in Assignment 5 have been successfully completed. This assignment covered creating and importing Python modules, building custom utility modules, and structuring code into packages using `__init__.py`.

---

## Tasks Completed

### Task 1 — Math Utilities Module (`Math_utils.py`)
- Created a custom module `Math_utils.py` with the following functions:
  - `add(a, b)` — returns sum of two numbers
  - `subtract(a, b)` — returns difference of two numbers
  - `square(a)` — returns square of a number
- Imported module in `main.py` using:
  - `import Math_utils as m` — for `add()` and `subtract()`
  - `from Math_utils import square` — for direct import

### Task 2 — String Utilities Module (`String_utils.py`)
- Created a custom module `String_utils.py` with the following functions:
  - `capitalize_words(s)` — capitalizes every word using `.title()`
  - `reverse_string(s)` — reverses the string using slicing `[::-1]`
  - `word_count(s)` — counts words using `.split()`
- Imported module in `main.py` using `import String_utils as word`

### Task 3 — Shop Package (`shop_package/`)
- Created a package `shop_package` with the following files:
  - `__init__.py` — exposes `apply_discount`, `flat_discount`, `calculate_total`, `apply_tax`
  - `discount.py` — contains `apply_discount(price, percent)` and `flat_discount(price)`
  - `billing.py` — contains `calculate_total(prices)` and `apply_tax(amount)`

### Task 4 — Importing from Package (`main.py`)
- Imported and used functions from `shop_package` in `main.py`:
  - `import shop_package.discount as disc`
  - `from shop_package.billing import calculate_total`
  - `from shop_package.discount import flat_discount`
  - `from shop_package.billing import apply_tax`
- Tested `disc.apply_discount(1000, 10)` and `calculate_total([100, 200, 300])`

---

## Concepts Covered

| Concept | Used in |
|---|---|
| Creating a module | Task 1, Task 2 |
| Importing a module (`import as`) | Task 1, Task 2 |
| Importing specific function (`from module import`) | Task 1, Task 4 |
| Creating a package | Task 3 |
| `__init__.py` | Task 3 |
| Importing from a package | Task 4 |
| Nested imports (`from package.module import`) | Task 4 |

---

## File Structure

```
GEN AI Assignment-5(Ashish)/
│
├── README.md
├── main.py
├── Math_utils.py
├── String_utils.py
│
├── shop_package/
│   ├── __init__.py
│   ├── discount.py
│   └── billing.py
│
└── images/
    ├── task1.png
    ├── task2.png
    ├── task3.png
    └── task4.png
```

---

## Functions Summary

### `Math_utils.py`
| Function | Description |
|---|---|
| `add(a, b)` | returns `a + b` |
| `subtract(a, b)` | returns `a - b` |
| `square(a)` | returns `a ** 2` |

### `String_utils.py`
| Function | Description |
|---|---|
| `capitalize_words(s)` | capitalizes every word |
| `reverse_string(s)` | reverses the string |
| `word_count(s)` | counts total words |

### `shop_package/discount.py`
| Function | Description |
|---|---|
| `apply_discount(price, percent)` | applies percentage discount |
| `flat_discount(price)` | subtracts flat ₹50 discount |

### `shop_package/billing.py`
| Function | Description |
|---|---|
| `calculate_total(prices)` | returns sum of all prices |
| `apply_tax(amount)` | applies 5% tax on amount |

---

## Notes

- No external libraries used — only built-in Python
- All modules and packages created from scratch
- `__init__.py` used to expose functions directly from the package
- `main.py` is the entry point that imports and tests all modules and packages

---

*Assignment 5 — Completed Successfully*