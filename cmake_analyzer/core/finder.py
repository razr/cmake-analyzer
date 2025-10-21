from pathlib import Path

def find_cmake_files(source_dir: Path):
    """Recursively find all CMake-related files."""
    return [p for p in source_dir.rglob("*") if p.suffix == ".cmake" or p.name == "CMakeLists.txt"]
