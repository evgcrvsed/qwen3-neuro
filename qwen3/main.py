from transformers import AutoModelForCausalLM, AutoTokenizer
import kagglehub, torch, os

model_name = kagglehub.model_download("qwen-lm/qwen-3/transformers/0.6b")
os.system('cls')
print('Model path:')
print(model_name) # Если что, то модель находится по этому пути! Так что при желании можно удалить!

print(f'Video card use: {torch.cuda.is_available()}')  # должно быть True
print(f'Video card: {torch.cuda.get_device_name()}')  # имя твоей видеокарты

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

messages = []

def get_answer(text):
    global messages
    # prepare the model input
    prompt = text
    messages.append({"role": "user", "content": prompt})

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # conduct text completion
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=32768
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

    # parsing thinking content
    try:
        # rindex finding 151668 ()
        index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
        index = 0

    # thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
    print(content)

while True:
    get_answer(input('Enter your request: '))
