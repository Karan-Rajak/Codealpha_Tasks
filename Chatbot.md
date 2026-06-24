# 🤖 CodeBot — Basic Chatbot

> **CodeAlpha Python Programming Internship — Task 4**

---

## 📋 Project Overview

CodeBot is a simple rule-based chatbot built using Python. It takes user input from the console and responds with predefined replies based on keyword matching. This project was built as part of the **CodeAlpha Python Internship** to demonstrate understanding of functions, conditionals, loops, and basic input/output in Python.

---

## ✨ Features

- Greets the user and responds to common phrases
- Handles unrecognized input gracefully
- Clean welcome screen on launch
- Exits safely on `bye`, `quit`, or keyboard interrupt (`Ctrl+C`)
- Empty input detection

---

## 🛠️ Tech Stack

| Tool       | Details              |
|------------|----------------------|
| Language   | Python 3.x           |
| Libraries  | None (built-in only) |
| Interface  | Command Line (CLI)   |

---

## 📁 Project Structure

```
CodeAlpha_ProjectName/
│
└── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## ▶️ How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/Karan-Rajak/CodeAlpha_Tasks/Chatbot.py.git
cd CodeAlpha_Tasks/Chatbot.py
```

**2. Run the script:**
```bash
python chatbot.py
```

> No external libraries needed. Works with Python 3.x out of the box.

---

## 💬 Sample Conversation

```
=============================================
       Welcome to CodeBot - CodeAlpha
=============================================
  Type 'help' to see what I can do.
  Type 'bye' to exit the chatbot.
=============================================

You: hello
Bot: Hi there! How can I help you today?

You: how are you
Bot: I'm doing great, thanks for asking! How about you?

You: what is your name
Bot: I'm CodeBot, a simple chatbot created as part of the CodeAlpha internship!

You: bye
Bot: Goodbye! Have a great day. 👋
=============================================
```

---

## 🧠 Key Concepts Used

- `if-elif-else` conditionals
- Functions and docstrings
- `while` loop
- String methods (`.lower()`, `.strip()`)
- Exception handling (`try/except`)
- `__name__ == "__main__"` pattern

---

## 📌 Supported Inputs

| User Says                        | Bot Responds                              |
|----------------------------------|-------------------------------------------|
| hello / hi / hey                 | Greeting response                         |
| how are you                      | "I'm doing great..."                      |
| i'm fine / good / fine           | "That's wonderful to hear!"               |
| what is your name / who are you  | Introduces itself as CodeBot              |
| what can you do / help           | Lists capabilities                        |
| who made you / who created you   | Credits the author                        |
| bye / goodbye / exit / quit      | Ends the conversation                     |
| *(anything else)*                | Politely says it didn't understand        |

---

## 🚀 Future Improvements

- Add more conversation topics
- Integrate NLP libraries like `nltk` or `spacy`
- Build a GUI using `tkinter`
- Connect to an API for real-time responses

---

## 👤 Author

**[Karan kumar]**
Python Programming Intern — CodeAlpha
GitHub: [github.com/Karan-Rajak](https://github.com/Karan-Rajak)

---

## 🏢 About CodeAlpha

CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This internship program provides hands-on experience in Python development and scripting.

- 🌐 Website: [www.codealpha.tech](https://www.codealpha.tech)
- 📧 Email: services@codealpha.tech
-
