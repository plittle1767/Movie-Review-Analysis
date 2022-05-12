"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by Preston Little
"""

# Add your critical thinking sentences and example review here.
"""
I think that the predicting capabilities of this program are pretty decent. It does a fair job of giving a score for a 
certain word (negative or positive) and gets really close to the actual score. A score ranging from 0 to 4 may not be as
good as a score ranging from 0 to 10. For example, when I ran my code, my output was:
    Please enter a review with no punctuation: i hated this movie it was so bad
    The predicted review score is 1.2580153997573524
"""

# Add your functions here.

def make_lowercase_lines_from_file(small_review_file):
    """
    This function will return a list from each line from the smallReviews.txt file and make them all lowercase
    :param small_review_file: A string with a filename in it
    :return: A list where each item in the list is a line from the file. Call the string lower() method on each line to
    make it lowercase letters
    """
    with open(small_review_file) as data:
        return list(map(lambda x: x.replace("\n", "").lower(), data.readlines()))


def make_word_total_value_dict_from_lines(lowercase_values):
    """
    This will give use the total value of the words by adding up the number of times a word appears
    :param lowercase_values: A list of lowercase string values. Each string must start with a number and then have words
    following
    :return: A dict with every word from the list as keys and the total value of the word as the value
    """
    word_total_dict = {}
    for line in lowercase_values:
        info = line.split()
        if len(info) > 0:
            score = float(info[0])
            for word in info[1:]:
                if word in word_total_dict:
                    word_total_dict[word] += score
                else:
                    word_total_dict[word] = score
    return word_total_dict


def make_word_total_count_dict_from_lines(lowercase_values):
    """
    Here we add the total number of times a key appears in all the reviews
    :param lowercase_values: A list of lowercase string values. Each string must start with a number and then have words
    following
    :return: A dict with every word from the list as keys and the total number of times it appears in all the reviews as
    the value
    """
    word_count_dict = {}
    for line in lowercase_values:
        data = line.split()
        if len(data) > 1:
            for word in data[1:]:
                if word in word_count_dict:
                    word_count_dict[word] += data[1:].count(word)
                else:
                    word_count_dict[word] = data[1:].count(word)
    return word_count_dict


def make_word_avg_value_from_total_and_count(word_total_dict, word_count_dict):
    """
    Here we average the values of the word_total_dict and word_count_dict parameters
    :param word_total_dict: The word_total_dict as computed above
    :param word_count_dict: The  word_count_dict as computed above
    :return: A dict with every word from the parameter dicts (the total dict and count dict should have the same keys
    stored) and the average of the total value and count for the word as the value in this new dict. Any word with an
    average between 1.75 and 2.25 should not be added to the dict
    """
    avg_value = {}
    for word in word_count_dict:
        average = word_total_dict[word] / word_count_dict[word]
        if average > 2.25 or average < 1.75:
            avg_value[word] = average
    return avg_value


def predict_review(words_from_a_review, average_value):
    """
    This function predicts the score of the movie review
    :param words_from_a_review: A string with the words from a review
    :param average_value: The average_value dict with words and their value
    :return: A number score predicting a movie rating for the string
    """
    data = words_from_a_review.split()
    average_value = {key: value for key, value in average_value.items() if not 1.75 <= value <= 2.25}
    interested_words = set(average_value.keys() & set(data))
    if len(interested_words) > 0:
        return sum(map(lambda x: average_value[x], interested_words)) / len(interested_words)
    else:
        return 0


def compare_prediction_with_actual(lines, avg_value_dict):
    """
    Given a list of movie reviews and a dictionary of words and their avg value, compare
    the predicted rating with the actual rating.
    :param lines: a list of movie reviews. Each review starts with a 0 to 4 movie rating.
    :param avg_value_dict: A dict of words and their average value in a movie review rating
    :return: None. This prints out some predicted and actual score for movie reviews.
    """
    for line in lines:
        words = line.split()
        actual_score = int(words[0])
        predicted_score = predict_review(" ".join(words[1:]), avg_value_dict)
        print("predicted:", predicted_score, "actual:", line)

def main():
    """
    Read a file of movie reviews, develop a dict of word values, and use
    those to make movie rating predictions.
    """
    # Add some testing code below here. Make a small list of reviews by hand or read in a small
    # file. Make small total value and count dicts to test the avg function. Make a small
    # avg dict to test the prediction function. Make these by hand to make the tests be as independent
    # from each other as possible.

    # You should not need to change the code below here. You can comment out some of the print statements if
    # they are producing so much text it is confusing.

    # read the reviews into a list
    # lines = make_lowercase_lines_from_file("smallReviews.txt")
    lines = make_lowercase_lines_from_file("MovieReviews.txt")  # uncomment this when you are ready to try the full
    # set of reviews.
    print(lines)  # examine the result

    # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    print(total_value_dict)  # examine the dict to see if it looks correct

    # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    print(total_count_dict)  # examine the dict to see if it looks correct

    # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    print(avg_value_dict)  # examine the dict to see if it looks correct

    # Compare actual and predicted movie ratings for a small number of reviews
    if len(lines) < 110:
        compare_prediction_with_actual(lines, avg_value_dict)  # use all for small review files
    else:
        compare_prediction_with_actual(lines[100:110], avg_value_dict)

    # Ask the user for a movie review and predict a rating. It should be without punctuation.
    personal_review = input("Please enter a review with no punctuation: ")
    personal_review = personal_review.lower()
    prediction = predict_review(personal_review, avg_value_dict)
    print("The predicted review score is", prediction)


if __name__ == "__main__":
    main()
