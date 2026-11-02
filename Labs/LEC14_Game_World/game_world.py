world= [[], []]

def add_object(depth, o=0):
    world[depth].append(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
        break


def update():
    for layer in world:
        for o in layer.copy():
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

