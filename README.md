# The Torchbearer

**Student Name:** Christopher Anderson
**Student ID:** 827320059
**Course:** CS 460 – Algorithms | Spring 2026



---

## Part 1: Problem Analysis



- **Why a single shortest-path run from S is not enough:**
*A single shortest-path run from S finds the cheapest way to reach each node on its own but can't find the order for  when to visit multiple chambers. This is becuase visiting them in a different order produces leads to different total costs.*
- **What decision remains after all inter-location costs are known:**
*After all inter-location costs are known we are left with finding out which order of relics minimizes total fuel.*
- **Why this requires a search over orders (one sentence):**
*This requires a serach over oders becuase the overal costs depeneds on the sequence of vists not the shortest immedidiate path.*

---

## Part 2: Precomputation Design

### Part 2a: Source Selection




| Source Node Type | Why it is a source                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| *Spawn Node S*   | *Starting here allows for the cheapest path from S to each relic to find route.*                                       |
| *R1, R2,.. Rk*   | *After getting each relic the torchbearer can go to any remaining relic so we need to cheapest path form every relic.* |


### Part 2b: Distance Storage



| Property                    | Your answer                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| Data structure name         | Nested Dictionary                                                       |
| What the keys represent     | Outer key = starting node, Inner key = destination                      |
| What the values represent   | The least amount of fuel needed to go from starting node to destination |
| Lookup time complexity      | O(1)                                                                    |
| Why O(1) lookup is possible | Hash table is used                                                      |


### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** *k + 1*
- **Cost per run:** *Cost = O(m * log(n))*
- **Total complexity:** *O((k+1) * m * log(n))*
- **Justification (one line):** *We have k + 1 runs since we start at S and there is k chambers. In each run we use a priority queue since it is Dijkstra's algorithm which is m * log(n) run time.*

---

## Part 3: Algorithm Correctness



### Part 3a: Invariant Explanation



- **For nodes already finalized (in S):**
*For nodes already finalized the nodes distance is locked as the shortest path and won't be updated again.*
- **For nodes not yet finalized (not in S):**
*For nodes not yet finalized the current distance represents the best path found so far using only already finalized nodes as stops, but it could still improve.*

### Part 3b: Invariant Maintenance


- **Initialization : why the invariant holds before iteration 1:**
*Before iteration 1 S is empty with all nodes having a distance of infinity and the source nodes distance is 0 since it is itself. The invariant holds because no nodes have been finalized.*
- **Maintenance : why finalizing the min-dist node is always correct:**
*When the min distance node is revelaed it's distance is always the shortest path. This is because all edge weights are non-negative and no other path can be smaller.*
- **Termination : what the invariant guarantees when the algorithm ends:**
*The invariant gurantees that when the heap is empty every node has been finialized and their distance value is the shortest distance to the source.*

### Part 3c: Why Correctness Matters


*This matters for the Route Planner because if Dijkstra's output is wrong the Route Planner would pick the wrong relic order and not find the minniumum fuel route.*

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** *The failure mode is that a greedy apporach will pick the cheapest current node even if it leads to to a more expensive overall route.*
- **Counter-example setup:** *A weighted and directed graph G{S,A,B,T} where A and B are relic chamners and with S pointing to A for 1, S pointing to B for 4, A pointing to T for 1, A pointing to B for 8 and B pointing to T for 1 and B pointing to A for 1.*
- **What greedy picks:** *A greedy algorithim selects S,A,B,T for a total cost of 10.*
- **What optimal picks:** *The optimal solution selects S,B,A,T for a total cost of 6.*
- **Why greedy loses:** *When the greedy path had to choose between S to A for 1 or S to B for 4, it picekd S to A. However, this forced the greedy algorithim to pick A to B for 8, a much slower apporach.*

### What the Algorithm Must Explore



- *The algorithm must explore every possible order of visiting relic chambers because the total cost depends on the order of the relics found not just the local shortest path costs between nodes.*

---

## Part 5: State and Search Space

### Part 5a: State Representation




| Component                | Variable name in code | Data type | Description                                                         |
| ------------------------ | --------------------- | --------- | ------------------------------------------------------------------- |
| Current location         | current_loc           | String    | This represents the current node the torchbear is in.               |
| Relics already collected | relics_visited_order  | list      | This represents the list of relics aquired this far in the journey. |
| Fuel cost so far         | cost_so_far           | float     | This represents the fuel used to get to this chamber.               |


### Part 5b: Data Structure for Visited Relics



| Property                                    | Your answer                                                                                                                                                                                   |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data structure chosen                       | Set                                                                                                                                                                                           |
| Operation: check if relic already collected | Time complexity: O(1) constant time.                                                                                                                                                          |
| Operation: mark a relic as collected        | Time complexity: O(1) constant time.                                                                                                                                                          |
| Operation: unmark a relic (backtrack)       | Time complexity: O(1) constant time.                                                                                                                                                          |
| Why this structure fits                     | Since checking if a relic is already collected, marking a relic as collected and bakctracking are all cosntant time a set can handle this while a list would requires checking all k options. |


### Part 5c: Worst-Case Search Space



- **Worst-case number of orders considered:** *k facotorial.*
- **Why:** *This is because the algorithim needs to know every possible combination of paths to be certain of the cheapest path.*

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking



- **What is tracked:** *The least expensive fuel route from what has been tracked so far with the relics order.*
- **When it is used:** *It is used during each call to the explore funciton.*
- **What it allows the algorithm to skip:** *This allows the algorithim to skip a path of the graph with a equal to or higher total cost compared to the current best path.*

### Part 6b: Lower Bound Estimation



- **What information is available at the current state:** *At the current state the fuel cost, where the torchbearer is, how many relics are left to be found and the current shortest path is known.*
- **What the lower bound accounts for:** *The lower bound accounts for how much fuel has already ben used plus the minnimum amount of fuel needed to reach the goal.*
- **Why it never overestimates:** *It will never overstiamte because it uses the optimal shorter path distance in it's assumption.*

### Part 6c: Pruning Correctness


- *Pruning is safe because if a new path is found to have a current cost equal to or higher than the current best path it is impossible to beat the current best path.*

---

## References


- *No references beyond lecture.*

