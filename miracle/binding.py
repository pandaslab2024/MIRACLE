import subprocess


def run_cmd(cmd, input_text=None):
    result = subprocess.run(
        cmd,
        input=input_text,
        text=True,
        capture_output=True
    )
    return result.stdout


def run_rnaup(target, tna):
    input_text = f"{target}\n{tna}"
    out = run_cmd(["RNAup"], input_text)

    try:
        line = [l for l in out.split("\n") if "(" in l][0]
        dg = float(line.split("(")[-1].replace(")", ""))
    except:
        dg = 0

    return dg


def run_rnacofold(seq1, seq2):
    out = run_cmd(["RNAcofold"], f"{seq1}&{seq2}")

    try:
        dg = float(out.split("\n")[1].split()[-1].replace("(", "").replace(")", ""))
    except:
        dg = 0

    return dg