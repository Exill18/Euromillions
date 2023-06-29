greetings = {
    'hola': 'Hello!',
    'hello': 'Hi!',
    'hi': 'Hey!',
    'hey!': 'Hi there!',
    'hey': 'Howdy!',
    'sup': 'Whats up?',
    'howdy': 'Hello!'
}

def generate_response(greeting):
    greeting_lower = greeting.lower()
    if greeting_lower in greetings:
        return greetings[greeting_lower]
    else:
        response = input("What should I say? ")
        greetings[greeting_lower] = response
        return "Response added!"

while True:
    user_input = input("You: ")
    ai_response = generate_response(user_input)
    print(f"AI: {ai_response}")

