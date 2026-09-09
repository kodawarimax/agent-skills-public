#!/usr/bin/env python3
"""Validate generated prompt artifacts at the trust boundary."""

from pathlib import Path
import re
import sys


SECRET_PATTERNS = (
    re.compile(r"\b(?:sk|ghp|github_pat|xox[baprs])-[-A-Za-z0-9_]{12,}\b", re.I),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:api[_ -]?key|password|token|secret)\s*[:=]\s*[^\s`]{8,}", re.I),
)
INJECTION_PATTERNS = (
    re.compile(r"ignore (?:all )?(?:previous|prior) instructions", re.I),
    re.compile(r"(?:curl|wget)\s+[^\n|]+\|\s*(?:bash|sh)", re.I),
    re.compile(r"(?:run|execute|download and execute) this command", re.I),
)
REQUIRED = ("## Use when", "## Prompt", "## Inputs", "## Output contract", "## Stop conditions", "## Evidence", "## Caveats")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    files = sorted(path.glob("*.md"))
    if not files:
        return [f"no markdown prompts found: {path}"]
    for file in files:
        text = file.read_text(encoding="utf-8")
        missing = [heading for heading in REQUIRED if heading not in text]
        if missing:
            errors.append(f"{file}: missing sections: {', '.join(missing)}")
        if "{{" not in text or "}}" not in text:
            errors.append(f"{file}: no {{variable}} placeholder found")
        if not re.search(r"\[t=\d{2}:\d{2}\]", text):
            errors.append(f"{file}: no timestamp evidence found")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{file}: secret-shaped text detected")
                break
        for pattern in INJECTION_PATTERNS:
            if pattern.search(text):
                errors.append(f"{file}: unsafe instruction pattern detected")
                break
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} PROMPT_DIR", file=sys.stderr)
        return 2
    errors = validate(Path(sys.argv[1]))
    if errors:
        print("prompt validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"prompt validation ok: {len(list(Path(sys.argv[1]).glob('*.md')))} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
