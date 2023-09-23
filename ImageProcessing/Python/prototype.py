import cv2

# Load the image
image = cv2.imread(r"C:\Users\SamuelChee\Desktop\COMP4521\ClimbingApp\ImageProcessing\TestImages\Moonboard2016(HQ,Front on).jpg")

# Scale the image by a percentage
scale_percentage = 50  # Set the desired scale percentage
scale_factor = scale_percentage / 100.0
image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
threshold1 = 50
threshold2 = 150
edges = cv2.Canny(gray, threshold1, threshold2)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image for displaying all contours
contour_image = image.copy()

# Draw all contours on the contour_image
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the image with all contours
cv2.imshow('All Contours', contour_image)

# Filter and sort rectangular contours
rectangular_contours = []
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    if len(approx) == 4:
        rectangular_contours.append(approx)

rectangular_contours = sorted(rectangular_contours, key=cv2.contourArea, reverse=True)

# Highlight the top 5 shapes on the original image
for i, contour in enumerate(rectangular_contours[:5]):
    cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
    cv2.putText(image, f"Shape {i+1}", (contour[0][0][0], contour[0][0][1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the image with highlighted shapes
cv2.imshow('Top 5 Shapes', image)

cv2.waitKey(0)
cv2.destroyAllWindows()z