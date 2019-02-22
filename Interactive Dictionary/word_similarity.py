#  A good way to check if the user mistyped a word
import difflib
from difflib import SequenceMatcher

print(SequenceMatcher(None, "rainn", "rain").ratio())