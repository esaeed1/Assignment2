from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

original_jokes = [
    "What’s the smartest insect? A spelling bee!",
    "Why did the scarecrow win a Nobel prize? Because she was outstanding in her field.",
    "What did one pickle say to the other? Dill with it.",
    "Why can't you ever tell a joke around glass? It could crack up.",
    "Why did the lamp sink? It was too light.",
    "How do billboards talk? Sign language.",
    "What did the ocean say to the shore? Nothing, it just waved!",
    "Did you hear the joke about the roof? Never mind, it would go over your head.",
    "What animal is always at a baseball game? A bat.",
    "My boss told me to have a good day? So I went home."
]

jokes = original_jokes.copy()


def reset_jokes():
    global jokes
    jokes = original_jokes.copy()


def get_jokes(num):
    global jokes
    formatted_jokes = []

    if len(jokes) == 0:
        reset_jokes()

    for i in range(num):
        random_joke = random.choice(jokes)
        question, answer = random_joke.split('? ')
        formatted_joke = {
            "Question": question,
            "Answer": answer
        }
        formatted_jokes.append(formatted_joke)
        jokes.remove(random_joke)

    return formatted_jokes


@app.route('/jokes', methods=['GET'])
def get_jokes_route():
    num = request.args.get('num', default=1, type=int)
    jokes_to_return = get_jokes(num)

    response = jsonify(jokes_to_return)
    response_data = json.dumps(response.json, indent=4)

    return response_data, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
