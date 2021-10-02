"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra+rb
    pass

def longest_run(mylist, key):
    longestRun = 0
    tracker = 0
    for i in range(len(mylist)-1):
        if mylist[i] ==  key:
            tracker += 1
        else:
            if tracker>0:
                if tracker>longestRun:
                    longestRun = tracker
                tracker = 0
    return longestRun
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
              
def helper(result1,result2):
    if result1.is_entire_range and result2.is_entire_range:
        lr = result1.longest_size + result2.longest_size
        return Result(lr,lr,lr, True)
    elif not result1.is_entire_range and result2.is_entire_range:
        if result1.right_size + result2.longest_size >= result1.longest_size:
            return Result(result1.left_size,result1.right_size + result2.left_size, result1.right_size + result2.longest_size, False)
        else:
            return Result(result1.left_size,result2.right_size,result1.longest_run,False)
    elif result1.is_entire_range and not result2.is_entire_range:
        if result1.right_size + result2.left_size >= result2.longest_size:
            return Result(result1.right_size+result2.left_size,result2.right_size, result1.right_size + result2.left_size, False)
        else:
            return Result(result1.left_size,result2.right_size,result2.longest_run,False)
    else:
        if (result1.right_size+ result2.left_size >= result1.longest_size) and  (result1.right_size+ result2.left_size >= result2.longest_size):
            return Result(result1.left_size, result2.right_size, result1.right_size+ result2.left_size, False)
        elif result1.longest_size >= result2.longest_size:
            return Result(result1.left_size, result2.right_size, result1.longest_size, False)
        else:
            return Result(result1.left_size, result2.right_size, result2.longest_size, False)


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return 1
        else:
            return 0
    final = helper2(mylist,key)
    return final.longest_size



def helper2(mylist,key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)

    rightResult = helper2(mylist[:len(mylist)//2],key)
    leftResult = helper2(mylist[len(mylist)//2:],key)
    finalResult = helper(rightResult,leftResult)
    return finalResult




## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
print(longest_run_recursive([2,12,12,8,12,12,12,12,0,12,1], 12))
print(longest_run_recursive([7], 5))
