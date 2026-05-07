# The Torchbearer

**Student Name:** Christopher Anderson
**Student ID:** 827320059
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
*A single shortest-path run from S finds the cheapest way to reach each node on its own but can't find the order for  when to visit multiple chambers. This is becuase visiting them in a different order produces leads to different total costs.*
- **What decision remains after all inter-location costs are known:**
*After all inter-location costs are known we are left with finding out which order of relics minimizes total fuel.*
- **Why this requires a search over orders (one sentence):**
*This requires a serach over oders becuase the overal costs depeneds on the sequence of vists not the shortest immedidiate path.*

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.


| Source Node Type | Why it is a source                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| *Spawn Node S*   | *Starting here allows for the cheapest path from S to each relic to find route.*                                       |
| *R1, R2,.. Rk*   | *After getting each relic the torchbearer can go to any remaining relic so we need to cheapest path form every relic.* |


### Part 2b: Distance Storage

> Fill in the table. No prose required.


| Property                    | Your answer                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| Data structure name         | Nested Dictionary                                                       |
| What the keys represent     | Outer key = starting node, Inner key = destination                      |
| What the values represent   | The least amount of fuel needed to go from starting node to destination |
| Lookup time complexity      | O(1)                                                                    |
| Why O(1) lookup is possible | Hash table is used                                                      |


### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** *k + 1*
- **Cost per run:** *Cost = O(m * log(n))*
- **Total complexity:** *O((k+1) * m * log(n))*
- **Justification (one line):** *We have k + 1 runs since we start at S and there is k chambers. In each run we use a priority queue since it is Dijkstra's algorithm which is m * log(n) run time.*

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
*For nodes already finalized the nodes distance is locked as the shortest path and won't be updated again.*
- **For nodes not yet finalized (not in S):**
*For nodes not yet finalized the current distance represents the best path found so far using only already finalized nodes as stops, but it could still improve.*

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
*Before iteration 1 S is empty with all nodes having a distance of infinity and the source nodes distance is 0 since it is itself. The invariant holds because no nodes have been finalized.*
- **Maintenance : why finalizing the min-dist node is always correct:**
*When the min distance node is revelaed it's distance is always the shortest path. This is because all edge weights are non-negative and no other path can be smaller.*
- **Termination : what the invariant guarantees when the algorithm ends:**
*The invariant gurantees that when the heap is empty every node has been finialized and their distance value is the shortest distance to the source.*

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

*This matters for the Route Planner because if Dijkstra's output is wrong the Route Planner would pick the wrong relic order and not find the minniumum fuel route.*

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** *Your answer here.*
- **Counter-example setup:** *Your answer here.*
- **What greedy picks:** *Your answer here.*
- **What optimal picks:** *Your answer here.*
- **Why greedy loses:** *Your answer here.*

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- *Your answer here.*

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.


| Component                | Variable name in code | Data type | Description |
| ------------------------ | --------------------- | --------- | ----------- |
| Current location         |                       |           |             |
| Relics already collected |                       |           |             |
| Fuel cost so far         |                       |           |             |


### Part 5b: Data Structure for Visited Relics

> Fill in the table.


| Property                                    | Your answer      |
| ------------------------------------------- | ---------------- |
| Data structure chosen                       |                  |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected        | Time complexity: |
| Operation: unmark a relic (backtrack)       | Time complexity: |
| Why this structure fits                     |                  |


### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** *Your answer (in terms of k).*
- **Why:** *One-line justification.*

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** *Your answer here.*
- **When it is used:** *Your answer here.*
- **What it allows the algorithm to skip:** *Your answer here.*

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** *Your answer here.*
- **What the lower bound accounts for:** *Your answer here.*
- **Why it never overestimates:** *Your answer here.*

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- *Your answer here.*

---

## References

> Bullet list. If none beyond lecture notes, write that.

- *Your references here.*

