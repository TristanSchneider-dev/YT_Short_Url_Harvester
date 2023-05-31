#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector<char> characters = { '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
std::string file_path = "possible_urls.txt";

void generate_combinations(std::ofstream& file) {
    int buffer_size = 1000;
    std::vector<std::string> buffer;

    for (char c1 : characters) {
        for (char c2 : characters) {
            for (char c3 : characters) {
                for (char c4 : characters) {
                    std::string combination = "https://www.youtube.com/shorts/";
                    combination += c1;
                    combination += c2;
                    combination += c3;
                    combination += c4;
                    combination += "\n";

                    buffer.push_back(combination);

                    if (buffer.size() >= buffer_size) {
                        for (const std::string& line : buffer) {
                            file << line;
                        }
                        buffer.clear();
                    }
                }
            }
        }
    }

    if (!buffer.empty()) {
        for (const std::string& line : buffer) {
            file << line;
        }
    }
}

int main() {
    std::ofstream file(file_path, std::ofstream::out);

    if (file.is_open()) {
        generate_combinations(file);
        file.close();
        std::cout << "Combinations have been successfully written to the file." << std::endl;
    }
    else {
        std::cerr << "Failed to open the file." << std::endl;
    }

    return 0;
}
