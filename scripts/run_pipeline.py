import argparse
from miracle.design import generate_candidates
from miracle.folding import run_rnaplfold
from miracle.binding import run_rnaup, run_rnacofold
from miracle.scoring import score_candidate

def read_fasta(file):
    with open(file) as f:
        return "".join([l.strip() for l in f if not l.startswith(">")])


def main():

    parser = argparse.ArgumentParser(
        description="MIRACLE: IRES-TNA design pipeline"
    )

    parser.add_argument("-i", "--input", required=True,
                        help="IRES sequence (FASTA)")
    parser.add_argument("-o", "--output", default="results.csv")

    args = parser.parse_args()

    seq = read_fasta(args.input)

    print("[1] Calculating accessibility...")
    accessibility = run_rnaplfold(seq)

    print("[2] Generating TNA candidates...")
    candidates = generate_candidates(seq, length=10)

    results = []

    print("[3] Scoring...")

    for pos, region, tna in candidates:

        acc = sum(accessibility[pos:pos+len(region)]) / len(region)

        dg_bind = run_rnaup(region, tna)
        dg_cofold = run_rnacofold(region, tna)

        score = score_candidate(dg_bind, dg_cofold, acc)

        results.append([
            pos, region, tna, dg_bind, dg_cofold, acc, score
        ])

    # 排序
    results.sort(key=lambda x: x[-1], reverse=True)

    print("\nTop 20 candidates:\n")

    for r in results[:20]:
        print(r)

    # 保存
    import csv
    with open(args.output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "position", "target", "TNA",
            "ΔG_binding", "ΔG_cofold",
            "accessibility", "score"
        ])
        writer.writerows(results[:20])


if __name__ == "__main__":
    main()