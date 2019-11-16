import random


def encrypt(text):
    words = text.split()
    result = [''.join(random.sample(i, len(i))) for i in words]
    return ''.join(result)


def build_dict(word_dict):

    words_by_length = {}
    for word in word_dict:
        key = len(word)
        if key in words_by_length:
            words_by_length[key].append(word)
        else:
            words_by_length[key] = [word]

    return words_by_length


def decrypt(text, dictionary, result=None):
    if not result:
        result = ()
    if len(text) == 0:
        return ' '.join(result)
    for length in sorted(dictionary.keys()):
        word = sorted(text[:length])
        for dict_word in dictionary[length]:
            if word == sorted(dict_word):
                next_result = result + (dict_word,)
                new_text = text[length:]
                s = decrypt(new_text, dictionary, next_result)
                if s:
                    return s
    return None


patter = "there was a fisherman named fisher who fished for some fish in a fissure till a " \
         "fish with a grin pulled the fisherman in now theyre fishing the fissure for fisher"
code = encrypt(patter)
word_dict = build_dict(set(patter.split()))

print(decrypt(code, word_dict))
