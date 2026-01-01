# "Column Name"	                         "Description"

# [0]Pregnancies	                         Number of times pregnant
# [1]Glucose	Plasma                     glucose concentration (2-hour OGTT)
# [2]BloodPressure	                     Diastolic blood pressure (mm Hg)
# [3]SkinThickness	                     Triceps skin fold thickness (mm)
# [4]Insulin	                                 2-hour serum insulin (mu U/ml)
# [5]BMI	                                         Body Mass Index (kg/m²)
# [6]DiabetesPedigreeFunction	 Genetic diabetes risk
# [7]Age	                                         Age in years
# [8]Outcome	                             Class label (0 = Non-diabetic, 1 = Diabetic)


from  numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.models import model_from_json

dataset = loadtxt('diabetes_dataset_samples.csv',delimiter = ',')
# print(dataset)

x = dataset[:, 0:8] #input
y = dataset[:, 8] #output

# print("input", x)
# print("output", y)

model = Sequential()

model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])

#model training
model.fit(x, y, epochs=50, batch_size=10)

#evaluation
_,accuracy = model.evaluate(x, y)
print('accuracy: %.2f' % (accuracy*100))

#model save
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("saved model to disk")