"""Check this documentation repository using only the Python standard library."""

from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]+\]\((<[^>\n]+>|[^\s)]+)\)")


def main():
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode("utf-8").split("\0")
    tracked_paths = {Path(name).as_posix() for name in tracked if name}
    errors = []
    document_count = 0
    for name in sorted(tracked_paths):
        path = ROOT / name
        lower_name = path.name.lower()
        if (
            (lower_name == ".env" or lower_name.startswith(".env."))
            and lower_name != ".env.example"
        ) or path.suffix.lower() in {".pem", ".key"} or any(
            part in {"private", ".local"} for part in path.relative_to(ROOT).parts
        ):
            errors.append(f"{name}: private configuration or key filename is tracked")
        if path.suffix.lower() != ".md":
            continue
        document_count += 1
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), 1):
            if line != line.rstrip():
                errors.append(f"{name}:{number}: trailing whitespace")
            if re.match(r"^(<{7}|={7}|>{7})(?:\s|$)", line):
                errors.append(f"{name}:{number}: unresolved conflict marker")
        for match in LINK.finditer(text):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{name}: local link leaves repository: {target}")
            elif resolved.relative_to(ROOT).as_posix() not in tracked_paths:
                errors.append(f"{name}: local link is not a tracked file: {target}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {document_count} Markdown files; local file links and file hygiene")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
