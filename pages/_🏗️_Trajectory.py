import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# st.set_page_config(
#         page_title="3DTrajectory",
#         # page_icon="🏢",
#     )

# bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
def draw_grid(size):
    # Define the image size
    img_size = (600, 300)
    # Create a new image
    img = Image.new("RGBA", img_size, (68, 70, 84, 0))
    # Create a drawing object
    draw = ImageDraw.Draw(img)
    # Define the grid line color
    color = (254, 0, 101, 50)
    # Draw the vertical grid lines
    for x in range(0, img_size[0], size):
        draw.line((x, 0, x, img_size[1]), fill=color, width=1)
    # Draw the horizontal grid lines
    for y in range(0, img_size[1], size):
        draw.line((0, y, img_size[0], y), fill=color, width=1)
    return img

realtime_update = st.checkbox("Update in realtime", True)
grid_size = st.slider('Grid Size', min_value=1, max_value=100, value=10, step=1)
bg_image = draw_grid(grid_size)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(254, 0, 101, 1)",  # Fixed fill color with some opacity
    stroke_width=1,
    stroke_color="rgba(10, 0, 0, 1)",
    background_color="rgba(68, 70, 84, 1)",
    background_image=bg_image,
    update_streamlit=realtime_update,
    width=600,
    height=300,
    drawing_mode="point",
    key="canvas",
)

if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"])
    # select specific columns
    selected_cols = ['type', 'originX', 'originY', 'left', 'top', 'width', 'height']
    selected_cols = [el for el in selected_cols if el in objects.columns]
    objects = objects.loc[:, selected_cols]
    st.dataframe(objects)

# Download the data into a excel file
if st.button("Download"):
    st.write("Downloading...")
    objects.to_excel("objects.xlsx", index=False)
    st.write("Done!")