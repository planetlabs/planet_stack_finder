# Author: JT (jt@planet.com)
# Description: Find stacks in geometries

from geodetics import arc_length_to_latitude
import numpy as np
from sklearn.cluster import DBSCAN


def findstacks(input_scenes, min_depth=2, max_sep_km=2, method="centers"):
    """
    Takes in a list of dictionaries that correspond to scenes. Returns stacks
    of scenes, which are (likely) smaller lists of dictionaries.
    Each dictionary in the list must have keys ['geometry']['coordinates'] or
    ['coordinates']

    Keywork arguments:
    md -- A list of metadata about scenes as returns from the API
    max_sep -- A clustering parameters, the maximial distance between
                centers of scenes in a cluster. Higher forces
                deeper stacks with less overlap.
    method -- whether to cluster based on centers or corners

    Return:
    stacks -- List of list of scenes, where stacks[i]
              is a list of the scenes in the i-th stack.
              Stacks are ordered in decreasing depth.

    stack_centers -- List of the centers of the stacks.
    """
    max_sep = arc_length_to_latitude(max_sep_km)

    if 'coordinates' in input_scenes[0]:
        coords = [s['coordinates'] for s in input_scenes]
    else:
        coords = [s['geometry']['coordinates'] for s in input_scenes]
    centers_raw = [[sum(coord[0][i][0] for i in range(4)) / 4,
                    sum(coord[0][i][1] for i in range(4)) / 4]
                   for coord in coords]
    centers = np.asarray(centers_raw)

    if method == "centers":
        dbs = DBSCAN(eps=max_sep, min_samples=1, metric='euclidean')
        clusters = dbs.fit_predict(centers)
    elif method == "corners":
        max_sep_corr = max_sep * 3
        dbs = DBSCAN(eps=max_sep_corr, min_samples=1, metric='euclidean')
        tmp_coords = [[item for sublist in c[0] for item in sublist][0:10]
                      for c in coords]
        clusters = dbs.fit_predict(np.asarray(tmp_coords))
    else:
        raise ValueError("Method %s not valid" % method)

    # cast to ints for easy bin counting
    cluster_ints = clusters.astype('int64')

    stack_counts = np.bincount(cluster_ints)
    sc = stack_counts  # for shorter next nice

    # order stack ids in descening order of depth
    deep_clus_ids = [
        cid for (clus_num, cid) in sorted(zip(sc, range(len(sc))))[::-1]]

    stacks = []
    stack_centers = []
    for idx in deep_clus_ids:
        in_stack_ids = list(np.where(clusters == idx)[0])
        this_stack = [input_scenes[i] for i in in_stack_ids]
        if len(this_stack) < min_depth:
            continue
        stacks.append(this_stack)

        scene_centers = [centers[i] for i in in_stack_ids]
        stack_center = np.mean(scene_centers, axis=0)
        stack_centers.append(stack_center.tolist())

    return stacks, stack_centers
