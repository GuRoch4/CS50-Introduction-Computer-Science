# TODO:Here is the main function of the program.
def main():
    text = str(input("Text: "))
    letters = c_letters(text)
    words = c_words(text)
    sentences = c_sentences(text)
    liau = c_liau(letters, words, sentences)

    if liau < 1:
        print(f"Before Grade 1")
    elif liau >= 16:
        print(f"Grade 16+")
    else:
        print(f"Grade {liau}")


# TODO: This function counts the number of letters in the
def c_letters(text):
    count = 0
    for i in text:
        if i.isalpha():  # Test if the character is alphabetic
            count += 1
    return count


# TODO: This function counts the number of words in the text
def c_words(text):
    count = 0
    for i in text:
        if i.isspace():  # Test if the character is a white space
            count += 1
    return count + 1


# TODO: This function counts the number of sentences in the text
def c_sentences(text):
    count = 0
    for i in text:
        if i in ['.', '!', '?']:  # Test if the character is between ., ! or ?
            count += 1
    return count


# TODO: This function uses the Coleman-Liau formula to calculate the approximate reading level needed to understand the text
def c_liau(letters, words, sentences):
    l = ((letters / words) * 100)
    s = ((sentences / words) * 100)
    return round(0.0588 * l - 0.296 * s - 15.8)  # Coleman-Liau calculation


main()