
# Coding Interview Prep

A centralized collection of my **LeetCode** and **NeetCode** solutions, automatically synchronized through GitHub Actions.

This repository documents my progress in data structures, algorithms, problem-solving, and technical interview preparation.

[![Sync Status](https://github.com/Rayan-Alam-UOIT/coding-interview-prep/actions/workflows/sync-solutions.yml/badge.svg)](https://github.com/Rayan-Alam-UOIT/coding-interview-prep/actions/workflows/sync-solutions.yml)
[![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-FFA116?logo=leetcode&logoColor=white)](https://github.com/Rayan-Alam-UOIT/leetcode-solutions)
[![NeetCode](https://img.shields.io/badge/NeetCode-Submissions-2563EB)](https://github.com/Rayan-Alam-UOIT/neetcode-submissions)
![Auto Sync](https://img.shields.io/badge/Auto_Sync-Every_15_Minutes-2088FF?logo=githubactions&logoColor=white)

---

## Progress Dashboard

<!-- STATS_START -->
### Solution Overview

| Metric | Count |
|---|---:|
| **Total platform-specific problems** | **1** |
| LeetCode problems | 1 |
| NeetCode problems | 0 |
| Solution code files | 1 |
| Programming languages | 1 |

### Programming Languages

| Language | Files | Share |
|---|---:|---:|
| Python | 1 | 100.0% |

*Last updated: November 17, 2026 at 17:07 UTC*

> Counts are based on solution folders and recognized source files. The same problem solved on both platforms is counted separately.
<!-- STATS_END -->

The statistics above are generated automatically from the synchronized solution files.

## Browse Solutions

| Platform | Description | Solutions |
|---|---|---|
| **LeetCode** | Algorithms and data structures | [Browse LeetCode](./LeetCode) |
| **NeetCode** | Structured interview preparation | [Browse NeetCode](./NeetCode) |

## Topics & Patterns

My interview preparation focuses on the following topics:

| Category | Key Concepts |
|---|---|
| Arrays & Hashing | Hash maps, sets, frequency counting |
| Two Pointers | Palindromes, sorted arrays |
| Sliding Window | Subarrays, substrings |
| Stack | Monotonic stacks, parentheses |
| Binary Search | Search space reduction |
| Linked Lists | Reversal, cycle detection |
| Trees | DFS, BFS, recursion |
| Heaps & Priority Queues | Top-K, streaming data |
| Backtracking | Permutations, combinations |
| Graphs | Traversal, shortest paths |
| Dynamic Programming | Memoization, tabulation |
| Greedy Algorithms | Local optimization |
| Intervals | Merging, overlapping ranges |
| Bit Manipulation | Binary operations |

## Repository Structure

```text
coding-interview-prep/
├── LeetCode/
│   └── <problem-folders>/
├── NeetCode/
│   └── <topic>/<problem-folders>/
├── scripts/
│   └── update_stats.py
├── .github/
│   └── workflows/
│       └── sync-solutions.yml
└── README.md
```

The original directory structures are preserved within each platform's folder.

## Automated Synchronization

```text
LeetCode                     NeetCode
   |                            |
   v                            v
leetcode-solutions       neetcode-submissions
   |                            |
   +-------------+--------------+
                 |
                 v
           GitHub Actions
                 |
                 v
         coding-interview-prep
          /             \
     LeetCode/        NeetCode/
```

**How it works:**

1. LeetCode submissions are saved to the existing `leetcode-solutions` repository.
2. NeetCode submissions are automatically committed to `neetcode-submissions`.
3. GitHub Actions checks both repositories every 15 minutes.
4. New or updated solutions are copied into their respective directories.
5. The statistics dashboard is regenerated automatically.
6. Changes are committed only when necessary.

## Languages & Tools

- **Python** — Primary language for interview preparation
- **Git & GitHub** — Version control
- **GitHub Actions** — Automated synchronization
- **LeetCode & NeetCode** — Coding practice

## Goals

- Strengthen data structures and algorithms fundamentals.
- Recognize common interview problem-solving patterns.
- Improve time and space complexity analysis.
- Write efficient, readable solutions.
- Maintain consistent coding practice.

---

*Solutions are provided for educational purposes and reflect my personal approaches to solving problems.*
