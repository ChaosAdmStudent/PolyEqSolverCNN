from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Convolution2D, MaxPooling2D, Flatten, Dropout 


def make_model():
    model = Sequential()

    #CNN Layers
    model.add(Convolution2D(32, (3,3), input_shape = (64,64,3)))
    model.add(MaxPooling2D ((2,2)))
    model.add(Convolution2D(32, (3,3), input_shape = (64,64,3)))
    model.add(MaxPooling2D ((2,2)))
    model.add(Convolution2D(32, (3,3), input_shape = (64,64,3)))
    model.add(MaxPooling2D ((2,2)))
    
    model.add(Flatten())
    
    #Hidden ANN Layers
    model.add(Dense(units = 128, kernel_initializer = "random_uniform", activation ="relu"))
    model.add(Dropout(0.5))

    model.add(Dense(units = 128, kernel_initializer = "random_uniform", activation ="relu"))
    model.add(Dropout(0.3)) 

    #Output Layer
    model.add(Dense(units = 14, kernel_initializer = "random_uniform", activation ="softmax"))

    #Compile and save
    model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
    model.save('./PolyEqSolver.h5')

    return model

if __name__ == "__main__":
    model = make_model()
    model.summary()