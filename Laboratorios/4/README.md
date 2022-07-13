# CI-0130-2022-S1 | Laboratory 4

This project was developed by:

**B82957** | Marco Ferraro Rodriguez <br>
**B71146** | Gabriel Bogantes Armijo

In the implementation of the project it is interesting to note that the value <i>m</i> is the same as the period thanks to the nature of the algorithm and the random number generator.

It is important to note that, the simulation has been run with smaller values because otherwise the simulation takes way too long for us to be able to document it, the program was left overnight executing and it did not print any values. The parameter for good_abm has been reduced to 1 million and instead of doing 100 000 simulations, 10 000 simulations were made. 

When the tests are executed the values used are the following:
<code>

    player_cards_numbers.append(index)
    stack.pop(index)
    player_cards_numbers.append(indexTwo)
    stack.pop(indexTwo)

</code>
Where the index value is decided by the Card array generated. To obtain the desired value expected it is important to take into account that the stack pops the value, changing the position of <i>n+k</i> values in the array. 

<code>

    symbols = ['D', 'H', 'S', 'T']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

</code>

The order is shown as follows: [ 1D, 1H, 1S, 1T, 2D, 2H, 2S, 2T, 3D, 3H, 3S, 3T, 4D, 4H, ... ]

<p>The values used to get the results are the following:</p>

- <u>A Pair of AA's</u>: Tested with the index = 1 on both cases thanks to the use of the stack to pop the previous values. [ 1H , 1S ]
    <p><b>Wins %:</b> 52.2</p>
    <p><b>Losses %:</b> 47.8</p>

    ![pairAAs](https://i.imgur.com/AqHHX73.png)
- <u>A Pair of 22's</u>: Tested with the index = 4 on both cases thanks to the use of the stack to pop the previous values. [ 4D, 4H ]
    <p><b>Wins %:</b> 52.54</p>
    <p><b>Losses %:</b> 47.59</p>

    ![pair22s](https://i.imgur.com/zfKBQot.png)
- <u>2 and 7 from a different suit</u>: Tested with the index = 4 and indexTwo = 26, which are equivalent to [ 2 D ] and [ 7 T ]
    <p><b>Wins %:</b> 34.49</p>    
    <p><b>Losses %:</b> 65.51</p>

    ![pair27s](https://i.imgur.com/Nqus0fJ.png)
