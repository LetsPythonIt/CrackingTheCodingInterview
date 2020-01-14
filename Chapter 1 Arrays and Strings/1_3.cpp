// Write a program to URLify a given string


// Write a method to URLify a string by replacing spaces with %20

#include<iostream>
#include<vector>

using namespace std;

vector<char> URLify(string userString){
	int len{userString.length()};
	vector<char> returnString;
	
	for (unsigned int i=0; i<len; i++){
		if (userString[i] == ' '){
			returnString.push_back('%');
			returnString.push_back('2');
			returnString.push_back('0');
		}
		else
			returnString.push_back(userString[i]);
	}
	
	return returnString;
}

int main(){
	string testString;
	cout << "Input a string with spaces in between\n";
	getline(cin, testString);
	
	vector<char> newString{URLify(testString)};
	
	// print out the vector
	for (unsigned int i=0; i<newString.size(); i++)
		cout << newString.at(i);
	
	cout << endl;
	
	return 0;
}

//int main(){

//	std::string input;
//	std::string testString;
//	int length;
//	
//	getline(cin, testString);
//	
//	for (unsigned int i=0; i < testString.size(); i++){
//		if (testString[i] == ' ')
//			cout << "%20";
//		else
//			cout << testString[i];
//	}
//}
