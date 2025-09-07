from bulang import run_bulang
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], "r") as file_reader:
                program = file_reader.read()
                print("Code:")
                print(program.strip())
                print("\nOutput:")
                run_bulang(program)
                print("-" * 30)
        else:
            print(f"File not found: {sys.argv[1]}")
    else:
        print(f"{sys.argv[0]} <filename>.bl")
