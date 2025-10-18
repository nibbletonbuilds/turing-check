#!/usr/bin/env python3

def load_password_list(path: str) -> set[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip()}


def is_password_in_list(password: str, pw_set: set[str]) -> bool:
    return password.strip() in pw_set

if __name__ == "__main__":
    list_path = "common_passwords.txt"
    pw_set = load_password_list(list_path)

    password = input("Enter password: ").strip()
    if is_password_in_list(password, pw_set):
        print("⚠️  Weak — found in the list!")
    else:
        print("✅  Safe — not found.")
