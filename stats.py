def count_words(file):
    num_words=len(file.split())
    print(num_words,' words found in the document')

def count_characters(file):
    file=file.lower()
    chars={}
    for i in file:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def dict_to_sorted_list(dict):
    sorted_chars = []
    for i in dict.keys():
        sorted_chars.append({'char': i, 'num': dict[i]})

    sorted_chars = sorted(sorted_chars, key=lambda x: x['num'], reverse=True)

    print('--------------------------------')
    print('Sorted characters by frequency:')
    for i in sorted_chars:
        print(i['char'], ':', i['num'])
    print('--------------------------------')