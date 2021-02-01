import json
import difflib

data = json.load(open('data.json'))


def search(w):
    _word_ = w.lower()
    try:
        return data[_word_]
    except:
        words = difflib.get_close_matches(_word_, data.keys(), cutoff=0.8)
        if len(words) > 0:
            print(f'did you mean %s instead? Click Y for yes and N for No' % words[0])
            try_again = input('Y or N: ')
            if try_again.upper() == 'Y':
                return search(words[0])
            elif try_again == 'N':
                return "Word doesn't exist"
            else:
                return 'We did not understand your query'
        else:
            print('This word does not exist in the dictionary.')


word = input('Enter a word: ')

output = search(word)

if type(output) == list:
    for item in output:
        print(item)