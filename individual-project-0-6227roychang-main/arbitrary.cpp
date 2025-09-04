#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <input_file> <output_file>" << endl;
        return 1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    if (!fin || !fout) return 1;

    long long a, b;
    fin >> a >> b;

    fout << "Tun-Wei, Chang, 6227648838\n";
    fout << "1> " << a << ", " << b << "\n";
    fout << "2> " << (a + b) << ", " << (a - b) << "\n";
    fout << "3> " << (a % b) << ", " << (a * b) << "\n";
    fout << "4> That's it!\n";
    return 0;
}
