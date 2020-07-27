# Chapter Exercise 

### Exercise 1.5.5
(10^9 * 10^6 * 10 / 10^9) seconds / (3600 * 24 seconds per day) ~ 115 days

### Exercise 1.5.6
2 * log(10^9) * 10^6 / 10^9 < 1 second

### Exercise 1.5.8
id[p] changes to id[q] when i == p; future accessed to id[p] will be different.

### Exercise 1.5.9
Impossible because height of tree (5) is bigger than log(10) < 4. (Proposition H)

### Exercise 1.5.12
See code.
Note : The amortized cost per operation for this algorithm is known to be logarithmic.

### Exercise 1.5.13
The amortized cost per operation for this algorithm is known to be bounded by a function known as the inverse Ackermann function and is less than 5 for any conceivable practical value of N.

### Exercise 1.5.14
Proof similar to Proposition H.

### Exercise 1.5.15
Worst case is when two trees have the same height and are not fully saturated.
We have (h+1 d+1) = (h d) + (h d+1) where h is the height of the previous tree(s) and d is the depth of the current level, which represents the number of nodes at the current level after two trees are combined.
Average = (\sum{k=0 to n} k * (n k)) / 2^n = n * 2^(n-1) / 2^n = n/2