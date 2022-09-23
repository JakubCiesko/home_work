import argparse
import time

def extract_token_and_info(string: str):
    import re
    return re.findall(r"(\w{2}).*?\w+?(\d).*?\w+(\d).*?\d{8}-(\w)", string)


def format_token_info(token_info: list) -> str:
    return '\t'.join(token_info[0])


def extract_token_info_from_file(file_path, new_file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = True
        with open(new_file_path, 'w', encoding='utf-8') as g:
            for line in f:
                token_and_info = extract_token_and_info(line)
                if token_and_info:
                    formatted_string = format_token_info(token_and_info)
                    g.write(formatted_string) if first_line else g.write("\n" + formatted_string)
                    first_line = False


parser = argparse.ArgumentParser(description="extracts info from cantonese")
parser.add_argument("cantonese_file", help="txt file with cantonese tokens and info")
parser.add_argument("new_txt_file", help="new txt file")
parser.add_argument("--t", dest="time", action="store_const", const=True, default=False, help="time execution")
args = parser.parse_args()

if __name__ == "__main__":
    ts = time.time()
    extract_token_info_from_file(file_path=args.cantonese_file, new_file_path=args.new_txt_file)
    te = time.time()
    if args.time:
        print(f'Time elapsed:\t{te - ts}s')