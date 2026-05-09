# wordcount_simulation.py – Python MapReduce simulation for word frequency
import sys
from collections import defaultdict

# Mapper
def mapper(lines):
    """Map: for each word emit (word, 1)"""
    pairs = []
    for line in lines:
        for word in line.strip().split():
            pairs.append((word.lower(), 1))
    return pairs

# Reducer
def reducer(mapped_pairs):
    """Reduce: sum counts per word"""
    counts = defaultdict(int)
    for word, count in mapped_pairs:
        counts[word] += count
    return counts

if __name__ == "__main__":
    # Read input from file specified as argument, or from a hardcoded test
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
    else:
        # Fallback test string
        lines = ["Hello world Hello Hadoop", "world Hadoop"]
    mapped = mapper(lines)
    result = reducer(mapped)
    for word, freq in sorted(result.items()):
        print(f"{word}\t{freq}")