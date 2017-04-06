"""
    minimal.py
    Find the minimum distance between two phrases inside a text,
    that does not include the negation word.
"""
import re

def get_separated_strings(text, separators):
    """ Return list of sentences from a text """
    sentences = []
    parsed_text = re.split("(\.|!!!)", text.strip())

    index = 0
    max_length = len(parsed_text)

    while index + 1 < max_length:
        sentences.append(parsed_text[index].strip() + parsed_text[index + 1].strip())
        index += 2

    return sentences

def get_distance_between_phrases(sentence, phrase1, phrase2, neg):
    """
        finds the distance between 2 phrases in sentence, ignores if it
        has the negation word in them
    """

    ph1_loc = sentence.find(phrase1)
    ph2_loc = sentence.find(phrase2)
    neg_loc = sentence.find(neg)

    # Check that pharse2 comes after pharse 1
    # Check that negation word isn't between phrase 1 and 2
    if ph1_loc > ph2_loc or (neg_loc > ph1_loc and neg_loc < ph2_loc):
        return -1

    serach_start = ph1_loc + len(phrase1)
    sentence_part = sentence[serach_start:ph2_loc]
    word_count = len(re.split('\W', sentence_part.strip()))

    return (word_count, sentence)


def get_distances(sentences, phrase1, phrase2, neg):
    """
        find the distance between phrases in each sentence
        returns a list of tuples with distance and the sentence
    """
    distances = []
    for sentence in sentences:
        dist = get_distance_between_phrases(sentence, phrase1, phrase2, neg)
        if dist != -1:
            distances.append(dist)

    return distances

def main():
    """ Handle script structure """

    print('--- minimal.py ---')

    # Read all input from user
    text = input('Text: ')
    phrase1 = input('Phrase1: ')
    phrase2 = input('Phrase2: ')
    neg = input('Negation word: ')

    sentences = get_separated_strings(text, SENTENCE_SEPARATORS)
    distances = get_distances(sentences, phrase1, phrase2, neg)

    minimal_distance = min(distances)
    print('--- Result ---')
    print('Sentence:' + minimal_distance[1])
    print('Distance between phrases: ' + str(minimal_distance[0]))

if __name__ == "__main__":
    main()
