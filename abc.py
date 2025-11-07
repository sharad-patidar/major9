import sys
from collections import Counter

# Simple LCS (Longest Common Subsequence) implementation
def lcs_length(a, b):
    n, m = len(a), len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def main():
    try:
        lines = sys.stdin.read().splitlines()
        if not lines:
            print("Impossible")
            return

        N = int(lines[0].strip())
        original_parts = lines[1].split()
        original_str = "".join(original_parts)

        # Convert 1-based fixed indices to 0-based
        fixed_positions = []
        if len(lines) > 2 and lines[2].strip():
            fixed_positions = [int(x) - 1 for x in lines[2].split()]

        # Count occurrences of each character
        freq = Counter(original_str)

        # Try all 6 permutations of A, B, C
        possible_orders = [
            ('A', 'B', 'C'),
            ('A', 'C', 'B'),
            ('B', 'A', 'C'),
            ('B', 'C', 'A'),
            ('C', 'A', 'B'),
            ('C', 'B', 'A')
        ]

        smallest_shift = float('inf')
        found_valid = False

        for perm in possible_orders:
            target = ""
            for ch in perm:
                target += ch * freq[ch]

            # Check if fixed positions match
            valid = True
            for pos in fixed_positions:
                if original_str[pos] != target[pos]:
                    valid = False
                    break

            if not valid:
                continue

            found_valid = True
            lcs_val = lcs_length(original_str, target)
            shifts_needed = N - lcs_val

            if shifts_needed < smallest_shift:
                smallest_shift = shifts_needed

        if not found_valid:
            print("Impossible")
        else:
            print(smallest_shift)

    except Exception:
        print("Impossible")


if __name__ == "__main__":
    main()