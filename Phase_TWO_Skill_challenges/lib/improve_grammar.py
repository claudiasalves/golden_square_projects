def improve_grammar(text):
    if text == "":
        raise Exception("There is no text to analyse.")
    if text[0].isupper() and text[-1] in [".", "?", "!"]:
        return True
    return False