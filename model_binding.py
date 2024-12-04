import numpy as np
import cv2

def prompt_model(text_prompt:str, canvas_sketch:np.ndarray) -> np.ndarray:
    
    '''
    Input: Text prompt: The text prompt
            Canvas Sketch: The sketch drawn on the canvas as a numpy array
    Output: The generated image from the model as numpy array
    '''
    
    # INFER YOUR MODEL HERE
    generated_image = cv2.imread("demo_image.png")
    generated_image = cv2.cvtColor(generated_image, cv2.COLOR_BGR2RGB)
    
    return generated_image



