from ntpath import join


def name_shuffler(str):
    str=str.split()
    name=str[0]
    sur=str[1]

    return ('{} {}'.format(sur , name))


print(name_shuffler('sheriff gaye'))