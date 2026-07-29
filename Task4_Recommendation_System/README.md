# 📚 Content-Based Book Recommendation System

A simple and interactive **Book Recommendation System** developed using **Python**, **Pandas**, and **Tkinter**. The application recommends similar books based on **Genre**, **Author**, and **Language** using a content-based recommendation approach.

The project provides a user-friendly graphical interface where users can enter a book title and receive personalized book recommendations.

---

# ✨ Features

- 📚 User-friendly GUI built with Tkinter
- 🔍 Search books by title
- 🤖 Content-based book recommendation system
- 📖 Recommends books based on:
  - Genre
  - Author
  - Language
- 📊 Displays complete book details
- ⚠️ Handles invalid book names
- 🗑️ Clear button to reset all inputs and results
- 💻 Simple and interactive interface

---

# 🛠️ Technologies Used

- Python 3
- Pandas
- Tkinter
- CSV Dataset

---

# 📚 Dataset

This project uses a custom **CSV dataset** containing details of various books.

### Dataset Attributes

- 📖 **Title** – Name of the book
- 👤 **Author** – Author of the book
- 🏷️ **Genre** – Category of the book
- 🌍 **Language** – Language of the book
- 📅 **Year** – Publication year

The recommendation engine analyzes these attributes and calculates a similarity score to recommend books that closely match the selected title.

---

# 📂 Project Structure

```text
Task3_Book_Recommendation_System/
│
├── book_recommendation.py          # Main application
├── book_dataset.csv                # Book dataset
├── README.md                       # Project documentation
├── .gitignore                      # Git ignored files
└── screenshots/
    ├── Welcome page.png
    ├── Recommend books.png
    └── Book not found.png
```

---

# ⚙️ How It Works

1. The application loads the book dataset from a CSV file using **Pandas**.
2. The user enters a book title and the desired number of recommendations.
3. The system searches for the selected book in the dataset.
4. It compares all books based on:
   - 📖 Genre
   - 👤 Author
   - 🌍 Language
5. Each matching attribute is assigned a score.
6. Books are ranked according to their similarity score.
7. The top matching books are displayed in the recommendation window.

---

# 📸 Screenshots

## 🏠 Welcome Page

![Welcome Page](screenshots/Welcome%20page.png)

---

## 📚 Recommend Books

![Recommend Books](screenshots/Recommend%20books.png)

---

## ❌ Book Not Found

![Book Not Found](screenshots/Book%20not%20found.png)

---


# 🔮 Future Enhancements

- ⭐ Add book cover images
- 🤖 Use Machine Learning for better recommendations
- 🔍 Enable partial and case-insensitive search
- ❤️ Add favorite books feature
- 📚 Recommend books using multiple preferences
- 🌐 Connect to an online book database API

---

# 👩‍💻 Author

### Mansi Sharma

This project is a part of CodSoft AI internship.
