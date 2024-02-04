
def covariance(X, Y, bias=False):
    X_mean = np.mean(X, dtype=np.float64)
    Y_mean = np.mean(Y, dtype=np.float64)
    if bias:
        n = len(X)
    else:
        n = len(X) - 1

    return np.sum((X - X_mean) * (Y - Y_mean)) / n


def covariance_matrix(X, Y, bias=False):
    return np.array([[1 - (covariance(f_val, l_val)/np.sqrt(np.var(f_val, ddof=1)*np.var(l_val, ddof=1))) for f_val in X.T] for l_val in Y.T]).T


def euclidean_distance_matrix(matrix):
    distance_matrix = cdist(matrix, matrix, 'euclidean')
    return distance_matrix


def weighted_pagerank(M, beta=0.85, epsilon=1e-8):
    n = len(M)
    d = np.sum(M, axis=1)
    P = M / d[:, np.newaxis]
    G = beta * P + (1 - beta) / n * np.ones((n, n))

    # Initial probability vector
    pi = np.ones(n) / n

    while True:
        pi_next = np.dot(pi, G)

        # Check for convergence
        if np.linalg.norm(pi_next - pi, 1) < epsilon:
            break

        pi = pi_next

    return pi

def mgfs(X, Y, beta=0.85, epsilon=1e-8, bias=False):
    cdm = covariance_matrix(X=X, Y=Y, bias=bias)
    edm = euclidean_distance_matrix(cdm)
    pr = weighted_pagerank(edm)

    return pr, np.argsort(pr)[::-1]