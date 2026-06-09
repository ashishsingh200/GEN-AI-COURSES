# Assignment 8 — Streamlit Web Applications

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)

## Overview

All tasks in Assignment 8 have been successfully completed. This assignment covered building interactive web applications using Streamlit — including text inputs, sliders, number inputs, selectboxes, sidebars, metrics, tables, and bar charts.

---

## Installation

```bash
pip install streamlit
```

## Running any app

```bash
streamlit run app_basic.py
streamlit run app_discount.py
streamlit run app_product_form.py
streamlit run app_dashboard.py
```

Each app opens automatically at `http://localhost:8501`

---

## Tasks Completed

### Task 1 — Basic Streamlit App (`app_basic.py`)
- Displays a title using `st.title()`
- Takes user's name as input using `st.text_input()` with a placeholder
- On clicking the **"Greet Me"** button, displays a personalized greeting
- Demonstrates basic input and button interaction in Streamlit

**Key widgets used:**
`st.title()`, `st.text_input()`, `st.button()`, `st.write()`

---

### Task 2 — Price Discount Calculator (`app_discount.py`)
- Displays a title using `st.title()`
- Takes product price as input using `st.number_input()`
- Uses `st.slider()` to select discount percentage (0% to 50%)
- Calculates discounted price dynamically
- On clicking **"Submit"**, displays the final price after discount
- Shows a before/after price comparison using `st.table()`

**Key widgets used:**
`st.number_input()`, `st.slider()`, `st.button()`, `st.table()`, `st.subheader()`

---

### Task 3 — Product Form with Sidebar (`app_product_form.py`)
- Displays a title using `st.title()`
- Entire form placed in the **sidebar** using `st.sidebar`
- Sidebar contains:
  - `st.sidebar.text_input()` — product name
  - `st.sidebar.selectbox()` — category (Stationery, Dairy, Electrical, Textiles)
  - `st.sidebar.number_input()` — price
  - `st.sidebar.button()` — Add Product button
- On clicking **"Add Product"**, displays product details in the main area

**Key widgets used:**
`st.sidebar.header()`, `st.sidebar.text_input()`, `st.sidebar.selectbox()`, `st.sidebar.number_input()`, `st.sidebar.button()`

---

### Task 4 — Simple Sales Dashboard (`app_dashboard.py`)
- Displays a title using `st.title()`
- Month selector using `st.selectbox()` with `index=None` (no default selection)
- Sales data stored as a dictionary `{'January': 1200, 'February': 1500, ...}`
- When a month is selected, displays its sales using `st.metric()`
- Divider added using `st.divider()`
- Monthly sales overview shown as a **bar chart** using `st.bar_chart()`

**Key widgets used:**
`st.selectbox()`, `st.metric()`, `st.divider()`, `st.bar_chart()`, `st.subheader()`

---

## Streamlit Concepts Covered

| Concept | Used in |
|---|---|
| `st.title()` | All apps |
| `st.write()` | Task 1, Task 2, Task 3 |
| `st.text_input()` | Task 1, Task 3 |
| `st.button()` | Task 1, Task 2 |
| `st.number_input()` | Task 2, Task 3 |
| `st.slider()` | Task 2 |
| `st.table()` | Task 2 |
| `st.sidebar` | Task 3 |
| `st.selectbox()` | Task 3, Task 4 |
| `st.metric()` | Task 4 |
| `st.bar_chart()` | Task 4 |
| `st.divider()` | Task 4 |
| `st.subheader()` | Task 2, Task 3, Task 4 |

---

## File Structure

```
GEN AI Assignment-8(Ashish)/
│
├── README.md
├── app_basic.py
├── app_discount.py
├── app_product_form.py
├── app_dashboard.py
│
└── images/
    ├── Screenshot 2026-06-08 at 1.44.29 PM.png
    ├── Screenshot 2026-06-08 at 1.44.36 PM.png
    ├── Screenshot 2026-06-08 at 1.44.41 PM.png
    └── Screenshot 2026-06-08 at 1.44.49 PM.png
```

---

## App Screenshots

| App | Screenshot |
|---|---|
| Basic App | `images/Screenshot 2026-06-08 at 1.44.29 PM.png` |
| Discount Calculator | `images/Screenshot 2026-06-08 at 1.44.36 PM.png` |
| Product Form | `images/Screenshot 2026-06-08 at 1.44.41 PM.png` |
| Sales Dashboard | `images/Screenshot 2026-06-08 at 1.44.49 PM.png` |

---

## Notes

- No external libraries used beyond `streamlit`
- All apps run independently — each is a separate `.py` file
- Sidebar used in Task 3 to separate form from main content
- Dynamic calculations in Task 2 update in real time as slider moves
- `index=None` in Task 4 selectbox ensures no default month is pre-selected

---

*Assignment 8 — Completed Successfully*
