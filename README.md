```markdown
# DataCleaner

`DataCleaner` is a Python script designed to clean text files by removing emojis and filtering out lines with fewer words than a specified threshold. This tool is particularly useful for preprocessing text data for analysis, ensuring that the input files are free of non-text elements and adhere to a minimum verbosity level.

## Features

- **Remove Emojis:** Strips all emoji characters from the text, ensuring that the output contains only textual information.
- **Filter Short Lines:** Allows specifying a minimum number of words per line; lines with fewer words are omitted from the output.
- **Flexible Input:** Accepts either a single file or multiple files by extension, making it easy to process individual or batches of files.
- **Preserves Original Files:** Outputs the cleaned content to new files, leaving the original files unmodified for reference or other uses.

## Installation

Before you can use `DataCleaner`, ensure you have Python 3.6+ installed on your system. You will also need to install the `emoji` library. You can install it using pip:

```bash
pip install emoji
```

## Usage

`DataCleaner` can be used directly from the command line. Here are some examples of how to use it:

### Cleaning a Single File

```bash
python DataCleaner.py path/to/yourfile.txt 4
```
This command will process `yourfile.txt`, removing all emojis and lines with fewer than 4 words. The result will be saved in `yourfile_cleaned.txt`.

### Cleaning Multiple Files by Extension

```bash
python DataCleaner.py txt 4
```
This command will process all `.txt` files in the script's directory, applying the same cleaning process as above to each file.

## Contributing

Contributions to `DataCleaner` are welcome! Whether it's bug reports, feature requests, or contributions to code, all are appreciated. Please open an issue or pull request on GitHub to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
