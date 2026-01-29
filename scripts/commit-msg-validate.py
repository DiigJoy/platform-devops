#!/usr/bin/env python3
import re
import sys


ALLOWED_TYPES = {
    "feat",
    "fix",
    "chore",
    "docs",
    "perf",
    "refactor",
    "test",
    "build",
    "ci",
    "style",
    "revert",
}

ALLOWED_SCOPES = {
    "platform",
    "iot-agri",
    "iot-animal",
    "microbiz",
    "infra",
    "docs",
    "ci",
}

HEADER_RE = re.compile(
    r"^(?P<type>[a-z]+)"
    r"\((?P<scope>[^)]+)\)"
    r"(?P<breaking>!)?"
    r": "
    r"(?P<summary>.+)$"
)


def _first_subject_line(message: str) -> str:
    for line in message.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped
    return ""


def main() -> int:
    if len(sys.argv) != 2:
        print("commit-msg validator: missing commit message file path.", file=sys.stderr)
        return 1

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as fh:
            msg = fh.read()
    except OSError as exc:
        print(f"commit-msg validator: cannot read {path}: {exc}", file=sys.stderr)
        return 1

    subject = _first_subject_line(msg)
    if not subject:
        print("commit-msg validator: empty commit message.", file=sys.stderr)
        return 1

    match = HEADER_RE.match(subject)
    if not match:
        print(
            "Commit message format inválido.\n"
            "Usa: <type>(<scope>)!?: <mensaje>\n"
            "Ejemplo: feat(iot-agri)!: add telemetry ingest endpoint",
            file=sys.stderr,
        )
        return 1

    msg_type = match.group("type")
    scope = match.group("scope")

    if msg_type not in ALLOWED_TYPES:
        print(
            f"Tipo inválido '{msg_type}'. Tipos permitidos: "
            + ", ".join(sorted(ALLOWED_TYPES)),
            file=sys.stderr,
        )
        return 1

    if scope not in ALLOWED_SCOPES:
        print(
            f"Scope inválido '{scope}'. Scopes permitidos: "
            + ", ".join(sorted(ALLOWED_SCOPES)),
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
