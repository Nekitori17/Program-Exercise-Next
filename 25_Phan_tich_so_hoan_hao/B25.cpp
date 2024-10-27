#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

vector<int> tim_cac_uoc(int so_vao)
{
  vector<int> cac_uoc;
  for (int i = 1; i <= ceil(sqrt(so_vao)); i++)
  {
    if (so_vao % i == 0)
    {
      cac_uoc.push_back(i);
    }
  }
  return cac_uoc;
}

vector<int> la_so_hoan_hao(int so_vao)
{
  vector<int> cac_uoc = tim_cac_uoc(so_vao);
  if (cac_uoc.size() == 0)
  {
    return {0};
  };

  int tong_uoc = 0;
  for (int x : cac_uoc)
  {
    tong_uoc += x;
  }
  if (tong_uoc == so_vao)
  {
    return cac_uoc;
  }
  else
  {
    return {0};
  }
}

int main()
{
  ifstream input_file("./B25.inp");
  ofstream output_file("./B25.out");

  string chu_so_vao;
  int so_vao;
  getline(input_file, chu_so_vao);
  so_vao = stoi(chu_so_vao);

  string dau_ra;
  for (int so: la_so_hoan_hao(so_vao)) {
    dau_ra += to_string(so) + " ";
  }

  output_file << dau_ra;
  input_file.close();
  output_file.close();
  return 0;
}