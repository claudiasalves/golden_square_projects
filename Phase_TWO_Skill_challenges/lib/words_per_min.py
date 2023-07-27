

def reading_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for empty text.")
    words = text.split()
    word_count = len(words)
    return word_count / 200




    # word_seconds = 200 / 60
    # string_list = len(text.split())
    # time_per_word = string_list / word_seconds
    # time_per_string = str(datetime.timedelta(seconds = time_per_word))
    # print(time_per_word)
    # return f"I read this text in " + time_per_string