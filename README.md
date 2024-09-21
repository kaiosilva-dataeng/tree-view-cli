# tree-view-cli

`tree-view-cli` is a Python script that generates a tree-like representation of a directory structure. It's designed to be simple, fast, and customizable, providing an easy way to visualize file system hierarchies directly from the command line.

## Features

- Generate a tree view of any directory
- Respect `.gitignore` rules, providing an accurate representation of version-controlled projects
- Customizable depth limit
- Alphabetical sorting of files and directories
- Cyclic reference detection to prevent infinite loops
- Cross-platform compatibility (works on any system with Python 3.6+)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `tree_view_cli.py` script.
2. Make the script executable (on Unix-like systems):

   ```bash
   chmod +x tree_view_cli.py
   ```

3. Optionally, you can add the script's directory to your PATH for easier access.

## Usage

Basic usage:

```bash
python tree_view_cli.py /path/to/directory
```

To limit the depth of the tree:

```bash
python tree_view_cli.py /path/to/directory --max-depth 2
```

### Options

- `directory`: The path to the directory you want to visualize (required)
- `--max-depth`: Maximum depth to display (optional, default is unlimited)

## Example Output

```
my-project/
├── src/
│   ├── main.py
│   └── utils/
│       ├── helper.py
│       └── config.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├── README.md
└── requirements.txt
```

Note: The output will exclude files and directories specified in .gitignore files.

## Development

### Running Tests

To run the tests, you'll need pytest installed. You can install it with:

```bash
pip install pytest
```

Then, run the tests with:

```bash
pytest test_tree_view_cli.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or encounter any issues, please feel free to open an issue in this repository.

---

Happy tree viewing!