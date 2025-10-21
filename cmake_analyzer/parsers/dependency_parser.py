import re
from pathlib import Path
from cmake_analyzer.core.parser_base import BaseParser

class DependencyParser(BaseParser):
    """
    Parses find_* and ExternalProject_Add() calls to extract dependencies.
    """

    _patterns = {
        "find_package": re.compile(
            r"find_package\s*\(\s*([A-Za-z0-9_+-]+)(?:\s+REQUIRED)?(?:\s+COMPONENTS\s+([A-Za-z0-9_+ \t-]+))?",
            re.IGNORECASE
        ),
        "find_library": re.compile(
            r"find_library\s*\(\s*([A-Za-z0-9_+-]+)\s+([A-Za-z0-9_./${}-]+)",
            re.IGNORECASE
        ),
        "find_file": re.compile(
            r"find_file\s*\(\s*([A-Za-z0-9_+-]+)\s+([A-Za-z0-9_./${}-]+)",
            re.IGNORECASE
        ),
        "ExternalProject_Add": re.compile(
            r"ExternalProject_Add\s*\(\s*([A-Za-z0-9_+-]+)",
            re.IGNORECASE
        ),
    }

    def parse(self, text: str, file_path: Path):
        dependencies = []

        for name, pattern in self._patterns.items():
            for match in pattern.finditer(text):
                if name == "find_package":
                    package = match.group(1)
                    components = match.group(2).split() if match.group(2) else []
                    dependencies.append({
                        "type": "package",
                        "name": package,
                        "components": components,
                    })
                elif name == "find_library":
                    var_name = match.group(1)
                    lib_name = match.group(2)
                    dependencies.append({
                        "type": "library",
                        "variable": var_name,
                        "library": lib_name,
                    })
                elif name == "find_file":
                    dependencies.append({
                        "type": "file",
                        "variable": match.group(1),
                        "path": match.group(2),
                    })
                elif name == "ExternalProject_Add":
                    dependencies.append({
                        "type": "external_project",
                        "name": match.group(1),
                    })

        return {
            "file": str(file_path),
            "dependencies": dependencies,
        }
