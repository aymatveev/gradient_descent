from typing import Callable, Iterable

def gradient(func: Callable, point: Iterable[float], delta: float = 0.001) -> Iterable[float]:
    n = len(point)
    diffs = (tuple((delta if jdx == idx else 0) for jdx in range(n)) for idx in range(n))
    point_with_deltas = (tuple(d + p for (d, p) in zip(diff, point)) for diff in diffs)
    return tuple((func(*pd) - func(*point)) / delta for pd in point_with_deltas)