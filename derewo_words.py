# Olha Svezhentseva
# 14.08.2022

import re
import argparse


def extract_words(input_file: str, output_file: str = "filtered_words") -> None:
    """The method extracts clean words from a file and saves them in TXT file."""
    words = set()
    with open(input_file, encoding='ISO-8859-15') as file_in, open(
            output_file, "w"
    ) as file_out:
        for line in file_in.readlines():
            if line[0] != "#":
                word = line.split(" ", 1)[0].split(',')[0]
                word = "".join(re.split(r'\(|\)', word))
                if word not in words:
                    words.add(word)
                    file_out.write(word + '\n')


if __name__ == "__main__":

    words_parser = argparse.ArgumentParser()
    words_parser.add_argument("--file", type=str)
    words_args = words_parser.parse_args()
    extract_words(words_args.file)

