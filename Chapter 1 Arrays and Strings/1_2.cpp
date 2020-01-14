// Given two strings, write a method to decide if one is a permutation of the other.

#include<iostream>
#include<algorithm>

using namespace std;

bool isPermutation(string testString1, string testString2){
	
	if (testString1.length() != testString2.length())
		return false;
	
	sort(testString1.begin(), testString1.end());
	sort(testString2.begin(), testString2.end());
	
	for (unsigned int i=0; i<testString1.length(); i++){
		if (testString1[i] != testString2[i])
			return false;
	}
	return true;
}

int main(){
	
	string userString1;
	string userString2;
	
	cout << "Enter a string: ";
	cin >> userString1;
	
	cout << "\nEnter second string: ";
	cin >> userString2;

	if (isPermutation(userString1, userString2))
		cout << "Strings are Permutation\n";
	else
		cout << "Strings ain't Permutations\n";
	
	
	return 0;
}
