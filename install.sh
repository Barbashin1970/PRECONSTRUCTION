#!/usr/bin/env bash
# Installs the preconstruction-ru and preconstruction-en skills on macOS and Linux:
#   ~/.claude/skills  — Claude Code (terminal, VS Code, JetBrains, Claude app)
#   ~/.agents/skills  — Codex and other agents that read the Agent Skills layout
#
#   ./install.sh              link the skills: `git pull` then updates them
#   ./install.sh --copy       copy instead: this folder can be deleted afterwards
#   ./install.sh --uninstall  remove the links that point into this folder
#
# Re-runnable. A name that is already taken is skipped, never overwritten.
# Messages are in English: the script is shared by Russian and foreign students.
# Claude Code users can skip this script and install the plugin instead — see README.md.
set -euo pipefail

mode=link
case "${1:-}" in
  "") ;;
  --copy) mode=copy ;;
  --uninstall) mode=uninstall ;;
  -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
  *) echo "Unknown option: ${1}. Use --copy, --uninstall or --help." >&2; exit 2 ;;
esac

repo_skills="$(cd "$(dirname "$0")/skills" 2>/dev/null && pwd -P)" || {
  echo "No skills/ folder next to this script." >&2; exit 1; }

for target in "${HOME}/.claude/skills" "${HOME}/.agents/skills"; do
  echo
  echo "Target: ${target}"
  [ "${mode}" = uninstall ] || mkdir -p "${target}"
  for src in "${repo_skills}"/*/; do
    src="${src%/}"
    [ -f "${src}/SKILL.md" ] || continue
    name="$(basename "${src}")"
    dest="${target}/${name}"
    case "${mode}" in
      uninstall)
        if [ -L "${dest}" ] && [ "$(readlink "${dest}")" = "${src}" ]; then
          rm "${dest}"
          echo "  removed link: ${name}"
        elif [ -e "${dest}" ] || [ -L "${dest}" ]; then
          echo "  left as is (not a link to this folder): ${dest}"
        fi
        ;;
      *)
        if [ -e "${dest}" ] || [ -L "${dest}" ]; then
          echo "  skipped (already exists): ${name}"
        elif [ "${mode}" = copy ]; then
          cp -R "${src}" "${dest}"
          echo "  copied: ${name}"
        else
          ln -s "${src}" "${dest}"
          echo "  linked: ${name}"
        fi
        ;;
    esac
  done
done

echo
case "${mode}" in
  link)
    echo "Done. Restart Claude Code (or run /reload-skills), then type /preconstruction-ru"
    echo "or /preconstruction-en. Keep this folder where it is: the links point to it."
    echo "Update later with: git pull" ;;
  copy)
    echo "Done. Restart Claude Code (or run /reload-skills), then type /preconstruction-ru"
    echo "or /preconstruction-en. Copies do not update: re-run with --copy after a new download." ;;
  uninstall)
    echo "Done. Copies made with --copy are not removed: delete those folders by hand." ;;
esac
