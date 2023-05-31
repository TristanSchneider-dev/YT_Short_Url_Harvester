import itertools

characters = ['-','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
file_path = "possible_urls.txt"


def generate_combinations():
    for combination in itertools.product(characters, repeat=4):
        yield "https://www.youtube.com/shorts/" + "".join(combination) + "\n"  # Whole Url
        #yield str(combination) + "\n" # Only ID (less storage)


# Write combinations to file with buffered writing (less storage operations)
buffer_size = 10000
buffer = []

with open(file_path, "w", buffering=buffer_size) as file:
    for combination in generate_combinations():
        buffer.append(combination)

        if len(buffer) >= buffer_size:
            file.writelines(buffer)
            buffer = []

    if buffer:
        file.writelines(buffer)

print("Combinations have been successfully written to the file.")
