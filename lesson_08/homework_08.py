list_for_sum = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

def sum_of_list(el_list):
    el = 0
    for e in el_list:
        el += e
    return el

def check_of_numb(s):
    el = s.split(',')
    numb_el = []
    for numb in el:
        try:
            numb_el.append(int(numb))
        except ValueError:
            print(f"Can't convert '{numb}' to an integer. Skipping...")
            return None

    return numb_el

for l in list_for_sum:
    ch_list = check_of_numb(l)
    if ch_list is not None:
        print(f"The sum of list {ch_list}: {sum_of_list(ch_list)}")
    else:
        print(f"Can't do it for list {l}")
