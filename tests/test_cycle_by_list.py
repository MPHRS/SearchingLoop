from cycle_by_list.cycle_by_list import (iscycle, dict_from_graph, isonegraph)
import pytest

# Test_Data for cycle
data_1 = ([[2,3], [1,2], [4,3], [4,5], [2,4]],True) # cycle in the middle of chain 
data_2 = ([[1,2], [2,3], [3,5], [3,4]],False) # straight chain
data_3 = ([[1,2], [2,3], [1,3],  [3,4], [4,5], [5,6], [5,7]],True) # cycle at the beggining of chain, and at the end with branching
data_4 = ([[1,2], [2,3], [3,4], [4,5], [5,6], [5,7], [5,8]],False) # chain at the end with branching
data_5 = ([[1,2], [2,3], [3,1]],True)  #pure cycle of three beads
data_6 = ([[1,2], [2,3]], False) # straight chain
data_7 = ([[1,2], [2,3], [2,4], [3,5], [1,6]], False) # branchibg in the middle
data_8 = ([[1,2], [2,3], [3,4], [2,5], [2, 6], [5,7]], False) # multiply side branch
data_9 = ([[1,2], [2,3], [2,4], [2,5], [2, 6], [1,7]], False) # multiply side branch
data_10 = ([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,1]], True) # long cycle of 8 beads
#Test data for isonegraph
data_11 = ([[1,2],[3,4]],False) # two chains of 2 beads
data_12 = ([[1,2],[3,4], [2,5], [5,6], [2,7]],False) # one branching chain and short
data_13 = ([[1,2],[2,3], [3,4]],True) # one chain
data_14 = ([[1,2],[2,3], [3,4], [4,5], [6,7], [7,8], [8,9] ],False) # one large chain



@pytest.mark.parametrize("bonds, expected_result", [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10])
def test_iscycle(bonds, expected_result):
    assert iscycle(bonds) == expected_result

@pytest.mark.parametrize("bonds, expected_result", [data_11, data_12, data_13,data_14])
def test_isonegraph(bonds, expected_result):     
    assert  isonegraph(bonds) == expected_result 


