class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries should have a title and contents.")
        self.title = title
        self.contents = contents
        self.full_entry = self.title + " " + self.contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}" 
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        # return "My Title: Some contents"
    

    def count_words(self):
        return len(self.full_entry.split())
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm == 0:
            raise Exception("You can't read.")
        return round(len(self.contents.split()) / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        # reading_time = int(len(self.contents.split()) / wpm)
        # for reading_time 

        # return self.contents.split() / wpm
        readable_words = wpm * minutes
        words = self.contents.split()
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + readable_words
        chunk = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk)