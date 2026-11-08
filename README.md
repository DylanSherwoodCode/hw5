### Attempt 1: linear probing + sum hash
The hash adds up the unicode value of every character and mods by the table size. On a collision it moves forward one slot until it finds an empty one. This was the worst attempt. Character sums only cover a few thousand values and ignore character order, so keys pile up in one area, and with the table 100% full, linear probing turns that into one huge cluster.

### Attempt 2: linear probing + polynomial hash
Same table, but the hash multiplies the running total by 31 before adding each character, Collisions were a lot less, which shows the hash function was the main problem. The table is still completely full, so linear probing still is not that great.

### Attempt 3: linkedList + polynomial hash
Each slot holds a list, and a colliding row is added to the end of that list. Every row already in the list counts as a collision. This was the best attempt so far

### Attempt 4: linkedList + sum hash
Uses the sum hash from attempt 1 with chaining, to compare a poor hash against attempt 3. 

### Attempt 5: linkedList + polynomial hash, 5× table
Takes the best combination (attempt 3) and makes the table 5× larger. The hash also mods inside the loop, so the number stays small for very long quotes. (Like for example the entire BEE movie script) This had the fewest collisions

