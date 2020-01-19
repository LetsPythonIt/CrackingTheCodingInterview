/*
 * Compute the sum of natural numbers until N.
 */
 
#include<iostream>
#include<cstring>

using namespace std;

int Natural(int N){
	// Base Case
	if (N==1)
		return 1;
	return N + Natural(N-1);
}


int main(){
	int Number{995};
	cout << Natural(Number) << endl;
	return 0;
}
