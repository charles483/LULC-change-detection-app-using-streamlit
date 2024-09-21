import streamlit as st
import ee
import folium
import geemap.foliumap as geemap
from datetime import datetime

# Authenticate and initialize the Earth Engine API
ee.Initialize()

# Streamlit app title
st.title("Land Use Change Detection using Landsat & GEE")

# Sidebar for input selection
st.sidebar.header("Select Parameters")

# Select the years for land use change detection
start_year = st.sidebar.selectbox("Start Year", list(range(1984, 2024)))
end_year = st.sidebar.selectbox("End Year", list(range(1984, 2024)))

# Define a region of interest (ROI) using coordinates or select from a map
st.sidebar.text("Select Region of Interest")
roi_coords = st.sidebar.text_area("Enter Coordinates for ROI (e.g., [[lat, lon], [lat, lon]])", "[[-1.286389, 36.817223], [-1.286389, 36.817223]]")

# Parse the input coordinates
try:
    roi = ee.Geometry.Polygon(eval(roi_coords))
except:
    st.error("Invalid Coordinates")

# Function to fetch Landsat data
def get_landsat_data(year, roi):
    # Select the Landsat collection and filter by date
    landsat = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR") \
        .filterBounds(roi) \
        .filterDate(f'{year}-01-01', f'{year}-12-31') \
        .map(mask_clouds)
    
    # Return the median image
    return landsat.median().clip(roi)

# Function to mask clouds using the pixel_qa band
def mask_clouds(image):
    cloud_mask = ee.Image(image.select('pixel_qa')).bitwiseAnd(1 << 5).eq(0)
    return image.updateMask(cloud_mask)

# Get the Landsat images for the selected years
image1 = get_landsat_data(start_year, roi)
image2 = get_landsat_data(end_year, roi)

# Create the change detection function
def detect_change(image1, image2):
    # Calculate Normalized Difference Vegetation Index (NDVI) for each image
    ndvi1 = image1.normalizedDifference(['B5', 'B4'])  # Landsat 8 NIR and Red bands
    ndvi2 = image2.normalizedDifference(['B5', 'B4'])
    
    # Compute the NDVI difference
    ndvi_diff = ndvi2.subtract(ndvi1)
    
    # Classify areas of significant change
    change_mask = ndvi_diff.gt(0.2).selfMask()  # Threshold for change detection
    
    return change_mask

# Apply the change detection algorithm
change_detection_result = detect_change(image1, image2)

# Visualize the results using Folium map
st.subheader("Map Visualization")

# Create a folium map
Map = geemap.Map(center=[-1.286389, 36.817223], zoom=8)

# Add the Landsat images to the map
Map.addLayer(image1, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 3000}, f'{start_year} Image')
Map.addLayer(image2, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 3000}, f'{end_year} Image')

# Add change detection result layer
Map.addLayer(change_detection_result, {'palette': 'red'}, 'Change Detection')

# Display the map in Streamlit
Map.to_streamlit(width=700, height=500)

# Download the results
st.subheader("Download Change Detection Results")
if st.button("Download Map"):
    # Export the change detection map as an image
    task = ee.batch.Export.image.toDrive(
        image=change_detection_result,
        description='change_detection',
        scale=30,
        region=roi
    )
    task.start()
    st.success("Exported map to Google Drive")

