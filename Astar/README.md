Start with an empty priority queue called OPEN
Insert ROOT into OPEN with cost 0

Create a map G_COST to store cost from root
Set G_COST[ROOT] = 0

Create a map PARENT to store parent of each node
Set PARENT[ROOT] = null

WHILE OPEN is not empty
    Remove node CURRENT with lowest cost from OPEN

    IF CURRENT is the GOAL
        Create empty PATH
        WHILE CURRENT is not null
            Add CURRENT to PATH
            CURRENT = PARENT[CURRENT]
        END WHILE
        Reverse PATH
        Return PATH
    END IF

    FOR each CHILD of CURRENT
        New cost = G_COST[CURRENT] + edge cost

        IF CHILD is not visited OR new cost is smaller
            Update G_COST[CHILD]
            Total cost = new cost + heuristic of CHILD
            Add CHILD to OPEN with total cost
            Set PARENT[CHILD] = CURRENT
        END IF
    END FOR
END WHILE

Return failure (no path found)
