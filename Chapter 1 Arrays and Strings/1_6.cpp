/*
 * String Compression
 * aabbcdd -> a2b2cd2
*/

#include<iostream>
#include<string>

using namespace std;

string compressString(string userString){
	string newString{""};
	int globalCount{0};
	
	for (unsigned int i{0}; i<userString.length(); i+=globalCount){
		int count{0};
		for (unsigned int j{i}; j<userString.length(); j++){
			if (userString[i] == userString[j])
				count++;
			else
				break;
		}
//	cout << userString[i] << to_string(count) << endl;
	newString = newString + userString[i] + to_string(count);
	globalCount = count;
	}
	
	if (newString.length() == 2*(userString.length()))
		return userString;
	else
		return newString;
}

int main(){
	
	string testString;
	cin >> testString;
	
	string newStr{compressString(testString)};
	cout << "\n"<< newStr << endl;
	
	return 0;
}
