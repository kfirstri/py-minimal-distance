"""
    minimal.py
    Find the minimum distance between two phrases inside a text,
    that does not include the negation word.
"""

TEXT_SEPERATORS = ['.', '!!!']

def get_next_seperator_index(text, start):
    """
        Get the location of the next seperator in the text (starting at start),
        return -1 if none found
    """

    locations = []
    for sep in TEXT_SEPERATORS:
        curr_location = text.find(sep, start)
        if curr_location != -1:
            locations.append((curr_location, len(sep)))

    # If there were no locations found return -1
    if len(locations) == 0:
        return -1

    return min(locations)

def get_sentences(text):
    """ Return list of sentences from a text """
    sentences = []
    curr_index = 0

    sep_tuple = get_next_seperator_index(text, 0)
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
        sep_tuple = get_next_seperator_index(text, curr_index)

    return sentences

def main():
    """ Handle script structure """

    print('--- minimal.py ---')

    # Read all input from user
    text = input('Text: ')
    phrase1 = input('Phrase1: ')
    phrase2 = input('Phrase2: ')
    neg = input('Negation word: ')

    sentences = get_sentences(text)

if __name__ == "__main__":
    main()
