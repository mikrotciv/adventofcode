#include <cstdio>
#include <exception>
#include <fstream>
#include <iostream>
#include <string>
#include <deque>

static const std::string FILENAME = "input.txt";

int getMaxCalories()
{
  int maxCalories{0};
  int elfCalories{0};

  std::ifstream inputFile(FILENAME);
  std::string line;
  while(std::getline(inputFile, line))
  {
    if (line.empty())
    {
      if (elfCalories > maxCalories) maxCalories = elfCalories;
      elfCalories = 0;
    }
    else
    {
      try
      {
        elfCalories += std::stoi(line);
      }
      catch (std::exception e)
      {
        std::cerr << "Failed to convert " << line << " to integer" << std::endl;
      }
    }
  }
  return maxCalories;
}

int topNCaloriesSum(int n)
{
  std::deque<int> topCalories(n, 0);
  int elfCalories{0};

  std::ifstream inputFile(FILENAME);
  std::string line;
  while(std::getline(inputFile, line))
  {
    if (line.empty())
    {
      for (size_t i=0; i < topCalories.size(); ++i)
      {
        if (elfCalories > topCalories[i])
        {
          topCalories.insert(topCalories.begin()+i, elfCalories);
          while(topCalories.size() > n) topCalories.pop_back();
          break;
        }
      }
      elfCalories = 0;
    }
    else
    {
      try
      {
        elfCalories += std::stoi(line);
      }
      catch (std::exception e)
      {
        std::cerr << "Failed to convert " << line << " to integer" << std::endl;
      }
    }
  }
  int totalSum{0};
  for (auto calories : topCalories) totalSum += calories;
  return totalSum;
}

int main()
{
  std::cout << "Elf carrying max calories: " << getMaxCalories() << std::endl;
  std::cout << "Sum of top three calories: " << topNCaloriesSum(3) << std::endl;
}