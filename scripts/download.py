import argparse
import os
import subprocess
from datetime import datetime

SESSION_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../SESSION"))


def parse():
    parser = argparse.ArgumentParser()
    today = datetime.today()
    parser.add_argument("--year", type=int, default=today.year)
    parser.add_argument("--day", type=int, default=today.day)
    return parser.parse_args()


def get_session():
    with open(SESSION_PATH) as f:
        return f.read()


def main():
    args = parse()
    session = get_session()
    out_path = os.path.join(os.path.dirname(__file__), "..", str(args.year), "input", str(args.day).rjust(2, "0"))

    cmd = f"curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie 'session={session}' --http1.1"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")

    with open(out_path, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
