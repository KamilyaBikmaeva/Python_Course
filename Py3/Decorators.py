import time


def max_freq(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        max_freq_word = ''
        max_count = 0
        for key in result:
            if result[key] > max_count:
                max_count = result[key]
                max_freq_word = key
        print(f'Most frequent word in sentence "{max_freq_word}", used {max_count} times')
        return result

    return wrapper


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        consumed = time.time() - start
        print(f'Took {consumed} seconds')
        return res
    return wrapper


@max_freq
@time_it
def count_words(string):
    words = str.split(string, ' ')
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    return words_freq


if __name__ == '__main__':
    sentence = 'Never gonna give you up Never gonna let you down Never gonna run around'
    print(count_words(sentence))
