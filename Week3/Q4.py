import numpy as np


# question 1-----------------------------------------------------------------------
def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


def question_1():
    train_data = create_train_data()
    print(train_data)
    return train_data


# question 2-----------------------------------------------------------------------
def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    total_samples = train_data.shape[0]

    for i, label in enumerate(y_unique):
        prior_probability[i] = np.sum(
            train_data[:, -1] == label) / total_samples

    return prior_probability


def question_2(train_data):
    prior_probability = compute_prior_probability(train_data)
    print("P(play tennis = No)", prior_probability[0])
    print("P(play tennis = Yes)", prior_probability[1])


# question 3-----------------------------------------------------------------------
def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j, label in enumerate(y_unique):
            label_data = train_data[train_data[:, -1] == label]
            for k, value in enumerate(x_unique):
                x_conditional_probability[j, k] = np.sum(
                    label_data[:, i] == value) / label_data.shape[0]

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


def question_3(train_data):
    _, list_x_name = compute_conditional_probability(
        train_data)
    print("x1 = ", list_x_name[0])
    print("x2 = ", list_x_name[1])
    print("x3 = ", list_x_name[2])
    print("x4 = ", list_x_name[3])


# question 4----------------------------------------------------------------------
def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


# Kiểm tra hàm get_index_from_value
def question_4(train_data):
    _, list_x_name = compute_conditional_probability(train_data)
    outlook = list_x_name[0]
    i1 = get_index_from_value("Overcast", outlook)
    i2 = get_index_from_value("Rain", outlook)
    i3 = get_index_from_value("Sunny", outlook)

    print(i1, i2, i3)


if __name__ == "__main__":
    train_data = question_1()
    print("\nQuestion 2:------------------------------")
    question_2(train_data)
    print("\nQuestion 3:------------------------------")
    question_3(train_data)
    print("\nQuestion 4:------------------------------")
    question_4(train_data)

    # question 5
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    # Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
    x1 = get_index_from_value("Sunny", list_x_name[0])
    print("P('Outlook'='Sunny' | 'Play Tennis'='Yes') = ",
          np. round(conditional_probability[0][1, x1], 2))

    # Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
    print("P('Outlook'='Sunny' | 'Play Tennis'=='No') = ",
          np.round(conditional_probability[0][1, x1], 2))
    
