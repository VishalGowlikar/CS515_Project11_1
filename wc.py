# file_path ='texting.txt'
import sys
import argparse

def wc(file):
    file_path = file
    with open(file_path, 'r') as vis:
        content = vis.read()
        words = content.split()
        words_res =  len(words)

    with open(file_path, 'r') as lines:
        line = lines.readlines()
        num_lines = len(line)
        
    
    with open(file_path,'r')as char:
        chars = char.read()
        num_chars = len(chars)
        return words_res, num_lines, num_chars
        
def main():
    parser = argparse.ArgumentParser(prog="wc",
        description="Counts words, lines and characters of input files.")
    parser.add_argument("new_files", type=str, nargs="*",
                        help="Takes file path to be processed", default=str(sys.stdin))
    parser.add_argument("-c", "--characters", action="store_true",
                        help="Only counts number of characters")
    parser.add_argument("-w", "--words", action="store_true",
                        help="Print the word counts.")
    parser.add_argument("-l", "--lines", action="store_true",
                        help="Print the line counts.")
    parser.add_argument("-wlc","--wolich", action ="store_true", 
                        help="print the words, lines , chars" )
    parser.add_argument("-wl","--woli", action="store_true",
                        help ="print the words and lines")
    parser.add_argument("-lc","--lich", action="store_true",
                        help ="print the words and lines")

    t_words = 0
    t_lines =0
    t_char = 0
    t_file = ""
    args = parser.parse_args()
    t_file = args.new_files
         
    for file in args.new_files:
        words, lines , chars = wc(file)
    
        t_words += words
        t_lines += lines
        t_char += chars

        if args.words:
            print(f"{words} words in {t_file}")
        elif args.lines:
                print(f"{lines} lines in {t_file}")
        elif args.characters:
                print(f"{chars} characters in {t_file}")
        elif args.wolich:
            print(f"{words},{lines},{chars}")
        elif args.woli:
            print(f"{words}, {lines}")
        elif args.lich:
            print(f"{lines},{chars}")
        else:
            print(f"{words}    | {lines} |  {chars}   |  {t_file}    ")

    if len(args.new_files) > 1:
        print(f"{t_words}    | {t_lines} |  {t_char}   |  total")

    sys.exit(0)


if __name__ == "__main__":
    main()