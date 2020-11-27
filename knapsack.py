# Objects which are divisible, ie we can take fraction
import pprint
def knapsack_divisible(bag_wt,wt_profit_dict):
    import collections
    profit_per_wt_dict = {}
    for obj,value_tup in wt_profit_dict.items():
        profit_per_wt_dict[obj] = round(value_tup[1]/value_tup[0],2)
    profit_per_wt_dict = collections.OrderedDict(sorted\
        (profit_per_wt_dict.items(), key=lambda x:x[1],reverse=True))
    knapsack_dict = {}
    profit = 0
    for obj, kg_price in profit_per_wt_dict.items():
        if bag_wt <= 0 :
            break
        else:
            wt = wt_profit_dict[obj][0]
            if wt > bag_wt:
                wt = bag_wt
            knapsack_dict[obj] = wt
            profit += kg_price*wt
            bag_wt -= wt
    return knapsack_dict, profit

obj_wt_profit = {'A':(2,10),'B':(3,5),'C':(5,15),
                'D':(7,7),'E':(1,6),'F':(4,18),'G':(1,3)}
#print(knapsack_divisible(15,obj_wt_profit))

# dp by tabulation method
def knapsack(bag_wt, wt_profit_dict):
    # dp table, width - bag wt from 0, 
    # height - from 0 to len(list) 
    # dp table is filled with profit values
    wt_profit_list = sorted(wt_profit_dict.items(),key=lambda x: x[1][0])
    wt_profit_list.insert(0,(0,(0,0)))
    dp_dict ={}
    # for profit=0, bag_wt=0
    for col in range(bag_wt+1):
        dp_dict[(0,col)]=0
    # when bag_wt=0, profit=0
    for row in range(len(wt_profit_list)):
        dp_dict[(row,0)] = 0
    # table: height=i, width = bag_wt starts from 0
    for row in range(1,len(wt_profit_list)):
        wt,profit = wt_profit_list[row][1]
        for b_wt in range(bag_wt+1):
            if wt > b_wt:
            # just copy the above value of the table
                dp_dict[(row,b_wt)] = dp_dict[(row-1,b_wt)]
            else:
                dp_dict[(row,b_wt)] = max(dp_dict[(row-1,b_wt)],
                # in the previous row bag_wt-wt of object + profit
                    dp_dict[(row-1, b_wt-wt)] + profit)
    max_profit = dp_dict[len(wt_profit_list)-1,bag_wt]
    find = max_profit
    knapsack_list = []
    # if the find element is from the previous row, 
    # then skip current row
    for row in range(len(wt_profit_list)-1,0,-1):
        find_status = False 
        # check whether the element is in the current row
        for col in range(bag_wt+1):
            if find == dp_dict[(row,col)]:
                find_status = True
                break
        # check whether the element is in the previous row
        for col in range(bag_wt+1):
            if find == dp_dict[(row-1,col)]:
                find_status = False
                break
        # find in which row the element is first appears
        if find_status:
            find -= wt_profit_list[row][1][1]
            knapsack_list.append(wt_profit_list[row][0])
    return max_profit,knapsack_list
    #return max_profit


obj_wt_profit_1 = {'A':(2,1),'B':(3,2),'C':(4,5),'D':(5,6)}
#print(knapsack(15,obj_wt_profit))
#print(knapsack(8,obj_wt_profit_1))

#TODO
# This wont work if the profit is not in the sorted form 
# same as that of wt.
def knapsack_other(bag_wt, wt_profit_dict):
    # dp table, width - bag wt from 0, 
    # height - from 0 to len(list) 
    # dp table is filled with profit values
    wt_profit_list = sorted(wt_profit_dict.items(),key=lambda x: x[1][0])
    wt_profit_list.insert(0,(0,(0,0)))
    dp_dict ={}
    # for profit=0, bag_wt=0
    for col in range(bag_wt+1):
        dp_dict[(0,col)]=0
    # when bag_wt=0, profit=0
    for row in range(len(wt_profit_list)):
        dp_dict[(row,0)] = 0
    # table: height=i, width = bag_wt starts from 0
    for row in range(1,len(wt_profit_list)):
        wt,profit = wt_profit_list[row][1]
        track = 0
        for b_wt in range(bag_wt+1):
            check_wt,check_profit = wt_profit_list[track][1]
            if wt > b_wt:
            # just copy the above value of the table
                dp_dict[(row,b_wt)] = dp_dict[(row-1,b_wt)]
            else:
                if wt+check_wt <= b_wt and track<row:
                    dp_dict[(row,b_wt)] = profit + check_profit
                    track +=1
                else:
                    dp_dict[(row,b_wt)] = dp_dict[(row,b_wt-1)]
    max_profit = dp_dict[len(wt_profit_list)-1,bag_wt]
    return max_profit

