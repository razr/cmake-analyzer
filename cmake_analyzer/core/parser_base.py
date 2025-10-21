class BaseParser:
    """Base interface for CMake analyzers."""
    def parse(self, text: str, file_path):
        raise NotImplementedError("Parser must implement parse()")
