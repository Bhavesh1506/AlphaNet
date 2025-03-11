import numpy as np
import matplotlib.pyplot as plt
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

patterns = {
    'A': np.array([
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]),
    'B': np.array([
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0]
    ]),
    'C': np.array([
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,1,1,1,1]
    ]),
    'D': np.array([
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0]
    ]),
    'E': np.array([
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,1,1,1]
    ]),
    'F': np.array([
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0]
    ]),
    'G': np.array([
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [0,1,1,1,1]
    ]),
    'H': np.array([
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]),
    'I': np.array([
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,1,1,1,1]
    ]),
    'J': np.array([
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,0,1,0,0],
        [0,1,0,0,0]
    ]),
    'K': np.array([
        [1,0,0,0,1],
        [1,0,0,1,0],
        [1,1,1,0,0],
        [1,0,0,1,0],
        [1,0,0,0,1]
    ]),
    'L': np.array([
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1]
    ]),
    'M': np.array([
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]),
    'N': np.array([
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1]
    ]),
    'O': np.array([
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ]),
    'P': np.array([
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0]
    ]),
    'Q': np.array([
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,0],
        [0,1,1,0,1]
    ]),
    'R': np.array([
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,1,0],
        [1,0,0,0,1]
    ]),
    'S': np.array([
        [0,1,1,1,1],
        [1,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [1,1,1,1,0]
    ]),
    'T': np.array([
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ]),
    'U': np.array([
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ]),
    'V': np.array([
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0]
    ]),
    'W': np.array([
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [0,1,0,1,0]
    ]),
    'X': np.array([
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1]
    ]),
    'Y': np.array([
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ]),
    'Z': np.array([
        [1,1,1,1,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
        [1,1,1,1,1]
    ])
}

def preprocess_pattern(pattern):
    return pattern.flatten() * 2 - 1

X = np.array([preprocess_pattern(patterns[letter]) for letter in alphabet[:len(patterns)]])
y = np.eye(len(patterns))

W = np.linalg.lstsq(X, y, rcond=None)[0]


def recognize_character(pattern):
    input_vector = preprocess_pattern(pattern)
    
    
    output = input_vector @ W
    
    print("\nConfidence scores for each letter:")
    print("-" * 40)
    print("Letter | Confidence Score")
    print("-" * 40)
    print("Raw output values:", output)

    for i, value in enumerate(output):
       
        print(f"  {alphabet[i]}    |    {value:.2f}")
    print("-" * 40)
    
    recognized_index = np.argmax(output)
    
    print(f"\nRecognized as letter '{alphabet[recognized_index]}' with confidence {output[recognized_index]:.2f}")
    
    return alphabet[recognized_index]
  
def test_recognition(test_letter):
    print(f"\nTesting recognition for letter: {test_letter}")
    test_pattern = patterns[test_letter]
    
    plt.figure(figsize=(5, 5))
    plt.imshow(test_pattern, cmap='binary')
    plt.title(f"Input Pattern - Letter {test_letter}")
    plt.axis('off')
    plt.show()
    
    recognized = recognize_character(test_pattern)


test_recognition('B')

