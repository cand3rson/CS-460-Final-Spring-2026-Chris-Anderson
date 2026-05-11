# Development Log – The Torchbearer

**Student Name:** Christopher Anderson
**Student ID:** 827320059


---

## Entry 1 – [05/05/2026]: Initial Plan



_After reading this exam I will implement this exam in parts. I notice that parts 2,5 and 6 require serious work so I will most likely do part 2 in one day and 5-6 at another time. Part 2 requires Dijkstra's algorithim to find travel cost. Parts 5-6 backtrack searching is needed while pruning branches early when we can't beat the best solution found so far._  
---

## Entry 2 – [05/06/2026]: Visited Node Issue in Part 2b



_When working on the logic for visting a node in 2b I forgot to let it 'continue'. This caused for nodes to be reivewed a redundant amount of times and overwritting shortest distances. This error was fixed by adding the continue check at the start of the while loop._

---

## Entry 3 – [05/10/2026]: Running into bug issues for Part 5b set implementation 

_When I was working on finding the optimal path I mistakenly passed in a list instead of converting it into a set for relics_remaining. This caused the constant time checks for membership to no longer hold true._

---

## Entry 4 – [5/10/2026]: Post-Implementation Reflection



_To fix the Part 5b issue I convereted the relics into a set in find_optimal_route before passing it to the explore function. With this it guranteed that all 3 requirements in Part 5b were given constant time. With this bug fix implemented the algorithim now tracks the remaining relics that need to be visited during recursion and will stay valid during backtracking. If I had more time I would add more test cases for graphs with hundereds of nodes. That way I could bullet proof my work._

---

## Final Entry – [05/10/2026]: Time Estimate



| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |1 |
| Part 2: Precomputation Design |1.5 |
| Part 3: Algorithm Correctness |0.5 |
| Part 4: Search Design |0.5 |
| Part 5: State and Search Space |2 |
| Part 6: Pruning |0.5 |
| Part 7: Implementation |15 |
| README and DEVLOG writing |6 |
| **Total** |27 |
