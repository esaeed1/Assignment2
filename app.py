from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

original_jokes = [
    "What is the smartest insect? A spelling bee!",
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


def get_jokes(num):
    random_jokes = random.sample(original_jokes, num)
    formatted_jokes = []

    for joke in random_jokes:
        question, answer = joke.split('? ')
        formatted_joke = {
            "Question": question,
            "Answer": answer
        }
        formatted_jokes.append(formatted_joke)

    return formatted_jokes


@app.route('/jokes', methods=['GET'])
def get_jokes_route():
    num = request.args.get('num', default=1, type=int)
    jokes_to_return = get_jokes(num)

    response_data = json.dumps(jokes_to_return, indent=4)

    return response_data, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
