import sys


num_inputs = int(sys.stdin.readline().strip())
shape_inputs = [shape.strip() for shape in sys.stdin.readlines()]

POLYHEDRONS = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

total_sides = sum([POLYHEDRONS[shape] for shape in shape_inputs])
print(total_sides)
