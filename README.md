# 📊 Parent-Teacher Meeting Dashboard (Powered by Gemini AI)

Welcome to the **Parent-Teacher Meeting Dashboard**, a Streamlit web app designed to streamline communication between teachers and parents. This app uses Google Gemini (Generative AI) to generate personalized, practical suggestions for parents based on student performance and parent feedback.

---

## 🌟 Features

✅ Load student performance data from a CSV file
✅ View key academic metrics like Math, Science, English, and Attendance
✅ Show strengths, weaknesses, and teacher comments
✅ Allow parents to leave feedback
✅ Use Gemini AI to generate tailored suggestions for parents based on feedback and performance
✅ Save parent feedback for future reference

---

## 📁 Project Structure

* `ptm_data.csv` – A CSV file containing student performance data
* `streamlit_app.py` – The main Streamlit application
* `GEMINI_API_KEY` – A required API key to access Google's Gemini AI

---

## 🧠 Gemini AI Integration

This app integrates **Google Gemini (generativeai)** to:

* Read and process student performance and parent feedback
* Generate 2–3 actionable suggestions for parents
* Keep responses concise (approximately 100 words or fewer)

---

## 🛠️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ptm-gemini-dashboard.git
cd ptm-gemini-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API Key

Create a `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY = "your_google_gemini_api_key"
```

### 4. Prepare your data

Ensure your `ptm_data.csv` file is in the root directory and follows this structure:

| Name | Math | Science | English | Attendance (%) | Strengths | Weaknesses | Comments             | Suggestions             | Parent Feedback |
| ---- | ---- | ------- | ------- | -------------- | --------- | ---------- | -------------------- | ----------------------- | --------------- |
| John | 85   | 90      | 88      | 95             | Creative  | Time Mgmt  | Shows good potential | Follow a study schedule |                 |

### 5. Run the app

```bash
streamlit run streamlit_app.py
```

---

## 🚀 Live Demo

Coming soon! (Feel free to deploy this on **Streamlit Cloud** or **Render** and share your version!)

---

## 🔒 Environment & Security

* API keys are stored securely using Streamlit's `secrets` feature.
* CSV file operations are cached for performance.
* Error handling ensures missing keys or files are handled gracefully.

---

## 📌 Key Notes for Contributors

* Ensure you do not commit your actual Gemini API key.
* Keep your CSV data anonymized or use sample data when sharing.
* Feel free to improve UI/UX, performance, or AI prompting!

---

## 📬 Feedback & Suggestions

If you find this useful, want new features, or have ideas, feel free to open an issue or submit a pull request. This app is built for the education community—your contributions matter!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).


