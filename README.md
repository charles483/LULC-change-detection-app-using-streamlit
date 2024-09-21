
---

# Land Use Change Detection App using Landsat & Google Earth Engine (GEE)

## Overview

This **Land Use Change Detection App** allows users to visualize and analyze land-use changes over time using **Landsat satellite imagery** and **Google Earth Engine (GEE)**. Users can upload region of interest (ROI) coordinates, select different years to compare, and detect changes in land cover based on satellite data from the Landsat series.

The app utilizes **Normalized Difference Vegetation Index (NDVI)** to detect changes in land cover, highlighting areas of significant change between two time periods. The app also provides interactive map visualizations and the ability to download the results for further analysis.

## Features

- **Select Two Years for Comparison**: Choose two different years (from 1984 to the present) to compare land cover changes.
- **Custom Region of Interest (ROI)**: Input coordinates for any geographical region of interest to focus the analysis.
- **Cloud Masking**: Automatically removes clouds and cloud shadows to ensure clearer imagery.
- **Change Detection**: Detects and highlights areas where significant land-use change has occurred based on NDVI differences.
- **Map Visualization**: Displays the selected Landsat images and change detection results using an interactive Folium map.
- **Download Results**: Export the change detection results as an image file or directly to your Google Drive.

## How to Use

### 1. Clone the Repository

To get started, clone the repository:

```bash
git clone https://github.com/your-username/landuse-change-detection-app.git
cd landuse-change-detection-app
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install streamlit earthengine-api folium geemap
```

### 3. Authenticate Google Earth Engine (GEE)

Before using the app, you need to authenticate your Google Earth Engine account:

```bash
earthengine authenticate
```

Follow the prompts to complete the authentication process.

### 4. Run the App

Launch the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will open the app in your default web browser.

### 5. Using the App

- **Select Parameters**: Choose two different years from the sidebar for the land use comparison.
- **Input ROI Coordinates**: Enter the coordinates of the region of interest (ROI) for the analysis. For example:
  ```text
  [[-1.286389, 36.817223], [-1.286389, 36.817223]]
  ```
- **View Maps**: The app will display the Landsat imagery for the two selected years and a change detection map highlighting areas of significant change.
- **Download Results**: Use the button provided to export the change detection map as an image file or download the processed map to Google Drive.

## Requirements

- **Python 3.7+**
- **Google Earth Engine Account**: Ensure you have a valid Earth Engine account. You can sign up at [earthengine.google.com](https://earthengine.google.com/).
- **Dependencies**:
  - `streamlit`
  - `earthengine-api`
  - `folium`
  - `geemap`

## How It Works

1. **Data Retrieval**: Landsat images are retrieved from Google Earth Engine for the two selected years.
2. **Cloud Masking**: Cloud and shadow pixels are masked to ensure clear imagery.
3. **NDVI Calculation**: The app computes the NDVI (Normalized Difference Vegetation Index) for both years.
4. **Change Detection**: The app detects areas where the NDVI difference exceeds a certain threshold, indicating significant land cover change.
5. **Visualization**: The app displays the images and change detection results on an interactive map.
6. **Exporting**: Users can export the final change detection results to their local machine or Google Drive.

## Future Enhancements

- **Advanced Change Detection Methods**: Incorporating other indices like NDWI (Water Index) or NDBI (Built-up Index) for more specific land-use classifications.
- **Custom Thresholds**: Allow users to adjust the change detection threshold for more control over results.
- **Additional Download Formats**: Support for downloading maps in more formats like PDF or shapefile.
- **Multi-temporal Analysis**: Compare land-use changes over multiple years instead of just two.

## Contributing

Contributions are welcome! If you would like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: [charleschuru94@gmail.com](mailto:charleschuru94@gmail.com)
- **GitHub**: [https://github.com/your-username](https://github.com/your-username)

---
