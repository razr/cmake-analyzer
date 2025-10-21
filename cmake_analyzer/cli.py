import argparse
from pathlib import Path
from cmake_analyzer.analyzers.cmake_api_analyzer import analyze_cmake_project
from cmake_analyzer.report import printer, json_reporter

def main():
    parser = argparse.ArgumentParser(description="Analyze a CMake project (Finder + File API + Parsers)")
    parser.add_argument("--source", type=Path, required=True, help="Path to CMake project source directory")
    parser.add_argument("--build", type=Path, default=Path("build"), help="Path to build directory")
    parser.add_argument("--reconfigure", action="store_true", help="Force clean & reconfigure build directory")
    parser.add_argument("--output", choices=["text", "json"], default="text", help="Output format")
    args = parser.parse_args()

    results = analyze_cmake_project(args.source, args.build, args.reconfigure)

    if args.output == "json":
        json_reporter.print_json_report(results)
    else:
        printer.print_text_report(results)

if __name__ == "__main__":
    main()
