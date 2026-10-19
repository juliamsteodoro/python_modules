import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1], 'r')
        content = file.read()
        print("---\n")
        print(content, end="\n")
        print("\n---")
        file.close()
        print(f"---File '{sys.argv[1]}' closed.")
        print("Transform data:")
        print("---\n")
        new_file = ""
        for char in content:
            if char == "\n":
                new_file += "#\n"
            else:
                new_file += char
        if len(content) > 0 and content[-1] != "\n":
            new_file += "#"
        print(new_file, end="\n")
        sys.stdout.write("---Enter new file name (or empty):")
        sys.stdout.flush()
        new_file_name = sys.stdin.readline()
        if len(new_file_name) > 0 and new_file_name[-1] == "\n":
            new_file_name = new_file_name[:-1]
        if new_file_name:
            try:
                print(f"Saving data to '{new_file_name}'")
                out_file = open(new_file_name, 'w')
                out_file.write(new_file)
                out_file.close()
                print(f"Data saved in file '{new_file_name}'.")
            except OSError as e:
                sys.stderr.write(
                    f"[STDERR] Error opening file "
                    f"'{new_file_name}': {e}\n"
                )
                print("Data not saved.")
        else:
            print("Not saving data.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")


if __name__ == "__main__":
    main()
