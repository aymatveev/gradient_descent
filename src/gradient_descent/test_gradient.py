import gradient
import importlib

def test_gradient():
    importlib.reload(gradient)

    def func(x):
        return (x - 5) ** 2
    
    point = (5,)
    
    result = gradient.gradient(func, point)

    print(f"Expected: 0\nActual: {result}")