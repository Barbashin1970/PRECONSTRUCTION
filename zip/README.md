# zip/ — готовые архивы навыков · ready skill archives

Архивы собирает `python3 tools/build_zips.py` из папки [skills/](../skills/README.md);
руками их не правят. Распаковывать перед загрузкой не нужно.

| Папка | Для чего | Как устроен архив |
|---|---|---|
| [claude/](claude/) | claude.ai и приложение Claude: **Customize → Skills → «+» → Create skill → Upload a skill** | папка навыка в корне архива — так требует claude.ai |
| [perplexity/](perplexity/) | Perplexity: **Настройка → Навыки → Создать навык → Загрузить навык** | `SKILL.md` в корне архива |

Для любого другого чата подойдёт любой из двух: распакуйте и приложите файлы.

---

| Folder | For | Layout |
|---|---|---|
| [claude/](claude/) | claude.ai and the Claude app: **Customize → Skills → + → Create skill → Upload a skill** | the skill folder at the archive root, as claude.ai requires |
| [perplexity/](perplexity/) | Perplexity: **Settings → Skills → Create skill → Upload skill** | `SKILL.md` at the archive root |

Built by `python3 tools/build_zips.py` from [skills/](../skills/README.md); never edited by hand.
