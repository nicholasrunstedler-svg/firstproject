"""This module is my attempt to study graph theory through computer science"""
from functions import permutation_generator, cartesian_product_for_listy_lists, number_theory, powerset
import sys
from random import randint



mylist = [[4, 2], [2, 3],[3, 4], [3,5]]

def recursion_time() -> None:
    """It's recursion time baby"""
    sys.setrecursionlimit(1000000)
    sys.set_int_max_str_digits(100000)


def get_kn(n: int) -> list:
    """Pass"""
    new = [] #The verticies
    for i in range(n):
        new.append(i)
    kn = [x for x in cartesian_product_for_listy_lists(new, new) if x[0] != x[1]] #All possible edges
    return new, kn

def get_kn2(n: int) -> list:
    new = []
    for i in range(n):
        new.append(i) #Vertex set
    kn = list([x for x in cartesian_product_for_listy_lists(new, new) if x[0] < x[1]])
    return kn


def explore(graph: list, current_path: list = None, allpaths: list = None) -> list:
    """Finds all legal walks in a graph without repeating edges"""
    if allpaths is None:
        current_path = []
        allpaths = []
    if len(graph) < 1:
        allpaths.append(current_path)

    for i in range(len(graph)):
        if current_path: #Not empty?
            if current_path[-1][1] == graph[i][0]:
                explore(graph[:i] + graph[i+1:], current_path + [graph[i]], allpaths)
        else:
            explore(graph[:i] + graph[i+1:], current_path + [graph[i]], allpaths)
    return allpaths #More like all walks but it's ok


sys.setrecursionlimit(200)
def all_paths(graph: list, current_path: list = None, allpaths: list = None) -> list:
    """Its all paths and cycles"""
    if allpaths is None:
        allpaths = []
        current_path = []
    if not graph: #Empty
        allpaths.append(current_path)
        #current_path = []
    #Otherwise
    for i in range(len(graph)):
        if current_path and current_path:
            if current_path[-1][1] == graph[i][0]:
                all_paths([x for x in graph if x[0] != graph[i][0]], current_path + [graph[i]], allpaths)
            else:
                all_paths(graph[:i] + graph[i+1:], current_path, allpaths)
        else:
            all_paths(graph[:i] + graph[i+1:], current_path + [graph[i]], allpaths) #If it's empty it dosen't matter
    return allpaths


def eliminate_cycles(walk: list):
    if walk[0][0] == walk[-1][-1]:
        return walk[:-1]
    return walk


def ispath(path: list):
    for peice in path:
            first = peice[0]
            idx = 0
            for otherpeice in path:
                if idx > 1:
                    return False
                if otherpeice == peice:
                    continue
                else:
                    if otherpeice[1] == first:
                        idx += 1 #first instance of first
            second = peice[1]
            idx = 0
            for otherpeice in path:
                if idx > 1:
                    return False
                if otherpeice == peice:
                    continue
                else:
                    if otherpeice[0] == second:
                        idx += 1 #first instance of first
    return True





def allpaths2(graph: list, currentpath: list = None, allpaths: list = None) -> list:
    if allpaths is None:
        allpaths = []
        currentpath = []
    if not graph and currentpath:
        allpaths.append(currentpath)

    for i in range(len(graph)):
        if not len(currentpath) == 0 and graph[i][0] == currentpath[-1][1]:
            print([x for x in graph if not any(x[1] == y[0] for y in currentpath)])
            allpaths2([x for x in graph if not any(x[1] == y[0] for y in currentpath)], currentpath + [graph[i]], allpaths)
            
        else:
            allpaths2(graph[:i] + graph[i+1:], currentpath + [graph[i]], allpaths)
            #print([x for x in graph if not any(x[1] == y[0] for y in currentpath)])
    return allpaths


def allpaths3(graph: list, currentpath: list = None, allpaths: list = None):
    """pass"""
    if allpaths is None:
        allpaths = []
        currentpath = []
    if not graph:
        allpaths.append(currentpath)

    for i in range(len(graph)):
        if (len(currentpath) != 0) and graph[i][0] == currentpath[-1][1]: #and (not any(x[0] == graph[i][1] for x in currentpath)):
            allpaths3(graph[i+1:], currentpath + [graph[i]], allpaths)
        elif len(currentpath) == 0:
            allpaths3(graph[i+1:], currentpath + [graph[i]], allpaths)
    return allpaths


def find_spanning_trees(n: int) -> list:

    N = [i for i in range(n)]
    G = [i for i in powerset(N) if len(i) == 2]
    D = [i for i in powerset(G)]
    #print(D)
    T = [tree for tree in D if (all(existspath(x,y, tree) for x in N for y in N))]
    return T


def existspath(u: int, v: int, edgeset: list, neighbourhood: list = None, layer = 1) -> bool:
    if u == v:
        return True
    if not any(edg[0] == u for edg in edgeset) or not any(edg[1] == v for edg in edgeset):
        return False
    if layer > len(edgeset) + 10:
        return False
    if neighbourhood is None:
        neighbourhood = []
        for edge in edgeset:
            if edge[0] == u:
                neighbourhood.append(edge)
    #Now edge is what we want it to be
    if any(x[1] == v for x in neighbourhood):
        return True
    else:
        existspath(u, v, [x for x in edgeset if x not in neighbourhood], [x for x in edgeset if any(y[1] == x[0] for y in neighbourhood)], layer + 1)


def strip_list(lst: list, stripped: list = None, nakey: set = None) -> set:
    """Strips a list of embedded lists to only a single layer set"""
    if stripped is None:
        stripped = []
        nakey = set({})
    if not lst:
        nakey.add(i for i in stripped)
    for entry in lst:
        if type(entry) == list:
            strip_list(entry, stripped, nakey)
        else:
            nakey.add(entry)
    return nakey


def find_subgraphs(graph: list):
    """Finds all subgraphs in the form of edge sets that still contain all the original verticies"""
    vertex_set = list(strip_list(graph))
    bigset = [i for i in powerset(graph) if len(strip_list(i)) == len(vertex_set)]
    return bigset


def eliminate_cycles2(graph: list) -> list:
    """Pass"""
    for edge in graph:
        if existspath(edge[1], edge[0]):
            pass


def spanning_trees(graph: list) -> list:
    """Finds spanning trees?"""
    # graph is just the graphs edge set
    vertex_set = list(strip_list(graph))
    subgraphs = find_subgraphs(graph)
    spanningtrees = [i for i in subgraphs if all(existspath(x,y,i) for x in vertex_set for y in vertex_set)]
    return spanningtrees

k = get_kn(3)[1]
print(k)
K = [[1, 2], [2, 0]]

