
# **Cybersecurity Framework for IoT-Enabled Autonomous Vehicles**

## **Project Overview**

This project aims to develop a simplified prototype of a cybersecurity framework designed to secure IoT-enabled autonomous vehicles. The prototype integrates machine learning for anomaly detection and blockchain technology to ensure data integrity and secure communication. This framework is tested in a simulated environment to evaluate its effectiveness in mitigating cyber threats.

## **Project Structure**

```plaintext
cybersecurity_framework_project/
├── data/
│   ├── raw_data/
│   │   └── simulated_iot_data.csv
│   ├── processed_data/
│   │   ├── training_data.csv
│   │   ├── testing_data.csv
│   │   └── anomaly_injected_data.csv
│   └── blockchain_logs/
│       └── blockchain_data.json
├── models/
│   ├── anomaly_detection_model.pkl
│   └── trained_model/
│       ├── isolation_forest.pkl
│       └── ...
├── web_app/
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── app.py
│   └── requirements.txt
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   ├── blockchain_implementation.ipynb
│   └── data_analysis_and_visualization.ipynb
├── tests/
│   ├── test_anomaly_detection.py
│   ├── test_blockchain.py
│   └── ...
└── README.md
```

## **Getting Started**

### **Prerequisites**

- Python 3.8+
- Pip (Python package manager)
- Virtual environment setup (optional but recommended)

### **Setup Instructions**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/cybersecurity_framework_project.git
   cd cybersecurity_framework_project
   ```
2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   Navigate to the `web_app/` directory and install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. **Data Preprocessing:**
   Use the Jupyter notebooks in the `notebooks/` directory to preprocess the data and train the machine learning model:

   - `data_preprocessing.ipynb`: Clean and preprocess the IoT data.
   - `model_training.ipynb`: Train the anomaly detection model.
   - `blockchain_implementation.ipynb`: Implement the blockchain for data integrity.
   - `data_analysis_and_visualization.ipynb`: Analyze and visualize the results.
5. **Run the Web Application:**
   Navigate to the `web_app/` directory and run the Flask application:

   ```bash
   python app.py
   ```

   Open your web browser and go to `http://localhost:5000` to access the dashboard.
6. **Testing:**
   Execute the test scripts located in the `tests/` directory to ensure everything is functioning correctly:

   ```bash
   pytest tests/
   ```

## **Features**

- **Anomaly Detection:** Machine learning algorithms are used to detect anomalies in IoT sensor data, identifying potential cyber threats.
- **Blockchain Integration:** Blockchain technology ensures the integrity of the data and secures communication within the IoT network.
- **Web Dashboard:** A simple web interface displays real-time data, anomalies, and blockchain logs, allowing for easy monitoring and analysis.

## **Usage**

1. **Data Monitoring:** The web dashboard allows you to monitor IoT sensor data and detect anomalies in real-time.
2. **Anomaly Injection:** You can simulate cyber-attacks by injecting anomalies into the data and observe how the system responds.
3. **Blockchain Validation:** The blockchain ensures that all data transactions are secure and immutable, providing a tamper-proof record of events.

## **Testing and Validation**

- **Anomaly Detection:** The system's accuracy in detecting anomalies can be validated using the test data in the `tests/` directory.
- **Blockchain Integrity:** The blockchain implementation ensures that any tampering with the data is detected, with logs stored in `blockchain_logs/`.

## **Future Work**

- **Expand Simulation Environments:** Integrate more advanced simulation platforms to mimic real-world conditions more accurately.
- **Enhanced Machine Learning Models:** Incorporate more sophisticated models and algorithms for improved anomaly detection.
- **Scalability:** Test the framework's scalability with larger datasets and more complex IoT networks.

## **Contributing**

If you have suggestions or improvements, feel free to submit a pull request or open an issue. Contributions are always welcome!

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive overview of the prototype, guiding users through setup, usage, and further development possibilities.
