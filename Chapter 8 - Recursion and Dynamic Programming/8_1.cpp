#include<iostream>
#include<string>

/*
 * You are climbing a stair case. It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 or 3 steps. In how many distinct ways can you climb to the top?
 */
 


using namespace std;

int climbStairs(int N){
	if (N==0)
		return 0;
	if (N==1)
		return 1;
	if (N==2)
		return 2;
	if (N==3)
		return 3;
	else
		return climbStairs(N-1) + climbStairs(N-2) + climbStairs(N-3);
}

int main(){
	
	int n = 2;
	int count;
	
	count = climbStairs(n);
	
	cout << count << endl;
	
	return 0;
	
	
}



