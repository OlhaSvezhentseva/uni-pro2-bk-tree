# Olha Svezhentseva
# 16.08.2022

import re
import argparse


def extract_words(input_file: str, output_file: str = "filtered_words") -> None:
    """The method extracts clean words from a file and saves them in a txt file"""
    words = set()
    try:
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
    except FileNotFoundError:
        raise("File not Found")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    args = parser.parse_args()
    extract_words(args.file)

