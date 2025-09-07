from bulang import run_bulang

if __name__ == "__main__":
    test_programs = [
        """
int x = 10;
int y = 20;
int result = x + y * 2;
print(result);
        """,
        """
string message = "Hello";
string name = "World";
print(message);
print(name);
        """,
        """
int age = 18;
if (age >= 18) {
    print("Adult");
} else {
    print("Minor");
}
        """,
        """
int i = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}
        """,
    ]

    for i, program in enumerate(test_programs):
        print(f"\n--- Test Program {i + 1} ---")
        print("Code:")
        print(program.strip())
        print("\nOutput:")
        run_bulang(program)
        print("-" * 30)
