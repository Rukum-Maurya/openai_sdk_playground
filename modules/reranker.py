from FlagEmbedding import FlagReranker
class Reranker:

    def __init__(self):
        self.model = FlagReranker(
            "BAAI/bge-reranker-v2-m3"
        )

    def rerank(self,query,candidates):
        pairs = [
            [query,document] 
            for document,_ in candidates
        ]
        scores =   self.model.compute_score(pairs)
        reranked = []
        for (document,_),score in zip(candidates,scores):
            reranked.append((document,score))
        reranked.sort(
            key=lambda x:x[1],
            reverse=True
        )
        return reranked
    