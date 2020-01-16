/*
 * Write a recursive function to multiply 2 pos no. without using
 * * operator.
 */
 
#include<iostream>
#include<cmath>

using namespace std;

int iterativeMultiply(int n1, int n2){
	int result{0};
	for (int i=0; i<n2; i++)
		result += n1;
	return result;
}

int multiply(int n1, int n2){
	
	if (n2 == 1)
		return n1;
	else
		return n1 + multiply(n1, n2-1);
}

int main()
{
	int n1{199};
	int n2{999};
	
//	if (n2 > n1){ // swap
//		n2 = n1 + n2;
//		n1 = n2 - n1;
//		n2 = n2 - n1;
//	}
	
	cout << n1 << " " << n2 << endl;
	
	cout << iterativeMultiply(n1, n2) << endl;
	cout << multiply(n1, n2) << endl;
	return 0;
}
