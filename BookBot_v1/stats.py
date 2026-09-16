#--------------------------------------------------------
#    Source of stats functions in Book_Bot main.py
#--------------------------------------------------------


# 1 Get basic word count
def get_word_count(book_text):
  words: list = book_text.split()
  return len(words)


# 2 Creating a Character Dictionary with character counts
def get_character_dict(book_text):
  char_dict = {}

  book_text = book_text.lower()
  for l in book_text:
    if l in char_dict:
      value = char_dict[l]
      char_dict[l] = value + 1
    else:
      char_dict[l] = 1
  char_dict = char_dict
  return char_dict


# 3 Sorting Key for chars_dict_to_sorted_list()
def sort_char_on(character: tuple[str, int]) -> int:
  return character[1]


# 4 Sorting a list made from get_character_dict() by character counts
def chars_dict_to_sorted_list(char_dict):
  chars_list = []

  for dict_entry in char_dict:
     count = char_dict[dict_entry]
     entry_tuple = (dict_entry, count)
     chars_list.append(entry_tuple)
  sorted_chars_by_counts = sorted(chars_list, reverse=True, key=sort_char_on)
  return sorted_chars_by_counts




