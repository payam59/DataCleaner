import os
import sys
import glob
import emoji

def remove_emojis(text):
    # Replace all emojis with an empty string
    return emoji.replace_emoji(text, replace='')

def clean_file(file_path, min_words):
    base_name = os.path.splitext(file_path)[0]
    output_file_path = f"{base_name}_cleaned.txt"
    
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for line in lines:
            cleaned_line = remove_emojis(line).strip()
            if len(cleaned_line.split()) >= min_words:
                output_file.write(cleaned_line + "\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: python DataCleaner.py <path/to/file or file extension> <min number of words>")
        sys.exit(1)
    
    path_or_extension = sys.argv[1]
    min_words = int(sys.argv[2])

    if os.path.isfile(path_or_extension):
        clean_file(path_or_extension, min_words)
    else:
        for file in glob.glob(f"*.{path_or_extension}"):
            clean_file(file, min_words)

if __name__ == "__main__":
    main()
