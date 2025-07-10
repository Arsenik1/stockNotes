# Stock Notes Manager - Setup Instructions

## Requirements
- Python 3.7 or newer (for best tkinter compatibility)
- No external packages required (uses only Python standard library)

## How to Run
1. Make sure you have Python installed. You can check by running:
   
   ```sh
   python --version
   ```
   or
   ```sh
   python3 --version
   ```

2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install requirements (not strictly necessary, but for completeness):
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   python main.py
   ```

## Notes
- The application will automatically create the `short_term` and `long_term` directories if they do not exist.
- Make sure the `forestTheme` folder and its contents are present in the same directory as `main.py` for the custom theme to work.
- If you encounter issues with tkinter, ensure it is included in your Python installation (it is by default for most distributions).
