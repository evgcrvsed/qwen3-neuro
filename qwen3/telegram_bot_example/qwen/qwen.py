# pip install transformers, kagglehub, accelerate, torch
# pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
from pprint import pprint


class QwenBot:
    def __init__(self):
        from collections import defaultdict

        from transformers import AutoModelForCausalLM, AutoTokenizer
        import kagglehub, torch, os

        print(f'Video card use: {torch.cuda.is_available()}')
        print(f'Video card: {torch.cuda.get_device_name() if torch.cuda.is_available() else 'None'}')

        model_name = kagglehub.model_download("qwen-lm/qwen-3/transformers/0.6b")
        os.system('cls')
        print('Model path:')
        print(model_name)

        model_path = kagglehub.model_download("qwen-lm/qwen-3/transformers/0.6b")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype="auto",
            device_map="auto"
        )
        # Словарь с историей диалогов пользователей
        self.user_messages = defaultdict(list)

    def get_answer(self, user_id: int, text: str) -> str:
        # Добавляем сообщение пользователя
        self.user_messages[user_id].append({"role": "user", "content": text})

        # Создаем текст для генерации
        prompt_text = self.tokenizer.apply_chat_template(
            self.user_messages[user_id],
            tokenize=False,
            add_generation_prompt=True,
            # enable_thinking=True
        )
        inputs = self.tokenizer([prompt_text], return_tensors="pt").to(self.model.device)

        # Генерация
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.4,
            top_p=0.8,
            repetition_penalty=1.2,
            eos_token_id=self.tokenizer.eos_token_id,
        )

        # Отбрасываем prompt
        generated_ids = outputs[0][len(inputs["input_ids"][0]):]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

        # Добавляем ответ в историю
        self.user_messages[user_id].append({"role": "assistant", "content": response})

        pprint(response)
        if "</think>" in response:
            response = response.split("</think>", 1)[1].strip()
        else:
            response = response

        return response
