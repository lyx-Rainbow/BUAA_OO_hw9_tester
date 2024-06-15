import random
import json
from cyaron import Graph

def generateData(nodeLimit:int, edgelimit:int):
    nodeNum = random.randint(2, nodeLimit)
    if (nodeNum * (nodeNum - 1) / 2) < edgelimit:
        edgelimit = nodeNum * (nodeNum - 1) / 2
    edgeNum = random.randint(1, edgelimit)
    graph = Graph.graph(nodeNum, edgeNum, weight_limit=(1, 100))

    node = set()
    apComs = []
    arComs = []
    mrComs = []
    commands = []
    for edge in graph.iterate_edges():
        arComs.append("ar " + str(edge.start) + " " + str(edge.end) + " " + str(random.randint(1, 100)))
        mrComs.append("mr " + str(edge.start) + " " + str(edge.end) + " " + str(random.randint(-100, 100)))
    for i in range(nodeNum):
        node.add(i)
        apComs.append("ap " + str(i) + " Name" + str(i) + " " + str(random.randint(1, 100)))

    commands.extend(apComs)
    commands.extend(arComs)
    commands.extend(mrComs)

    for i in range(nodeNum):
        slice = random.sample(list(node), 2)
        chance = random.random()
        if chance < 0.25:
            commands.append("qv " + str(slice[0]) + " " + str(slice[1]))
        elif chance < 0.5:
            commands.append("qci " + str(slice[0]) + " " + str(slice[1]))
        elif chance < 0.75:
            commands.append("qbs")
        else:
            commands.append("qts")

    random.shuffle(commands)

    for command in commands:
        print(command)

if __name__ == '__main__':
    parameters = json.load(open("parameter.json"))
    generateData(parameters["nodeLimit"], parameters["edgeLimit"])