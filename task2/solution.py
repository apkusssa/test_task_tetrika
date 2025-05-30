import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
import time
import logging
import re


# URL = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
BASE_URL = "https://ru.wikipedia.org"
START_URL = "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
RUS_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def get_animal_counts():
    counts = defaultdict(int)
    next_page = START_URL

    while next_page:
        url = BASE_URL + next_page
        logging.info(f"Парсим страницу: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for li in soup.select("div.mw-category li"):
            name = li.text.strip()
            if name:
                first_letter = name[0].upper()
                if re.fullmatch(r"[А-ЯЁ]", first_letter):  # Только русские заглавные буквы
                    counts[first_letter] += 1

        next_link = soup.find("a", string="Следующая страница")
        next_page = next_link["href"] if next_link else None

        time.sleep(0.3)

    logging.info(f"Cборы данных завершены. Найдено букв: {len(counts)}")
    return counts



def save_to_csv(counts, filename="beasts.csv"):
    logging.info(f"Сохраняем данные в файл: {filename}")
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter in sorted(counts, key=lambda x: RUS_ALPHABET.index(x)):
            writer.writerow([letter, counts[letter]])
    logging.info("Сохранение завершено.")

if __name__ == "__main__":
    counts = get_animal_counts()
    save_to_csv(counts)
    logging.info("Всё готово!")