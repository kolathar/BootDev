#=========================================================================================
#                            Main Function of BookBot
#
#   Purpose: Analyze a book's text as a string and print stats to the terminal
#=========================================================================================

#python imports
import sys


#import functions from stats.py
from stats import get_word_count , get_character_dict , chars_dict_to_sorted_list


# call book contents from file, and return body of book as string
def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents


#print out a report to the terminal
def report_printer(book_path, word_count, sorted_char_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for entry in sorted_char_list:
    character, count = entry
    if str.isalpha(character):
      print(f"{character}: {count}")
  print("============= END ===============")
  return


###   MAIN PROGRAM DEFINITION   ###

def main():

  #check book path given at run
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  #define book path
  book_path = sys.argv[1]

  # call get_book_text and save contents into a variable to pass through funtions
  book_text = get_book_text(book_path)

  #stats functions
  word_count = get_word_count(book_text)
  char_dict = get_character_dict(book_text)
  sorted_char_list = chars_dict_to_sorted_list(char_dict)

  #report funciton
  report_printer(book_path, word_count, sorted_char_list)

#-------------------------------------------------------------------------------------------------------------------

main()
