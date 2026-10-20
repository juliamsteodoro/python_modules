import os
import site
import sys

def main() -> None:
    if sys.prefix != sys.base_prefix:
        venv_name = os.path.basename(sys.prefix)
        site_pkg = site.getsitepackages()

        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment! "
              "Safe to install reagents without affecting the global system.\n")
        print("Reagent installation path:")
        print(site_pkg)
    else:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You are in the global environment! "
              "Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("  python3 -m venv lab_env")
        print("  source lab_env/bin/activate  # On Unix")
        print("  lab_env\\Scripts\\activate     # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()