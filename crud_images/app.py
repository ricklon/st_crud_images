import streamlit as st
import sqlite3
from PIL import Image
import io

# Initialize the SQLite database
conn = sqlite3.connect('images.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS images
             (id INTEGER PRIMARY KEY, image BLOB, name TEXT)''')
conn.commit()

# Function to insert image into the database
def insert_image(image, name):
    with conn:
        c.execute("INSERT INTO images (image, name) VALUES (?, ?)", (image, name))
        conn.commit()
    st.cache_data.clear()  # Clear the cache after insert

# Function to retrieve all images from the database
@st.cache_data
def get_cached_images():
    c.execute("SELECT id, image, name FROM images")
    images = c.fetchall()
    return images

# Function to delete an image from the database
def delete_image(image_id):
    with conn:
        c.execute("DELETE FROM images WHERE id = ?", (image_id,))
        conn.commit()
    st.cache_data.clear()  # Clear the cache after delete

# Function to update an image in the database
def update_image(image_id, new_image, new_name):
    with conn:
        c.execute("UPDATE images SET image = ?, name = ? WHERE id = ?", (new_image, new_name, image_id))
        conn.commit()
    st.cache_data.clear()  # Clear the cache after update

# Set page configuration
st.set_page_config(page_title="Image Upload and Management App", layout="wide")

# Sidebar: Pre-render the sidebar to prevent visual glitch
with st.sidebar:
    st.header("CRUD and Gallery App")
    st.markdown("This app demonstrates how to implement CRUD operations with images using Streamlit and SQLite.")
    st.markdown("You can upload, view, update, delete, and browse images in a gallery format.")
    st.header("Database Management")
    with open("images.db", "rb") as file:
        st.download_button(
            label="Download Database",
            data=file,
            file_name="images.db",
            mime="application/octet-stream"
        )

# Main content
st.title("Image Upload and Management App")

# Use session state to track uploaded image
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# Add .tif support to the file uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif", "tiff"])

if uploaded_image is not None:
    image_name = st.text_input("Enter a name for the image")
    if st.button("Upload Image"):
        if image_name:
            with st.spinner("Uploading image..."):
                # Simulate progress
                progress = st.progress(0)
                for i in range(100):
                    progress.progress(i + 1)
                image_bytes = uploaded_image.read()
                insert_image(image_bytes, image_name)
                st.success(f"Image '{image_name}' uploaded successfully!")
                st.session_state.uploaded_image = None  # Reset session state after upload
        else:
            st.warning("Please enter a name for the image.")

# Gallery Section using st.container
st.header("Image Gallery")
images = get_cached_images()

# Display the images in a grid layout (gallery view)
if images:
    cols = st.columns(4)  # Adjust the number of columns as per your layout preference
    for index, image in enumerate(images):
        image_id, image_data, image_name = image
        img = Image.open(io.BytesIO(image_data))
        with cols[index % 4]:  # Ensures images wrap correctly
            st.image(img, caption=image_name, use_column_width=True)
            with st.container():
                action = st.radio("Select Action", ["View", "Update", "Delete"], key=f"action_{image_id}")
                if action == "Delete":
                    delete_image(image_id)
                    st.success(f"Image '{image_name}' deleted successfully!")
                    # Force refresh the images after deletion
                    images = get_cached_images()
                    st.rerun()
                elif action == "Update":
                    new_image = st.file_uploader(f"Update image for '{image_name}'", type=["jpg", "jpeg", "png", "tif", "tiff"], key=f"update_upload_{image_id}")
                    new_name = st.text_input(f"New name for '{image_name}'", key=f"new_name_{image_id}")
                    if new_image and new_name:
                        new_image_bytes = new_image.read()
                        update_image(image_id, new_image_bytes, new_name)
                        st.success(f"Image '{image_name}' updated successfully!")
                        # Force refresh the images after update
                        images = get_cached_images()
                        st.rerun()
