import re
import os

import networkx as nx
import random
import utils


def validate_file(path):
    """File must not exceed 100KB and must contain only numbers and spaces"""
    if os.path.getsize(path) > 100000:
        print(f"{path} exceeds 100KB, make sure you're not repeating edges!")
        return False
    with open(path, "r") as f:
        if not re.match(r"^[\d\.\s]+$", f.read()):
            print(f"{path} contains characters that are not numbers and spaces")
            return False
    return True


def read_input_file(path, max_size=None):
    """
    Parses and validates an input file

    :param path: str, a path
    :param max_size: int, number of max add_nodes_from
    :return: networkx Graph is the input is well formed, AssertionError thrown otherwise
    """
    with open(path, "r") as fo:
        n = fo.readline().strip()
        assert n.isdigit()
        # total students
        n = int(n)

        # budget
        stress_budget = fo.readline().strip()
        assert bool(re.match(r"(^\d+\.\d{1,3}$|^\d+$)", stress_budget))
        stress_budget = float(stress_budget)
        assert 0 < stress_budget < 100

        lines = fo.read().splitlines()
        fo.close()

        # validate lines
        for line in lines:
            tokens = line.split(" ")

            assert len(tokens) == 4
            assert tokens[0].isdigit() and int(tokens[0]) < n
            assert tokens[1].isdigit() and int(tokens[1]) < n
            assert bool(re.match(r"(^\d+\.\d{1,3}$|^\d+$)", tokens[2]))
            assert bool(re.match(r"(^\d+\.\d{1,3}$|^\d+$)", tokens[3]))
            assert 0 <= float(tokens[2]) < 100
            assert 0 <= float(tokens[3]) < 100


        # [si, sj, hij: happiness, str i,j: stress]
        G = nx.parse_edgelist(lines, nodetype=int, data=(("happiness", float),("stress", float),))
        G.add_nodes_from(range(n))

        #check completeness and connectivity
        assert nx.is_connected(G)
        assert len(G.edges()) == n*(n-1)//2

        if max_size is not None:
            assert len(G) <= max_size

        return G, stress_budget


def write_input_file(G, stress_budget, path):
    with open(path, "w") as fo:
        n = len(G)
        s_total = stress_budget
        lines = nx.generate_edgelist(G, data=["happiness","stress"])
        fo.write(str(n) + "\n")
        fo.write(str(s_total) + "\n")
        fo.writelines("\n".join(lines))
        fo.close()


def read_output_file(path, G, s):
    """
    Parses and validates an output file

    :param path: str, a path
    :param G: the input graph corresponding to this output
    :return: networkx Graph is the output is well formed, AssertionError thrown otherwise
    """
    with open(path, "r") as fo:
        nodes = set()
        rooms = set()
        D = {}
        lines = fo.read().splitlines()
        fo.close()

        for line in lines:
            tokens = line.split()
            assert len(tokens) == 2
            #validate node
            node = int(tokens[0])
            assert tokens[0].isdigit() and 0 <= node < len(G)
            assert node not in nodes
            nodes.add(node)
            #validate rooms
            room = int(tokens[1])
            assert tokens[0].isdigit() and 0 <= room < len(G)
            rooms.add(room)

            D[node] = room

        assert len(nodes) == len(G)
        assert utils.is_valid_solution(D, G, s, len(rooms))

    return D


def write_output_file(D, path):
    """
    Writes a mapping to an output file

    :param path: str, a path
    :param D: dict, a mapping
    :return: None -- creates a text file
    """
    with open(path, "w") as fo:
        for key, value in D.items():
            fo.write(str(key) + " " + str(value) + "\n")
        fo.close()


def create_input_file(path, students, stress_budget):
    # create the graph
    # path = where to write .in file
    # students = number of students
    # stress_budget = stress budget
    lst = []
    for x in range(students-1):
        for y in range(x+1, students):
            happy = round(float(random.randint(0, 98)) + random.random(), 3)
            stress = round(float(random.randint(0, stress_budget)) + random.random(), 3)
            lst.append(str(x) + " " + str(y) + " " + str(happy) + " " + str(stress))
    G = nx.parse_edgelist(lst, nodetype=int, data=(("happiness", float),("stress", float),))
    G.add_nodes_from(range(students))
    write_input_file(G, stress_budget, path)


def solve(G, path, students, stress_budget):
    # sort G from lowest to highest stress
    total_rms = 1
    S_max_per_room = stress_budget
    rooms = {}
    curr_room = 0
    G_sorted = sorted(G.edges.data(), key=lambda x: x[2]["stress"])
    for x in range(len(G_sorted)):
        # keep putting students in until stress > stress_budget
        for node in G_sorted:
            print(G[0][field]) (2, 9, {'happiness': 12.03, 'stress': 0.081})
            G[0][2]["stress"]
            if curr_room not in rooms:
                rooms[curr_room] = []
            rooms[curr_room].append([node[0], node[1], node[2]["stress"]])
            curr_stress = calculate_stress(G_sorted, rooms, curr_room)
            if curr_stress > S_max_per_room and another_room_available(total_rooms, curr_room):
                while curr_stress > S_max_per_room:
                    removeMostStressful(rooms, curr_room)
                    curr_stress = calculate_stress(G_sorted, rooms, curr_room)
            elif curr_stress > S_max_per_room and not another_room_available(total_rooms, curr_room):
                total_rms += 1
                rooms.clear()
            else:
                break
    # convert rooms
    return rooms


def another_room_available(total_rooms, curr_room):
    return true if total_rooms < curr_room + 1 else false


def removeMostStressful(rooms, curr_room):
    highestStress = rooms[curr_room][0][2]
    highestPair = rooms[curr_room]
    for pair in rooms[curr_room]:
        if pair[0][2] > highestStress:
            highestStress = pair[0][2]
            highestPair = pair
    rooms[curr_room].remove(pair)


def calculate_stress(G, rooms, curr_room):
    # put other people into room and sort them
    people = []
    for each in rooms[curr_room]:
        people.append(each[0])
        people.append(each[1])
    people = sorted(set(people))
    rooms[curr_room].clear()
    for i in range(len(people)-1):
        for j in range(1+i, len(people)):
            G.get_edge_data(i, j)
    print(rooms[curr_room])


def create_output_file(G, path, students, stress_budget):
    rooms = solve(G, path, students, stress_budget)
    write_output_file(rooms, path)


def cheese(path, students, stress_budget):
    D = {}
    for each in range(students):
        D[each] = each
    write_output_file(D, path)

create_input_file("samples/10.in", 10, 12)
create_input_file("samples/20.in", 20, 12)
create_input_file("samples/50.in", 50, 99)

cheese("samples/10.out", 10, 12)
cheese("samples/20.out", 20, 12)
cheese("samples/50.out", 50, 99)

# creates a G
def create_graph(students, stress_budget):
    lst = []
    for x in range(students-1):
        for y in range(x+1, students):
            happy = round(float(random.randint(0, 6)) + random.random(), 3)
            stress = round(float(random.randint(0, stress_budget)) + random.random(), 3)
            lst.append(str(x) + " " + str(y) + " " + str(happy) + " " + str(stress))
    G = nx.parse_edgelist(lst, nodetype=int, data=(("happiness", float),("stress", float),))
    G.add_nodes_from(range(students))
    print(G.get_edge_data(0,1)["stress"])
    return G


# create_output_file(G_test, "samples/10.in", 10, 50)