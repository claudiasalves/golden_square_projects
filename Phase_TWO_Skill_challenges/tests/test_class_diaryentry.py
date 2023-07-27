from lib.class_diaryentry import *
import pytest

"""
Given a title and contents
Format the entry like "My Entry: tese are the contents.
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

"""
given empy title
raise an error
"""
def test_no_title():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "Some contents")
    error_message = str(e.value)
    assert error_message == "Diary entries should have a title and contents."

"""
given empy contents
raise an error
"""
def test_no_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("My Title", "")
    error_message = str(e.value)
    assert error_message == "Diary entries should have a title and contents."

"""
Given a title and contents
return the number of words in the diary entry
"""
def test_word_count():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

def test_word_count_with_no_words():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Diary entries should have a title and contents."

"""
Given contents of 2 words
and wpm of 2
return the estimate reading time of 1minute
"""
def test_reading_speed():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given contents of 4 words
and wpm of 2
return the estimate reading time of 2 minutes
"""
def test_reading_speed_with_4_words():
    diary_entry = DiaryEntry("My Title", "Some contents and more")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given contents of 3 words
and wpm of 2
return the estimate reading time of 2 minutes
"""
def test_reading_speed_with_4_words():
    diary_entry = DiaryEntry("My Title", "Some contents and")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_no_speed():
    diary_entry = DiaryEntry("My Title", "Some contents and")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "You can't read."
"""
Given contents of six words
given a wpm of 2
and reading time of 1 minutes
return 2 first strings that can be read
"""
def test_what_strings_can_be_read_in_1():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

"""
Given contents of six words
given a wpm of 2
and reading time of 2 minutes
return 2 first strings that can be read
"""
def test_what_strings_can_be_read_in_2():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

"""
Given contents of 6 words
and wpm of 2 and 1 minute
first time #chunk returns "one two"
next time "three four"
"""

def test_does_not_repeat_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
