#include <iostream>
#include <vector>

using namespace std;

class Node{

};

class Problem{
    private:
        initialState;
        goalState;
        operators;


};

class algoSelector{
    private:
        vector<int> puzzle = {1,0,3,4,2,6,7,5,8};
        int method;
    public:
        void setMethod(int choice2) { method = choice2; }
        void setPuzzle(vector<int> userPuzzle) { puzzle = userPuzzle; }
        void runMethod();
        void UCS(Problem problem);
        void AMT();
        void AED();
};

void algoSelector::UCS(Problem problem){
    
}
void algoSelector::AMT(){

}
void algoSelector::AED(){

}
void algoSelector::runMethod(){
    switch(method){
        case 1:
            UCS();
            break;
        case 2:
            AMT();
            break;
        case 3:
            AED();
            break;
    }
}

int main()
{
int type, method;
vector<int> puzzle;

while (true){ 
    cout << "Welcome to acarp022 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle." << endl;
    cin >> type;
    if (type == 1 || type == 2) break;
}

if (type == 2){

    cout << "Enter your puzzle, use a zero to represent the blank\nEnter the first row, use a space between numbers: ";
    
    cout << "\nEnter the second row, use space or tabs between numbers: ";

    cout << "\nEnter the third row, use space or tabs between numbers: ";

}

while (true){
    cout << "Enter your choice of algorithm:\nUniform Cost Search.\nA* with the Misplaced Tile heuristic.\nA* with the Euclidean distance heuristic." << endl;
    cin >> method;
    if (method == 1 || method == 2|| method == 3) break;
}

algoSelector puzzle_solver;
if(type == 1) puzzle_solver.setMethod(method);
if(type == 2){
    puzzle_solver.setMethod(method);
    puzzle_solver.setPuzzle(puzzle);
}

puzzle_solver.runMethod();


return 0;
}