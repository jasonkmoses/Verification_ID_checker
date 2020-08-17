import os
import matplotlib.pyplot as plt
from pathlib import Path
from skimage import data
from tensorflow import keras
import numpy as np
DIR_2 = "/Users/jasonmoses/testingId"
DIR = "/Users/jasonmoses/dataIDS"
Category = ["ID", "notID"]
train_labels = []
test_labels = []
i = 25
for cate in Category:
    path = os.path.join(DIR, cate)
    for img in os.listdir(path)[1:i]:
        if i == i:
            print(img)
            if os.error.with_traceback == True:
                print("error")
            print(os.path.join(path, img) + " TrainingtData :####################### Number: " + str(os.listdir(path)[1:i].index(img)) + " " + cate)
            print(os.path.splitext(img)[0])
            IMG_ARRAY = np.array(data.imread(os.path.join(path, img), as_grey=True))[1:]
            for n in os.listdir(path)[1:]:
                IMG = np.array([data.imread(os.path.join(path, n), as_grey=True)])[1:]
                train_images = np.resize(IMG, (48, 280, 90))
            print("........")
            if cate == Category[0]:
                print("found Id photo")
                train_labels.append(Category.index(cate))
            elif cate == Category[1]:
                print("This photo is not an Id")
                train_labels.append(Category.index(cate))
            else:
                print("This is Ds_Store")
                pass
            print(train_labels)
            print(IMG_ARRAY)
            plt.imshow(IMG_ARRAY, cmap=plt.cm.binary)
            plt.colorbar()
            plt.show()
        else:
            print("error")
            pass
    k = i
    print("...............................")
    print("Showing TESTING IMAGES NOW")
    print("...............................")
    print(os.listdir(os.path.join(DIR_2, cate)))
    for img_2 in os.listdir(os.path.join(DIR_2, cate))[1:]:
        if k <= k:
            print(img_2)
            for l in os.listdir(os.path.join(DIR_2,cate)):
                    cate = Path(os.path.join(os.path.join(DIR_2, cate), l))
            print(img_2)
            print("^^^^^^^^^^^^^^^^^^^^^^")
            print("type is " + str(cat.parent.name))
            print("--------------------------TEST_IMGS------------------------------")
            TEST_IMG = np.array(data.imread(os.path.join(os.path.join(DIR_2, cate), img_2), as_grey=True))[1:]
            for r in os.listdir(os.path.join(DIR_2, cate))[1:]:
                IMG_2 = np.array([data.imread(os.path.join(os.path.join(DIR_2, cate), r), as_grey=True)])
                test_images = np.resize(IMG_2, (10, 280, 90))
            print(os.path.join(os.path.join(DIR_2, cate), r))
            print("........")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            if  cate == Category[0]:
                test_labels.append(Category.index(str(cate.parent.name)))
                print("**************************************")
                print("found Id photo of Test")
                print("**************************************")
            elif cate == Category[1]:
                test_labels.append(Category.index(str(cate.parent.name)))
                print("**************************************")
                print("This photo is not an Id Test")
                print("**************************************")
            else:
                print("This is Ds_Store Test")
                pass
print("----------------------------------------------Test Images------------------------------")
print(test_images)
print("----------------------------------------------Test Labels------------------------------")
print(test_labels)
print("----------------------------------------------Train Images------------------------------")
print(train_images)
print("----------------------------------------------Train Labels------------------------------")
print(train_labels)
model = keras.Sequential([
keras.layers.Flatten(input_shape=(280, 90)),
keras.layers.Dense(280, activation="softmax"),
keras.layers.Dense(70, activation="sigmoid")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
print("--------------------------------------------------------------------------")
print("//////////////////////////////////")
print("model is processing")
print("******************************************************")
model.fit(train_images, train_labels, epochs=5)
test_loss, test_acc = model.evaluate(test_images, test_labels)
#DONT UNCOMMNENT THE LINE BELOW UNTIL THE MODEL IS READY TO BE SAVED THEN UNCOMMENT AND AFTER THAT RUN ->
# model.save('Verification_ML_Model')
print(os.listdir(DIR_2)[1:])
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Now showing results for images")
prediction = model.predict(test_images)
for v in range(5):
    print("-------Test_Acc------------")
    print(test_acc)
    print("Accuracy: " + str(test_acc))
    print(np.max(prediction))
    print("prediction: "+ str((prediction)))
    print(";;;")
    plt.xlabel("Actual: " + cate)
    plt.title("Prediction: " + Category[int(round(np.max((prediction))))])
    plt.ylabel("Number of index:" + str(v))
    plt.imshow(TEST_IMG)
    plt.show()
