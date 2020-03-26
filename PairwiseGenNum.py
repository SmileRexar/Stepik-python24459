#Example generator for full element in list
import itertools
def Func(n, debug_mode=False):
    for mas in itertools.product(*[range(0, 10) for i in range(n)]):
        if (debug_mode):
            print(mas)
        yield mas

a=list(Func(5))
a
a[2]