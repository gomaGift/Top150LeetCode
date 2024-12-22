def count_unique_hits(N, K, elasticities):
    hit_tiles = set()

    for elasticity in elasticities:
        hit = 1
        while elasticity <= N:
            hit_tiles.add(elasticity)
            hit += 1
            elasticity *= hit
    for title in hit_tiles:
        print(title)

    return len(hit_tiles)


if __name__ == "__main__":
    N = 17
    K = 3
    elasticities = [2, 3, 7]
    print(count_unique_hits(N, K, elasticities))