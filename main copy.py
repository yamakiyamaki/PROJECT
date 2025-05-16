# main.py
from time import sleep

def test_generate_scene():
    # Mock SLM output
    threejs_code = """
    import * as THREE from 'three';

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    """
    
    with open("static/scene.js", "w") as f:
        f.write(threejs_code)

def generate_scene():
    threejs_code = """
    const mat_red = new THREE.MeshStandardMaterial({ color: 0xff0000 });
    const boxG = new THREE.BoxGeometry(0.5, 0.05, 0.5);
    const boxM = new THREE.Mesh(boxG, mat_red);
    boxM.position.set(0, 0.5, 0);
    scene.add(boxM);

    const mtlLoader = new MTLLoader();
    mtlLoader.setPath('CatModel/');
    mtlLoader.load('cat.mtl', (materials) => {
    materials.preload();

    const objLoader = new OBJLoader();
    objLoader.setMaterials(materials);
    objLoader.setPath('CatModel/');

    objLoader.load('cat.obj', (object) => {
        object.position.set(0, 0, 0);
        object.scale.set(0.05, 0.05, 0.05);
        object.rotation.x = -Math.PI / 2;
        scene.add(object);
    });
});
    """
    with open("static/scene.js", "w") as f:
        f.write(threejs_code)

def generate_scene_js():
    js_code = """
function populateScene(scene, THREE, OBJLoader, MTLLoader) {
    const mtlLoader = new MTLLoader();
    mtlLoader.setPath('CatModel/');
    mtlLoader.load('cat.mtl', (materials) => {
        materials.preload();
        const objLoader = new OBJLoader();
        objLoader.setMaterials(materials);
        objLoader.setPath('CatModel/');
        objLoader.load('cat.obj', (object) => {
            object.position.set(0, 0, 0);
            object.scale.set(0.05, 0.05, 0.05);
            object.rotation.x = -Math.PI / 2;
            scene.add(object);
        });
    });
}
"""
    with open("static/scene.js", "w") as f:
        f.write(js_code)

def generate_dynamic_scene():
    code = """
    import * as THREE from 'three';

    export default function addToScene(scene) {
    const cube = new THREE.Mesh(
        new THREE.BoxGeometry(1, 1, 1),
        new THREE.MeshStandardMaterial({ color: 0xff0000 })
    );
    cube.position.set(1, 0, 0);
    scene.add(cube);
    }

    """
    with open("static/scene.js", "w") as f:
        f.write(code)

def generate_cat_scene():
    js_code = """
import * as THREE from 'three';
import { MTLLoader } from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/MTLLoader.js';
import { OBJLoader } from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/OBJLoader.js';

export default function(scene) {
  const mtlLoader = new MTLLoader();
  mtlLoader.setPath('/static/CatModel/');
  mtlLoader.load('cat.mtl', (materials) => {
    materials.preload();

    const objLoader = new OBJLoader();
    objLoader.setMaterials(materials);
    objLoader.setPath('/static/CatModel/');
    objLoader.load('cat.obj', (object) => {
      object.position.set(2, 0, 0);
      object.scale.set(0.05, 0.05, 0.05);
      object.rotation.x = -Math.PI / 2;
      scene.add(object);
      console.log("Cat model added");
    });
  });
}
"""
    with open("static/scene.js", "w") as f:
        f.write(js_code)

if __name__ == "__main__":
    while True:
        # test_generate_scene()
        # generate_scene()
        # generate_scene_js()
        # generate_dynamic_scene()
        generate_cat_scene()
        print("scene.js updated")
        sleep(5)  # simulate periodic updates