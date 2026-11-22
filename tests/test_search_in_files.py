from pathlib import Path

from txt_search.searcher import search_in_files


def test_finds_word_in_single_file(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("первая\nздесь кот\nтретья\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert len(result) == 1
    path, line_no, line = result[0]
    assert path == str(f)
    assert line_no == 2
    assert line == "здесь кот"


def test_returns_correct_line_number(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("one\ntwo\nthree кот\nfour\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert len(result) == 1
    assert result[0][1] == 3


def test_case_insensitive_by_default(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("Кот\nКОТ\nкот\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert len(result) == 3
    assert [r[1] for r in result] == [1, 2, 3]


def test_case_sensitive(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("Кот\nкот\n", encoding="utf-8")

    lower = search_in_files([str(f)], "кот", case_sensitive=True)
    upper = search_in_files([str(f)], "Кот", case_sensitive=True)

    assert len(lower) == 1
    assert lower[0][1] == 2
    assert len(upper) == 1
    assert upper[0][1] == 1


def test_multiple_matches_same_file(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text(
        "кот раз\nкот два\nбез совпадений\nкот три\n",
        encoding="utf-8"
    )

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert [r[1] for r in result] == [1, 2, 4]


def test_no_matches(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("собака\nптица\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)
    assert result == []


def test_rstrip_removes_newline(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("кот\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert result[0][2] == "кот"
    assert "\n" not in result[0][2]


def test_multiple_files(tmp_path: Path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("кот в первом\n", encoding="utf-8")
    f2.write_text("кот во втором\n", encoding="utf-8")

    result = search_in_files([str(f1), str(f2)], "кот", case_sensitive=False)

    paths = {r[0] for r in result}
    assert paths == {str(f1), str(f2)}


def test_skips_unreadable_file(tmp_path: Path):
    good = tmp_path / "good.txt"
    good.write_text("кот тут\n", encoding="utf-8")

    fake = tmp_path / "fake.txt"
    fake.mkdir()

    result = search_in_files(
        [str(fake), str(good)],
        "кот",
        case_sensitive=False
    )

    assert len(result) == 1
    assert result[0][0] == str(good)


def test_empty_file(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)
    assert result == []


def test_empty_word(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("кот\n", encoding="utf-8")

    result = search_in_files([str(f)], "", case_sensitive=False)
    assert result == []


def test_whole_word_only(tmp_path: Path):
    f = tmp_path / "a.txt"
    f.write_text("который час\nкот спит\nкота позвали\n", encoding="utf-8")

    result = search_in_files([str(f)], "кот", case_sensitive=False)

    assert len(result) == 1
    assert result[0][1] == 2
    assert result[0][2] == "кот спит"


def test_windows1251_file(cp1251_file: Path):
    result = search_in_files([str(cp1251_file)], "кот", case_sensitive=False)

    assert len(result) == 1
    assert "кот" in result[0][2].lower()