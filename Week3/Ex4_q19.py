import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'No'],
            ['Sunny', 'Hot', 'High', 'Strong', 'No'],
            ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'No'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']]
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = ['No', 'Yes']
    prior_probability = np.zeros(len(y_unique))
    for i, y in enumerate(y_unique):
        prior_probability[i] = np.sum(
            train_data[:, -1] == y) / train_data.shape[0]
    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['No', 'Yes']
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

        for j, y in enumerate(y_unique):
            y_count = np.sum(train_data[:, -1] == y)
            for k, x in enumerate(x_unique):
                x_count = np.sum((train_data[:, i] == x) & (
                    train_data[:, -1] == y))
                x_conditional_probability[j, k] = x_count / y_count
        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]


def prediction_play_tennis(_, list_x_name, prior_probability, conditional_probability):

    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p0 = prior_probability[0] \
        * conditional_probability[0][0, x1] \
        * conditional_probability[1][0, x2] \
        * conditional_probability[2][0, x3] \
        * conditional_probability[3][0, x4]

    p1 = prior_probability[1]\
        * conditional_probability[0][1, x1]\
        * conditional_probability[1][1, x2]\
        * conditional_probability[2][1, x3]\
        * conditional_probability[3][1, x4]

    # print(p0, p1)

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


# prediction_play_tennis()
X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
