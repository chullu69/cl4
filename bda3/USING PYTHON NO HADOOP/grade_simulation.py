"""
Assignment 3: MapReduce Simulation for Student Grades
Input file: Each line "student_id,score"
Example:
S1,85
S1,90
S2,78
"""
import sys
from collections import defaultdict

def mapp(lines):
    """Map: emit (student_id, score)"""
    mapped = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            student_id = parts[0].strip()
            try:
                score = float(parts[1].strip())
                mapped.append((student_id, score))
            except ValueError:
                pass
    return mapped

def redu(mapped_pairs):
    """Reduce: calculate average and assign grade"""
    # Group by student_id
    groups = defaultdict(list)
    for sid, sc in mapped_pairs:
        groups[sid].append(sc)

    grades = {}
    for sid, scores in groups.items():
        avg = sum(scores) / len(scores)
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[sid] = (avg, grade)
    return grades

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            data = f.readlines()
    else:
        # default test data
        data = ["S1,85\n", "S1,90\n", "S2,78\n", "S3,45\n", "S2,82\n"]

    mapped = mapp(data)
    results = redu(mapped)
    for sid in sorted(results.keys()):
        avg, grade = results[sid]
        print(f"{sid}\t{avg:.2f}\t{grade}")