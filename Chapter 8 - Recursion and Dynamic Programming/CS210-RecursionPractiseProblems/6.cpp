/*
 *  Reverse a string using recursion.
 */
 
#include<iostream>
#include<algorithm>

using namespace std;

void reverse(string &str, unsigned int k){
	static unsigned int i{0};
	
	if (k==str.length())
		return;
	
	reverse(str, k+1);
	
	if (i <= k)
		swap(str[i++], str[k]);
	
	}

int main(){

	string testString{"Reverse This String"};
	reverse(testString, 0);
	cout << testString << endl;
	
	return 0;
}
