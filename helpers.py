def caesarShift(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result


def generate_histogram(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = ''.join(c for c in text if c.isalpha()).lower()
    

    def plot_histogram(histogram):
        letters = list(histogram.keys())
        counts = list(histogram.values())

        plt.bar(letters, counts)
        plt.xlabel('Letters')
        plt.ylabel('Frequency')
        plt.title('Letter Frequency Histogram')
        plt.show()

    # Generate the histogram
    histogram = generate_histogram(cyperText)

    # Plot the histogram
    plot_histogram(histogram)
    # Count the frequency of each letter
    letter_counts = Counter(cleaned_text)
    
    # Sort the letters in alphabetical order
    sorted_letters = sorted(letter_counts.keys())
    
    # Generate the frequency histogram
    histogram = {letter: letter_counts[letter] for letter in sorted_letters}
    
    return histogram


def letterFrequency(string):
    freq_dict = {}
    for char in string:
        if char.isalpha():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    freq_dict = dict(sorted(freq_dict.items()))
    return freq_dict

def frequencyPlot(cyperText):
    cypherFrequency = letterFrequency(cyperText)

    letters = list(cypherFrequency.keys())
    counts = list(cypherFrequency.values())

    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Histogram')
    plt.show()