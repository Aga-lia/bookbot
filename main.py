import os
file_path = os.path.expanduser("~/workspace/github.com/Aga-lia/bookbot/books/frankenstein.txt")

def main():
    text = get_text(file_path)
    num_words = get_num_words(text)
    char_dict = get_dict_char(text)
    char_list = get_list_dict(char_dict)
    ordered_list = get_sorted_list(char_list)
    report = create_report(file_path, num_words, ordered_list)
    #print(ordered_list)
    print(report)


def get_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

def get_num_words(text):
    words = text.split()
    return len(words)

def get_dict_char(text):
    char_dict = {}
    for i in text:
        i_low = i.lower()
        if i_low in char_dict:
            char_dict[i_low] += 1
        else:
            char_dict[i_low] = 1
    return char_dict

def get_list_dict(char_dict):
    list_of_char_dict = []
    for char in char_dict:
        charac = char_dict[char]
        list_of_char_dict.append({char : charac})
    return list_of_char_dict

def sort_on(dict):
    for i in dict:
        return dict[i]

def get_sorted_list(char_list):
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def create_report(file_path, num_words, ordered_list):
    nice_report1 = f"--- Report for {file_path} ---\n"
    nice_report2 = f"\nThis text contains {num_words} words\n"
    nice_report3 = ""
    for i in ordered_list:
        key = (list(i))
        value = (list(i.values()))
        if (key[0].isalpha()) == True :
            nice_report3 += (f"\nThe letter '{key[0]}' is present {value[0]} time")
    report = nice_report1 + nice_report2 + nice_report3
    return report

main()


