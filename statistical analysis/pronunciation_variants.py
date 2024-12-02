from collections import defaultdict
import re

# Example function to normalize phonemes
def normalize_phonemes(phonemes):
    # Normalizes phonemes by removing extra spaces and ensuring consistent format
    phonemes = phonemes.strip()
    phonemes = re.sub(r'\s+', ' ', phonemes)  # Replace multiple spaces with single space
    return phonemes

# Example function to generate pronunciation variants
def generate_pronunciation_variants(word_phoneme_dict):
    pronunciation_variants = defaultdict(list)
    
    # Iterate through the word-phoneme dictionary
    for word, phonemes in word_phoneme_dict.items():
        phonemes = normalize_phonemes(phonemes)
        phoneme_list = phonemes.split()
        
        # Simple logic to generate variants (add your own logic as needed)
        # For example, for homophones or different pronunciations:
        if 'a' in phoneme_list:
            variant = phoneme_list[:]
            variant[phoneme_list.index('a')] = 'aa'  # Changing 'a' to 'aa'
            pronunciation_variants[word].append(' '.join(variant))
        
        if 'i' in phoneme_list:
            variant = phoneme_list[:]
            variant[phoneme_list.index('i')] = 'ee'  # Changing 'i' to 'ee'
            pronunciation_variants[word].append(' '.join(variant))

        # Add the original phoneme representation
        pronunciation_variants[word].append(phonemes)
    
    return pronunciation_variants

# Example input: dictionary of Hindi words and their phoneme representations
word_phoneme_dict = {
    'नई': 'n ə i',
    'यात्रा': 'j a t r a',
    'विद्यालय': 'v i d y a l ə y',
    'समुद्र': 's ə m u d r'
}

# Generate pronunciation variants
pronunciation_variants = generate_pronunciation_variants(word_phoneme_dict)

# Print the results
for word, variants in pronunciation_variants.items():
    print(f"Word: {word}")
    for i, variant in enumerate(variants, 1):
        print(f"  Variant {i}: {variant}")
