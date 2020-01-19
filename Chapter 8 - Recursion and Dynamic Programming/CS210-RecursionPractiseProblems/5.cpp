/*
 *  Find Greatest Common Divisor (GCD) of 2 numbers using recursion.
 */
 
#include<iostream>

using namespace std;

int GCD(int a, int b){
	if (b==0)
		return a;
	return GCD(b, a%b);
}


int main(){
	int A{24};
	int B{21};
	cout << GCD(A, B) << endl;
	return 0;
}
