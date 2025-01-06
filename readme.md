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

## Implementation
One non-standard aspect of this implementation is that live cells age. They appear gradually darker the older they get. This behaviour is turned off by default.  Use the aging parameter (-a) to specify a max age for cells.

## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/python_game_of_life.git
```

Create a virtual environment using your preferred method. E.g.

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
```

Install dependencies

```bash
$ pip install -r requirements.txt
```

If there are any problems running the project, try updating to the latest versions of PIP and PyGame.

## Running Python OCR

```bash
$ python game_of_life.py [-h] [-s CELL_SIZE] [-r ROWS] [-c COLUMNS]

arguments:
  -h, --help                  show this help message and exit
  -s, --cell_size CELL_SIZE   The size of a cell within the grid
  -r, --rows ROWS             The number of rows in the grid
  -c, --columns COLUMNS       The number of columns in the grid
  -a, --aging AGING           The number of generations that a living cell survives, Default is forever
```
