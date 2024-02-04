# MGFS

Implementation of method outlined by the paper below

```
Amin Hashemi, Mohammad Bagher Dowlatshahi, Hossein Nezamabadi-pour,
MGFS: A multi-label graph-based feature selection algorithm via PageRank centrality,
Expert Systems with Applications,
Volume 142,
2020,
113024,
ISSN 0957-4174,
https://doi.org/10.1016/j.eswa.2019.113024.
(https://www.sciencedirect.com/science/article/pii/S0957417419307419)
Abstract: In multi-label data, each instance corresponds to a set of labels instead of one label whereby the instances belonging to a label in the corresponding column of that label are assigned 1, while instances that do not belong to that label are assigned 0 in the data set. This type of data is usually considered as high-dimensional data, so many methods, using machine learning algorithms, seek to choose the best subset of features for reducing the dimensionality of data and then to create an acceptable model for classification. In this paper, we have designed a fast algorithm for feature selection on the multi-label data using the PageRank algorithm, which is an effective method used to calculate the importance of web pages on the Internet. This algorithm, which is called multi-label graph-based feature selection (MGFS), first constructs an M × L matrix, called Correlation Distance Matrix (CDM), where M is the number of features and L represents the number of class labels. Then, MGFS creates a complete weighted graph, called Feature-Label Graph (FLG), where each feature is considered as a vertex, and the weight between two vertices (or features) represents their Euclidean distance in CDM. Finally, the importance of each graph vertex (or feature) is estimated via the PageRank algorithm. In the proposed method, the number of features can be determined by the user. To prove the performance of the proposed algorithm, we have tested this algorithm with several methods for multi-label feature selection and on several multi-label datasets with different dimensions. The results show the superiority of the proposed method in the classification criteria and run-time.
Keywords: Multi-label feature selection; Correlation distance matrix; Feature-label graph; PageRank centrality

```