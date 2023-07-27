def check_todo(text):
    if text == "":
        raise Exception("There are no tasks.")
    if "#TODO" in text:
        return "Don't forget this"
    return "All done!"