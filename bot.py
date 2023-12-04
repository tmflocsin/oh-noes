import json

# Load JSON data for responses
def load_responses(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)

# Save the updated responses to the JSON file
def save_responses(file, data):
    with open(file, 'w') as bot_responses:
        json.dump(data, bot_responses, indent=2)

# Store JSON data for responses
response_data = load_responses("responses.json")

# Find the best match in responses and return the corresponding answer and keywords
def find_best_match(user_input: str, responses: dict) -> str | None:
    for question, answer in responses.items():
        for keyword in response_data[question]["keywords"]:
            if keyword.lower() in user_input.lower():
                return answer
    return None

# Main chatbot function
def chatbot():
    while True:
        # Define a list of stop words to exclude from keywords
        stop_words = [
            "a", "an", "and", "are", "as", "at", "be", "for", "from", "has", "he", "in", "is", "what", "give",
            "recipe", "tell", "about", "do", "know", "where", "how", "to", "cook", "ingredients", "make", 
            "bake", "fry", "boil", "grill", "roast", "prepare", "method", "step", "by", "can", "you", "food",
            "me", "list", "of","it", "its", "on", "that", "the", "was", "were", "will", "with", "dish"
        ]

        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break

        # Check for responses
        answer_data = find_best_match(user_input, response_data)

        if user_input == "":
            print("Bot: Please type something so we can chat :(")
        elif answer_data:
            print(f"Bot: {answer_data['answer']}")
        else:
            # If the bot doesn't know the answer, ask the user
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                # Extracting keywords from the user's input and removing stop words
                keywords = [word for word in user_input.lower().split() if word not in stop_words]

                # Add the new entry to the knowledge base with keywords
                response_data[user_input] = {
                    "answer": new_answer,
                    "keywords": keywords
                }

                save_responses('responses.json', response_data)
                print("Bot: Thank you! I've learned something new.")


if __name__ == "__main__":
    chatbot()
