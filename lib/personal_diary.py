def make_snippet(string):
    result = string.split()[:5]
    if len(result) <= 5:
        return " ".join(result)
    else:
        return " ".join(result) + "..."
