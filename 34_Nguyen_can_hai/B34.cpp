#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
  ifstream input_file("./B34.inp");
  ofstream output_file("./B34.out");

  string chu_so_vao;
  int so_vao;
  getline(input_file, chu_so_vao);
  so_vao = stoi(chu_so_vao);

  output_file << to_string(static_cast<int>((sqrt(so_vao))));
  return 0;
}