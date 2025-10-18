# Turing Check

**Turing Check** is a comprehensive password analysis and security tool. It helps you evaluate the strength of passwords, detect weak or compromised passwords, and provides actionable feedback to improve security. Designed for developers, security enthusiasts, and anyone who wants smarter password management.

---

## Features

* ✅ Check if a password exists in a known list of compromised passwords.
* ✅ CLI-based for fast and lightweight usage.
* ✅ Designed for extension into a full-fledged password security toolkit.
* ⏳ Evaluate password strength using entropy and character diversity.
* ⏳ Detect dictionary words, common patterns, and repetitions.
* ⏳ Generate actionable feedback to improve password security.

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:nibbletonbuilds/turing-check.git
cd turing-check
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Current version uses only standard Python libraries; future updates may require `rich` for colored CLI output.

---

## Usage

1. **Check a password against a list of known passwords:**

```bash
python password_in_list.py
```

Enter a password when prompted. The tool will tell you if the password is found in the list.

2. **Analyze password strength and patterns:**

```bash
python turing_check.py
```

* Input your password.
* Receive a detailed report: entropy, character variety, duplicate patterns, and actionable suggestions.

---

## Roadmap

We plan to expand Turing Check into a more complete password security solution. Future updates may include:

* **Privacy-focused checks**: hashed password lookups to prevent sending sensitive data.
* **Expanded password databases**: integration with top 10k and 100k common passwords for more thorough checks.
* **Batch analysis**: ability to check multiple passwords at once and output results in JSON or CSV.
* **Interactive GUI/web version**: user-friendly interface for broader accessibility.
* **AI-based recommendations**: smart suggestions for creating stronger, more resilient passwords.
* **Security audit tools**: insights into patterns in your existing passwords for improved security hygiene.

---

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork, submit pull requests, or open issues on GitHub.

---

## License

MIT License — see `LICENSE` for details.

---

## Author

**Nibbleton**
GitHub: [nibbletonbuilds](https://github.com/nibbletonbuilds)
