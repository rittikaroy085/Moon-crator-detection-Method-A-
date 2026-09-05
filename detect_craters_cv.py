import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "lunar_surface.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image. Check the file path!")
    exit()
blurred = cv2.GaussianBlur(image, (5, 5), 0)
circles = cv2.HoughCircles(
    blurred, 
    cv2.HOUGH_GRADIENT, 
    dp=1.2, 
    minDist=30,      
    param1=50,       
    param2=35,       
    minRadius=10,    
    maxRadius=100   
)
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    print(f"Detected {len(circles)} potential craters!")
    
    for (x, y, r) in circles:
        cv2.circle(output_image, (x, y), r, (0, 0, 255), 2)
        cv2.circle(output_image, (x, y), 2, (255, 0, 0), 3)
else:
    print("No craters detected. Try tweaking the param2 or radius values.")
#results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Lunar Surface")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Detected Craters")
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.show()
