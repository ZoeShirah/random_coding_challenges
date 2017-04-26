def wordpattern(pattern, input):

    var_set = set([char for char in pattern])
    var_list = [char for char in pattern]

    patters = dict()
    curr = ""
    for i in range(len(input)):
        if input[i] in curr:
            for m in range(len(curr)):
                if input[i] == curr[m]:
                    match = True
                    l = 1
                    while match:
                        if i+l < len(input) and m+l < len(curr):
                            if input[i+l] != curr[m+l]:
                                match = False
                            else:
                                l = l+1
                        else:
                            match = False
                    if l > 1:
                        patters[curr[m:m+l]] = None
                        curr = curr[:m]+curr[m+l:]
                        i = i+l
                        break
                    else:
                        curr += input[i]
        else:
            curr += input[i]

    print patters

    pattern_match = ''
    i = 0
    for i in range(len(input)):
        for item in patters:
            print item
            chars = len(item)
            if input[:chars] == item:
                if patters[item]:
                    pattern_match += patters[item]
                    input = input[chars:]
                elif var_set:
                    patters[item] = var_list[0]
                    taken = var_list.pop(0)
                    var_set.remove(taken)
                    while var_list[0] == taken:
                        var_list.pop(0)
                        if not var_list:
                            break

    print pattern_match

    if pattern_match == pattern:
        return 1
    return 0
