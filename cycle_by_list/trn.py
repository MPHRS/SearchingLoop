# import numpy as np


# class Node():

#     def __init__(self, inf):
#         self.inf = inf
#         self.next = None
#         self.previous = None
#     def __str__(self):
#         return f'{self.inf}->{self.next}'
#     def coordinate():
#         pass
    
# class LinkedList():
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         return str(self.head)
    
#     def sborka(self, nodes):
#         self.head = nodes[0]
#         tmp = self.head
#         new_nodes = []
#         set_of_nodes = {tmp.inf}
#         i = 0
#         for element in nodes[1:]:
#             # if not tmp.next in set_of_nodes:
#                 if tmp.next in set_of_nodes:
#                     i=1
#                 if tmp.next == element.inf:
#                     tmp.next = element
#                     tmp = element
#                     set_of_nodes.add(tmp.inf)
#                 else:
#                     new_nodes.append(element)
#             # else:
#             #     tmp.next = element.inf
#             #     tmp = element
#         if i == 1:
#             print('here we have cycle')
#         return new_nodes
    
# def nodes_list(n_list):
#         nodes = []
#         for element in n_list:
#             nodes.append(Node(element[0]))
#             nodes[-1].next = element[1]   
#         return nodes 

# def list_of_linked(nodes):
#     chains = []
#     while True:
#         temp = LinkedList()
#         nodes = temp.sborka(nodes)
#         chains.append(temp)
#         if len(nodes) == 0:
#             break
#     return chains


# if __name__ == '__main__':
#     our_data = [[1,4], [1,6], [2,3], [5,6],  [5,7], [6,7]]
#     nodes = nodes_list(our_data)
#     print(nodes[0])
#     chains = list_of_linked(nodes)
#     [print(el) for el in chains]


#     """def iscycle(bonds: list[int]) -> bool
#        return (False/True)
       
#        def isonegraph(bonds: list[int]) -> bool
#         return (False/True)"""
tt = [[5, 2], [0, 1]]  
pp = [[0, 0], [0, 0]]
for el, j in tt, range(len(tt)):
    for i in range(2):
        pp[j][i] = el[-i]