# coding=utf-8

# Created by lruoran on 16-12-21


def remove_redundant_blank(codes):
    new_codes = []
    for code in codes:
        tmp = ''
        flag = False
        idx = 0
        while idx < len(code):
            if code[idx].isalnum():
                flag = True
            if flag and idx < len(code)-1 and code[idx].isspace() and code[idx+1].isspace():
                idx += 1
                continue
            tmp += code[idx]
            idx += 1
        new_codes.append(tmp)
    return '\n'.join(new_codes)