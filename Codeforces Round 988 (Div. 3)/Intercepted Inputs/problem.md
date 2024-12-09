Link to the problem:
(https://codeforces.com/contest/2037/problem/B)

To help you prepare for your upcoming Codeforces contest, Citlali set a grid problem and is trying to give you a 𝑛 by 𝑚 grid through your input stream. Specifically, your input stream should contain the following:

* The first line contains two integers 𝑛 and 𝑚 — the dimensions of the grid.
* The following 𝑛 lines contain 𝑚 integers each — the values of the grid.

However, someone has intercepted your input stream, shuffled all given integers, and put them all on one line! Now, there are 𝑘 integers all on one line, and you don't know where each integer originally belongs. Instead of asking Citlali to resend the input, you decide to determine the values of 𝑛 and 𝑚 yourself.

Output any possible value of 𝑛 and 𝑚 that Citlali could have provided.

Input:

The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains an integer 𝑘 (3≤𝑘≤2*10^5) — the total number of inputs in your input stream.

The following line of each test case contains 𝑘 integers 𝑎1,𝑎2,…,𝑎𝑘 (1≤𝑎𝑖≤𝑘) — the shuffled inputs of your input stream. It is guaranteed that 𝑛 and 𝑚 are contained within the 𝑘 integers.

It is guaranteed that the sum of 𝑘 over all test cases does not exceed 2*10^5.

Output:

For each test case, output two integers, one possible value of 𝑛 and 𝑚. If multiple possible answers exist, output any.

Example:

Input
5
3
1 1 2
11
3 3 4 5 6 7 8 9 9 10 11
8
8 4 8 3 8 2 8 1
6
2 1 4 5 3 3
8
1 2 6 3 8 5 5 3

Output
1 1
3 3
2 3
4 1
1 6

* Note
In the first test case, the initial input could have been the following:

1 1

2

In the second test case, the initial input could have been the following:

3 3

4 5 6

7 8 9

9 10 11