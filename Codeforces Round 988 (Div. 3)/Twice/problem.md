Link to the problem:

(https://codeforces.com/contest/2037/problem/A)

Kinich wakes up to the start of a new day. He turns on his phone, checks his mailbox, and finds a mysterious present. He decides to unbox the present.

Kinich unboxes an array 𝑎 with 𝑛 integers. Initially, Kinich's score is 0. He will perform the following operation any number of times:

* Select two indices 𝑖 and 𝑗 (1≤𝑖<𝑗≤𝑛) such that neither 𝑖 nor 𝑗 has been chosen in any previous operation and 𝑎𝑖=𝑎𝑗.          
   Then, add 1 to his score.

Output the maximum score Kinich can achieve after performing the aforementioned operation any number of times.

Input
The first line contains an integer 𝑡 (1≤𝑡≤500) —- the number of test cases.

The first line of each test case contains an integer 𝑛 (1≤𝑛≤20) —- the length of 𝑎.

The following line of each test case contains 𝑛 space-separated integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛).

Output
For each test case, output the maximum score achievable on a new line.

Example:

Input
5
1
1
2
2 2
2
1 2
4
1 2 3 1
6
1 2 3 1 2 3

Output:
0
1
0
1
3

Note
In the first and third testcases, Kinich cannot perform any operations.

In the second testcase, Kinich can perform one operation with 𝑖=1 and 𝑗=2.

In the fourth testcase, Kinich can perform one operation with 𝑖=1 and 𝑗=4.