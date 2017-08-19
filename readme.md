[![Build Status](https://travis-ci.org/richardadalton/python_game_of_life.svg?branch=master)](https://travis-ci.org/richardadalton/python_game_of_life)

# Conway's Game Of Life

## About
Game of Life is a cellular automaton devised by Mathematician John Conway. The game consists of a grid of cells, each of which are either alive or dead. The evolution of the cells is entirely determined by the initial pattern. The game requires no user input.

## Rules
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

