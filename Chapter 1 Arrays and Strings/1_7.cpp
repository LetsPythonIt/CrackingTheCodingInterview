/*
 * Write a method to rotate the image by 90deg
 * Can you do it inplace?
 */
 

#include<iostream>
#include<vector>

using namespace std;


vector<vector<int>> transposeImage(vector<vector<int>> userImage){
	// Transpose an image
	int height = int(userImage.size()); // Square Matrix (NxN)
	vector<vector<int>> newImage(userImage.size(), vector<int>(userImage.size()));
	
	for (int i=0; i<height; i++){
		for (int j=0; j<height; j++){
			newImage[i][j] = userImage[j][i];
		}
	}
	return newImage;
}

vector<vector<int>> rotatedImage180(vector<vector<int>> userImage){
	// Rotate an Image 180 ACW
	
	int height = int(userImage.size()); // Square Matrix (NxN)
	
	vector<vector<int>> newImage(userImage.size(), vector<int>(userImage.size()));
	
	for (int i=0; i<height; i++){
		int row{0};
		for (int j=0; j<height; j++){
			newImage[height-1-i][height-1-j] = userImage[i][j];
		}
		row++;
	}
	return newImage;
}

vector<vector<int>> rotatedImage(vector<vector<int>> userImage){
	// Rotate an Image 90 ACW
	
	int height = int(userImage.size()); // Square Matrix (NxN)
	
	vector<vector<int>> newImage(userImage.size(), vector<int>(userImage.size()));
	
	for (int i=0; i<height; i++){
		int row{0};
		for (int j=0; j<height; j++){
			newImage[height-1-j][i] = userImage[i][j];
		}
		row++;
	}
	return newImage;
}


void printVector(vector<vector<int>> userVector){
	// prints a 2D vector
	int height{int(userVector.size())};
	int wide{int(userVector[0].size())};
	
	for (int i=0; i< height; i++){
		for(int j=0; j<wide; j++){
			cout << userVector[i][j] << " ";
		}
		cout << "\n";
	}
}

int main(){
	// Declaring an Image
	vector<vector<int>> image{{1,2,3},{4,5,6},{7,8,9}};
	
	// print the User vector
	printVector(image);
	
	// Rotate the image
	vector<vector<int>> newImage{rotatedImage(image)};
	
	// print the Rotated Vector
	cout << endl;
	printVector(newImage);
	
	return 0;
}
