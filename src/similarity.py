from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from tqdm import tqdm

def similarity(name):
    df = pd.read_csv("newdata.csv")
    sen = df.iloc[:,2]
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sen_embeddings = model.encode(sen)
    sen_embeddings.shape
    cosine_similarity(
        [sen_embeddings[1],sen_embeddings[4]],
        [sen_embeddings[0],sen_embeddings[2]]
    )
    cosine_similarity(
        [sen_embeddings[1]],
        [sen_embeddings[0],sen_embeddings[2]]
    )
    similarity_df = pd.DataFrame(columns = ['from_article','to_article','similarity_score'])
    cos_sim = cosine_similarity(sen_embeddings,sen_embeddings)
    len = df.shape[0]
    for i in range(len):
        for j in range(len):
            similarity_df = similarity_df.append({'from_article':i,'to_article':j,'similarity_score':cos_sim[i][j]},ignore_index=True)

    similarity_df['from_article'] = similarity_df['from_article'].astype('int32')
    similarity_df['to_article'] = similarity_df['to_article'].astype('int32')
    similarity_df.to_csv(name,index = False)
