import keras, keras_hub
import kagglehub

# from qwen3.main import model_name

# kagglehub.login() # if you don't have the model installed, you need to log in!
model_name = kagglehub.model_download("keras/gemma/keras/gemma_1.1_instruct_2b_en")

print("Path to model files:", model_name)

gemma_lm = keras_hub.models.GemmaCausalLM.from_preset(model_name)

# Шаг 3: Генерация
print(gemma_lm.generate("Keras is a", max_length=30))
print(gemma_lm.generate(["Keras is a", "I want to say"], max_length=30))
