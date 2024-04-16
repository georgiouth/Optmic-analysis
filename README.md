# Particle Analysis Script

This Python script performs particle analysis on a specified image, calculating the area and equivalent diameter of detected particles in micrometers. The script utilizes OpenCV for image processing and contour detection, and Pandas for data manipulation and exporting results to a CSV file.

## Prerequisites

To run this script, you need to have Python installed along with the following libraries:
- OpenCV (`cv2`) for image processing.
- NumPy (`numpy`) for numerical operations.
- Pandas (`pandas`) for data handling.

You can install these packages using pip:
```bash
pip install opencv-python numpy pandas
```
## Usage
Ensure that you have the required libraries installed. Place the script in a directory.

Run the script using Python from your terminal or command prompt: 
```python particle_analysis.py```

## Output

The script outputs a CSV file (particle_analysis.csv) containing the following columns:

Area (sq micrometers): The area of each particle in square micrometers. Equivalent Diameter (micrometers): The diameter of each particle in micrometers, calculated from the area. After processing, the script will save the results to particle_analysis.csv.

## Contributing
Feel free to fork the repository, make improvements, or customize the script as per your needs.

## License
This script is distributed under the MIT License, which allows free use, modification, and distribution for both personal and commercial purposes. Details of the MIT License can be found at MIT License.

## Disclaimer
This script is provided "as is", without warranty of any kind. Use at your own risk.


