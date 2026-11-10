"""Small offline checker for this repository's inline Markdown links."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(root):
    issues = []
    files = sorted(p for p in root.rglob("*.md") if ".git" not in p.relative_to(root).parts)
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        private_patterns = (
            r"/home/[^\s/]+/",
            r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])",
            r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
            r"\b[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}\b",
            r"-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----",
        )
        if any(re.search(pattern, text) for pattern in private_patterns):
            issues.append((relative, "privacy-marker"))
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            if not (path.parent / unquote(url.path)).is_file():
                issues.append((relative, "missing-local-link"))
    return files, issues


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    files, issues = check(root)
    for relative, code in issues:
        print(f"{relative}: {code}")
    print(f"Markdown files: {len(files)}; findings: {len(issues)}")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
