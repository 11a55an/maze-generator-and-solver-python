# Maze Generator and Solver using BFS and DFS

This project implements a maze generator and solver using Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. The generator creates a random maze, and the solver finds a path from the start to the goal in the generated maze using either BFS or DFS.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Algorithms](#algorithms)

## Introduction

The primary goal of this project is to demonstrate the functionalities of maze generation and solving using BFS and DFS algorithms. The maze generator creates a maze with specified dimensions, and the maze solver finds a path from the start to the goal within the maze.

## Features

- Random maze generation using Pyamaze
- Maze solving using Breadth-First Search (BFS)
- Maze solving using Depth-First Search (DFS)

## Setup

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/11a55an/maze-generator-and-solver-python.git
   ```

2. Ensure you have Python 3.x installed.

## Usage

1. Run the maze generator:
  ```bash
   python maze.py
   ```

2. Run the maze solver using BFS:
  ```bash
   python bfsMaze.py
   ```

3. Run the maze solver using dfs:
  ```bash
   python dfsMaze.py
   ```

## Algorithms

### Breadth-First Search

Breadth-First Search is an algorithm that explores a graph by starting at the source node and then exploring all the neighboring nodes at the present depth prior to moving on to nodes at the next depth level.

### Depth-First Search

Depth-First Search is an algorithm that explores a graph by starting at the source node and then exploring as far as possible along each branch before backtracking.
