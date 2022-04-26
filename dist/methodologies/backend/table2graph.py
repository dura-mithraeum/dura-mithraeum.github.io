import csv
import json
from unicodedata import name

def main():
    triples = []
    with open('info.csv', 'r') as file:
        reader = csv.reader(file)
        keys = next(reader)
        
        for line in reader:
            for n in range(len(line) - 1):
                temp_triple = [line[0], keys[n + 1], line[n + 1]]
                #print(line[0] + ", " + keys[n + 1] + ", " + line[n + 1])
                triples.append(temp_triple)
                #store triples
        #for triple in triples:
            #print(triple)

    
    print(keys)

        #create node list
    nodes = []
    colors = [
        "red",
        "orange",
        "blue",
        "green",
        "yellow",
        "indigo",
        "violet",
        "brown",
        "black",
        "purple",
        "Crimson",
        "CadetBlue",

    ]
        
    for triple in triples:
        if triple[1] == "name":
            temp_node = {"label": triple[0], "name": triple[2], "color": "gray"}
            counter = 0
            for node in nodes:
                if node == temp_node:
                    break
                else:
                    counter += 1
                    continue
            if counter == len(nodes):
                nodes.append(temp_node)

        # assign colors for each of the potential keys 
        # in a way that is scalable, for situations where you have more types of properties. 
        # all you'd hav eto do is put more colors in the color array
        for i in range(len(keys) - 1):
            if triple[1] == keys[i + 1]:
                col = colors[i]
            
        temp_node = {"label": triple[2], "color": col}
        counter = 0
        for node in nodes:
            if node == temp_node:
                break
            if node["label"] == name:
                break
            if node["label"] == "/":
                break
            if node["label"] == "?":
                break
            if node["label"] == "???":
                break
            else:
                counter += 1
                continue
        if counter == len(nodes):
            nodes.append(temp_node)

    for i  in range(len(nodes)):
        print(nodes[i])
    #print(len(nodes))

    #making edges
    edges = []

    for triple in triples:
        # creating the source and a target
        edge_temp = {"source": None, "target": None}
        for i  in range(len(nodes)):
            if triple[0] == nodes[i]["label"]:
                edge_temp["source"] = i + 1
            if triple[2] == nodes[i]["label"]:
                edge_temp["target"] = i + 1
        edges.append(edge_temp)
    
    final = {"nodes": nodes, "edges": edges}

    #for i  in range(len(edges)):
        #print(edges[i])
    #print(len(edges))
    #writing into the json file
    
    with open('info_sheet.json', 'w') as outfile:
        outfile.write(json.dumps(final, indent = 4))

main()
