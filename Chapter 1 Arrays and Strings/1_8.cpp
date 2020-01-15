/*
 * Write an Algo such that if an element in an MxN matrix is 0, its entire row
 * and column becomes zero
 */
 
#include<iostream>
#include<vector>

using namespace std;

vector<vector<int>> zeroMatrix(vector<vector<int>> userImage){
	// Rotate an Image 90 ACW
	
	int M = int(userImage.size()); //  rows
	int N = int(userImage[0].size()); // columns
	
//	vector<vector<int>> newImage(M, vector<int>(N));
	vector<int> zeroRow;
	vector<int> zeroCol;
	
	for (int i=0; i<M; i++){
		for (int j=0; j<M; j++){
			if (userImage[i][j] == 0){
				zeroRow.push_back(i);
				zeroCol.push_back(j);
			}
		}
	}
	
	for (int i=0; i<zeroRow.size(); i++){
		for (int row=0; row<M; row++){
			for (int col=0; col<N; col++){
				if (row == zeroRow[i])
					userImage[row][col] = 0;
//				else
//					newImage[row][col] = userImage[row][col];
			}
		}
	}
	
	
	for (int i=0; i<zeroCol.size(); i++){
		for (int row=0; row<M; row++){
			for (int col=0; col<N; col++){
				if (col == zeroCol[i])
					userImage[row][col] = 0;
//				else
//					newImage[row][col] = newImage[row][col];
			}
		}
	}
	
	return userImage;
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
	vector<vector<int>> image{{1,2,3},{4,0,6},{7,8,0}};
	
	// print the User vector
	printVector(image);
	
	// Rotate the image
	vector<vector<int>> newImage{zeroMatrix(image)};
	
	// print the Rotated Vector
	cout << endl;
	printVector(newImage);
	
	return 0;
}
