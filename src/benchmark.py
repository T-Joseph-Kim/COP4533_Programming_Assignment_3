import os
import sys
import time

# so we can import from the same folder
sys.path.insert(0, os.path.dirname(__file__))
from hvlcs import parse_input, build_dp_table, reconstruct

def run_benchmark():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

    # get all test input files
    test_files = []
    for f in sorted(os.listdir(data_dir)):
        if f.startswith('test') and f.endswith('.in'):
            test_files.append(os.path.join(data_dir, f))

    if len(test_files) == 0:
        print("No test files found in data/")
        sys.exit(1)

    print("File\t\t|A|\t|B|\tValue\tTime (s)")
    print("----\t\t---\t---\t-----\t--------")

    for filepath in test_files:
        char_values, a, b = parse_input(filepath)

        start = time.time()
        dp = build_dp_table(char_values, a, b)
        subseq = reconstruct(dp, char_values, a, b)
        end = time.time()

        elapsed = end - start
        max_val = dp[len(a)][len(b)]
        filename = os.path.basename(filepath)

        print(filename + "\t" + str(len(a)) + "\t" + str(len(b)) + "\t" + str(max_val) + "\t" + str(round(elapsed, 6)))

if __name__ == '__main__':
    run_benchmark()
