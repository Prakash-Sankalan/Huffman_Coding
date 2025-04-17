# 🌲 Generalized Huffman Coding (n-ary Huffman Encoder/Decoder)

This project implements a **generalized Huffman coding algorithm** that supports **n-ary** encodings (binary, ternary, etc.). It allows users to input symbol probabilities and generate efficient prefix-free codes. The program also calculates entropy, average code length, and coding efficiency.

---

## 📌 Features

- ✅ Supports **custom symbol sets** and **probability inputs**
- ✅ Works for any **alphabet size ≥ 2** (binary, ternary, quaternary, etc.)
- ✅ Calculates:
  - Huffman codes for each symbol
  - Encoded binary/ternary/n-ary string
  - Decoded text from encoded string
  - Entropy (H), average code length (R), and coding efficiency (H/R)

---

## 🛠️ How to Use

1. Clone the repo and run the script:
    ```bash
    python huffman.py
    ```

2. Follow the prompts:
    - Enter number of symbols
    - Define each symbol and its probability
    - Choose the alphabet size (e.g., 2 for binary, 3 for ternary)
    - Enter a text using those symbols

3. View the output:
    - Huffman codes per symbol
    - Encoded and decoded text
    - Entropy (H), average code length (R), efficiency

---

## 📈 Sample Output

=== Huffman Coding Program === Enter number of symbols: 3 Enter symbol character (e.g., A, B, etc.): A Enter probability for A (0-1): 0.5 Enter symbol character (e.g., A, B, etc.): B Enter probability for B (0-1): 0.3 Enter symbol character (e.g., A, B, etc.): C Enter probability for C (0-1): 0.2 Enter alphabet size (2 for binary, 3 for ternary, etc.): 2 Enter text to encode (use defined symbols): ABAC

Results: Symbol Codes: {'A': '0', 'B': '10', 'C': '11'} Encoded Text: 0100110 Decoded Text: ABAC Entropy (H): 1.4855 Average Code Length (R): 1.5000 Coding Efficiency (H/R): 99.03%
