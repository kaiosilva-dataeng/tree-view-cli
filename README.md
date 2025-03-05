# tree-view-cli

A fast, customizable command-line tool for generating tree-like representations of directory structures, with intelligent handling of .gitignore rules and cross-platform compatibility.

## Features

- 🚀 **Fast execution**: Optimized Python implementation for quick directory processing
- 🔍 **Gitignore support**: Automatically respects .gitignore rules to match version-controlled projects
- 🌲 **Customizable depth**: Control how many levels of directories to display
- 🔄 **Cyclic detection**: Prevents infinite loops from symbolic links
- 🖥️ **Cross-platform**: Works consistently across Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher

## Installation

```bash
# Clone the repository
git clone https://github.com/kaiosilva-dataeng/tree-view-cli.git
cd tree-view-cli

# Install dependencies using uv
uv sync
```

## Usage

Basic usage:

```bash
python tree_view_cli.py /path/to/directory
```

Limiting directory depth:

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

## Development

### Setting Up Development Environment

```bash
# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
uv sync --dev
```

### Running Tests

```bash
# Run tests
task test

# Run linting
task lint

# Format code
task format
```

### Development Tasks

The project uses `taskipy` to manage common development tasks:

- `task lint`: Run Ruff linting checks
- `task format`: Format code with Ruff
- `task run`: Run the tree-view-cli on the current directory
- `task test`: Run the test suite with coverage reporting

### Docker Support

For Docker-based development and deployment, see [Docker Setup](README.Docker.md).

The Docker setup provides:
- Multi-stage builds for efficient image size
- Development environment with hot reloading
- Separate services for testing and coverage viewing
- Security-focused production configuration

## CI/CD

This project uses GitHub Actions for continuous integration. The workflow includes:
- Linting and code formatting checks using Ruff
- Running tests with pytest
- Coverage reporting

## Project Structure

```
tree-view-cli/
├── tests/
│   ├── conftest.py           # Test fixtures and setup
│   └── test_tree_view_cli.py # Test suite
├── .github/
│   └── workflows/            # CI configuration
├── .vscode/                  # VS Code configuration
├── Dockerfile                # Docker configuration
├── compose.yaml              # Docker Compose configuration
├── tree_view_cli.py          # Main application module
├── pyproject.toml            # Project metadata and dependencies
├── README.md                 # Project documentation
└── README.Docker.md          # Docker-specific documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Python community for the robust standard library functions that make this tool possible
- Inspired by the Unix `tree` command, but with additional features for modern development workflows
