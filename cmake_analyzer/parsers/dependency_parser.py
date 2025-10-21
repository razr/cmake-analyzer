import re
from cmake_analyzer.core.parser_base import BaseParser

class DependencyParser(BaseParser):
    """Extracts dependencies from CMakeLists.txt and .cmake files."""

    patterns = {
        "find_package": re.compile(r"find_package\s*\(\s*([A-Za-z0-9_]+)", re.IGNORECASE),
        "find_library": re.compile(r"find_library\s*\(\s*([A-Za-z0-9_]+)", re.IGNORECASE),
        "find_file": re.compile(r"find_file\s*\(\s*([A-Za-z0-9_]+)", re.IGNORECASE),
        "external_project": re.compile(r"ExternalProject_Add\s*\(\s*([A-Za-z0-9_]+)", re.IGNORECASE),
    }

    def parse(self, text, file_path):
        deps = {}
        for name, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                deps[name] = sorted(set(matches))
        return {"file": str(file_path), "dependencies": deps}
