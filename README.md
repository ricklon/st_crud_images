# Image Upload and Management App

This project is a Streamlit-based web application for uploading, viewing, and managing images using SQLite as the backend database. The app supports CRUD (Create, Read, Update, Delete) operations and provides a gallery-style view of all uploaded images.

## Features

- **Upload Images**: Supports `.jpg`, `.jpeg`, `.png`, and `.tif` (TIFF) formats.
- **Image Gallery**: Displays uploaded images in a grid layout.
- **CRUD Operations**: Perform Create, Read, Update, and Delete actions on images.
- **Responsive Layout**: Uses Streamlit’s `st.container` and `st.columns` for a clean, responsive UI.
- **Cached Image Retrieval**: Utilizes `@st.cache_data` for faster data loading.
- **Progress Bar and Spinners**: Provides real-time feedback during image uploads.
- **Download Database**: Easily download the SQLite database from the sidebar.

## Getting Started

### Prerequisites

- Python 3.7+
- Poetry (for managing dependencies)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/crud_images.git
   cd crud_images
   ```

2. **Install Dependencies:**

   ```bash
   poetry install
   ```

3. **Run the App:**

   ```bash
   poetry run streamlit run ./crud_images/app.py --server.port 8502
   ```

4. **Access the App:**

   Open your browser and go to `http://localhost:8502`.

## Project Structure

```plaintext
crud_images/
│
├── images.db             # SQLite database storing image data
├── app.py                # Main Streamlit application script
├── README.md             # Project documentation (this file)
├── pyproject.toml        # Poetry configuration file
└── ...
```

## How to Use

1. **Uploading Images:**
   - Drag and drop or select an image using the file uploader.
   - Enter a name for the image before uploading.
   - The upload progress is shown with a progress bar.

2. **Viewing Images:**
   - Uploaded images are displayed in a grid layout.
   - You can see the image name and select actions like View, Update, or Delete.

3. **Updating Images:**
   - Select "Update" from the radio buttons next to the image.
   - Upload a new image or change the image name.

4. **Deleting Images:**
   - Select "Delete" from the radio buttons next to the image.
   - The image will be removed from the gallery and the database.

5. **Downloading the Database:**
   - Use the "Download Database" button in the sidebar to get a copy of the SQLite database.

## Advanced Features

- **Caching with `@st.cache_data`:** Image retrieval is cached to improve performance.
- **Responsive Layout:** The gallery adapts to different screen sizes using Streamlit’s layout features.
- **Visual Feedback:** Spinners and progress bars enhance user interaction during long operations.

## Known Issues

- **Sidebar Loading Glitch:** The sidebar content might load slightly after the main content due to how Streamlit renders UI elements. This has been mitigated by pre-rendering the sidebar early in the script.

## Future Improvements

- Add more image processing features like filters or cropping.
- Integrate authentication for secure image management.
- Support for more image formats and metadata handling.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
