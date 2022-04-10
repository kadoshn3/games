//KINECT 4
#include <iostream>

using namespace std;
void kinect(char x[6][7]);
void answers(char x[6][7], bool& win);
int main() {

	int column, turns;
	turns = 0;
	char board[6][7] = {
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
		{ ' ', ' ', ' ', ' ', ' ', ' ', ' ' }
	};
	bool win = false;
	cout << "\tKINECT 4" << endl << endl;
	kinect(board);
	cout << endl;
	int row[6] = { 0, 0, 0, 0, 0, 0 };
	do {
		cout << "Enter a column (1-6): ";
		cin >> column;
		cout << endl;
		if ((turns % 2) == 0) {
			if (column == 1) {
				board[5 - row[0]][column - 1] = 'O';
				row[0]++;
				if (row[0] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 2) {
				board[5 - row[1]][column - 1] = 'O';
				row[1]++;
				if (row[1] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 3) {
				board[5 - row[2]][column - 1] = 'O';
				row[2]++;
				if (row[2] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 4) {
				board[5 - row[3]][column - 1] = 'O';
				row[3]++;
				if (row[3] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 5) {
				board[5 - row[4]][column - 1] = 'O';
				row[4]++;
				if (row[4] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 6) {
				board[5 - row[5]][column - 1] = 'O';
				row[5]++;
				if (row[5] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
		}
		if (!(turns % 2) == 0) {

			if (column == 1){
				board[5 - row[0]][column - 1] = 'X';
				row[0]++;
				if (row[0] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 2){
				board[5 - row[1]][column - 1] = 'X';
				row[1]++;
				if (row[1] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 3){
				board[5 - row[2]][column - 1] = 'X';
				row[2]++;
				if (row[2] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 4){
				board[5 - row[3]][column - 1] = 'X';
				row[3]++;
				if (row[3] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 5){
				board[5 - row[4]][column - 1] = 'X';
				row[4]++;
				if (row[4] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
			if (column == 6){
				board[5 - row[5]][column - 1] = 'X';
				row[5]++;
				if (row[5] > 6) {
					cout << "Invalid move. Enter a different column" << endl;
					turns++;
				}
			}
		}
		kinect(board);
		answers(board, win);
		cout << endl;
		turns++;
	} while (win == false);
	cin.get();
	cin.get();
	return 0;
}

void kinect(char x[6][7]) {
	int numbers[6] = { 1, 2, 3, 4, 5, 6 };
	cout << "      ";
	for (int i = 0; i < 6; i++)
		cout << numbers[i] << "   ";
	cout << endl;
	for (int i = 0; i < 6; i++) {
		cout << "   ";
		for (int j = 0; j < 7; j++) {
			cout << " | " << x[i][j];
			if (j == 6)
				cout << endl;	
		}
		if (i == 5)
			cout << "   |+++++++++++++++++++++++++|" << endl;
	}
}

void answers(char board[6][7], bool& win) {
	int winner = 2;
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++)
			if ((board[i][j] == 'O' && board[i][j + 1] == 'O' && board[i][j + 2] == 'O' && board[i][j + 3] == 'O')
				|| (board[i][j] == 'O' && board[i + 1][j] == 'O' && board[i + 2][j] == 'O' && board[i + 3][j] == 'O')
				|| (board[i][j] == 'O' && board[i + 1][j + 1] == 'O' && board[i + 2][j + 2] == 'O' && board[i + 3][j + 3] == 'O'))
				//|| (board[i][j] == 'O' && board[i - 1][j - 1] == 'O' && board[i - 2][j - 2] == 'O' && board[i - 3][j - 3] == 'O'))
			{
				win = true;
				winner = 0;
			}
		for (int j = 7; j > 0; j--)
			if (board[i][j] == 'O' && board[i - 1][j - 1] == 'O' && board[i - 2][j - 2] == 'O' && board[i - 3][j - 3] == 'O')
			{
				win = true;
				winner = 0;
			}
	}
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++)
			if (   (board[i][j] == 'X' && board[i][j + 1] == 'X' && board[i][j + 2] == 'X' && board[i][j + 3] == 'X')
				|| (board[i][j] == 'X' && board[i + 1][j] == 'X' && board[i + 2][j] == 'X' && board[i + 3][j] == 'X')
				|| (board[i][j] == 'X' && board[i + 1][j+1] == 'X' && board[i + 2][j+2] == 'X' && board[i + 3][j+3] == 'X'))
			{
				win = true;
				winner = 1;
			}
		for (int j = 7; j > 0; j--)
			if (board[i][j] == 'X' && board[i + 1][j + 1] == 'X' && board[i + 2][j + 2] == 'X' && board[i + 3][j + 3] == 'X')
			{
				win = true;
				winner = 1;
			}
	}
	if (winner == 1)
		cout << " X's win! Congratulations";
	if (winner == 0)
		cout << " O's win! Congratulations";
}
