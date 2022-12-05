import re
import os
from os.path import join

LANG = {"python": "py", "rust": "rs", "typescript": "ts", "c-sharp": "cs", "ruby": "rb"}
BASE_DIRS = sorted([f for f in os.listdir(".") if f.isnumeric()], reverse=True)
BASE_URL = "https://github.com/Zonotora/adventofcode/blob/main/"

s = "# adventofcode\n"
for year in BASE_DIRS:
    s += f"\n## {year}\n\n"
    s += "| |"
    for key in LANG:
        s += f" {LANG[key]} |"
    s += "\n|"
    for _ in range(len(LANG) + 1):
        s += " - |"
    s += "\n"

    for day in range(1, 26):
        day = f"{day}".rjust(2, "0")
        s_day = ""
        for key in LANG:
            path = join(year, key)
            if os.path.exists(path):
                files = [f for f in os.listdir(path) if re.match(r".*\d.*", f) and "swp" not in f and "test" not in f]
                f_exists = False
                for f in files:
                    if day in f:
                        s_day += f" [✓][{year}-{key}-{day}] |"
                        f_exists = True
                        break
                if not f_exists:
                    s_day += f" |"
            else:
                s_day += f" |"
        if year in s_day:
            s += f"| {day} |{s_day}\n"
    s += "\n"

    lang = sorted([f for f in os.listdir(year) if f in LANG])
    for key in LANG:
        path = join(year, key)
        if os.path.exists(path):
            day = sorted(
                [f for f in os.listdir(path) if re.match(r".*\d.*", f) and "swp" not in f and "test" not in f]
            )
            for d in day:
                url = join(BASE_URL, year, key, d)
                d_tag = re.findall(r"\d+", d)[0]
                s += f"[{year}-{key}-{d_tag}]: {url}\n"
print(s)
