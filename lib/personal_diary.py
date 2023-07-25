def make_snippet(string):
    result = string.split()
    if len(result) > 5:
        return " ".join(result[:5]) + "..."
    return string
