import re
from bs4 import BeautifulSoup
import requests


def word_frequency(arg1, arg_type, arg3=True):
    """Takes a file or string as arguments and  returns a generator of word frequencies
          of form (frequency, word). By default, returns words sorted by frequencies in descending
          order, to get values in descending order pass True as an argument."""
    if arg_type == 'f':
        try:
            text = open(arg1)
            lines = text.__iter__()
        except FileNotFoundError:
            print(f"No file '{arg1}' in current directory.")
            quit()
    elif arg_type == 's' and isinstance(arg1, str):
        text = arg1
        lines = text.split('\n')
    else:
        print("Invalid Type")
        quit()
    count_dict = dict()
    try:
        # There is no need of the outer for loop and the whole process can just be done by
        # re.findall on entire contents of file/string, but for loop makes it memory efficient in case
        #  the file/string is too large to be read at once.
        for line in lines:
            words = re.findall("\b?([a-z0-9]+)\b?", line.lower())
            # Instead of re.findall, line.translate(maketrans("", "", string.punctuation)).lower().split() can also
            # be used, but I observed that string.punctuation doesn't have all the symbols that need to
            # removed and this method counts words like "mind-numbing" as one word "mind-numbing".
            # There are none of the above problems with re.findall method.

            for word in words:
                count_dict[word] = count_dict.get(word, 0) + 1
    except UnicodeDecodeError:
        print("File in unsupported format")
        quit()
    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=arg3)
    for items in count_list:
        yield items


############ Below are the functions meant for scraping wikipedia #####################


def short_def(search_):
    """Scrapes wikipedia to return a short defeniton of string as argument."""
    source = requests.get(f'https://en.wikipedia.org/wiki/{search_}').text

    soup = BeautifulSoup(source, 'lxml')
    intrs = soup.body
    intrs = intrs.find('div', class_='mw-body')
    intrs = intrs.find('div', class_='vector-body')
    intrs_list = intrs.find_all('p', class_='')
    for item in intrs_list:
        if item.b:
            intrs = item
            break
    heading = intrs.b.text
    if heading.startswith('Other reasons this'):
        return "Sorry, your search can't be found. Try again with different words."

    if intrs.text.endswith('may refer to:\n'):
        return "Sorry, your search can't be found. Try again with different words."

    return f">>>{heading.title()}\n{intrs.text}"


def wiki(search_):
    """A modified version of short_def, which returns the definition of argument as well as
    definitions of all the keywords found within the definition of argument."""
    source = requests.get(f'https://en.wikipedia.org/wiki/{search_}').text

    soup = BeautifulSoup(source, 'lxml')
    intrs = soup.body
    intrs = intrs.find('div', class_='mw-body')
    intrs = intrs.find('div', class_='vector-body')
    intrs_list = intrs.find_all('p', class_='')
    for item in intrs_list:
        if item.b:
            intrs = item
            break
    sl = [search_]
    for x in intrs.find_all('a'):
        try:
            sl.append(x['title'])
        except KeyError:
            continue
    for s in sl:
        yield short_def(s)
