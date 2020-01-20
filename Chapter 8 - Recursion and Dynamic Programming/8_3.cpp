/*
 * Magic Index: A[i] = i
 * Given a sorted array of distinct integers, write method to find magic index.
 */
 
#include<iostream>
#include<vector>

using namespace std;

int BS(int arr[], int low, int high){
	if(high >= low){
		int mid = (low+high)/2;
		if(mid == arr[mid])
			return mid;
		if(mid > arr[mid])
			return BS(arr, mid+1, high);
		else
			return BS(arr, low, mid-1);
	}
	return -1;
}

int main(){
	
	int arr[] = {-10, -1, 0, 3, 10, 11, 30, 50, 100};
	int length{sizeof(arr)/sizeof(arr[0])};
	cout << BS(arr, 0, length-1) << endl;
	
	return 0;
}
