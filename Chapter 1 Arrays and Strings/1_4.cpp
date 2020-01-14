// Write a method to check if a string is a permutation of a palindrome

#include<iostream>
#include<vector>
#include<algorithm>

bool permutationPalindrome(std::string userString){
	// returns true if a string is a permutation of a palindrome
	
	sort(userString.begin(), userString.end()); // sort the string

	std::vector<int> asciiChar;
	std::vector<int> charCount;
	
	for (int i=0; i<userString.length(); i++){
		if (std::find(asciiChar.begin(), asciiChar.end(), userString[i]) != userString.end())
			break;
		else{
			
		}
	}
	
	
	
	for (int i=0; i<128; i++){
		
	}
}

int main(){
	
	std::string testString;
	getline(std::cin, testString);
	
	if(permutationPalindrome(testString))
		std::cout << "Yes, permutation of a palindrome." << std::endl;
	else
		std::cout << "No!" << std::endl;
	
	return 0;
}
