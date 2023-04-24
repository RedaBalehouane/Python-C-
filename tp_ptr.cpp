#include <iostream>
#include <vector>
using namespace std;

typedef struct {
	double valeur;
	int nombre;
}monnaie;

double totalCaisse(vector<monnaie>* caisse);
double totalRendu(vector<monnaie> caisse);
void afficherCaisse(vector<monnaie> caisse);
vector<monnaie> aRendre(double donner, double prix, vector<monnaie>* caisse);

int main()
{
	vector<monnaie> caisse = { {500,3},{100,7},{50,12},{20,22},{10,15},
		{5,25},{2,15},{1,25},{0.5,20}
	};
	
	double somme = totalCaisse(&caisse);
	afficherCaisse(caisse);
	
	cout << "Somme totale : " << somme<< endl;

	vector<monnaie> rendu = aRendre(1500, 100, &caisse);

	double sommeRendue = totalRendu(rendu);

	afficherCaisse(rendu);

	cout << "Somme rendue : " << sommeRendue << endl;
	return 0;
}

double totalCaisse(vector<monnaie>* caisse)
{
	double sum = 0;

	for (int i = 0; i < (*caisse).size(); i++)
	{
		sum += (*caisse)[i].valeur * (*caisse)[i].nombre;
	}

	return sum;
}

double totalRendu(vector<monnaie> caisse)
{
	double sum = 0;

	for (int i = 0; i < caisse.size(); i++)
	{
		sum += caisse[i].valeur * caisse[i].nombre;
	}
	return sum;
}

vector<monnaie> aRendre(double donner, double prix, vector<monnaie>* caisse)
{
	double residus = donner - prix;
	vector<monnaie> billets = { {500,0},{100,0},{50,0},{20,0},{10,0},
		{5,0},{2,0},{1,0},{0.5,0}
	};
	int i = 0;

	while (residus > 0.0)
	{

		if (residus >= (*caisse)[i].valeur && (*caisse)[i].nombre > 0)
		{
			residus -= (*caisse)[i].valeur;
			(*caisse)[i].nombre -= 1;
			billets[i].nombre += 1;

		}
		else {
			i++;
		}
	}
	return billets;
}

void afficherCaisse(vector<monnaie> caisse)
{
	cout << "Caisse principale : "<< endl;

	cout << "Billets :       Nombres :            "<<endl;
	for (int i = 0; i < caisse.size(); i++)
	{
		cout << caisse[i].valeur << "                       " << caisse[i].nombre << endl;
	}
}
