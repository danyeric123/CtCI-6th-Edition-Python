from functools import cmp_to_key

def comparator(a, b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        if a[1] > b[1]:
            return 1
        else:
            return -1


def solver(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    hmap = {}
    for competitor in competitors:
        hmap[competitor]=0

    for review in reviews:
        for el in review.split():
            if el in hmap:
                hmap[el] += 1

    competitor_count = []
    for key in hmap:
        competitor_count.append([hmap[key], key])
    competitor_count = sorted(competitor_count, key = cmp_to_key(comparator))

    return [competitor_count[i][1] for i in range(min(topNCompetitors, numCompetitors))]





print(solver(
    6, 
    2, 
    ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular'], 
    6,
    [
        "newshop is providing good services in the city; everyone should use newshop",
        "best services by newshop",
        "fashionbeats has great services in the city",
        "I am proud to have fashionbeats",
        "mymarket has awesome services",
        "Thanks Newshop for the quick delivery"
    ]
    )
)