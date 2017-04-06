"""
    minimal.py
    Find the minimum distance between two phrases inside a text,
    that does not include the negation word.
"""
import re

SENTENCE_SEPARATORS = ['.', '!!!']

def get_next_seperator_index(text, start, separators):
    """
        Get the location of the next seperator in the text (starting at start),
        return -1 if none found
    """

    locations = []
    for sep in separators:
        curr_location = text.find(sep, start)
        if curr_location != -1:
            locations.append((curr_location, len(sep)))

    # If there were no locations found return -1
    if len(locations) == 0:
        return -1

    return min(locations)

def get_separated_strings(text, separators):
    """ Return list of sentences from a text """
    sentences = []
    curr_index = 0

    sep_tuple = get_next_seperator_index(text, 0, separators)
    while sep_tuple != -1:
        # Parse the recieved tuple for location and length
        # and calculate the new location for the substring
        sep_loc = sep_tuple[0]
        sep_len = sep_tuple[1]
        new_location = sep_loc + sep_len + 1

        # Save the sentence to the list without extra spaces.
        sentences.append(text[curr_index:new_location].strip())

        # Find the next sentence
        curr_index = new_location
        sep_tuple = get_next_seperator_index(text, curr_index, separators)

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
