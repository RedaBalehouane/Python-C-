#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

typedef struct
{
    double a,b,c,d;
} matrix;

vector<vector<double>> createMatrix(int n);
void showMatrix(vector<vector<double>> matrix);
vector<vector<double>> productMatrix(vector<vector<double>> m1, vector<vector<double>> m2, int n);
double getMin(vector<vector<double>> matrix);
double getMax(vector<vector<double>> matrix);
vector<vector<double>> fillMatrix(int n);

int main()
{
    int k;
    cout<<"Entrez la taille de la matrice : ";
    cin>> k;

    vector<vector<double>> m1 = fillMatrix(k);
    showMatrix(m1);

    vector<vector<double>> m2 = fillMatrix(k);
    showMatrix(m2);

    vector<vector<double>> m3 = productMatrix(m1, m2, k);
    showMatrix(m3);

    return 0;
}

vector<vector<double>> createMatrix(int n)
{
    vector<vector<double>> matrix;
    matrix.resize(n);

    for(int i = 0; i<n; i++)
    {   
        matrix[i].resize(n);
    }

    return matrix;
}

vector<vector<double>> fillMatrix(int n)
{
    vector<vector<double>> matrix = createMatrix(n);
    cout<<"Entrez les valeurs (i,j) de la matrice : \n";

        for(int i = 0; i<n; i++)
        {
            for(int j = 0; j<n; j++)
            {
                cout<<"M["<< i+1 <<" , "<< j+1<<" ] = ";
                cin>>matrix[i][j];
            }
        }
     cout<<"\n";
    return matrix;
}

void showMatrix(vector<vector<double>> matrix)
{
    double min = getMin(matrix);
    double max = getMax(matrix);

    for(int i = 0; i<matrix.size(); i++)
    {
        for(int j = 0; j<matrix.size(); j++)
        {
            cout<< setw(4)<< matrix[i][j]<<"  ";
        }
        cout<<"\n";
    }
        cout<<"Le plus petit coefficient de la matrice est : "<<min<<" \n";
        cout<<"Le plus grand coefficient de la matrice est : "<<max<<" \n";
}

vector<vector<double>> productMatrix(vector<vector<double>> m1, vector<vector<double>> m2, int n)
{
    vector<vector<double>> matrix = createMatrix(n);
    double sum;

      for(int i = 0; i<n; i++)
      {
        for(int j = 0; j<n; j++)
        {
            sum = 0;

            for(int k = 0; k<n; k++)
            {
                sum += m1[i][k]*m2[k][j];
            }
            matrix[i][j] = sum;
        }
    }
    return matrix;
}

double getMin(vector<vector<double>> matrix)
{
 	int min = matrix[0][0];
	for(int i = 0; i<matrix.size(); i++)
	{
        for(int j = 0; j<matrix.size(); j++)
            if(min > matrix[i][j])
            {
                min = matrix[i][j];
            }
	}
	return min;
}

double getMax(vector<vector<double>> matrix)
{
 	int max = matrix[0][0];
	for(int i = 0; i<matrix.size(); i++)
	{
        for(int j = 0; j<matrix.size(); j++)
            if(max < matrix[i][j])
            {
                max = matrix[i][j];
            }
	}
	return max;
}
