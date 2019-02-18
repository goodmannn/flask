def is_isbn_or_key(word: str):
    """
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(word) and short_word.isdigit():
        isbn_or_key = 'key'

    return isbn_or_key
