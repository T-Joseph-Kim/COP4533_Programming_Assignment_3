import sys

def parse_input(filepath):
    """Read the input file and return char values, string A, and string B."""
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')

    k = int(lines[0])

    # read character values
    char_values = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        char_values[parts[0]] = int(parts[1])

    string_a = lines[k + 1]
    string_b = lines[k + 2]

    return char_values, string_a, string_b

def build_dp_table(char_values, a, b):
    """Build the DP table where dp[i][j] is the max value common subsequence of a[0..i-1] and b[0..j-1]."""
    m = len(a)
    n = len(b)

    # initialize table with zeros
    dp = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        dp.append(row)

    # fill in the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                # characters match, add the value of this character
                dp[i][j] = dp[i-1][j-1] + char_values.get(a[i-1], 0)
            else:
                # take the better of skipping a char from either string
                if dp[i-1][j] >= dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    return dp

def main():
    if len(sys.argv) < 2:
        print("Usage: python hvlcs.py <input_file>")
        sys.exit(1)

    char_values, a, b = parse_input(sys.argv[1])
    dp = build_dp_table(char_values, a, b)

    # print the max value
    print(dp[len(a)][len(b)])

if __name__ == '__main__':
    main()
