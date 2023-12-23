import speech_recognition as sr
import pyttsx3

class HealthBot:
    def __init__(self):
        self.symptom_tree = {
            'fever': {
                'cough': {
                    'shortness of breath': 'Possible respiratory infection. Consult a doctor.',
                    'no shortness of breath': 'Common cold. Rest and stay hydrated.'
                },
                'no cough': 'Fever may be due to various reasons. Consult a doctor for an accurate diagnosis.'
            },
            'no fever': {
                'fatigue': {
                    'muscle pain': 'Possible flu. Rest and stay hydrated. Consult a doctor if symptoms persist.',
                    'no muscle pain': 'Fatigue can be caused by various factors. Ensure proper rest and nutrition.'
                },
                'no fatigue': 'No specific symptoms detected. Monitor your health and consult a doctor if needed.'
            },
            'headache': {
                'sore throat': {
                    'difficulty swallowing': 'Possible strep throat. Consult a doctor for a throat swab.',
                    'no difficulty swallowing': 'Likely a common cold. Rest and stay hydrated.'
                },
                'no sore throat': 'Headache may be due to various reasons. Consult a doctor for an accurate diagnosis.'
            },
            'infectious diseases': {
                'influenza flu': {
                    'fever': 'Fever is a common symptom of influenza (flu). Consult a healthcare professional for evaluation.',
                    'cough': 'Cough, often severe, may be associated with influenza. Consult a healthcare professional for evaluation.',
                    'body aches': 'Body aches and fatigue are common in individuals with influenza. Consult a healthcare professional.'
                },
                'common cold': {
                    'runny nose': 'Runny or stuffy nose is a common symptom of the common cold. Consult a healthcare professional for evaluation.',
                    'sneezing': 'Frequent sneezing may be associated with the common cold. Consult a healthcare professional for evaluation.',
                    'sore throat': 'Sore throat and mild cough are common symptoms of the common cold. Consult a healthcare professional.'
                },
                'urinary tract infection uti': {
                    'burning sensation during urination': 'A burning sensation during urination may indicate a urinary tract infection (UTI). Consult a healthcare professional for evaluation.',
                    'frequent urination': 'Frequent and urgent need to urinate may be associated with a UTI. Consult a healthcare professional.',
                    'cloudy or foul-smelling urine': 'Cloudy or foul-smelling urine may be indicative of a UTI. Consult a healthcare professional.'
                },
                'gastroenteritis': {
                    'diarrhea': 'Diarrhea, often with abdominal cramps, may be indicative of gastroenteritis. Consult a healthcare professional for evaluation.',
                    'vomiting': 'Vomiting, along with nausea, is common in individuals with gastroenteritis. Consult a healthcare professional for evaluation.',
                    'dehydration': 'Dehydration due to fluid loss is a concern in gastroenteritis. Consult a healthcare professional for evaluation.'
                },
                'strep throat': {
                    'severe sore throat': 'Severe sore throat, often with white patches on the tonsils, may indicate strep throat. Consult a healthcare professional for evaluation.',
                    'painful swallowing': 'Painful swallowing and difficulty in swallowing may be associated with strep throat. Consult a healthcare professional.',
                    'swollen lymph nodes': 'Swollen lymph nodes in the neck are common in individuals with strep throat. Consult a healthcare professional for evaluation.'
                },
                'pneumonia': {
                    'persistent cough': 'A persistent cough, often with phlegm, may be associated with pneumonia. Consult a healthcare professional for evaluation.',
                    'shortness of breath': 'Shortness of breath, especially with activity, may indicate pneumonia. Consult a healthcare professional.',
                    'chest pain': 'Chest pain, particularly during breathing or coughing, may be associated with pneumonia. Consult a healthcare professional for evaluation.'
                },
                'skin infections cellulitis': {
                    'red and swollen skin': 'Red and swollen skin, often with warmth, may indicate cellulitis. Consult a healthcare professional for evaluation.',
                    'tenderness and pain': 'Tenderness and pain in the affected area are common symptoms of cellulitis. Consult a healthcare professional.',
                    'fever': 'Fever may accompany cellulitis. Consult a healthcare professional for evaluation.'
                },
                'sexually transmitted infections stis chlamydia gonorrhea': {
                    'unusual genital discharge': 'Unusual genital discharge may be indicative of a sexually transmitted infection (STI) such as chlamydia or gonorrhea. Consult a healthcare professional for evaluation.',
                    'burning sensation during urination': 'A burning sensation during urination may be associated with STIs like chlamydia and gonorrhea. Consult a healthcare professional.',
                    'pelvic pain': 'Pelvic pain, especially in women, may be a symptom of STIs. Consult a healthcare professional for evaluation.'
                },
                # Add more infectious diseases and symptoms as needed...
            },
            'mental health disorders': {
                'depression': {
                    'persistent sadness': 'Persistent sadness and a lack of interest in activities may indicate depression. Consult a mental health professional for evaluation.',
                    'changes in sleep': 'Changes in sleep patterns, such as insomnia or hypersomnia, may be associated with depression. Consult a mental health professional.',
                    'fatigue and loss of energy': 'Fatigue and loss of energy are common symptoms of depression. Consult a mental health professional for evaluation.'
                },
                'generalized anxiety disorder': {
                    'excessive worrying': 'Excessive worrying about various aspects of life may indicate generalized anxiety disorder. Consult a mental health professional for evaluation.',
                    'restlessness': 'Restlessness and an inability to relax may be associated with generalized anxiety disorder. Consult a mental health professional.',
                    'difficulty concentrating': 'Difficulty concentrating and mind going blank are common symptoms of generalized anxiety disorder. Consult a mental health professional.'
                },
                'bipolar disorder': {
                    'extreme mood swings': 'Extreme mood swings between mania and depression may indicate bipolar disorder. Consult a mental health professional for evaluation.',
                    'impulsivity': 'Impulsivity and risky behaviors during manic episodes may be associated with bipolar disorder. Consult a mental health professional.',
                    'decreased need for sleep': 'A decreased need for sleep during manic episodes is a characteristic of bipolar disorder. Consult a mental health professional.'
                },
                'schizophrenia': {
                    'hallucinations': 'Hallucinations, such as hearing voices, may indicate schizophrenia. Consult a mental health professional for evaluation.',
                    'delusions': 'Delusions, false beliefs that are resistant to reason or contrary to reality, may be associated with schizophrenia. Consult a mental health professional.',
                    'disorganized thinking': 'Disorganized thinking and speech patterns are common symptoms of schizophrenia. Consult a mental health professional.'
                },
                'attention deficit hyperactivity disorder': {
                    'inattention': 'Inattention, difficulty sustaining focus, and frequent careless mistakes may indicate ADHD. Consult a mental health professional for evaluation.',
                    'hyperactivity': 'Hyperactivity, restlessness, and impulsive behavior are common symptoms of ADHD. Consult a mental health professional.',
                    'difficulty waiting turn': 'Difficulty waiting turn and interrupting others are characteristic behaviors of ADHD. Consult a mental health professional.'
                },
                # Add more mental health disorders and symptoms as needed...
            },
            # Add more top-level categories and conditions as needed...
        }

        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("Listening")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    def get_diagnosis(self, symptoms):
        current_node = self.symptom_tree
        for symptom in symptoms:
            if symptom in current_node:
                current_node = current_node[symptom]
            else:
                return 'No specific diagnosis found for "{}". Please consult a healthcare professional for evaluation.'.format(symptom)

        if isinstance(current_node, dict):
            return self._interactive_diagnosis(current_node)
        else:
            return self._display_diagnosis_result(current_node)

    def _interactive_diagnosis(self, node):
        while isinstance(node, dict):
            self.speak("Do you have the following symptoms?")
            options = list(node.keys())
            for option in options:
                self.speak(option)

            user_response = self.listen()
            if user_response is None:
                self.speak("I'm sorry, I couldn't understand your response.")
                return 'Speech Recognition Error'

            if user_response.lower() in [option.lower() for option in options]:
                selected_option = next(option for option in options if option.lower() == user_response.lower())
                node = node[selected_option]
            else:
                self.speak("Invalid choice. Please speak one of the listed symptoms.")

        return self._display_diagnosis_result(node)

    def _display_diagnosis_result(self, diagnosis):
        result = f"\nDiagnosis: {diagnosis}\nRecommendation: Follow the provided instructions and consult a healthcare professional if symptoms persist or worsen."
        self.speak(result)
        return result


# Example usage with voice input and output:
health_bot = HealthBot()

# Start with the root of the symptom tree
current_symptoms = []
current_node = health_bot.symptom_tree

while isinstance(current_node, dict):
    health_bot.speak("Current symptoms:")
    health_bot.speak(str(current_symptoms))
    health_bot.speak("Do you have the following symptoms?")

    options = list(current_node.keys())
    for option in options:
        health_bot.speak(option)

    user_response = health_bot.listen()
    if user_response is None:
        health_bot.speak("I'm sorry, I couldn't understand your response.")
        break

    if user_response.lower() == "exit":
        break  # User said "exit," exit the loop

    if user_response.lower() in [option.lower() for option in options]:
        selected_option = next(option for option in options if option.lower() == user_response.lower())
        current_symptoms.append(selected_option)
        current_node = current_node[selected_option]
    else:
        health_bot.speak("Invalid choice. Please speak one of the listed symptoms.")

result = health_bot.get_diagnosis(current_symptoms)
print(result)
