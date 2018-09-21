#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <iostream>
using namespace std;

//questions
//1. is dynamic array superior to vector? how much so?
//2. Should I use a single block of memory for x and y?
//3. Is my understanding of the concept of filtering correct?

//3. what additional optimizations can I do? (process matrix multiplication in blocks?),
// storing max/min inside of heap? Multithreading?
// what about optimizations while calculating dy & dx?


int ** matrixMultiply(int ** m) {
	return NULL;
}

int main() {
	int rowLength, columnLength;
	cout << "row";
	cin >> rowLength;
	cout << "column";
	cin >> columnLength;

	int ** m = new int[rowLength][columnLength];
	for (int i = 0; i < rowLength; i++)
		for (int j = 0; j < columnLength; j++)
			m[i][j] = rand();

	for (int i = 0; i < rowLength; i++)
		for (int j = 0; j < columnLength; j++)
			cout << m[i][j] << endl;

	return 0;
}
