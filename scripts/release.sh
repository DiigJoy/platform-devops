#!/usr/bin/env bash
set -euo pipefail

tag_prefix="${1:?tag prefix required}"
shift
if [[ "$#" -lt 1 ]]; then
  echo "At least one path is required."
  exit 1
fi
app_paths=("$@")

latest_tag="$(git tag --list "${tag_prefix}*" --sort=-v:refname | head -n 1 || true)"
if [[ -n "${latest_tag}" ]]; then
  range="${latest_tag}..HEAD"
  current_version="${latest_tag#${tag_prefix}}"
else
  range=""
  current_version="0.0.0"
fi

commit_shas="$(git log ${range} --format=%H -- "${app_paths[@]}" || true)"
if [[ -z "${commit_shas}" ]]; then
  echo "No commits touching ${app_paths[*]} since ${latest_tag:-start}; skipping tag."
  exit 0
fi

bump="none"
while IFS= read -r sha; do
  subject="$(git show -s --format=%s "${sha}")"
  body="$(git show -s --format=%b "${sha}")"

  if grep -Eq '(^|\n)BREAKING CHANGE:' <<< "${body}" || grep -Eq '(^|\n)BREAKING-CHANGE:' <<< "${body}"; then
    bump="major"
    break
  fi

  if grep -Eq '^[a-zA-Z]+(\([^)]*\))?!: ?' <<< "${subject}"; then
    bump="major"
    break
  fi

  if [[ "${bump}" != "minor" ]] && grep -Eq '^feat(\([^)]*\))?: ?' <<< "${subject}"; then
    bump="minor"
  fi

  if [[ "${bump}" == "none" ]] && grep -Eq '^(fix|perf)(\([^)]*\))?: ?' <<< "${subject}"; then
    bump="patch"
  fi
done <<< "${commit_shas}"

if [[ "${bump}" == "none" ]]; then
  echo "No Conventional Commits requiring a release; skipping tag."
  exit 0
fi

next_version="$(CURRENT_VERSION="${current_version}" BUMP="${bump}" python - <<'PY'
import os
major, minor, patch = map(int, os.environ["CURRENT_VERSION"].split("."))
bump = os.environ["BUMP"]
if bump == "major":
    major += 1
    minor = 0
    patch = 0
elif bump == "minor":
    minor += 1
    patch = 0
elif bump == "patch":
    patch += 1
print(f"{major}.{minor}.{patch}")
PY
)"

new_tag="${tag_prefix}${next_version}"
if git rev-parse "${new_tag}" >/dev/null 2>&1; then
  echo "Tag ${new_tag} already exists; skipping."
  exit 0
fi

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git tag -a "${new_tag}" -m "Release ${new_tag}"
git push origin "${new_tag}"
