from functions import cleanup_time
import sys
sys.setrecursionlimit(100)
cleanup_time()
def status(name, **kwargs):
    print(name)
    for key, value in kwargs.items():
        print(key.replace('_', ' ').capitalize(), ':', value)
    return None

#status("William", homosexual=True, has_aids=True, likes_anal=True)

#u=input().split()
#print(u)


def dictmaker(lst: list, dkt=None) -> dict:
    """pass"""
    if dkt is None:
        dkt = {}
    if len(lst) == 0:
        return dkt
    else:
        dkt[lst[0]] = lst[1]
        return dictmaker(lst[2:], dkt)

#n = int(input())
#
#dicts = []
#
#for _ in range(n):
#    info = input().split()
#    dicts.append(dict(zip(info[0::2], info[1::2])))    

def merge_dictionaries(*dicts, **kwargs) -> dict:
    """pass"""
    master_dict: dict = {}
    # If mode, then defualt order priority will be used
    # If not mode, then last dict will overwrite values of the previous
    if 'tiebreaker' in kwargs:
        if kwargs['tiebreaker'] == 'first':
            mode: bool  = True
        else:
            mode: bool = False
    else:
        mode: bool = True
    
    for dkt in dicts:
        for key, value in dkt.items():
            if key in master_dict and mode:
                continue
            elif key in master_dict and not mode:
                master_dict.update({
                    key : value
                })
            else:
                master_dict[key] = value

    

