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
