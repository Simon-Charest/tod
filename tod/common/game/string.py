def pluralize(word, count=2):
    return word if count <= 1 else f"{word}s"
