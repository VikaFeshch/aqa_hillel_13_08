import re


def average_of_list(lst):
    return sum(lst) / len(lst)

def find_substring(str1, str2):
    num_incl = -1
    num_incl = str1.find(str2)
    return num_incl

def change_formate_date(i_d, sep="."):
    return sep.join(map(str, i_d))

def count_words(ch_text):
    text_sentences = re.split(r'(?<=[.!?])\s+', ch_text)
    return len(text_sentences[len(text_sentences) - 1].split())