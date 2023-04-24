/*Withdaw, deposit, work, drink, repeat*/
/*Entrainement au passage par adresse.*/
#include <iostream>
#include <vector>
using namespace std;

typedef struct
{
	string name;
	double sold;
	double cash;
}user;

user userCreate(string* name, double* sold);
void showUser(user* client);
void deposit(user* client, double amount);
void withdraw(user* client, double amount);
void earnMoney(user* client, int time);
void buyCoffee(user* client, int amount);

int main()
{
	string name;
	double sold;
	user client;
	int choice;
	double amount;
	int time;

	cout << "***********************************************************************" << endl;
	cout << "Bienvenue dans le systeme bancaire le plus trivial qui puisse exister." << endl;
	cout << "***********************************************************************" << endl;

	cout << "Entrez le nom de l'utilisateur : ";
	cin >> name;
	cout << endl <<"Entrez le solde de depart de l'utilisateur : ";
	cin >> sold;
	cout << endl;

	client = userCreate(&name, &sold);


	while (true)
	{
		cout << "Que voulez vous faire : (1) Retirer, (2) Deposer, (3) Travailler, (4) Afficher le solde, (5) Prendre du cafe : ";
		cin >> choice;

		switch (choice)
		{
		case 1:
			cout << "Combien voulez vous retirer : ";
			cin >> amount;
			withdraw(&client, amount);
			cout << endl;
			break;

		case 2:
			cout << "Combien voulez vous deposer : ";
			cin >> amount;
			deposit(&client, amount);
			cout << endl;
			break;

		case 3:
			cout << "Combien d'heures voulez vous travailler (1$/h) : ";
			cin >> time;
			earnMoney(&client, time);
			cout << endl;
			break;

		case 4:
			showUser(&client);
			break;

		case 5:
			cout << "Combien de tasses voulez vous : ";
			cin >> amount;
			cout << endl;
			buyCoffee(&client, amount);
			break;
		}

	}
	return 0;
}

user userCreate(string* name, double* sold)
{
	user client;
	client.name = *name;
	client.sold = *sold;
	client.cash = 0;

	return client;
}

void showUser(user* client)
{
	cout << "-------------" << endl;
	cout << "Client : " << (*client).name << endl;
	cout << "Solde : " << (*client).sold << "$" << endl;
	cout << "Cash : " << (*client).cash << "$" << endl;
	cout << "-------------" << endl;
}

void withdraw(user* client, double amount)
{
	double soldAfter = (*client).sold - amount;

	if (soldAfter < 0)
	{
		cout << "Solde insuffisant." << endl;
		return;
	}

	if (soldAfter >= 0)
	{
		(*client).sold = soldAfter;
		(*client).cash += amount;
		cout << "Vous avez retirez : " << amount << "$" << endl;
	}
}

void deposit(user* client, double amount)
{
	double cashAfter = (*client).cash - amount;
	if (cashAfter < 0)
	{
		cout << "Cash insuffisant." << endl;
		return;
	}

	if (cashAfter >= 0)
	{
		(*client).sold += amount;
		(*client).cash -= amount;
		cout << "Vous avez deposer : " << amount << "$" << endl;
	}
}

void earnMoney(user* client, int time)
{
	for (int i = 0; i < time; i++)
	{
		(*client).cash += 1;
	}
	cout << "Vous avez gagner : " << time << "$" << endl;
}

void buyCoffee(user* client, int amount)
{
	double diff = (*client).sold - (*client).cash;
	
	if ((*client).cash < 2 * amount && (*client).sold < 2 * amount)
	{
		cout << "Vous etes trop pauvre pour vous acheter " << amount << " tasses de cafe :(" << endl;
		cout << "Pensez a travailler"<< endl;
		return;
	}

	if ((*client).cash < 2 * amount && (*client).sold >= 2*amount)
	{
		cout << "Cash insuffisant, le payement se fera par CB." << endl;
		cout << "Vous avez acheter " << amount << " tasse(s) de cafe !" << endl;
		cout << "Bonne degustation !" << endl;
		(*client).sold -= 2 * amount;
	}

	if ((*client).sold < 2 * amount && (*client).cash >= 2 * amount)
	{
		cout << "Solde insuffisant, le payement se fera par Cash." << endl;
		cout << "Vous avez acheter " << amount << " tasse(s) de cafe !" << endl;
		cout << "Bonne degustation !" << endl;
		(*client).cash -= 2 * amount;
	}
}