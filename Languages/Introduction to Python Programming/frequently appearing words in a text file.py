# Question 5: 10 most frequently appearing words in a text file

from collections import Counter

def frequent_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower().split()
        word_count = Counter(text)
        most_common = word_count.most_common(10)
        return most_common

file_path = input("Enter the file path: ")
print(frequent_words(file_path))
