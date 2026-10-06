#!/usr/bin/env python3
"""Export the canonical family atlas from qca-causal-cones into canonical_atlas/.

Usage (from the root of atlas-qca-students):

    python3 tools/export_canonical_atlas.py <path-to-qca-causal-cones> <commit>

Files are read with `git show <commit>:<path>`, so the copy is tied to one
commit. Relative links that point to files also copied here are kept. Links to
student-edition chapters are redirected to the copies at the repository root.
Every other relative link points into the private research repository; it is
replaced by its plain text so that the public page has no 404 links.
"""

import os
import re
import subprocess
import sys

SRC_DIR = "docs/family_atlas"
OUT_DIR = "canonical_atlas"
FILES = ["FAMILY_BIBLE.md", "RELATIONS.md", "relations.csv"]
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
NOTE = (
    "> Copia publicada del atlas canónico de `qca-causal-cones` "
    "(commit `{commit}`). Las referencias a informes, teoría, scripts, debates "
    "y estado del repositorio de investigación, que es privado, aparecen como "
    "texto sin enlace.\n\n"
)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], check=True, capture_output=True, text=True
    ).stdout


def rewrite(text, rel, copied):
    here = os.path.dirname(os.path.join(SRC_DIR, rel))

    def sub(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, frag = target.partition("#")
        resolved = os.path.normpath(os.path.join(here, path))
        inner = os.path.relpath(resolved, SRC_DIR)
        if inner in copied:
            return m.group(0)
        if inner.startswith("student_edition/"):
            dest = os.path.join("..", inner[len("student_edition/"):])
            new = os.path.relpath(dest, os.path.dirname(rel) or ".")
            return f"[{label}]({new}{'#' + frag if frag else ''})"
        return label

    return LINK.sub(sub, text)


def main():
    repo, commit = sys.argv[1], sys.argv[2]
    commit = git(repo, "rev-parse", commit).strip()
    families = [
        os.path.relpath(p, SRC_DIR)
        for p in git(repo, "ls-tree", "--name-only", commit, f"{SRC_DIR}/families/").split()
    ]
    copied = set(FILES + families)
    for rel in sorted(copied):
        text = git(repo, "show", f"{commit}:{SRC_DIR}/{rel}")
        if rel.endswith(".md"):
            text = rewrite(text, rel, copied)
            title, sep, rest = text.partition("\n\n")
            text = title + sep + NOTE.format(commit=commit[:7]) + rest
        out = os.path.join(OUT_DIR, rel)
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"exported {len(copied)} files from {commit}")


if __name__ == "__main__":
    main()
