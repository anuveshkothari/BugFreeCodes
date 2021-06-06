Problem Statement:
Chefland has 2 different types of coconut, type A and type B. Type A contains only xa milliliters of coconut water and type B contains only xb grams of coconut pulp. Chef's nutritionist has advised him to consume Xa milliliters of coconut water and Xb grams of coconut pulp every week in the summer. Find the total number of coconuts (type A + type B) that Chef should buy each week to keep himself active in the hot weather.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, four integers xa, xb, Xa, Xb.
Output
For each test case, output in a single line the answer to the problem.

Constraints
1≤T≤15000
100≤xa≤200
400≤xb≤500
1000≤Xa≤1200
1000≤Xb≤1500
xa divides Xa.
xb divides Xb.
Subtasks
Subtask #1 (100 points): original constraints

Sample Input
3
100 400 1000 1200
100 450 1000 1350
150 400 1200 1200
Sample Output
13
13
11
Explanation
TestCase 1: Number of coconuts of Type A required = 1000100=10 and number of coconuts of Type B required = 1200400=3. So the total number of coconuts required is 10+3=13.

TestCase 2: Number of coconuts of Type A required = 1000100=10 and number of coconuts of Type B required = 1350450=3. So the total number of coconuts required is 10+3=13.

TestCase 3: Number of coconuts of Type A required = 1200150=8 and number of coconuts of Type B required = 1200400=3. So the total number of coconuts required is 8+3=11.


Solution:
package com.challenge.june;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class COCONUT {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Scanner sc = new Scanner(System.in);

//		String test = br.readLine();
		
//		int t = Integer.parseInt(test);
		int t = 0;
		if(sc.hasNextInt())
			t = sc.nextInt();
		while (t-- > 0) {
//			String testCase = br.readLine();

//			String[] splitCase = testCase.split(" ");

//			int xa = Integer.parseInt(splitCase[0]);
//			int xb = Integer.parseInt(splitCase[1]);
//			int Xa = Integer.parseInt(splitCase[2]);
//			int Xb = Integer.parseInt(splitCase[3]);
			int xa = sc.nextInt();
			int xb = sc.nextInt();
			int Xa = sc.nextInt();
			int Xb = sc.nextInt();

			int total = (Xa / xa) + (Xb / xb);

			System.out.println(total);
		}
	}

}
