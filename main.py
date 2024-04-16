import cv2
import numpy as np
import pandas as pd

def calculate_area_and_diameter(contours, scale_factor):
    areas = []
    diameters = []
    for cnt in contours:
        area_pixels = cv2.contourArea(cnt)
        area_micrometers = area_pixels / (scale_factor ** 2)
        equivalent_diameter = 2 * np.sqrt(area_micrometers / np.pi)
        areas.append(area_micrometers)
        diameters.append(equivalent_diameter)
    return areas, diameters

def main():
    # Constants
    PIXELS_PER_MICROMETER = 2.26

    # Load image
    image_path = input("Enter the path to the image: ")
    image = cv2.imread(image_path, 0)  # Read in grayscale

    if image is None:
        print("Error: Image not found.")
        return

    # Ask user for the minimum area threshold
    min_area = float(input("Enter the minimum area (in square micrometers) for particle analysis: "))

    # Otsu's thresholding
    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate areas and equivalent diameters
    areas, diameters = calculate_area_and_diameter(contours, PIXELS_PER_MICROMETER)

    # Filter based on the minimum area and create DataFrame
    data = {'Area (sq micrometers)': areas, 'Equivalent Diameter (micrometers)': diameters}
    df = pd.DataFrame(data)
    filtered_df = df[df['Area (sq micrometers)'] >= min_area]

    # Save to CSV
    csv_path = 'particle_analysis.csv'
    filtered_df.to_csv(csv_path, index=False)
    print(f"Data saved to {csv_path}")

if __name__ == "__main__":
    main()
