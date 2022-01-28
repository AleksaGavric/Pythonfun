import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plot

breast_cancer_data = load_breast_cancer()

training_data, validation_data, training_labels,validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

right_k = [0, 0] #[k, score]
accuracies = []

for k in range(1, 101):
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  score = classifier.score(validation_data, validation_labels)

  if (score > right_k[1]):
    right_k[0] = k
    right_k[1] = score

  accuracies.append(score)

print(right_k)

k_list = range(1,101)

plot.scatter(k_list, accuracies)
plot.xlabel("k")
plot.ylabel("Validation Accuracy")
plot.title("Breast Classifier Accuracy")
plot.show()
