def counter(text):
    splitup = text.split()
    count = len(splitup)
    return count

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def char_count(text):
    dict = {}
    for char in text:
        lower = char.lower()
        if lower.isalpha() == False:
            continue
        if lower in dict:
            dict[lower] += 1
        else:
            dict[lower] = 1
    return dict

def sorter(dict):
    sorted = []
    for item in dict:
        add = {"char": item, "num": dict[item]}
        sorted.append(add)
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(items):
    return items["num"]