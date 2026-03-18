def score_candidate(dg_bind, dg_cofold, acc):

    w1, w2, w3 = 1.0, 0.5, 0.3

    return (
        w1 * (-dg_bind) +
        w2 * acc +
        w3 * (-dg_cofold)
    )