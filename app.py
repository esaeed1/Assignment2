from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "What’s the smartest insect? A spelling bee!",
    "Why did the scarecrow win a Nobel prize? Because she was outstanding in her field.",
    "What did one pickle say to the other? Dill with it.",
    "Why cant you ever tell a joke around glass? It could crack up.",
    "Why did the lamp sink? It was too light.",
    "How do billboards talk? Sign language.",
    "What did the ocean say to the shore? Nothing, it just waved!",
    "Did you hear the joke about the roof? Never mind, it would go over your head.",
    "What animal is always at a baseball game? A bat.",
    "My boss told me to have a good day? So I went home."
]


@app.route('/')
def get_joke():
    random_joke = random.choice(jokes)
    question, answer = random_joke.split('? ')
    formatted_joke = f"Question: {question}?<br>Answer: {answer}"
    return formatted_joke


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
