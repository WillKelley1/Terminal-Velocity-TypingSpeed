# Typing Speed Test Made from Python

import time

# Function to calculate the WPM
def calculate_wpm(start_time, end_time, word_count):
    total_time_minutes = (end_time - start_time) / 60
    wpm = word_count / total_time_minutes
    return wpm

# Function to calculate accuracy
def calculate_accuracy(input_text, reference_text):
    input_words = input_text.split()
    reference_words = reference_text.split()
    correct_words = sum(1 for i, word in enumerate(input_words) if i < len(reference_words) and word == reference_words[i])
    total_words = len(reference_words)
    accuracy = (correct_words / total_words) * 100
    return accuracy

# Sample text for typing
sample_text = """The quick brown fox jumps over the lazy dog. 
This is a common English sentence that contains all of the letters of the alphabet. 
It's used to test typing speed and accuracy."""

# Display instructions and the sample text
print("Type the following text as quickly and accurately as possible:\n")
print(sample_text)
input("Press Enter to start...")

# Start timing
start_time = time.time()
typed_text = input("\nStart typing here:\n")
end_time = time.time()

# Calculate results
word_count = len(sample_text.split())
wpm = calculate_wpm(start_time, end_time, word_count)
accuracy = calculate_accuracy(typed_text, sample_text)

# Display results
print(f"\nResults: ")
print(f"Words per Minute (WPM): {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
