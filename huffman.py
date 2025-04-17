from math import log

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.children = []

class HuffmanCoding:
    def __init__(self, probabilities, alphabet_size=2):
        self.probabilities = probabilities
        self.codes = {}
        self.root = None
        self.alphabet_size = alphabet_size

    def build_tree(self):
        nodes = [Node(char, freq) for char, freq in self.probabilities.items()]

        # Add dummy nodes if needed to satisfy (n-1) condition for n-ary tree
        while (len(nodes) - 1) % (self.alphabet_size - 1) != 0:
            nodes.append(Node(None, 0))

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            children = nodes[:self.alphabet_size]
            parent = Node(None, sum(child.freq for child in children))
            parent.children = children
            nodes = nodes[self.alphabet_size:] + [parent]

        self.root = nodes[0]

    def generate_codes(self, node=None, current_code=""):
        if node is None:
            node = self.root

        if node.char is not None:
            self.codes[node.char] = current_code
            return

        for i, child in enumerate(node.children):
            self.generate_codes(child, current_code + str(i))

    def encode(self, text):
        return ''.join(self.codes[char] for char in text)

    def decode(self, encoded_text):
        decoded = []
        node = self.root
        for digit in encoded_text:
            node = node.children[int(digit)]
            if node.char is not None:
                decoded.append(node.char)
                node = self.root
        return ''.join(decoded)

    def calculate_efficiency(self):
        # Entropy H (with log base alphabet_size)
        H = -sum(prob * log(prob, self.alphabet_size) for prob in self.probabilities.values())

        # Average code length R
        R = sum(self.probabilities[char] * len(code) for char, code in self.codes.items())

        # Coding Efficiency (H / R * 100)
        efficiency = (H / R) * 100

        return efficiency, H, R


def get_user_input():
    symbols = {}
    n = int(input("Enter number of symbols: "))

    for _ in range(n):
        while True:
            char = input("Enter symbol character (e.g., A, B, etc.): ").strip().upper()
            if char in symbols:
                print("Error: Symbol already exists!")
                continue
            break

        while True:
            try:
                prob = float(input(f"Enter probability for {char} (0-1): "))
                if prob <= 0 or prob > 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid probability! Must be between 0 and 1.")

        symbols[char] = prob

    # Verify probabilities sum to 1
    total = sum(symbols.values())
    if abs(total - 1) > 1e-9:
        print(f"Warning: Probabilities sum to {total:.2f}. Normalizing to 1.")
        for char in symbols:
            symbols[char] /= total

    # Get alphabet size
    while True:
        try:
            alphabet_size = int(input("Enter alphabet size (2 for binary, 3 for ternary, etc.): "))
            if alphabet_size < 2:
                raise ValueError
            break
        except ValueError:
            print("Invalid! Must be integer ≥ 2.")

    # Get text to encode
    while True:
        text = input("Enter text to encode (use defined symbols): ").upper()
        if all(c in symbols for c in text):
            break
        print("Error: Text contains undefined symbols5!")

    return symbols, alphabet_size, text


def main():
    print("=== Huffman Coding Program ===")
    probabilities, alphabet_size, text = get_user_input()

    hc = HuffmanCoding(probabilities, alphabet_size)
    hc.build_tree()
    hc.generate_codes()

    encoded = hc.encode(text)
    decoded = hc.decode(encoded)
    efficiency, entropy, avg_code_length = hc.calculate_efficiency()

    print("\nResults:")
    print(f"Symbol Codes: {hc.codes}")
    print(f"Encoded Text: {encoded}")
    print(f"Decoded Text: {decoded}")
    print(f"Entropy (H): {entropy:.4f}")
    print(f"Average Code Length (R): {avg_code_length:.4f}")
    print(f"Coding Efficiency (H/R): {efficiency:.2f}%")

if __name__ == "__main__":
    main()
