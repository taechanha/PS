import builtins
import sys
sys.setrecursionlimit(10**6)

(lambda __y, __print, __operator, __g: [[[[[(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: [(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: [(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: [(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: (lambda __continue: [[(lambda __after: (__print(cnt), (exit(), __after())[1])[1] if (res >= given) else __after())(lambda: (lambda __after: __continue() if (res in clock_nums) else __after())(lambda: (clock_nums.add(res), [__this() for __g['cnt'] in [(__operator.iadd(__g['cnt'], 1))]][0])[1])) for __g['res'] in [(get_clock_num([a, b, c, d]))]][0] for __g['d'] in [(__i)]][0])(__this) if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(1, 10)), [], lambda: __this()) for __g['c'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(1, 10)), [], lambda: __this()) for __g['b'] in [(__i)]][0] if __i is not __sentinel else __after())(next(
    __items, __sentinel)))())(iter(range(1, 10)), [], lambda: __this()) for __g['a'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(1, 10)), [], lambda: None) for __g['clock_nums'] in [(set())]][0] for __g['given'] in [(get_clock_num(nums))]][0] for __g['get_clock_num'], get_clock_num.__name__ in [(lambda arr: (lambda __l: [[(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: [(__l['arr'].append(__l['arr'].pop(0)), [__this() for __l['min_num'] in [(min(__l['min_num'], int(''.join(map(str, __l['arr'])))))]][0])[1] for __l['_'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(4)), [], lambda: __l['min_num']) for __l['min_num'] in [(float('inf'))]][0] for __l['arr'] in [(arr)]][0])({}), 'get_clock_num')]][0] for __g['cnt'] in [(1)]][0] for __g['nums'] in [(list(map(int, input().split())))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), __import__('builtins', level=0).__dict__['print'], __import__('operator', level=0), globals())
