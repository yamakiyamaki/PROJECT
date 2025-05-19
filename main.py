# main.py
from time import sleep
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText
import json

# -------------------- smolVLM -----------------------
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



# --------------------- Generate scene.js ----------------------------
def generate_chat_scene(chat_text="Trust me kid.", screen_text="Equation is here"):
    chat_text_json = json.dumps(chat_text)        # e.g. → "I'll repeat what I say..."
    screen_text_json = json.dumps(screen_text)    # e.g. → "Equation is here"

    js_code = f"""
import * as THREE from 'three';
import {{ MTLLoader }} from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/MTLLoader.js';
import {{ OBJLoader }} from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/OBJLoader.js';
import {{ CSS2DRenderer, CSS2DObject }} from 'three/addons/renderers/CSS2DRenderer.js';
import {{ FontLoader }} from 'three/addons/loaders/FontLoader.js';
import {{ TextGeometry }} from 'three/addons/geometries/TextGeometry.js';

export default function(scene) {{
    const mtlLoader = new MTLLoader();
    mtlLoader.setPath('/static/CatModel/');
    mtlLoader.load('cat.mtl', (materials) => {{
        materials.preload();
        const objLoader = new OBJLoader();
        objLoader.setMaterials(materials);
        objLoader.setPath('/static/CatModel/');
        objLoader.load('cat.obj', (object) => {{
            object.position.set(2, 0, 0);
            object.scale.set(0.05, 0.05, 0.05);
            object.rotation.x = -Math.PI / 2;
            scene.add(object);
            console.log("Cat model added");
        }});
    }});

    const loader = new FontLoader();
    loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function (font) {{
        const chatText_g = new TextGeometry({chat_text_json}, {{
            font: font,
            size: 0.2,
            height: 0.05
        }});
        const screenText_g = new TextGeometry({screen_text_json}, {{
            font: font,
            size: 0.2,
            height: 0.05
        }});
        const textMaterial = new THREE.MeshStandardMaterial({{ color: 0x000000 }});
        const chatText = new THREE.Mesh(chatText_g, textMaterial);
        chatText.position.set(-1.3, 1, 1.1);
        scene.add(chatText);

        const screenText = new THREE.Mesh(screenText_g, textMaterial);
        screenText.position.set(-2.5, 4, 0.1);
        scene.add(screenText);
    }});
}}
"""

    with open("static/scene.js", "w", encoding="utf-8") as f:
        f.write(js_code)

#TODO: split text


# -------------------- main ----------------------
if __name__ == "__main__":
    while True:
        # test_generate_scene()
        # generate_scene()
        # generate_scene_js()
        # generate_dynamic_scene()
        generate_chat_scene(screen_text=lines[0])
        print("scene.js updated")
        sleep(5)  # simulate periodic updates