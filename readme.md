# Task 1: Common Voice Dataset Augmentation

### Objective

Your task is to augment the [Mozilla Common Voice dataset](https://commonvoice.mozilla.org/en/datasets) to increase the diversity of the training data. This will improve the robustness of speech recognition models by introducing variations such as noise, pitch shifting, and speed changes.

### Instructions

1. **Download the Common Voice Dataset** :

* Go to the [Common Voice website](https://commonvoice.mozilla.org/en/datasets).
* Select a language of your choice (you can start with **English** or  **Uzbek** , depending on your preference).
* Download the dataset.

1. **Install Required Libraries** :

* Use Python and libraries such as `audiomentations`, `pydub`, or `torchaudio` for augmentation.
* You can install them using:
  <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install audiomentations torchaudio
  </code></div></div></pre>

1. **Augmentation Techniques** :

* **Noise Injection** : Add background noise to simulate real-world environments.
* **Pitch Shifting** : Alter the pitch of the audio to create diversity in vocal tone.
* **Speed Variation** : Slow down or speed up the audio to test robustness.
* **Volume Scaling** : Modify the audio volume to simulate different recording levels.

1. **Implementation** :

* Write a Python script to apply augmentation techniques to the audio files.
* Ensure that the augmented files are saved in a separate folder, while maintaining the original dataset structure.

1. **Save the Augmented Dataset** :

* Save your augmented audio files in a folder named `augmented_common_voice`.
* Maintain the metadata to keep track of what kind of augmentation was applied to each file.

1. **Deliverables** :

* Submit the Python script used for augmentation.
* Upload a sample of the augmented dataset (5-10 examples of each augmentation type).

### Resources

* [Mozilla Common Voice Dataset](https://commonvoice.mozilla.org/en/datasets)
* [Audiomentations Documentation](https://github.com/iver56/audiomentations)

---

## Task 2: Classification of People's Feedback

### Objective

Your task is to build a classification model that can classify people’s feedback as **Positive** or  **Negative** . We will use the **Amazon Customer Reviews Dataset** for this task.

### Dataset

* Dataset link: [Amazon Customer Reviews Dataset]()

### Instructions

1. **Download the Dataset** :

* The dataset is available in CSV format, containing millions of reviews across various product categories.
* Focus on the following columns:
  * `review_body`: The text of the feedback.
  * `star_rating`: The rating given by the customer (1-5). Treat **1-2** stars as **Negative** and **4-5** stars as **Positive** (ignore 3-star reviews for simplicity).

1. **Preprocessing** :

* **Text Cleaning** : Remove special characters, convert to lowercase, and remove stopwords.
* **Label Encoding** : Encode the star ratings as `0` for **Negative** and `1` for  **Positive** .

1. **Modeling** :

* Split the data into **training** and **testing** sets (e.g., 80% training, 20% testing).
* Use a simple machine learning model like  **Logistic Regression** ,  **Random Forest** , or **Support Vector Machine (SVM)** for classification.
* Optionally, you can try more advanced models like **BERT** or **RoBERTa** for text classification.

1. **Evaluation** :

* Evaluate the model’s performance using metrics like  **accuracy** ,  **precision** ,  **recall** , and  **F1-score** .
* Plot the confusion matrix to see where the model performs well or poorly.

1. **Deliverables** :

* Submit the Python code (or Jupyter notebook) for data cleaning, model training, and evaluation.
* Include a report summarizing the model's performance and any challenges faced.

### Tools and Libraries

* Python: `pandas`, `scikit-learn`, `nltk`, `matplotlib`, `seaborn`
* Optional: Hugging Face Transformers for BERT-based models

---

### Final Submission

* For Task 1: Submit your code for dataset augmentation along with a sample of augmented audio.
* For Task 2: Submit your Python code or Jupyter notebook along with a short report of your findings.

Good luck, and feel free to ask any questions during the process!
