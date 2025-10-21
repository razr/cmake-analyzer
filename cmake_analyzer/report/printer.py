def print_text_report(results):
    print("\n=== CMake Analyzer Report ===")

    # --- Files ---
    print("\n[FILES]")
    for f in results.get("files", []):
        print(f"  - {f}")

    # --- Dependencies ---
    print("\n[DEPENDENCIES]")
    for dep in results.get("dependencies", []):
        print(f"  {dep['file']}:")
        for d in dep.get("dependencies", []):
            dep_type = d.get("type", "unknown")
            if dep_type == "package":
                name = d.get("name")
                comps = d.get("components", [])
                comp_str = f" (components: {', '.join(comps)})" if comps else ""
                print(f"    - {dep_type}: {name}{comp_str}")
            elif dep_type == "library":
                print(f"    - {dep_type}: {d.get('variable')} -> {d.get('library')}")
            elif dep_type == "file":
                print(f"    - {dep_type}: {d.get('variable')} -> {d.get('path')}")
            elif dep_type == "external_project":
                print(f"    - {dep_type}: {d.get('name')}")
            else:
                print(f"    - {dep_type}: {d}")

