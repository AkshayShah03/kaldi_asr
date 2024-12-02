import spacy_udpipe
from collections import Counter
import sys

def load_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def analyze_text(text):
    # Load the Hindi language model
    spacy_udpipe.download("hi")
    nlp = spacy_udpipe.load("hi")

    # Tokenize and POS tagging
    doc = nlp(text)

    # Counting POS tags
    pos_counts = Counter([token.pos_ for token in doc])

    # Extracting unique nouns, pronouns, etc.
    unique_pos = {}

    for token in doc:
        pos = token.pos_
        if pos not in unique_pos:
            unique_pos[pos] = set()
        unique_pos[pos].add(token.text)

    # Print results
    print(f"Total Sentences: {len(list(doc.sents))}")
    print(f"Total Words: {len(doc)}")
    for pos, count in pos_counts.items():
        print(f"{pos}: {count} (Unique: {len(unique_pos[pos])})")

def main(file_path):
    text = load_text_file(file_path)
    analyze_text(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_hindi_text.py <file_path>")
    else:
        file_path = sys.argv[1]
        main(file_path)

