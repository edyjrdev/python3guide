#!/usr/bin/env python

def consumer(f):
  def h_f(*args, **kwargs):
    gen = f(*args, **kwargs)
    next(gen)
    return gen

  return h_f


@consumer
def filter_lift(stage, target):
    while True:
        target.send(stage + (yield))


@consumer
def filter_mean(window, target):
    values = []
    while True:
        values.append((yield))
        if len(values) >= window:
            target.send(sum(values)/window)
            values.pop(0)


@consumer
def output():
    while True:
        print((yield))


if __name__ == "__main__":
    p = output()
    f = filter_lift(10, p)
    f = filter_mean(2, f)

    for d in [1, 3, 2, 4, 2, 1]:
        f.send(d)
