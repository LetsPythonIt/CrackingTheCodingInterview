#include<iostream>
#include<string>

/*
 * You are climbing a stair case. It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 or 3 steps. In how many distinct ways can you climb to the top?
 */
 


using namespace std;

int Memory[100]; //  Global array

int climbStairs(int N){
	if ((N<4) and (N>-1))
		return N;
	if (Memory[N] != -1)
		return Memory[N];
	Memory[N] = climbStairs(N-1) + climbStairs(N-2) + climbStairs(N-3);
	return Memory[N];
}

int main(){
	
	int n = 46;
	int count;
	
	for (int i=0; i<100; i++)
		Memory[i] = -1;
	
	count = climbStairs(n);
	
	cout << count << endl;
	
	return 0;
	
	
}


