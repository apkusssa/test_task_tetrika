import os
import csv
from solution import get_animal_counts, save_to_csv

def test_get_animal_counts_non_empty():
    counts = get_animal_counts()
    assert isinstance(counts, dict)
    assert len(counts) > 0
    # Проверим, что все ключи — русские заглавные буквы
    for letter in counts:
        assert letter.isalpha()
        assert "А" <= letter <= "Я" or letter == "Ё"

def test_save_to_csv(tmp_path):
    counts = {"А": 10, "Б": 5, "Ё": 1}
    test_file = tmp_path / "test_output.csv"
    save_to_csv(counts, filename=str(test_file))

    # Проверим содержимое файла
    with open(test_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows == [["А", "10"], ["Б", "5"], ["Ё", "1"]]
