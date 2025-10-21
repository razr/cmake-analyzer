from pathlib import Path
from cmake_analyzer.core.finder import find_cmake_files
from cmake_analyzer.parsers.dependency_parser import DependencyParser

def analyze_cmake_project(source_path: Path, build_path: Path, reconfigure: bool = False):
    """Main CMake project analysis entry point."""
    results = {"files": [], "dependencies": []}

    cmake_files = find_cmake_files(source_path)
    results["files"] = [str(f) for f in cmake_files]

    parser = DependencyParser()
    for f in cmake_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        results["dependencies"].append(parser.parse(text, f))

    return results
