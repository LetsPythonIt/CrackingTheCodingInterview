// Implement an algorithm to determine if a string has all unique characters.

#include<iostream>
#include<algorithm>


using namespace std;

bool isUnique(std::string userString){
	// returns true if a string has all unique characters.
	
	// Sort the string to reduce the number of loops.
	sort(userString.begin(), userString.end());
	
	for (int i=0; i < userString.length(); i++){
		if (userString[i-1] == userString[i])
			return false;
	}
	
	return true;
}


int main(){
	
	cout << "Enter a string: ";
	std::string testString;
	cin >> testString;
	bool result{isUnique(testString)};
	
	if (result)
		cout << "String is unique\n";
	else
		cout << "String is not unique\n";
	
	
	return 0;
}
