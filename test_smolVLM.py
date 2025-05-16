import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM2-256M-Video-Instruct")
model = AutoModelForImageTextToText.from_pretrained(
    "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="cuda"
)

conversation = [
    {
        "role": "user",
        "content":[
            # {"type": "image", "url": "http://images.cocodataset.org/val2017/000000039769.jpg"},
            {"type": "image", "url": "https://support.goodnotes.com/hc/article_attachments/7443668068751"},
            {"type": "text", "text": "Explain this equation for kids to understand."}
        ]
    }
]

inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)

output_ids = model.generate(**inputs, max_new_tokens=128)
generated_texts = processor.batch_decode(output_ids, skip_special_tokens=True)
print(generated_texts)

def clean_text_for_textgeometry(text):
    return text.replace('\n', ' ').replace('\r', '')

def split_by_length(text, length=44):
    return [text[i:i+length] for i in range(0, len(text), length)]

raw_text = generated_texts[0]

# Extract the part after "Assistant:"
assistant_part = raw_text.split("Assistant:", 1)[-1].strip()

# Clean it up for TextGeometry
cleaned_text = clean_text_for_textgeometry(assistant_part)
print(cleaned_text)

lines = split_by_length(cleaned_text, 44)
print(lines[0])

# # Video
# conversation = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "video", "path": "/path/to/video.mp4"},
#             {"type": "text", "text": "Describe this video in detail"}
#         ]
#     },
# ]

# inputs = processor.apply_chat_template(
#     conversation,
#     add_generation_prompt=True,
#     tokenize=True,
#     return_dict=True,
#     return_tensors="pt",
# ).to(model.device, dtype=torch.bfloat16)

# generated_ids = model.generate(**inputs, do_sample=False, max_new_tokens=100)
# generated_texts = processor.batch_decode(generated_ids, skip_special_tokens=True)
# print(generated_texts[0])