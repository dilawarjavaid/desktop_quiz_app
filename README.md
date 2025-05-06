🧠 Quiz Application (Tkinter + Python)

This is a simple GUI-based quiz application built using Python's `tkinter` module. It fetches quiz data from a remote JSON source and allows users to select a quiz, answer multiple-choice questions, and view their score at the end.

---

## 📦 Features

- ✅ Fetches quiz data from an online source
- 🧑‍🏫 Lets users choose from multiple quizzes
- ❓ Displays one question at a time with 4 answer choices
- 🎯 Tracks your score and shows it at the end
- 🔁 Resets automatically after each quiz

---

## 🖥️ GUI Preview

> **Note**: This app uses a basic GUI built with `tkinter`.

- **Quiz Selection Screen**  
  Allows you to choose a quiz from a list.

- **Question Screen**  
  Displays a question with four options.

- **Result Popup**  
  Shows your final score in a message box.

---

## 🌐 Data Source

Quiz questions are fetched from this public JSON file:
```

[https://raw.githubusercontent.com/arditsulceteaching/hosted\_files/main/geo.json](https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json)

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/quiz-tkinter-app.git
cd quiz-tkinter-app
````

### 2. Install Dependencies

You only need the `requests` library, which can be installed with:

```bash
pip install requests
```

### 3. Run the App

```bash
python quiz_main.py
```

---

## 📁 File Structure

```
quiz_app.py       # Main Python file with the QuizApp class
README.md         # Project description and instructions
```

---

## 📌 To-Do / Future Improvements

* [ ] Add timer for each question
* [ ] Support for custom quizzes (local JSON upload)
* [ ] Show correct/incorrect feedback instantly
* [ ] Better UI using a framework like Tkinter.ttk or PyQt

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

* JSON data by [Ardit Sulce](https://github.com/arditsulceteaching)
* Built with ❤️ using Python and Tkinter


