import argparse


def extract_dmy_strings(date: str,
                        pattern=r"(\d+)\..*?(\w+).*?(\d+)") -> str:
    import re
    return re.findall(pattern, date)[0]


def format_output(*strings: str) -> str:
    output_string = str()
    for string in strings:
        output_string += string + '\t'
    return output_string.strip('\t')


def format_headlines_file(file_name, new_file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        with open(new_file_name, 'w', encoding='utf-8') as g:
            position_counter = 0
            for line in f:
                if not position_counter % 6:
                    date = line.strip()
                    day, month, year = extract_dmy_strings(date)
                if position_counter % 6 == 2:
                    time = line.strip()
                if position_counter % 6 == 4:
                    headline = line.strip()
                    if position_counter != 4:
                        year = '\n' + year
                    g.write(format_output(year, month, day, time, headline))
                position_counter += 1
    return


parser = argparse.ArgumentParser(description="Formats headline txt file.")
parser.add_argument("original_file_path", help="(original) file to be formatted")
parser.add_argument("new_file_path", help="new file")
args = parser.parse_args()


if __name__ == "__main__":
    format_headlines_file(file_name=args.original_file_path, new_file_name=args.new_file_path)
