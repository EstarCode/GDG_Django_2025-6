def word_frequency(sentences):
    words = sentences.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    print(freq)


def main():
    sentence = input("Enter a sentence: ")
    result = word_frequency(sentence)
    return result


if __name__ == "__main__":
    main()
