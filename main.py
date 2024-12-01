import random
import re

class SimpleAI:
    def __init__(self):
        self.memory = []
        # Базовые слова для ответа
        self.words = ["да", "нет", "почему", "куда", "как", "зачем", "что", "когда", "где", "интересно", "может быть", "возможно"]

    def analyze_input(self, user_input):
        words = self.tokenize(user_input)
        self.memory.append(words)

    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def generate_response(self, user_input):
        if not self.memory:
            return "Привет! Чем могу помочь?"

        all_words = list(set(self.words + [word for message in self.memory for word in message]))

        response_length = random.randint(3, 6)  # Длина ответа
        response_words = random.sample(all_words, min(response_length, len(all_words)))

        return self.create_coherent_sentence(response_words)

    def create_coherent_sentence(self, words):
        # Формируем простое предложение
        predicate = ' '.join(words)

        sentence = f"{predicate}".capitalize()

        if not sentence.endswith(('.', '!', '?')):
            sentence += random.choice(['.', '!', '?'])

        return sentence

    def chat(self, user_input):
        self.analyze_input(user_input)
        return self.generate_response(user_input)

ai = SimpleAI()

print("ИИ: Привет! Расскажи мне что-нибудь. (Для выхода напиши 'выход')")
while True:
    user_input = input("Вы: ")
    if user_input.lower() in {'выход', 'exit'}:
        print("ИИ: До встречи! Было приятно поговорить.")
        break
    elif user_input.lower() == 'память':
        print(f"ИИ: Память: {ai.memory}")
    else:
        response = ai.chat(user_input)
        print(f"ИИ: {response}")
