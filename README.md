# 🧩 cmake-analyzer

`cmake-analyzer` is a modular Python toolkit that analyzes **CMake projects** — it discovers, parses, and summarizes configuration, dependency, and option information from `CMakeLists.txt` and `.cmake` files.

---

## 🚀 Features

- 🔍 **Finder**: Recursively locates all `CMakeLists.txt` and `.cmake` files in a project.
- 🧠 **Dependency Parser**: Extracts dependencies such as `find_package()`, `find_library()`, and `ExternalProject_Add()`.
- ⚙️ **CMake API Analyzer** *(extendable)*: Integrates with the [CMake File API](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html) for deeper introspection.
- 🪶 **Modular architecture**: Add your own parsers easily (`BaseParser` interface).
- 🧾 **Reporting**: Output results in human-readable text or JSON.

---

## 📁 Project Structure

```
cmake-analyzer/
├── cmake_analyzer/
│   ├── cli.py                # Command-line interface entry point
│   ├── core/
│   │   ├── finder.py         # Finds CMake files
│   │   └── parser_base.py    # Base class for all parsers
│   ├── parsers/
│   │   └── dependency_parser.py  # Extracts dependencies and packages
│   ├── analyzers/
│   │   └── cmake_api_analyzer.py # Main integration logic
│   └── report/
│       ├── printer.py        # Console output
│       └── json_reporter.py  # JSON output
├── examples/
│   └── minimal_project/      # Example CMake project
├── tests/                    # (Placeholder for unit tests)
├── pyproject.toml            # Build and CLI definition
└── README.md
```

---

## 💻 Installation

### Option 1: Run directly (no installation)
```bash
python -m cmake_analyzer.cli --source ./examples/minimal_project
```

### Option 2: Install as CLI tool
```bash
pip install .
cmake-analyzer --source ./examples/minimal_project
```

---

## ⚙️ Usage

```bash
cmake-analyzer --source <path-to-cmake-project> [--output json] [--reconfigure]
```

**Example:**
```bash
cmake-analyzer --source examples/minimal_project
```

**Output:**
```
=== CMake Analyzer Report ===

[FILES]
  - examples/minimal_project/CMakeLists.txt

[DEPENDENCIES]
  examples/minimal_project/CMakeLists.txt: ['find_package', 'find_library']
```

---

## 🧩 Architecture Overview

Each **parser** implements a subclass of `BaseParser` and returns structured data.

Example: `DependencyParser` detects
- `find_package()`
- `find_library()`
- `find_file()`
- `ExternalProject_Add()`

You can add new parsers for:
- CMake options (`option()`, `set()`)
- Platform detection (`APPLE`, `UNIX`, `WIN32`)
- Compiler and language (`CXX_STANDARD`, `C_STANDARD`)
- Linker / libc / external toolchain flags

---

## 🧱 Extending the Tool

To create a new parser:

```python
from cmake_analyzer.core.parser_base import BaseParser

class MyCustomParser(BaseParser):
    def parse(self, text, file_path):
        # custom logic
        return {"file": str(file_path), "info": "custom data"}
```

Then register and use it in `cmake_api_analyzer.py`.

---

## 🧪 Example Project

A minimal test project is included in `examples/minimal_project`:

```cmake
cmake_minimum_required(VERSION 3.10)
project(MinimalExample LANGUAGES C CXX)
find_package(Python3 REQUIRED)
find_library(M_LIB m)
add_executable(main main.cpp)
target_link_libraries(main PRIVATE Python3::Python ${M_LIB})
```

Run analysis:

```bash
cmake-analyzer --source examples/minimal_project
```

---

## 🧰 Roadmap

- [ ] Add parser for CMake `option()` and `set()` variables  
- [ ] Add parser for compiler/language settings (`C_STANDARD`, `CXX_STANDARD`)  
- [ ] Add platform condition parser (`APPLE`, `UNIX`, `WIN32`, `LINUX`, etc.)  
- [ ] Support HTML and Markdown report generation

---

## 🪪 License

MIT License — feel free to use and extend.
