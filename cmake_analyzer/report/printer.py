def print_text_report(results):
    print("\n=== CMake Analyzer Report ===")
    print("\n[FILES]")
    for f in results.get("files", []):
        print(f"  - {f}")
    print("\n[DEPENDENCIES]")
    for dep in results.get("dependencies", []):
        print(f"  {dep['file']}: {list(dep['dependencies'].keys())}")
