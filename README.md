# Flashcard App

This is a simple flashcard application built with Python and Tkinter to help you learn and memorize French words.

## Features

- **Learn French Words**: Displays French words on flashcards.
- **Reveal Translation**: Flip the card to see the English translation.
- **Track Progress**: Mark words you know, and they won't be shown again.
- **Persistent Learning**: The app saves your progress, so you can pick up where you left off.

## Setup and Usage

### Prerequisites

- Python 3
- `pip` for installing packages

### Installation

1. **Clone the repository and navigate into the directory:**
   ```bash
   # Make sure to replace the URL with the actual URL of the repository
   git clone https://github.com/Vroom101/Flash-card-app
   cd Flash-card-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the application, run the following command:
```bash
python main.py
```

## How It Works

The application uses a CSV file (`data/french_words.csv`) containing a list of French words and their English translations.

- When you start the app, it loads words from `data/words_to_learn.csv` if it exists. This file contains the words you still need to learn from your previous session.
- If `data/words_to_learn.csv` is not found, it loads the full list from `data/french_words.csv`.
- A random French word is displayed. After 3 seconds, the card automatically flips to show the English translation.
- If you know the word, click the "right" button. The word is removed from your learning list, and your progress is saved to `data/words_to_learn.csv`.
- If you don't know the word, click the "wrong" button to see the next card. The current word will remain in your learning list.
