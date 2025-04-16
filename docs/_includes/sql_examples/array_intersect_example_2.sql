SELECT ARRAY_SORT(
        ARRAY_INTERSECT([ 5, 4, 3, 2, 1 ],[ 5, 3, 1 ])
    ) as sorted;