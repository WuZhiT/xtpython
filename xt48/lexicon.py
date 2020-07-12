lexicon = {
    "north": 'direction',
    "west": 'direction',
    "east": 'direction',
    "south": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "1234": 'number',
    "3": 'number',
    "91234": 'number',
    "ASDFADFASDF": 'error',
    "IAS": 'error' 
}

def scan(sentence):

    results =[]
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type, word))

    return results