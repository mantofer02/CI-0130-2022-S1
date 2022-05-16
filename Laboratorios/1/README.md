# CI-0130-2022-S1 | Laboratory 1

This project was developed by:

**B82957** | Marco Ferraro Rodriguez
**B71146** | Gabriel Bogantes Armijo

- [CI-0130-2022-S1 | Laboratory 1](#ci-0130-2022-s1--laboratory-1)
  - [What is Linear Programing?](#what-is-linear-programing)
  - [How does the simplex method work?](#how-does-the-simplex-method-work)
    - [History](#history)
    - [Overview](#overview)
    - [Standard form](#standard-form)
    - [Simplex tableau](#simplex-tableau)
    - [Pivot operations](#pivot-operations)
  - [How does the bounded linear programing works?](#how-does-the-bounded-linear-programing-works)
    - [Algorithm](#algorithm)
  - [Run the program](#run-the-program)

## What is Linear Programing?

<p> Linear programing, also known as linear optimization is a mathematical method to best achieve optimization regarding minimization and
maximization of costs.It is based in linear relationships, the procedure consists of analizing an objective function that is subject 
to linear equality and linear inequality constraints. Its design is always based as a convex polytope when drawn in an "X" and "Y" ascis table. The idea behind linear programing is to find all the points in the polytope where this function has the smallest or largest value if such point exists. It is important to note that one of the restraints behind this mathematical procedure is that every possible value always has to be positive. </p>

<p>There are several ways to complete this algorithm, the following are the main ones:
<ol>
    <li> Linear programing through graphical method </li>
    <li> Linear programing through simplex method </li>
    <li> Linear programing through binary method </li>
    <li> Linear programming with bounds </li>
</ol>
</p>

## How does the simplex method work?

### History

<p> The simplex algorithm was originally developed by George Bernard Dantzig. This American mathematician worked on planning methods for the US Army Air Force during World War II.
During 1946 his colleague challenged him to create a planning process to distract him from taking another job, he did through formulating linear inequalities inspired by
Wassily Leontief (input-output analyst). During 1947 Dantzig included an objective function as part of his formulation, this made his theory more mathematically tractable. Later, Dantzig published
his research as a thesis to earn his doctorate. After that, the column used in this thesis gave Dantzing insight that made him believe that the Simplex method would be very efficient.
</p>

### Overview

<p>
The simplex algorithm operates on linear programs in the canonical form:

Maximize <strong> c<sup>T</sup>x </strong>
subject to <strong> Ax <= b </strong> and <strong> x >= 0 </strong> with <strong>c = (c<sub>1</sub>, ..., c<sub>n</sub>)</strong> the coeficients of the objective function. The <strong>( . )<sup>T<sup></strong> is the matrix transponse, and <strong> x = (x<sub>1</sub>, ..., x<sub>n</sub>) </strong> are the variables of the problem, <strong>A</strong> is a <em>p x n</em> matrix, and <strong>b = (b<sub>1</sub> ..., b<sub>n</sub>)</strong>. There is a straightforward process to convert any linear program into one in standard form. 

In geomertric terms, the feasible region by all values of <strong>x</strong> such that <strong>Ax</strong> <= <strong>b</strong> and for every <em>i, x<sub>i</sub></em> >= 0 is a convex polytope. An extreme point or vertex of this polytope is known as a <em>basic feasible solution </em>. This shows the importance of the constraints that the problem has, without them there would not be a finite ammount of extreme points. </p>

The solution of a linear program is acomplished in two steps:
<ol>
    <li> In the fist step, a starting extreme points is found, depending on the problem's nature it might be trivial but it can be solved by applying the simplex algorithm to a modified version of the original program. The typical results out of this step are that a basic feasible solution is found or that the feasible region is empty (this would make the linear program infeasible). </li>
    <li>In the second step, the simplex algorithm is applied using the feasible solution found in the first step. The possible results from this step are an optimun basc fesaible solution or an infinite edge on which the objective function is unbound above. </li>
</ol>

### Standard form

<p>The transformation of a liuner program to one in standard form is done by the following way: 

For each variable with a lower bound other than 0, a new variable is introuced representing the difference between the variable and bound. For instance:


<strong>x<sub>1</sub> >= 5</strong> </p>

a new variable, <strong>y<sub>1</sub></strong>, is introduced with 

<strong>y<sub>1</sub> = x<sub>1</sub> - 5 

x<sub>1</sub> = y<sub>1</sub> + 5</strong>

The second equation may be usted to eliminate <strong>x<sub>1</strong> from the linear program. This makes all lower bound constraints able to be changed to non-negativity restrictions. 

Then, for each remaining inequality constraint, a new variable called <em>slack variable </em> is introduced to change the constraint from an inequality to an equality. For example, the inequality:
<strong>x<sub>2</sub> + 2x<sub>3</sub> <= 3 </strong> is now replaced with <strong>x<sub>2</sub> + 2x<sub>3</sub> + s<sub>1</sub> = 3 </strong>

This makes it easier to perform algebraic manipulation on inequalities in this form. It is important to know that in equalities where a >= appears some authors frefer to the variable introduced as a <em>surplus variable</em>.

### Simplex tableau

A linear program is then represented as a tableau. The first row represent the objective function and the remaining rows specify teh constraints. Also, aditional columns need to be added to represent the slack or surplus variables. If the columns of the pivot element can be rearranged so that it contains the identity matrix then tableau is said to be in canonical form.

### Pivot operations

When a geometrical operation of moving from a basic and trivial feasible solution to an adjacent basic feasible solution is implemented as a <em> pivot operation </em>. First a nonzero pivot element is selected to a nonbasic column. Then, it is rearanged through algebraic operations so the value changes to 1. In effect, the variable corresponding to the pivot column enters the set of basic variables and is called the entering variable where as the variable being replaced leaves the set of basic variables and is called the leaving variable.

## How does the bounded linear programing works?

The simplex method works very well to obtain a feasible solution for maximization or minimization but sometimes it is required to have whole values regarding the variables. This method uses either way to solve the problem at first, then it checks if the values are whole numbers. If they are not whole numbers, it proceeds to bound the possible solutions on both sides (uper and lower) until the values become whole numbers.

### Algorithm

When a tablue is in canonical form, the simplex method can be applied to it. The simplex algorithm proceeds to perform successive and iterative pivot operations each of which give an improved basic feasible solution. The choice of pivot element at each step is largely determined by te requirement that this pivot improves the solution. After this, the process repeats itself until the best feasible solution is found. 

In this project, a simplex method calculator will be built. It will recieve an objective function, and its respective constraints through a set of strings.
The program will parse and execute the simplex method to solve any doable maximization and minimization functions. It is important to note that the program is able
to recieve any amount of variables and constraints. Aditionally, the program will be able to perform the lienar programing through bounding. It consist of
bounding the variables into whole numbers. For example: if the X1 value is 5.6, the new added restraints are 5 <= X1 and 6 >= X1. This method is very useful 
if the expected result consists of a whole ammount of possible options. 

## Run the program

For this specific simplex calculator the user has to enter the equation and the constraints through the main function parameters. It has to follow the format shown bellow:

<strong> Equation</strong>: The equation has to have at least one or more sub indexed variables with their respective coeficient, if the coeficient equals to 1 it is not necesarry for it to be written on the string. For example: {"Cx<sub>1</sub>, ... , Cx<sub>n</sub>"}

<strong> Restriction</strong>: It depends whether the restriction is lower or upper bound the inequality changes between "<=" or ">=". For example:{"Cx<sub>1</sub>, ... , Cx<sub>n
</sub> <= N"} 

When the equation and restrictions are set and ready to be calculated, the user is able to run the program by running the following commands in the respective directory: 

<center>
  <code> 
    python main.py 
  </code> 
</center>

[Bound Simplex Exercise](bound_simplex.md)