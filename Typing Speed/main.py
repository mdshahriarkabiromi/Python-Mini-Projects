import time
import random

def typing_tester():
    # List of sample texts to test the user's typing speed and accuracy
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "A quick movement of the enemy will jeopardize five gunboats.",
        "The five boxing wizards jump quickly."
    ]

    # Select a random sample text
    sample_text = random.choice(sample_texts)
    
    # Start timer
    start_time = time.time()

    # Get user input
    user_input = input("Type the following text: " + sample_text + "\n")

    # End timer
    end_time = time.time()

    # Calculate typing speed in characters per second
    typing_speed_cps = len(sample_text) / (end_time - start_time)

    # Calculate accuracy
    accuracy = 0
    for i in range(len(sample_text)):
        if i < len(user_input) and sample_text[i] == user_input[i]:
            accuracy += 1
    accuracy = accuracy / len(sample_text) * 100

    # Print results
    print("Typing speed: {:.2f} characters per second".format(typing_speed_cps))
    print("Accuracy: {:.2f}%".format(accuracy))

typing_tester()