def knapsack_set(bag_wt,wt_profit_dict):
    obj_wt_profit_list = sorted(wt_profit_dict.items(),key=lambda x: x[1][0])
    import collections
    import copy
    #list_dict = collections.defaultdict(list)
    list_dict= {'list_0':[(0,0)]}

    for index in range(len(obj_wt_profit_list)):
        wt_obj,profit_obj = obj_wt_profit_list[index][1]
        temp_list = []
        for wt_temp, profit_temp in list_dict[f'list_{index}']:
            temp_list.append((wt_obj+wt_temp,profit_obj+profit_temp))

        list_dict[f'list_{index+1}'] = copy.deepcopy(list_dict[f'list_{index}'])
        p_wt,p_profit = list_dict[f'list_{index+1}'][-1]
        for wt, profit in temp_list:
            if wt > p_wt and wt<=bag_wt:
                list_dict[f'list_{index+1}'].append((wt,profit))
                p_wt,p_profit = wt, profit
            else:
                if profit > p_profit and wt<=bag_wt:
                    list_dict[f'list_{index+1}'].pop()
                    list_dict[f'list_{index+1}'].append((wt,profit))
                    p_wt,p_profit = wt, profit
                else:
                    continue
    max_profit = list_dict[f'list_{len(wt_profit_dict)}'][-1][1]
    find = list_dict[f'list_{len(wt_profit_dict)}'][-1]
    knapsack_list = []
    # if the find (wt,profit) is from the previous list, 
    # then skip current list 

    # list_dict index and obj_wt_profit_list index are different
    for index in range(len(wt_profit_dict)-1,-1,-1):
        find_status = False 
        # check whether the element is in the current list 
        if find in list_dict[f'list_{index+1}']:
            find_status = True
        # check whether the element is in the previous row
        if find in list_dict[f'list_{index}']:
            find_status = False
        # find in which row the element is first appears
        if find_status:
            find = (find[0]-obj_wt_profit_list[index][1][0],\
                find[1]-obj_wt_profit_list[index][1][1])
            knapsack_list.append(obj_wt_profit_list[index][0])
    #
    return max_profit,knapsack_list
#print(knapsack_set(15,obj_wt_profit))
#print(knapsack(15,obj_wt_profit))


def generate_dict(num):
    import random
    char = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    d = {}
    for i in range(num):
        n = i 
        char_selection = []
        while True:
            x,y=divmod(n,26)
            char_selection.append(y)
            if x==0:
                break
            elif x<26:
                char_selection.append(x-1)
                break
            else:
                n=x
        c = ''
        for i in char_selection:
            c = char[i]+c
        d[c] = (random.randint(1,50),random.randint(10,100))
        #val = random.randint(1,50)
        #d[c] = (val, 2*val)
    # dict with profit increases with weight
    dd = {}
    p_wt,p_profit = 1,1
    i = 1
    while len(dd) < num:
        wt,profit = random.randint(p_wt,p_wt * 2), random.randint(p_profit*2,p_profit*3)
        if wt > p_wt and profit > p_profit:
            dd[i] = (wt,profit)
            i +=1
            p_wt, p_profit = wt, profit
    return dd
#print(generate_dict(5))


import unittest
import random
from hypothesis import Verbosity
class Test_knapsack(unittest.TestCase):
    known_values = [(15,{'A':(2,10),'B':(3,5),'C':(5,15),
                'D':(7,7),'E':(1,6),'F':(4,18),'G':(1,3)}),
                (8,{'A':(2,1),'B':(3,2),'C':(4,5),'D':(5,6)})]

    true_value = {'A':(2,1),'B':(3,2),'C':(4,5),'D':(5,6)}

    def test_known_values(self):
        for wt, d in self.known_values:
            self.assertEqual(knapsack(wt,d),knapsack_set(wt,d))
    def test_known_values_1(self):
        for wt, d in self.known_values:
            self.assertEqual(knapsack(wt,d)[0],knapsack_other(wt,d))
    def test_known_values_2(self):
        for num in range(5,100):
            d = generate_dict(num)
            result = knapsack(random.randint(1,100),d)
            self.assertEqual(type(result),tuple)
    def test_true_value(self):
        self.assertEqual(knapsack(8,self.true_value)[0],knapsack_other(8,self.true_value))

    def test_knapsack_knapsackSet(self):
        for num in range(5,100):
            d = generate_dict(num)
            w = random.randint(10,100)
            self.assertEqual(knapsack(w,d),knapsack_set(w,d))
