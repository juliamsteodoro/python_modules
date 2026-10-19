def secure_archive(
    filename: str, action: str = "read", content: str = " "
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(filename, 'w') as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, 'r') as file:
                data = file.read()
            return (True, data)
    except OSError as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    test_1 = secure_archive("/not/existing/file")
    print(f"Using 'secure_archive' to read from a nonexistent file: {test_1}")

    test_2 = secure_archive("/etc/master.passwd")
    print(
        "Using 'secure_archive' to read from an inaccessible file: "
        f"{test_2}"
    )

    test_3 = secure_archive("ancient_fragment.txt")
    print(f"Using 'secure_archive' to read from a regular file: {test_3}")

    if test_3[0]:
        test_4 = secure_archive("vault_backup.txt", "write", test_3[1])
        print(
            "Using 'secure_archive' to write previous content "
            f"to a new file: {test_4[1]}"
        )


if __name__ == "__main__":
    main()
