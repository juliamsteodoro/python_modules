def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    try:
        import pandas as pd
        pandas_version = pd.__version__
        has_pandas = True
        print(f"[OK] pandas ({pandas_version}) - Data manipulation ready")
    except ImportError:
        has_pandas = False
        pandas_version = ""
        print("[MISSING] pandas is not installed.")
    try:
        import numpy as np
        numpy_version = np.__version__
        has_numpy = True
        print(f"[OK] numpy ({numpy_version}) - Numerical computation ready")
    except ImportError:
        has_numpy = False
        numpy_version = ""
        print("[MISSING] numpy is not installed.")

    if has_numpy and has_pandas:
        print(
        "pip vs Poetry: requirements.txt declares what to install; "
        "pip resolves it at install time. pyproject.toml declares the same "
        "constraints, and Poetry pins the resolved versions in poetry.lock "
        "so every install is identical."
    )
        print("All reagents present and accounted for.")
    else:
        print("To install missing reagents:")
        print("  pip: pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install")


if __name__ == "__main__":
    main()
