from typing import Dict


def dict_from_graph(data) -> Dict:
    """ Making a dictionary with all bonds
    
    input param:
    data - list of bonds: [[bond_1], [..], [bond_n]]
    output params:
    dict_of_bonds: {1_bead: list(beads), .. , n_bead: list(beads)}"""
    dict_of_bonds = dict()
    for node in data:
        for i in node:
            if not i in dict_of_bonds:
                dict_of_bonds[i] = list(node)
            else:
                dict_of_bonds[i].extend(node)
            dict_of_bonds[i].remove(i)
    dict_of_bonds.keys()
    return dict_of_bonds
def iscycle(data) -> bool:
    """ returns true if there is a loop
    input param:
    data - list of bonds: [[bond_1], [..], [bond_n]]"""
    if isonegraph(data):
        dict_of_bonds = dict_from_graph(data)
        visited = set()
        flag = 0
        tmpflag = 0
        for bead in sorted(dict_of_bonds.keys()):
            if len(dict_of_bonds[bead]) == 1:
                continue
            elif len(dict_of_bonds[bead]) == 2:
                tmpflag = 0
                for bonded in sorted(dict_of_bonds[bead]):
                    if not bonded in visited:
                        visited.add(bonded)
                    else:
                        tmpflag += 1
                if tmpflag > 1:
                    flag += 2 
            else:
                for bonded in sorted(dict_of_bonds[bead]):
                    if bonded in visited:
                        flag += 1
                    else:
                        visited.add(bonded)   
        if flag > 1:
            return True
        else:
            return False
    else:
        raise Exception('Data is not corrected - there are more than one chain')

def isonegraph(data) -> bool:
    """ returns true if there are not more than one chain
    input param:
    data - list of bonds: [[bond_1], [..], [bond_n]]"""
    dict_of_bonds = dict_from_graph(data)
    visited = set()
    flag = 0
    for bead in sorted(dict_of_bonds.keys()): 
        for bonded in sorted(dict_of_bonds[bead]):
            if not bonded in visited:
                visited.add(bonded)
        if not bead in visited:
            flag += 1
    if flag > 1:
        return False
    else:
        return True    
    
    
if __name__ == '__main__':
    our_data_1 = [[1,2], [2,3], [3,5], [3,4]]
    print(isonegraph(our_data_1))