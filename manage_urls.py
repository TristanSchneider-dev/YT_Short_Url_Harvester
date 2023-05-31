def read_short_urls_file(file_path):    # Read the short URLs from a file and return them as a list.
    short_urls = []
    with open(file_path, "r") as file:
        for line in file:
            short_url = line.strip()
            short_url = short_url[31:]  # Cut the URL to the desired length or adjust to your requirements
            short_urls.append(short_url)
    return short_urls


def get_unique_characters(urls):    # Get a list of the used unique characters
    unique_characters = set()
    for url in urls:
        unique_characters.update(set(url))
    unique_characters_list = list(unique_characters)

    sorted_characters = sorted(unique_characters_list)
    return sorted_characters

if __name__ == '__main__':
    file_path = "yt_short_urls.txt"
    urls = read_short_urls_file(file_path)

    characters = get_unique_characters(urls)
    print(characters)

    num_characters = len(characters)
    print(num_characters)

'''
YT Uses the following 64 Characters for it's URL generation
['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''