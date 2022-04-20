import hypernetx as hnx
import matplotlib.pyplot as plt
import pandas as pd 
import networkx as nx
import preprocess as pp

#Hypergraph
def build():
    gr = pd.read_csv("similarity_scores.csv",index_col=0)
    l =[]
    for i in range(len(gr)):
        if (gr.similarity_score[i] >= 0.75):
            if (gr.from_article[i] != gr.to_article[i] ):
                l.append(['{}'.format(gr.from_article[i]),'{}'.format(gr.to_article[i])])


    G = nx.Graph()

    #Add nodes to Graph    
    G.add_nodes_from(sum(l, []))

    #Create edges from list of nodes
    q = [[(s[i],s[i+1]) for i in range(len(s)-1)] for s in l]

    for i in q:
        #Add edges to Graph
        G.add_edges_from(i)

    #Find all connnected components in graph and list nodes for each component
    count=1
    l=[]
    for i in nx.connected_components(G):
        l.append({'hypernode':count, 'vertex_list':tuple(list(i))})
        count +=1
    ver = []
    for i in gr.from_article:
        ver.append('{}'.format(i))
    ver = list(set(ver))
    ver_hy = []
    for i in range(len(l)):
        for j in l[i]['vertex_list']:
            ver_hy.append(j)
    result = [i for i in ver if i not in ver_hy]
    count = len(l)
    for i in result:
        count +=1
        l.append({'hypernode':count, 'vertex_list':('{}'.format(i),)})

    res = {sub['hypernode'] : sub['vertex_list'] for sub in l}
    hy = hnx.Hypergraph(res)
    return hy,l

def draw(hy):
    hnx.draw(hy)

def hyper_file(l):
    data = pd.DataFrame(l,columns=['hypernode','vertex_list','normalized_text'])
    ne = pd.read_csv('newdata.csv',index_col=0)
    ne['news'] = ne['news'].apply(pp.nltk_process)
    for i in range(len(data.vertex_list)):
        a = list(data.vertex_list[i])
        emp = []
        for j in a:
            emp += ne.iloc[int(j)].news
        data.normalized_text[i] = emp
        data.to_csv('hypernode.csv')