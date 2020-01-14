/*
 * Check if two strings are one edit away
 * Edits:
 * 		1. Replace
 * 		2. Remove
 * 		3. Insert
 */
 
 
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>

using namespace std;

bool IsOneEditAway(string s1, string s2){
	
	// Condition 1
	if (abs(int(s1.length()) - int(s2.length())) > 1)
		return false;
	
	// Condition 2
	if (abs(int(s1.length()) - int(s2.length())) == 0){
		int diffCount{0};
		for(unsigned int i=0; i<s1.length(); i++){
			if (s1[i] != s2[i])
				diffCount++;
		}
		if (diffCount > 1)
			return false;
	}
	
	// Condition 3
	if (abs(int(s1.length()) - int(s2.length())) != 0){
		int diffCount{0};
		string shortString{s1};
		string LongString{s2};
		
		// Make sure s1 is the shorter one
		if (s1.length() > s2.length()){
			shortString = s2;
			LongString = s1;
		}
		
		cout << shortString << endl;
		cout << LongString << endl;
		
		for (unsigned int i=0; i < shortString.length(); i++){
			int charPresent{0};
			for (unsigned int j=0; j < LongString.length(); j++){
				if (shortString[i] == LongString[j])
					charPresent++;
			}
			if (charPresent != 0)
				diffCount++;
		}
//		cout << diffCount << endl;
		if (diffCount > 1)
			return false;
	}
	
	return true;
	
}

int main(){
	string str1;
	string str2;
	
	cin >> str1 >> str2;
	
	if(IsOneEditAway(str1, str2))
		cout << "Yes\n";
	else
		cout << "No\n";
}
 
