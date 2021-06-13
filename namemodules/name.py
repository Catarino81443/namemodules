def printName(full_name):
    name = full_name.split()
    no_prep = []
    for ele in name:
        if ele.lower() not in ["da", "das", "de", "do", "dos", "e"]:
            no_prep += [ele]
    if len(no_prep) == 1:
        print(f"First name: {no_prep[0]}")
    elif len(no_prep) == 2:
        print(f"First name: {no_prep[0]}\nLast name: {no_prep[-1]}")
    else:
        print(f"First name: {no_prep[0]}\nSecond Name: {no_prep[1]}\nLast names: {no_prep[2:]}")