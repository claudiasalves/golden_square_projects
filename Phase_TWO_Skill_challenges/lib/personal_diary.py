def make_snippet(string):
    if len(string.split()) <= 5:
        return string
    return " ".join(string.split()[:5]) + "..."