#include<bits/stdc++.h>
using namespace std;
 
struct Move
{
    int row, col;
};

char maxplayer = 'x', minplayer = 'o';
bool isleft(char board[3][3])
{
    for (int i = 0; i<3; i++)
        for (int j = 0; j<3; j++)
            if (board[i][j]=='_')
                return true;
    return false;
}
 
int calculatevalue(char board[3][3])
{
    for (int row = 0; row<3; row++)
    {
        if (board[row][0]==board[row][1] &&
            board[row][1]==board[row][2])
        {
            if (board[row][0]==maxplayer)
                return +10;
            else if (board[row][0]==minplayer)
                return -10;
        }
    }
    for (int col = 0; col<3; col++)
    {
        if (board[0][col]==board[1][col] &&
            board[1][col]==board[2][col])
        {
            if (board[0][col]==maxplayer)
                return +10;
 
            else if (board[0][col]==minplayer)
                return -10;
        }
    }
 
    if (board[0][0]==board[1][1] && board[1][1]==board[2][2])
    {
        if (board[0][0]==maxplayer)
            return +10;
        else if (board[0][0]==minplayer)
            return -10;
    }
 
    if (board[0][2]==board[1][1] && board[1][1]==board[2][0])
    {
        if (board[0][2]==maxplayer)
            return +10;
        else if (board[0][2]==minplayer)
            return -10;
    }
    return 0;
}
int minimax(char board[3][3], int depth, bool isMax)
{
    int score = calculatevalue(board);
    if (score == 10)
        return score;
    if (score == -10)
        return score;
    if (isleft(board)==false)
        return 0;
    if (isMax)
    {
        int best = -1000;
        for (int i = 0; i<3; i++)
        {
            for (int j = 0; j<3; j++)
            {
                if (board[i][j]=='_')
                {
                    board[i][j] = maxplayer;
                    best = max( best,minimax(board, depth+1, !isMax) );
                    board[i][j] = '_';
                }
            }
        }
        return best;
    }
 
    else
    {
        int best = 1000;
        for (int i = 0; i<3; i++)
        {
            for (int j = 0; j<3; j++)
            {
                if (board[i][j]=='_')
                {
                    board[i][j] = minplayer;
                    best = min(best,minimax(board, depth+1, !isMax));
                    board[i][j] = '_';
                }
            }
        }
        return best;
    }
}
Move findBestMove(char board[3][3])
{
    int bestVal = -1000;
    Move bestMove;
    bestMove.row = -1;
    bestMove.col = -1;
    for (int i = 0; i<3; i++)
    {
        for (int j = 0; j<3; j++)
        {
            if (board[i][j]=='_')
            {
                board[i][j] = maxplayer;
                int moveVal = minimax(board, 0, false);
                board[i][j] = '_';
                
                if (moveVal > bestVal)
                {
                    bestMove.row = i;
                    bestMove.col = j;
                    bestVal = moveVal;
                }
            }
        }
    }
    return bestMove;
}
Move findBestMoveHuman(char board[3][3])
{
    int bestVal = 1000;
    Move bestMove;
    bestMove.row = -1;
    bestMove.col = -1;
    for (int i = 0; i<3; i++)
    {
        for (int j = 0; j<3; j++)
        {
            if (board[i][j]=='_')
            {
                board[i][j] = minplayer;
                int moveVal = minimax(board, 0, true);
                board[i][j] = '_';
                
                if (moveVal < bestVal)
                {
                    bestMove.row = i;
                    bestMove.col = j;
                    bestVal = moveVal;
                }
            }
        }
    }
    return bestMove;
}
void print(char board[3][3])
{
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++)
			{
				printf(" %c | ",board[i][j]);
			}
			printf("\n---+---+---\n");
		}
 
}

int main()
{
	int row,col;
    char board[3][3] =
    {
        { '_', '_','_' },
        { '_', '_', '_' },
        { '_', '_', '_' }
    };
	while(isleft(board))
	{
		scanf("%d %d",&row,&col);
		board[row][col]='o';
		Move bestMove = findBestMove(board);
		board[bestMove.row][bestMove.col]='x';
		print(board);
		if(calculatevalue(board)==10)
		{
			printf("Computer wins\n");
			break;
		}
		else if (calculatevalue(board)==-10)
		{
			printf("You wins\n");
			break;
		}
		bestMove=findBestMoveHuman(board);
		printf("Suggestion: %d %d",bestMove.row,bestMove.col);
	}
	if(!isleft(board))
	{
		if(calculatevalue(board)==10)
		{
				printf("Computer wins\n");
		}
		else if(calculatevalue(board)==-10)
		{
				printf("You wins\n");
		}
		else if(calculatevalue(board)==0)
		{
			printf("Draw\n");
		}
	}
    return 0;
}
