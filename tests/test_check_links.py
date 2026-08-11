import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check-links.py"
SPEC = importlib.util.spec_from_file_location("check_links", SCRIPT)
check_links = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_links)


def test_relative_path_uses_article_directory(tmp_path):
    article = tmp_path / "articles" / "nested" / "article.md"
    target = tmp_path / "inbox" / "used" / "source.md"

    assert check_links.relative_path(target, article) == "../../inbox/used/source.md"


def test_fix_replaces_duplicate_link_only_once(tmp_path):
    article = tmp_path / "articles" / "nested" / "article.md"
    target = tmp_path / "inbox" / "used" / "source.md"
    article.parent.mkdir(parents=True)
    target.parent.mkdir(parents=True)
    target.write_text("source", encoding="utf-8")
    article.write_text(
        "[one](../inbox/used/source.md)\n[two](../inbox/used/source.md)\n",
        encoding="utf-8",
    )
    item = {
        "article_path": article,
        "link": "../inbox/used/source.md",
        "candidates": [target],
    }

    fixed = check_links.fix([item, item.copy()])

    assert fixed == 2
    assert article.read_text(encoding="utf-8").count(
        "../../inbox/used/source.md"
    ) == 2

