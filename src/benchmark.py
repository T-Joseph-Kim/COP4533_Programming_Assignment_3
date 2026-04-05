import os
import sys
import time

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

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

    print("File\t\t|A|\t|B|\t|A|*|B|\tValue\tTime (s)")
    print("----\t\t---\t---\t-------\t-----\t--------")

    labels = []
    sizes = []
    times = []

    for filepath in test_files:
        char_values, a, b = parse_input(filepath)

        start = time.perf_counter()
        dp = build_dp_table(char_values, a, b)
        reconstruct(dp, char_values, a, b)
        end = time.perf_counter()

        elapsed = end - start
        max_val = dp[len(a)][len(b)]
        filename = os.path.basename(filepath)
        table_size = len(a) * len(b)

        print(filename + "\t" + str(len(a)) + "\t" + str(len(b)) + "\t" +
              str(table_size) + "\t" + str(max_val) + "\t" + str(round(elapsed, 6)))

        labels.append(filename.replace('.in', ''))
        sizes.append(table_size)
        times.append(elapsed)

    if HAS_MATPLOTLIB:
        graph_path = os.path.join(data_dir, 'runtime_graph.png')
        _plot_runtime(labels, times, graph_path)
        print("\nRuntime graph saved to: " + graph_path)
    else:
        print("\nmatplotlib not installed — skipping graph generation")
        print("Install with: pip install matplotlib")

def _plot_runtime(labels, times, output_path):
    times_ms = [t * 1000 for t in times]
    x = list(range(len(labels)))

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(x, times_ms, color='steelblue', edgecolor='black', linewidth=0.7)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
    ax.set_xlabel('Input File')
    ax.set_ylabel('Runtime (ms)')
    ax.set_title('HVLCS Solver — Empirical Runtime Comparison')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    for bar, t in zip(bars, times_ms):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(times_ms) * 0.01,
                f'{t:.3f}', ha='center', va='bottom', fontsize=7)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

if __name__ == '__main__':
    run_benchmark()
