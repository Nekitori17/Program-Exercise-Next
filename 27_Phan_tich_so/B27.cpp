#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

bool la_so_nt(int so_vao) {
  if (so_vao < 2) {
    return false;
  } else if (so_vao == 2) {
    return true;
  }

  for (int i = 2; i <= ceil(sqrt(so_vao)); i++) {
    if (so_vao % i == 0) {
      return false;
    }
  }
  return true;
}

vector<int> phan_tich_so(int den) {
  vector<int> cac_so_nt;
  for (int so = 2; so <= den; so++) {
    if (la_so_nt(so)) {
      cac_so_nt.push_back(so);
    }
  }

  for (int vi_tri_1 = 0; vi_tri_1 < cac_so_nt.size(); vi_tri_1++) {
    for (int vi_tri_2 = vi_tri_1 + 1; vi_tri_2 < cac_so_nt.size(); vi_tri_2++) {
      if (cac_so_nt[vi_tri_1] + cac_so_nt[vi_tri_2] == den) {
        return {cac_so_nt[vi_tri_1], cac_so_nt[vi_tri_2]};
      }
    }
  }

  return {den};
}

int main() {
  ifstream input_file("./B27.inp");
  ofstream output_file("./B27.out");

  string chu_so_vao;
  int so_vao;
  getline(input_file, chu_so_vao);
  so_vao = stoi(chu_so_vao);

  string dau_ra;
  for (int so : phan_tich_so(so_vao)) {
    dau_ra += to_string(so) + " ";
  }

  output_file << dau_ra;
  input_file.close();
  output_file.close();
  return 0;
}
