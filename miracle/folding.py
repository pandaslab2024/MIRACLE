import subprocess
import tempfile
import os


def run_cmd(cmd, input_text=None):
    result = subprocess.run(
        cmd,
        input=input_text,
        text=True,
        capture_output=True
    )
    return result.stdout


def run_rnaplfold(seq, window=80, span=40):
    accessibility = []

    with tempfile.TemporaryDirectory() as tmp:
        old = os.getcwd()
        os.chdir(tmp)

        # 运行 RNAplfold
        run_cmd([
            "RNAplfold",
            "-W", str(window),
            "-L", str(span),
            "-u", "10"
        ], seq)

        try:
            with open("plfold_lunp") as f:
                next(f)  # 跳过表头
                for line in f:
                    vals = line.strip().split()
                    if len(vals) < 2:
                        continue  # 跳过空行
                    try:
                        val = float(vals[1])
                        accessibility.append(val)
                    except ValueError:
                        # 遇到非数字行（如 l=1）就跳过
                        continue
        finally:
            os.chdir(old)

    return accessibility