import networkx as nx
import matplotlib.pyplot as plt
import time

class Timer():
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        return self.end_time - self.start_time


def show_graph(M, n):
    G = nx.Graph()
    MAX_M = n*n
    pos = {}
    plt.figure(figsize=(n, n))
    colors = []
    
    for y in range(len(M)):
        for x in range(len(M[0])):
            m = M[y][x]
            if m < MAX_M:
                G.add_edge(str(m), str(m+1))
            pos[str(m)] = (x, n-y)
            if 256 < MAX_M:
                colors.append(m // 10)
            else:
                colors.append(m)

    if 256 < MAX_M:
        grad = MAX_M // 10
    else:
        grad = MAX_M

    nx.draw_networkx(G, pos=pos, node_color=colors, cmap=plt.get_cmap("Blues", grad))
    plt.show()

if __name__=="__main__":
    timer = Timer()
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    show_graph(M, 3)
    print("[*] Time:", timer.end())
