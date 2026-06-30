def prioritize_attack_paths(paths):
    """
    Keep only the highest-impact attack path
    for each starting identity.
    """

    best_paths = {}

    for path in paths:
        if len(path) < 2:
            continue

        source = path[0]

        if (
            source not in best_paths
            or len(path) > len(best_paths[source])
        ):
            best_paths[source] = path

    return list(best_paths.values())