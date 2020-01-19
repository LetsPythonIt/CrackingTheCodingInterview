/*
 * Write a function for mutliply(a, b), where a and b are both positive
 * integers, but you can only use the + or − operators.
 */
 
#include<iostream>
#include<cstring>

using namespace std;

int Multiply(int A, int B){
	// Base Case
	if (B==0)
		return B;
	return A + Multiply(A, B-1);
}


int main(){
	int A{9};
	int B{10};
	cout << Multiply(A, B) << endl;
	return 0;
}
